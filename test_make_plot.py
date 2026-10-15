import unittest

from make_plot import parse_log, render_svg

LOG = """commit\tabc123\t2026-09-27T21:42:59-07:00

10\t2\tskills/a/SKILL.md
-\t-\tskills/bin.dat
3\t0\tskills/b.md
7\t7\tREADME.md
commit\tdef456\t2026-10-05T10:00:00-07:00

0\t5\tskills/a/SKILL.md
commit\tghi789\t2026-10-06T10:00:00-07:00

4\t4\tCHANGELOG.md
"""


class TestParseLog(unittest.TestCase):
    def test_sums_and_skips_binary(self):
        s = parse_log(LOG)
        self.assertEqual(len(s), 3)
        # README.md numstat is outside the trees and must not be summed.
        self.assertEqual((s[0]["added"], s[0]["removed"]), (13, 2))
        self.assertEqual((s[1]["added"], s[1]["removed"]), (0, 5))
        self.assertEqual(s[0]["hash"], "abc123")

    def test_commit_outside_trees_gets_zero_point(self):
        s = parse_log(LOG)
        self.assertEqual((s[2]["added"], s[2]["removed"]), (0, 0))
        self.assertEqual(s[2]["hash"], "ghi789")

    def test_empty(self):
        self.assertEqual(parse_log(""), [])

    def test_excluded_commit_dropped(self):
        log = ("commit\t4b035f68e7124dbf5b85559f8e30c1940ac1e848"
               "\t2026-09-27T21:42:59-07:00\n\n"
               "100\t0\tskills/a.md\n"
               "commit\tabc123\t2026-09-28T10:00:00-07:00\n\n"
               "1\t1\tskills/a.md\n")
        s = parse_log(log)
        self.assertEqual([p["hash"] for p in s], ["abc123"])


class TestRender(unittest.TestCase):
    def test_two_lines_weekly_ticks(self):
        s = [
            {"hash": "a", "date": "2026-09-27T21:42:59-07:00",
             "added": 5, "removed": 1},
            {"hash": "b", "date": "2026-10-05T10:00:00-07:00",
             "added": 9, "removed": 4},
            {"hash": "c", "date": "2026-10-14T10:00:00-07:00",
             "added": 2, "removed": 12},
        ]
        svg = render_svg(s)
        self.assertEqual(svg.count("<polyline"), 2)
        for pl in svg.split("<polyline")[1:]:
            points = pl.split('points="')[1].split('"')[0].split()
            self.assertEqual(len(points), 3)
        # Sep 27 (Sun) -> week ticks at Sep 28? Mondays in range: Sep 28,
        # Oct 5, Oct 12 -> at least two date labels present.
        labels = [d for d in ("2026-09-28", "2026-10-05", "2026-10-12")
                  if d in svg]
        self.assertGreaterEqual(len(labels), 2)

    def test_empty_series_renders(self):
        svg = render_svg([])
        self.assertIn("<svg", svg)
        self.assertEqual(svg.count("<polyline"), 2)


if __name__ == "__main__":
    unittest.main()
