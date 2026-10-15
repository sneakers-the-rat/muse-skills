#!/usr/bin/env python3
"""Fetch or crop a product image for Style Try-on.

Download mode finds the product's image URL in the shopping result files (or
its product details), downloads it, checks it is a JPG, PNG, or WebP, and saves
it under ~/workspace/shopping/tryon/. --alternates instead saves up to three
other views of a catalog product, one path per line. Crop mode (--from-file
with --crop-top-percent) keeps everything below the given share of the image
height, removing a model's face above the product. --rebuild-results writes a
shopping result file for catalog products whose original result file is gone.

Prints the saved workspace-relative path, or `failed` with the reason on
stderr.
"""

from __future__ import annotations

import argparse
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
SHOPPING_CLI = "/opt/hatch/bin/shopping"
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


def find_image_url(product_id: str, result_files: list[str]) -> str | None:
    def walk(node: object) -> str | None:
        if isinstance(node, dict):
            if product_id in (node.get("product_id"), node.get("result_id"), node.get("id")):
                url = node.get("image_url")
                if isinstance(url, str) and url.startswith(("https://", "http://")):
                    return url
            for value in node.values():
                if (found := walk(value)) is not None:
                    return found
        elif isinstance(node, list):
            for value in node:
                if (found := walk(value)) is not None:
                    return found
        return None

    for path in result_files:
        try:
            data = json.loads(Path(os.path.expanduser(path)).read_text())
        except (OSError, ValueError):
            continue
        if (url := walk(data)) is not None:
            return url
    return None


def catalog_product(product_id: str) -> dict | None:
    """The `product` object from `shopping product-details`, or None."""
    if not Path(SHOPPING_CLI).exists() or product_id.startswith("browser:"):
        return None
    try:
        out = subprocess.run(
            [SHOPPING_CLI, "product-details", "--product-id", product_id],
            capture_output=True, text=True, timeout=60, check=True,
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
        with urllib.request.urlopen(request, timeout=60) as response:
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


def download(url: str, stem: str) -> int:
    try:
        target = fetch_image(url, stem)
    except ImageError as error:
        return fail(str(error))
    print(display_path(target))
    return 0


def alternates(product_id: str, result_files: list[str]) -> int:
    urls = catalog_image_urls(catalog_product(product_id))
    if not urls:
        return fail("no product details or images for this product")
    # Download mode used the result file's image, or the first product image.
    primary = find_image_url(product_id, result_files) or urls[0]
    stem = safe_stem(product_id)
    saved = 0
    for url in (url for url in urls if url != primary):
        if saved == MAX_ALTERNATES:
            break
        try:
            target = fetch_image(url, f"{stem}-alt{saved + 1}")
        except ImageError as error:
            print(f"product_image: skipped one view: {error}", file=sys.stderr)
            continue
        print(display_path(target))
        saved += 1
    return 0 if saved else fail("no other views of this product")


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


def crop(source: str, percent: int) -> int:
    if not 1 <= percent <= 90:
        return fail("--crop-top-percent must be between 1 and 90")
    path = Path(os.path.expanduser(source))
    if not path.is_absolute():
        path = HOME / path
    gm = shutil.which("gm")
    if gm is None or not path.is_file():
        return fail("cannot crop: missing gm or source image")
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
        return fail(f"crop failed: {error}")
    print(display_path(target))
    return 0


def main() -> int:
    parser = Parser(description=__doc__)
    parser.add_argument(
        "--product-id", action="append", default=[],
        help="catalog product_id or browser result_id; repeat only with --rebuild-results",
    )
    parser.add_argument("--results", action="append", default=[], help="shopping result file; repeat for each")
    parser.add_argument("--alternates", action="store_true", help="save up to three other views of the product")
    parser.add_argument("--rebuild-results", action="store_true", help="write a result file from product details")
    parser.add_argument("--from-file", help="crop this saved image instead of downloading")
    parser.add_argument("--crop-top-percent", type=int, help="with --from-file: drop this top share of the height")
    args = parser.parse_args()

    if args.from_file:
        if args.crop_top_percent is None:
            return fail("--from-file needs --crop-top-percent")
        return crop(args.from_file, args.crop_top_percent)
    if args.rebuild_results:
        if not args.product_id:
            return fail("--rebuild-results needs --product-id")
        return rebuild_results(args.product_id)
    if len(args.product_id) > 1:
        return fail("give one --product-id")
    product_id = args.product_id[0] if args.product_id else None
    if product_id is None:
        return fail("give --product-id")
    if args.alternates:
        return alternates(product_id, args.results)
    url = find_image_url(product_id, args.results)
    if url is None:
        urls = catalog_image_urls(catalog_product(product_id))
        url = urls[0] if urls else None
    if url is None:
        return fail("no image URL found for this product")
    return download(url, safe_stem(product_id))


if __name__ == "__main__":
    # The skill reads stdout for a path or `failed`, so no error may escape as a
    # traceback.
    try:
        sys.exit(main())
    except Exception as error:
        sys.exit(fail(f"unexpected error: {error}"))
