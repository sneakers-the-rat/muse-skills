#!/usr/bin/env python3
"""Save or crop product photos for Style Try-on.

Saving downloads each product's main image into ~/workspace/shopping/tryon/, in
parallel, plus up to three other views for products named with --alternates-for.
Fallback products download alongside, and each product whose photo fails is
replaced by the next fallback that saved. The URL comes from the shopping result
files, else from catalog product details. A browser product uses the copy of its
image that its shopping results card hosts on Meta's CDN when there is one, since
some merchants stall direct downloads.
--crop keeps what is below a share of each photo's height, removing a model's
face. --rebuild-results writes a result file for catalog products whose original
is gone. Each photo gets one output line, its saved path or `failed (<reason>)`, a
fallback's line names the product it replaces, and `failed` alone means nothing
was saved.
"""

from __future__ import annotations

import argparse
import collections
import concurrent.futures
import glob
import http.client
import json
import os
import re
import shutil
import subprocess
import sys
import urllib.request
from pathlib import Path
from typing import NoReturn

HOME = Path(os.path.expanduser("~"))
TRYON_DIR = HOME / "workspace" / "shopping" / "tryon"
MAX_IMAGE_BYTES = 25 * 1024 * 1024
MAX_ALTERNATES = 3
MAX_FALLBACKS = 2
MAX_CROP_PERCENT = 60
# Product images arrive in a second or two, so give up early on a stalled merchant.
IMAGE_TIMEOUT_SECONDS = 10
DETAILS_TIMEOUT_SECONDS = 20
SHOPPING_CLI = "/opt/hatch/bin/shopping"
# The files shopping.resolve_results writes for results cards, newest first.
CARD_RESULT_GLOBS = ("/var/tmp/hatch-shopping-results-*.json", "/tmp/hatch-shopping-results-*.json")
# Optional product-details fields that shopping.resolve_results reads.
OPTIONAL_RESULT_FIELDS = ("brand", "sale_price", "currency")
CHECKOUT_FLAGS = ("is_agentic_checkout_creation_enabled", "is_agentic_checkout_completion_enabled")


class ImageError(Exception):
    pass


def fail(reason: str) -> int:
    print(f"product_image: {reason}", file=sys.stderr)
    print("failed")
    return 1


class Parser(argparse.ArgumentParser):
    """Reports argument errors as `failed`, like every other error."""

    def error(self, message: str) -> NoReturn:
        sys.exit(fail(message))


def display_path(path: Path) -> str:
    """The path relative to home when it is under home, else absolute."""
    try:
        return str(path.relative_to(HOME))
    except ValueError:
        return str(path)


def image_type(data: bytes) -> str | None:
    if data.startswith(b"\xff\xd8\xff"):
        return "jpg"
    if data.startswith(b"\x89PNG"):
        return "png"
    if len(data) >= 12 and data[:4] == b"RIFF" and data[8:12] == b"WEBP":
        return "webp"
    return None


def safe_stem(value: str) -> str:
    stem = re.sub(r"[^A-Za-z0-9_-]+", "-", value.split("browser:")[-1]).strip("-")
    return stem[:80] or "product"


def is_web_url(value: object) -> bool:
    return isinstance(value, str) and value.startswith(("https://", "http://"))


def result_records(path: str) -> list[dict]:
    """Every object in a result file, or none if it can't be read."""
    try:
        data = json.loads(Path(os.path.expanduser(path)).read_text())
    except (OSError, ValueError):
        return []
    records = []
    nodes = collections.deque([data])
    while nodes:
        node = nodes.popleft()
        if isinstance(node, dict):
            records.append(node)
            nodes.extend(node.values())
        elif isinstance(node, list):
            nodes.extend(node)
    return records


def find_product(product_id: str, result_files: list[str]) -> dict | None:
    for path in result_files:
        for record in result_records(path):
            if product_id in (record.get("product_id"), record.get("result_id"), record.get("id")):
                if is_web_url(record.get("image_url")):
                    return record
    return None


def card_image_url(product: dict, result_files: list[str]) -> str | None:
    """The card's image for a browser product when it differs from the merchant's,
    which is the copy hosted on Meta's CDN. Cards match by product page URL."""
    page = product.get("url")
    if not is_web_url(page):
        return None
    cards = sorted(
        {path for pattern in CARD_RESULT_GLOBS for path in glob.glob(pattern)},
        key=lambda path: os.path.getmtime(path) if os.path.exists(path) else 0,
        reverse=True,
    )
    for path in [*result_files, *cards]:
        for record in result_records(path):
            if (
                record.get("url") == page
                and record.get("is_image_available") is True
                and is_web_url(record.get("image_url"))
                and record["image_url"] != product["image_url"]
            ):
                return record["image_url"]
    return None


