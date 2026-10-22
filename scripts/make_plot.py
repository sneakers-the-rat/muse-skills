#!/usr/bin/env python3
"""Generate plot.svg for the skill-history repo.

One point per commit on each of two lines: lines added and lines removed
in the tracked skill trees (skills/, workflow-skills/), measured with
`git log --numstat`. The x axis is commit time with tick marks every
week. The y axis is log-scaled: gridlines and labels sit at powers of ten
(10e0, 10e1, ...) and the top power is the smallest one covering the
largest value in the data — nothing about the scale is fixed. Values of
0 sit on the 10e0 floor. The point for the run currently in progress is
passed on the command line and appended, so the plot committed in a
snapshot already includes that snapshot's own point.

Pure stdlib. Usage:
  make_plot.py --repo PATH --out PATH \
      [--current-added N --current-removed N --current-date ISO]
"""
import argparse
import subprocess
from datetime import datetime, timedelta

TREES = ("skills", "workflow-skills")

# Commits excluded from the plot entirely (no point on either line):
# repo-restructuring events whose line counts are artifacts of the
# archive's own mechanics, not skill changes — they skew the y-axis.
#   4b035f6  the initial archive commit (full tree import)
#   a5c7238  the 2026-10-14 contraction (tree became symlink entries)
#   5a6ab99  safety copies swept into the repo by the old script
#   ecb5cd9  the 2026-10-15 restructure (symlinks resolved back to files)
EXCLUDED_COMMITS = {
    "4b035f68e7124dbf5b85559f8e30c1940ac1e848",
    "a5c7238ce306b61ed9ec1f2ffb114522ad089048",
    "5a6ab99b9e2bbfdb1fd036a9a770801e66da8544",
    "ecb5cd9d76d992dd56168eda8e9f9172993f5f9b",
}


def parse_log(text):
    """Parse full `git log --format=commit%x09%H%x09%cI --numstat` output
    into one {hash, date, added, removed} dict PER COMMIT, in log order.
    Only numstat lines under the tracked skill trees are summed; a commit
    that touched nothing in the trees still gets its (0, 0) point."""
    series = []
    cur = None
    for line in text.splitlines():
        if line.startswith("commit\t"):
            parts = line.split("\t")
            if parts[1] in EXCLUDED_COMMITS:
                cur = None
                continue
            cur = {"hash": parts[1], "date": parts[2], "added": 0, "removed": 0}
            series.append(cur)
        elif cur is not None and "\t" in line:
            f = line.split("\t")
            if (len(f) >= 3 and f[0].isdigit() and f[1].isdigit()
                    and f[2].startswith(tuple(t + "/" for t in TREES))):
                cur["added"] += int(f[0])
                cur["removed"] += int(f[1])
    return series


def load_series(repo):
    out = subprocess.run(
        ["git", "-C", repo, "log", "--reverse",
         "--format=commit%x09%H%x09%cI", "--numstat"],
        capture_output=True, text=True, check=True).stdout
    return parse_log(out)


def _top_exponent(v):
    """Smallest exponent e >= 1 with 10**e >= v: the plot's top gridline
    is the first power of ten that covers the largest value in the data."""
    import math
    if v <= 10:
        return 1
    return max(1, math.ceil(math.log10(v)))


