#!/usr/bin/env python3
"""Tests for tools/check_book.py.

Run with:
    python3 -m unittest discover -s tools -p 'test_*.py'
"""

from __future__ import annotations

import io
import json
import sys
import tempfile
import unittest
from contextlib import redirect_stdout
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import check_book  # noqa: E402


CLEAN = """# Introduction — Test

A claim.[^intro-one]

Table 1 compares the positions.

| Position | Claim |
|---|---|
| **A** | B |

**Caption.** Table 1. Test table.

[^intro-one]: Author, *Title* (2020), 1. [Consulted text](https://example.org). Accessed October 29, 2026. Used for: the claim.
"""


class CheckBookTest(unittest.TestCase):
    def setUp(self) -> None:
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        (self.root / "chapters").mkdir()

    def tearDown(self) -> None:
        self.tmp.cleanup()

    def write(self, name: str, text: str) -> Path:
        path = self.root / "chapters" / name
        path.write_text(text, encoding="utf-8")
        return path

    def check(self, *paths: Path) -> check_book.Checker:
        return check_book.run(list(paths), self.root)

    def codes(self, checker: check_book.Checker) -> set[str]:
        return {issue.code for issue in checker.issues}

    def test_clean_document(self) -> None:
        path = self.write("00-introduction.md", CLEAN)
        checker = self.check(path)
        self.assertEqual([], checker.issues)
        self.assertEqual(1, checker.stats.notes)
        self.assertEqual(1, checker.stats.tables)

    def test_missing_definition(self) -> None:
        path = self.write(
            "00-introduction.md", "# Introduction — Test\n\nA claim.[^intro-gone]\n"
        )
        self.assertIn("note-missing-definition", self.codes(self.check(path)))

    def test_duplicate_definition_across_files(self) -> None:
        text = "# Chapter — Test\n\nA claim.[^dup]\n\n[^dup]: A note. Used for: the claim.\n"
        first = self.write("a.md", text)
        second = self.write("b.md", text)
        self.assertIn(
            "note-duplicate-definition", self.codes(self.check(first, second))
        )

    def test_unused_definition(self) -> None:
        path = self.write(
            "00-introduction.md",
            "# Introduction — Test\n\n[^intro-unused]: A note. Used for: nothing.\n",
        )
        self.assertIn("note-unused-definition", self.codes(self.check(path)))

    def test_ragged_table(self) -> None:
        path = self.write(
            "00-introduction.md",
            "# Introduction — Test\n\n| A | B |\n|---|---|\n| 1 |\n",
        )
        self.assertIn("table-ragged", self.codes(self.check(path)))

    def test_table_reference_and_bold(self) -> None:
        text = """# Introduction — Test

| Position | Claim |
|---|---|
| A | B |

**Caption.** Table 1. Test table.
"""
        path = self.write("00-introduction.md", text)
        found = self.codes(self.check(path))
        self.assertIn("table-reference", found)
        self.assertIn("table-leading-cell", found)

    def test_typography(self) -> None:
        path = self.write(
            "00-introduction.md",
            '# Introduction — Test\n\nHe said "hello" in 1861-65.\n',
        )
        found = self.codes(self.check(path))
        self.assertIn("straight-double-quote", found)
        self.assertIn("hyphen-range", found)

    def test_content_after_notes(self) -> None:
        text = """# Introduction — Test

A claim.[^intro-one]

[^intro-one]: A note. Used for: the claim.

Trailing prose.
"""
        path = self.write("00-introduction.md", text)
        self.assertIn("content-after-notes", self.codes(self.check(path)))

    def test_separate_sources_heading(self) -> None:
        path = self.write(
            "00-introduction.md", "# Introduction — Test\n\n## Sources\n\nA list.\n"
        )
        self.assertIn("separate-sources", self.codes(self.check(path)))

    def test_missing_link_target(self) -> None:
        path = self.write(
            "00-introduction.md",
            "# Introduction — Test\n\nSee [the missing file](nope.md).\n",
        )
        self.assertIn("link-missing", self.codes(self.check(path)))

    def test_editorial_check_exempt_from_used_for(self) -> None:
        text = """# Introduction — Test

A question.[^intro-check]

[^intro-check]: Editorial check — see [the source](https://example.org).
"""
        path = self.write("00-introduction.md", text)
        self.assertNotIn("note-used-for", self.codes(self.check(path)))

    def test_missing_file(self) -> None:
        path = self.root / "chapters" / "00-introduction.md"
        self.assertIn("file-missing", self.codes(self.check(path)))

    def test_extra_file_warns_in_manifest_mode(self) -> None:
        intro = self.write("00-introduction.md", CLEAN)
        self.write("notes.md", "# Notes\n")
        checker = check_book.run([intro], self.root, full_manifest=True)
        self.assertIn("file-extra", self.codes(checker))

    def test_json_report(self) -> None:
        path = self.write("00-introduction.md", CLEAN)
        output = io.StringIO()
        with redirect_stdout(output):
            status = check_book.main(
                [str(path), "--root", str(self.root), "--json"]
            )
        report = json.loads(output.getvalue())
        self.assertEqual(0, status)
        self.assertTrue(report["ok"])
        self.assertEqual(1, report["stats"]["notes"])

    def test_strict_cli_exit_codes(self) -> None:
        text = """# Introduction — Test

| Position | Claim |
|---|---|
| A | B |

**Caption.** Table 1. Test table.

Table 1 is cited.
"""
        path = self.write("00-introduction.md", text)
        with redirect_stdout(io.StringIO()):
            self.assertEqual(0, check_book.main([str(path), "--root", str(self.root)]))
            self.assertEqual(
                1,
                check_book.main(
                    [str(path), "--root", str(self.root), "--strict"]
                ),
            )


if __name__ == "__main__":
    unittest.main()