def catalog_product(product_id: str) -> dict | None:
    """The `product` object from `shopping product-details`, or None."""
    if not Path(SHOPPING_CLI).exists() or product_id.startswith("browser:"):
        return None
    try:
        out = subprocess.run(
            [SHOPPING_CLI, "product-details", "--product-id", product_id],
            capture_output=True, text=True, timeout=DETAILS_TIMEOUT_SECONDS, check=True,
        ).stdout
        product = json.loads(out).get("product")
    except (OSError, subprocess.SubprocessError, ValueError, AttributeError):
        return None
    return product if isinstance(product, dict) else None


def catalog_image_urls(product: dict | None) -> list[str]:
    images = product.get("images") if product else None
    if not isinstance(images, list):
        return []
    urls = (image.get("url") for image in images if isinstance(image, dict))
    return [url for url in urls if isinstance(url, str) and url.startswith(("https://", "http://"))]


def fetch_image(url: str, stem: str) -> Path:
    request = urllib.request.Request(
        url,
        headers={"User-Agent": "Mozilla/5.0", "Accept": "image/png,image/jpeg,image/webp"},
    )
    try:
        with urllib.request.urlopen(request, timeout=IMAGE_TIMEOUT_SECONDS) as response:
            data = response.read(MAX_IMAGE_BYTES + 1)
    except (OSError, ValueError, http.client.HTTPException) as error:
        # ValueError and HTTPException cover malformed URLs, such as a raw space
        # or a non-ASCII character, and truncated responses.
        raise ImageError(f"download failed: {error}") from error
    if len(data) > MAX_IMAGE_BYTES:
        raise ImageError("image is too large")
    kind = image_type(data)
    if kind is None:
        raise ImageError("not a JPG, PNG, or WebP image")
    target = TRYON_DIR / f"{stem}.{kind}"
    try:
        TRYON_DIR.mkdir(parents=True, exist_ok=True)
        target.write_bytes(data)
    except OSError as error:
        raise ImageError(f"could not save the image: {error}") from error
    return target


def fetch_first(urls: list[str], stem: str) -> Path:
    """Saves the first of these URLs that downloads, reporting the last failure."""
    for url in urls[:-1]:
        try:
            return fetch_image(url, stem)
        except ImageError as error:
            print(f"product_image: {stem}: trying the merchant's image: {error}", file=sys.stderr)
    return fetch_image(urls[-1], stem)


def save_product(product_id: str, result_files: list[str], with_alternates: bool) -> list[str]:
    product = find_product(product_id, result_files)
    url = product["image_url"] if product else None
    urls = catalog_image_urls(catalog_product(product_id)) if url is None or with_alternates else []
    url = url or next(iter(urls), None)
    if url is None:
        raise ImageError("no image URL found for this product")
    card_url = card_image_url(product, result_files) if product and product_id.startswith("browser:") else None
    stem = safe_stem(product_id)
    others = [other for other in urls if other != url][:MAX_ALTERNATES] if with_alternates else []
    with concurrent.futures.ThreadPoolExecutor(max_workers=1 + len(others)) as pool:
        main = pool.submit(fetch_first, [card_url, url] if card_url else [url], stem)
        views = [pool.submit(fetch_image, other, f"{stem}-view{n}") for n, other in enumerate(others, start=2)]
    lines = [f"{product_id}: {display_path(main.result())}"]
    for n, view in enumerate(views, start=2):
        try:
            lines.append(f"{product_id} view {n}: {display_path(view.result())}")
        except ImageError as error:
            print(f"product_image: {product_id}: skipped one view: {error}", file=sys.stderr)
    return lines


def download(
    product_ids: list[str], fallback_ids: list[str], result_files: list[str], alternates_for: set[str]
) -> int:
    everything = product_ids + fallback_ids
    with concurrent.futures.ThreadPoolExecutor(max_workers=len(everything)) as pool:
        futures = {
            product_id: pool.submit(save_product, product_id, result_files, product_id in alternates_for)
            for product_id in everything
        }

    def outcome(product_id: str) -> list[str] | ImageError:
        try:
            return futures[product_id].result()
        except ImageError as error:
            return error

    saved_fallbacks = (outcome(fallback_id) for fallback_id in fallback_ids)
    spare = (lines for lines in saved_fallbacks if not isinstance(lines, ImageError))
    saved = 0
    for product_id in product_ids:
        lines = outcome(product_id)
        if isinstance(lines, ImageError):
            print(f"{product_id}: failed ({lines})")
            if (lines := next(spare, None)) is None:
                continue
            lines = [f"{lines[0]} (in place of {product_id})", *lines[1:]]
        print("\n".join(lines))
        saved += 1
    if not saved:
        print("failed")
        return 1
    return 0