def render_svg(series, width=960, height=360):
    if not series:
        now = datetime.now().astimezone().isoformat(timespec="seconds")
        series = [{"hash": "", "date": now, "added": 0, "removed": 0}]
    pts = [(datetime.fromisoformat(p["date"]), p["added"], p["removed"])
           for p in series]
    t0 = min(p[0] for p in pts)
    t1 = max(p[0] for p in pts)
    if t1 <= t0:
        t1 = t0 + timedelta(days=1)
    top_exp = _top_exponent(max(max(p[1], p[2]) for p in pts))

    ml, mr, mt, mb = 58, 14, 30, 42
    iw, ih = width - ml - mr, height - mt - mb
    span = (t1 - t0).total_seconds()

    def x(dt):
        return ml + (dt - t0).total_seconds() / span * iw

    def y(v):
        import math
        # Log scale: value v sits log10(v) of top_exp decades above the
        # floor; values <= 1 (including 0) sit on the 10e0 floor line.
        decades = math.log10(v) if v > 1 else 0.0
        return mt + ih - decades / top_exp * ih

    def polyline(idx):
        return " ".join(f"{x(p[0]):.1f},{y(p[idx]):.1f}" for p in pts)

    # Weekly ticks: first tick is the Monday of the week containing t0.
    tick = (t0 - timedelta(days=t0.weekday())).replace(
        hour=0, minute=0, second=0, microsecond=0)
    if tick < t0 - timedelta(days=7):
        tick += timedelta(days=7)
    ticks = []
    while tick <= t1:
        if tick >= t0 - timedelta(days=7):
            ticks.append(tick)
        tick += timedelta(days=7)
    if not ticks:
        ticks = [t0]

    grid = []
    for e in range(top_exp + 1):
        yy = y(10 ** e)
        grid.append(
            f'<line x1="{ml}" y1="{yy:.1f}" x2="{ml + iw}" y2="{yy:.1f}" '
            f'stroke="#e3e3e3" stroke-width="1"/>'
            f'<text x="{ml - 6}" y="{yy + 3:.1f}" font-size="9" '
            f'text-anchor="end" fill="#555">10e{e}</text>')
    tick_svg = []
    for tk in ticks:
        xx = x(tk)
        tick_svg.append(
            f'<line x1="{xx:.1f}" y1="{mt}" x2="{xx:.1f}" y2="{mt + ih}" '
            f'stroke="#eeeeee" stroke-width="1"/>'
            f'<text x="{xx:.1f}" y="{mt + ih + 14}" font-size="9" '
            f'text-anchor="middle" fill="#555">{tk:%Y-%m-%d}</text>')

    circles_a = "".join(
        f'<circle cx="{x(p[0]):.1f}" cy="{y(p[1]):.1f}" r="1.6" '
        f'fill="#1a9850" fill-opacity="0.65"/>' for p in pts)
    circles_r = "".join(
        f'<circle cx="{x(p[0]):.1f}" cy="{y(p[2]):.1f}" r="1.6" '
        f'fill="#d64541" fill-opacity="0.65"/>' for p in pts)

    lx = ml + iw - 168
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">
<rect width="{width}" height="{height}" fill="#ffffff"/>
<text x="{ml}" y="18" font-size="13" font-weight="bold" fill="#222">Skill files &#8212; lines added / removed per commit</text>
{''.join(grid)}
{''.join(tick_svg)}
<line x1="{ml}" y1="{mt}" x2="{ml}" y2="{mt + ih}" stroke="#888"/>
<line x1="{ml}" y1="{mt + ih}" x2="{ml + iw}" y2="{mt + ih}" stroke="#888"/>
<polyline points="{polyline(1)}" fill="none" stroke="#1a9850" stroke-width="1.5"/>
<polyline points="{polyline(2)}" fill="none" stroke="#d64541" stroke-width="1.5"/>
{circles_a}{circles_r}
<line x1="{lx}" y1="12" x2="{lx + 22}" y2="12" stroke="#1a9850" stroke-width="2"/>
<text x="{lx + 27}" y="15" font-size="10" fill="#222">added</text>
<line x1="{lx + 78}" y1="12" x2="{lx + 100}" y2="12" stroke="#d64541" stroke-width="2"/>
<text x="{lx + 105}" y="15" font-size="10" fill="#222">removed</text>
</svg>
'''


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--current-added", type=int)
    ap.add_argument("--current-removed", type=int)
    ap.add_argument("--current-date")
    args = ap.parse_args()

    series = load_series(args.repo)
    if args.current_added is not None and args.current_date:
        series.append({"hash": "(current)", "date": args.current_date,
                       "added": args.current_added,
                       "removed": args.current_removed or 0})
    with open(args.out, "w") as fh:
        fh.write(render_svg(series))
    print(f"plot: {len(series)} commits plotted -> {args.out}")


if __name__ == "__main__":
    main()