def crop_one(source: str, percent: int) -> str:
    if not 1 <= percent <= MAX_CROP_PERCENT:
        raise ImageError(f"crop percent must be between 1 and {MAX_CROP_PERCENT}")
    path = Path(os.path.expanduser(source))
    if not path.is_absolute():
        path = HOME / path
    gm = shutil.which("gm")
    if gm is None or not path.is_file():
        raise ImageError("missing gm or source image")
    try:
        size = subprocess.run(
            [gm, "identify", "-format", "%w %h", str(path)],
            capture_output=True, text=True, timeout=30, check=True,
        ).stdout.split()
        width, height = int(size[0]), int(size[1])
        top = height * percent // 100
        target = path.with_name(f"{path.stem}-crop.png")
        subprocess.run(
            [gm, "convert", str(path), "-crop", f"{width}x{height - top}+0+{top}", str(target)],
            capture_output=True, timeout=60, check=True,
        )
    except (OSError, subprocess.SubprocessError, ValueError, IndexError) as error:
        raise ImageError(f"crop failed: {error}") from error
    return display_path(target)


def crop(specs: list[str]) -> int:
    saved = 0
    for spec in specs:
        source, _, percent = spec.rpartition("=")
        try:
            if not source or not percent.isdigit():
                raise ImageError("give PATH=PERCENT")
            print(f"{source}: {crop_one(source, int(percent))}")
            saved += 1
        except ImageError as error:
            print(f"{source or spec}: failed ({error})")
    if not saved:
        print("failed")
        return 1
    return 0


def rebuild_results(product_ids: list[str]) -> int:
    products = []
    for product_id in product_ids:
        product = catalog_product(product_id)
        urls = catalog_image_urls(product)
        if product is None or not urls or not all(
            isinstance(product.get(field), str) for field in ("name", "url")
        ):
            print(f"product_image: no product details for {product_id}", file=sys.stderr)
            continue
        entry = {
            "product_id": product_id,
            "name": product["name"],
            "url": product["url"],
            "image_url": urls[0],
        }
        for field in ("price", *OPTIONAL_RESULT_FIELDS):
            if product.get(field) is not None:
                entry[field] = product[field]
        for flag in CHECKOUT_FLAGS:
            if product.get(flag) is True:
                entry[flag] = True
        products.append(entry)
    if not products:
        return fail("no product details for these products")
    target = TRYON_DIR / f"results-{safe_stem('-'.join(product_ids))}.json"
    try:
        TRYON_DIR.mkdir(parents=True, exist_ok=True)
        target.write_text(json.dumps({"products": products}, indent=2))
    except OSError as error:
        return fail(f"could not save the result file: {error}")
    print(display_path(target))
    return 0


def main() -> int:
    parser = Parser(description=__doc__, allow_abbrev=False)
    parser.add_argument(
        "--product-id", action="append", default=[],
        help="catalog product_id or browser result_id; repeatable",
    )
    parser.add_argument(
        "--results", action="append", default=[],
        help="shopping result file behind the products; repeatable",
    )
    parser.add_argument(
        "--fallback-id", action="append", default=[],
        help=f"product to use in place of one whose photo fails, in order; up to {MAX_FALLBACKS}",
    )
    parser.add_argument(
        "--alternates-for", action="append", default=[],
        help="catalog product_id to save with its other views; repeatable",
    )
    parser.add_argument(
        "--crop", action="append", default=[], metavar="PATH=PERCENT",
        help="keep what is below PERCENT of the photo's height; repeatable",
    )
    parser.add_argument("--rebuild-results", action="store_true", help="write a result file from product details")
    args = parser.parse_args()

    if args.crop:
        if args.product_id or args.rebuild_results:
            return fail("use --crop on its own")
        return crop(args.crop)

    # --alternates-for adds a product only when it isn't a spare, so a head-item
    # spare keeps its replacement role.
    product_ids = list(dict.fromkeys(
        args.product_id + [item for item in args.alternates_for if item not in args.fallback_id]
    ))
    if not product_ids:
        return fail("give --product-id")
    if args.rebuild_results:
        if args.fallback_id:
            return fail("--fallback-id only applies to saving photos")
        return rebuild_results(product_ids)
    fallback_ids = [fallback for fallback in dict.fromkeys(args.fallback_id) if fallback not in product_ids]
    if len(fallback_ids) > MAX_FALLBACKS:
        print(f"product_image: using only the first {MAX_FALLBACKS} --fallback-id", file=sys.stderr)
        fallback_ids = fallback_ids[:MAX_FALLBACKS]
    return download(product_ids, fallback_ids, args.results, set(args.alternates_for))


if __name__ == "__main__":
    # The skill reads stdout for paths or `failed`, so no error may escape as a
    # traceback.
    try:
        sys.exit(main())
    except Exception as error:
        sys.exit(fail(f"unexpected error: {error}"))
