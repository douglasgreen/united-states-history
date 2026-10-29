#!/usr/bin/env python3
"""Structural checks for the manuscript.

This is a Markdown-level checker, not a build. It verifies the things that can
be established before rendering: the file manifest, headings, the combined
footnote namespace, pipe-table shape, local links, house typography, and word
counts. It does not verify that a citation supports a claim, that a scene is
documented, or that a table fits a typeset page.

Usage:
    python3 tools/check_book.py
    python3 tools/check_book.py chapters/00-introduction.md
    python3 tools/check_book.py --strict
    python3 tools/check_book.py --json

Exit status is 0 when there are no errors, 1 when there are errors (or, with
--strict, warnings), and 2 for invalid usage.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
import unicodedata
from collections import Counter, defaultdict
from dataclasses import dataclass, field
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parent.parent
CHAPTERS = "chapters"


# ---------------------------------------------------------------------------
# Data structures


@dataclass
class Issue:
    level: str  # "error", "warning", or "info"
    code: str
    path: Path
    line: int
    message: str

    def as_dict(self, root: Path) -> dict:
        try:
            shown = str(self.path.relative_to(root))
        except ValueError:
            shown = str(self.path)
        return {
            "level": self.level,
            "code": self.code,
            "file": shown,
            "line": self.line,
            "message": self.message,
        }


@dataclass
class Heading:
    level: int
    text: str
    line: int
    number: tuple[int, ...] | None = None


@dataclass
class Table:
    start: int
    end: int
    columns: int
    rows: list[tuple[int, list[str]]] = field(default_factory=list)
    caption: str | None = None
    caption_line: int | None = None
    number: int | None = None


@dataclass
class Doc:
    path: Path
    text: str
    lines: list[str]
    masked: list[str]
    defs: dict[str, int] = field(default_factory=dict)
    refs: dict[str, list[int]] = field(default_factory=dict)
    headings: list[Heading] = field(default_factory=list)
    tables: list[Table] = field(default_factory=list)
    words: int = 0


@dataclass
class Stats:
    files: int = 0
    words: int = 0
    notes: int = 0
    tables: int = 0
    links: int = 0


# ---------------------------------------------------------------------------
# File manifest


def expected_files(root: Path) -> list[Path]:
    """Return the stable Stage 2 file manifest from AGENTS.md section 1."""
    base = root / CHAPTERS
    files = [base / "00-introduction.md"]
    files += [base / f"{n:02d}-chapter-{n}.md" for n in range(1, 51)]
    files += [
        base / "51-appendix-a.md",
        base / "52-appendix-b.md",
        base / "53-appendix-c.md",
        base / "54-appendix-d.md",
        base / "55-appendix-e.md",
    ]
    return files


def expected_prefix(path: Path) -> str | None:
    name = path.name
    if name == "00-introduction.md":
        return "intro-"
    match = re.fullmatch(r"(\d{2})-chapter-\d+\.md", name)
    if match:
        return f"ch{match.group(1)}-"
    match = re.fullmatch(r"5[1-5]-appendix-([a-e])\.md", name)
    if match:
        return f"app-{match.group(1)}-"
    return None


# ---------------------------------------------------------------------------
# Masking and parsing


def mask_document(text: str) -> list[str]:
    """Return lines with code spans, link targets, and URLs blanked out.

    Length is preserved so column positions and line numbers remain valid.
    """
    lines = text.splitlines()
    out: list[str] = []
    in_fence = False
    fence = ""
    for line in lines:
        stripped = line.lstrip()
        if stripped.startswith("```") or stripped.startswith("~~~"):
            marker = stripped[:3]
            if not in_fence:
                in_fence, fence = True, marker
                out.append(" " * len(line))
                continue
            if marker == fence:
                in_fence = False
                out.append(" " * len(line))
                continue
        if in_fence:
            out.append(" " * len(line))
            continue
        masked = re.sub(r"`[^`]*`", lambda m: " " * len(m.group(0)), line)
        masked = re.sub(
            r"\]\([^)]*\)",
            lambda m: "](" + " " * (len(m.group(0)) - 3) + ")",
            masked,
        )
        masked = re.sub(r"https?://\S+", lambda m: " " * len(m.group(0)), masked)
        out.append(masked)
    return out


DEF_RE = re.compile(r"^\[\^([^\]\s]+)\]:")
REF_RE = re.compile(r"\[\^([^\]\s]+)\](?!:)")


def parse_document(path: Path) -> Doc:
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()
    masked = mask_document(text)
    doc = Doc(path=path, text=text, lines=lines, masked=masked)

    for i, line in enumerate(masked, start=1):
        match = DEF_RE.match(line)
        if match:
            doc.defs[match.group(1)] = i
        for ref in REF_RE.finditer(line):
            doc.refs.setdefault(ref.group(1), []).append(i)

    doc.headings = parse_headings(masked)
    doc.tables = parse_tables(lines, masked)
    doc.words = count_words(masked, doc.defs)
    return doc


def parse_headings(masked: list[str]) -> list[Heading]:
    headings: list[Heading] = []
    for i, line in enumerate(masked, start=1):
        match = re.match(r"^(#{1,6})\s+(.*?)\s*#*\s*$", line)
        if not match:
            continue
        level = len(match.group(1))
        text = match.group(2).strip()
        number = None
        numbered = re.match(r"^(\d+(?:\.\d+)*)\.\s+", text)
        if numbered:
            number = tuple(int(part) for part in numbered.group(1).split("."))
        headings.append(Heading(level=level, text=text, line=i, number=number))
    return headings


def split_row(line: str) -> list[str]:
    value = line.strip()
    while value.startswith(">"):
        value = value[1:].lstrip()
    if value.startswith("|"):
        value = value[1:]
    if value.endswith("|"):
        value = value[:-1]
    return [cell.strip() for cell in re.split(r"(?<!\\)\|", value)]


def is_separator(cells: list[str]) -> bool:
    if not cells:
        return False
    return all(re.fullmatch(r":?-{3,}:?", cell.replace(" ", "")) for cell in cells)


def parse_tables(lines: list[str], masked: list[str]) -> list[Table]:
    tables: list[Table] = []
    i = 0
    while i < len(lines) - 1:
        if "|" not in masked[i] or "|" not in masked[i + 1]:
            i += 1
            continue
        header = split_row(masked[i])
        separator = split_row(masked[i + 1])
        if is_separator(header) or not is_separator(separator):
            i += 1
            continue
        columns = len(header)
        table = Table(start=i + 1, end=i + 2, columns=columns)
        j = i + 2
        while j < len(lines) and "|" in masked[j] and masked[j].strip():
            if masked[j].lstrip().startswith("#"):
                break
            table.rows.append((j + 1, split_row(masked[j])))
            table.end = j + 1
            j += 1
        tables.append(table)
        i = max(j, i + 2)
    return tables


def count_words(lines: list[str], defs: dict[str, int]) -> int:
    """Count body words, excluding fenced code and footnote definitions."""
    text_lines: list[str] = []
    in_fence = False
    fence = ""
    def_lines = set()
    for key, start in defs.items():
        def_lines.add(start)
        n = start
        while n < len(lines):
            line = lines[n]
            if line.strip() and not line.startswith((" ", "\t")):
                break
            if line.strip():
                def_lines.add(n + 1)
            n += 1
    for i, line in enumerate(lines, start=1):
        stripped = line.lstrip()
        if stripped.startswith("```") or stripped.startswith("~~~"):
            marker = stripped[:3]
            if not in_fence:
                in_fence, fence = True, marker
                continue
            if marker == fence:
                in_fence = False
                continue
        if in_fence or i in def_lines:
            continue
        if "|" in line and is_separator(split_row(line)):
            continue
        line = REF_RE.sub("", line)
        text_lines.append(line)
    words = re.findall(r"[\w’'-]+", "\n".join(text_lines), re.UNICODE)
    return len(words)


# ---------------------------------------------------------------------------
# Checks


class Checker:
    def __init__(self, root: Path):
        self.root = root
        self.issues: list[Issue] = []
        self.stats = Stats()

    def add(self, level: str, code: str, path: Path, line: int, message: str) -> None:
        self.issues.append(Issue(level, code, path, line, message))

    # -- per-file checks ---------------------------------------------------

    def check_doc(self, doc: Doc) -> None:
        self.stats.files += 1
        self.stats.words += doc.words
        self.stats.notes += len(doc.defs)
        self.stats.tables += len(doc.tables)
        self.check_title(doc)
        self.check_headings(doc)
        self.check_tables(doc)
        self.check_typography(doc)
        self.check_definitions(doc)
        self.check_links(doc)

    def check_title(self, doc: Doc) -> None:
        first = next((i for i, line in enumerate(doc.lines) if line.strip()), None)
        if first is None:
            self.add("error", "file-empty", doc.path, 1, "file is empty")
            return
        line = doc.lines[first]
        if not re.match(r"^#\s+\S", line):
            self.add(
                "error",
                "title-missing",
                doc.path,
                first + 1,
                "first nonblank line must be a level-one heading",
            )
        h1s = [h for h in doc.headings if h.level == 1]
        if len(h1s) != 1:
            self.add(
                "error",
                "title-count",
                doc.path,
                h1s[1].line if len(h1s) > 1 else 1,
                f"expected exactly one level-one heading, found {len(h1s)}",
            )

    def check_headings(self, doc: Doc) -> None:
        previous = 0
        numbered_h2: list[Heading] = []
        for heading in doc.headings:
            if previous and heading.level > previous + 1:
                self.add(
                    "error",
                    "heading-skip",
                    doc.path,
                    heading.line,
                    f"heading level jumps from {previous} to {heading.level}",
                )
            previous = heading.level
            if heading.level == 2 and heading.number and len(heading.number) == 1:
                numbered_h2.append(heading)
            if heading.level == 3 and heading.number and len(heading.number) == 2:
                if not numbered_h2:
                    self.add(
                        "error",
                        "subsection-orphan",
                        doc.path,
                        heading.line,
                        "numbered subsection has no numbered section",
                    )
                elif heading.number[0] != numbered_h2[-1].number[0]:
                    self.add(
                        "error",
                        "subsection-parent",
                        doc.path,
                        heading.line,
                        f"subsection {heading.number[0]}.{heading.number[1]} "
                        f"is under section {numbered_h2[-1].number[0]}",
                    )
        if numbered_h2:
            expected = list(range(1, len(numbered_h2) + 1))
            actual = [h.number[0] for h in numbered_h2]
            if actual != expected:
                first_bad = next(
                    (h for h, want in zip(numbered_h2, expected) if h.number[0] != want),
                    numbered_h2[-1],
                )
                self.add(
                    "error",
                    "section-sequence",
                    doc.path,
                    first_bad.line,
                    f"numbered sections are {actual}, expected {expected}",
                )
            current = None
            seen: Counter[int] = Counter()
            for heading in [
                h
                for h in doc.headings
                if h.level == 3 and h.number and len(h.number) == 2
            ]:
                parent = heading.number[0]
                if parent != current:
                    current = parent
                    seen = Counter()
                seen[parent] += 0
                expected_sub = seen[parent] + 1
                if heading.number[1] != expected_sub:
                    self.add(
                        "error",
                        "subsection-sequence",
                        doc.path,
                        heading.line,
                        f"subsection {parent}.{heading.number[1]} is out of order; "
                        f"expected {parent}.{expected_sub}",
                    )
                seen[parent] = heading.number[1]

    def check_tables(self, doc: Doc) -> None:
        for table in doc.tables:
            header = split_row(doc.masked[table.start - 1])
            separator = split_row(doc.masked[table.start])
            if len(header) != len(separator):
                self.add(
                    "error",
                    "table-header",
                    doc.path,
                    table.start,
                    f"header has {len(header)} cells but separator has {len(separator)}",
                )
            for line, cells in table.rows:
                if len(cells) != table.columns:
                    self.add(
                        "error",
                        "table-ragged",
                        doc.path,
                        line,
                        f"row has {len(cells)} cells; expected {table.columns}",
                    )
            if not table.rows:
                self.add(
                    "warning",
                    "table-empty",
                    doc.path,
                    table.start,
                    "table has no body rows",
                )
            self.find_caption(doc, table)
            if table.caption is None:
                self.add(
                    "info",
                    "table-uncaptioned",
                    doc.path,
                    table.start,
                    "table has no caption; treated as a planning table, not a registered manuscript table",
                )
                continue
            self.check_table_reference(doc, table)
            self.check_table_bold(doc, table)

    def find_caption(self, doc: Doc, table: Table) -> None:
        for offset in range(0, 5):
            index = table.end + offset
            if index >= len(doc.lines):
                break
            line = doc.lines[index].strip()
            if not line:
                continue
            match = re.match(r"^\*\*Caption\.\*\*", line)
            number_match = re.search(r"Table\s+(\d+)", line)
            if match:
                table.caption = line
                table.caption_line = index + 1
                if number_match:
                    table.number = int(number_match.group(1))
                return
            break

    def check_table_reference(self, doc: Doc, table: Table) -> None:
        if table.number is None:
            return
        pattern = re.compile(rf"\bTable\s+{table.number}\b")
        exclude = set(range(table.start, table.end + 1))
        if table.caption_line:
            exclude.add(table.caption_line)
        for i, line in enumerate(doc.masked, start=1):
            if i in exclude:
                continue
            if pattern.search(line):
                return
        self.add(
            "warning",
            "table-reference",
            doc.path,
            table.start,
            f"Table {table.number} is never cited in the surrounding text",
        )

    def check_table_bold(self, doc: Doc, table: Table) -> None:
        for line, cells in table.rows:
            if not cells:
                continue
            if not re.fullmatch(r"\*\*.+\*\*", cells[0]):
                self.add(
                    "warning",
                    "table-leading-cell",
                    doc.path,
                    line,
                    "leading cell is not bold",
                )

    def check_typography(self, doc: Doc) -> None:
        for i, line in enumerate(doc.masked, start=1):
            if '"' in line:
                self.add(
                    "error",
                    "straight-double-quote",
                    doc.path,
                    i,
                    "use curly quotation marks",
                )
            if "'" in line:
                self.add(
                    "error",
                    "straight-apostrophe",
                    doc.path,
                    i,
                    "use curly apostrophes",
                )
            if "..." in line:
                self.add(
                    "error",
                    "three-periods",
                    doc.path,
                    i,
                    "use the ellipsis character …",
                )
            if "\u00a0" in line:
                self.add(
                    "error",
                    "nonbreaking-space",
                    doc.path,
                    i,
                    "use an ordinary space",
                )
            if line.rstrip("\n").endswith("  "):
                self.add(
                    "warning",
                    "hard-break",
                    doc.path,
                    i,
                    "paragraph ends with a Markdown hard break",
                )
            if re.search(r"\t", line):
                self.add("warning", "tab", doc.path, i, "line contains a tab")
            if re.search(r"\b(?:Chs?\.|pp?\.|pages?)\s*\d+-\d+", line):
                self.add(
                    "error",
                    "hyphen-range",
                    doc.path,
                    i,
                    "use an en dash in a range",
                )
            for match in re.finditer(r"(?<![\w-])(\d{4})-(\d{2}|\d{4})(?![\w-])", line):
                tail = line[match.start() : match.end() + 1]
                if re.match(r"\d{4}-\d{2}-\d{2}", tail):
                    continue
                self.add(
                    "error",
                    "hyphen-range",
                    doc.path,
                    i,
                    f"use an en dash in the range {match.group(0)}",
                )
            if re.search(r"(?<!-)(?<!---)--(?!-)(?!-)", line):
                self.add(
                    "warning",
                    "double-hyphen",
                    doc.path,
                    i,
                    "use an em dash or en dash, not --",
                )

    def check_definitions(self, doc: Doc) -> None:
        if not doc.defs:
            return
        first_def = min(doc.defs.values())
        for i, line in enumerate(doc.lines, start=1):
            if i <= first_def or not line.strip():
                continue
            if DEF_RE.match(line):
                continue
            if line.startswith((" ", "\t")):
                continue
            self.add(
                "error",
                "content-after-notes",
                doc.path,
                i,
                "content appears after the footnote definitions",
            )
            break

        for key, start in doc.defs.items():
            if re.fullmatch(r"\d+", key):
                self.add(
                    "error",
                    "note-numeric-key",
                    doc.path,
                    start,
                    f"footnote key {key!r} is numeric; use a descriptive key",
                )
            prefix = expected_prefix(doc.path)
            if prefix and not key.startswith(prefix):
                self.add(
                    "warning",
                    "note-prefix",
                    doc.path,
                    start,
                    f"footnote key {key!r} does not start with {prefix!r}",
                )
            block = definition_block(doc.lines, start)
            body = block.split("]:", 1)[-1].lstrip()
            if re.search(r"\bibid\.?\b", block, re.IGNORECASE):
                self.add(
                    "error",
                    "note-ibid",
                    doc.path,
                    start,
                    "do not use ibid.; give the short citation",
                )
            for ref in REF_RE.finditer(block):
                self.add(
                    "error",
                    "note-nested-reference",
                    doc.path,
                    start,
                    f"definition for {key!r} contains a footnote reference",
                )
            if not body.startswith("Editorial check") and (
                "http" in block or "doi:" in block
            ):
                if "Used for:" not in block:
                    self.add(
                        "warning",
                        "note-used-for",
                        doc.path,
                        start,
                        f"citation note {key!r} has no 'Used for:' annotation",
                    )

        common = set(doc.defs) & set(doc.refs)
        if not common:
            return
        # Rendered note numbering follows first reference; Pandoc controls that
        # order. Source-file definition order is not a requirement.

    def check_links(self, doc: Doc) -> None:
        for i, line in enumerate(doc.lines, start=1):
            if not line.strip() or doc.masked[i - 1].strip() == "":
                continue
            for match in re.finditer(r"\[[^\]]*\]\(([^)]+)\)", line):
                if match.start() > 0 and line[match.start() - 1] == "!":
                    continue
                target = match.group(1).strip()
                if target.startswith("<") and target.endswith(">"):
                    target = target[1:-1]
                target = target.split()[0] if target else ""
                if not target or target.startswith(
                    ("http://", "https://", "mailto:", "tel:", "#")
                ):
                    continue
                self.stats.links += 1
                path_part, _, anchor = target.partition("#")
                path_part = unquote(path_part)
                if not path_part:
                    target_path = doc.path
                else:
                    target_path = (doc.path.parent / path_part).resolve()
                if not target_path.exists():
                    self.add(
                        "error",
                        "link-missing",
                        doc.path,
                        i,
                        f"link target does not exist: {target}",
                    )
                    continue
                if anchor:
                    self.check_anchor(doc, i, target_path, anchor, target)

    def check_anchor(
        self, doc: Doc, line: int, target_path: Path, anchor: str, target: str
    ) -> None:
        try:
            text = target_path.read_text(encoding="utf-8")
        except (OSError, UnicodeDecodeError):
            return
        slugs = set()
        for heading_line in mask_document(text):
            match = re.match(r"^#{1,6}\s+(.*?)\s*#*\s*$", heading_line)
            if match:
                slugs.add(slugify(match.group(1)))
        if anchor not in slugs:
            self.add(
                "warning",
                "link-anchor",
                doc.path,
                line,
                f"link anchor not found in target: {target}",
            )

    # -- cross-file checks -------------------------------------------------

    def check_notes(self, docs: list[Doc]) -> None:
        definitions: dict[str, list[tuple[Path, int]]] = defaultdict(list)
        references: dict[str, list[tuple[Path, int]]] = defaultdict(list)
        for doc in docs:
            for key, line in doc.defs.items():
                definitions[key].append((doc.path, line))
            for key, lines in doc.refs.items():
                for line in lines:
                    references[key].append((doc.path, line))
        for key, places in definitions.items():
            if len(places) > 1:
                path, line = places[1]
                first = places[0]
                self.add(
                    "error",
                    "note-duplicate-definition",
                    path,
                    line,
                    f"footnote {key!r} is already defined at "
                    f"{first[0].name}:{first[1]}",
                )
        for key, places in references.items():
            if key not in definitions:
                path, line = places[0]
                self.add(
                    "error",
                    "note-missing-definition",
                    path,
                    line,
                    f"footnote {key!r} has no definition",
                )
        for key, places in definitions.items():
            if key not in references:
                path, line = places[0]
                self.add(
                    "error",
                    "note-unused-definition",
                    path,
                    line,
                    f"footnote {key!r} is defined but never referenced",
                )

    def check_sources_heading(self, doc: Doc) -> None:
        for i, line in enumerate(doc.masked, start=1):
            if re.match(
                r"^#{1,6}\s+(?:Sources|References|Bibliography|Works Cited)\s*$",
                line,
                re.IGNORECASE,
            ):
                self.add(
                    "error",
                    "separate-sources",
                    doc.path,
                    i,
                    "citations belong in the combined footnote list, not a separate list",
                )


def definition_block(lines: list[str], start: int) -> str:
    selected = [lines[start - 1]]
    n = start
    while n < len(lines):
        line = lines[n]
        if line.strip() and not line.startswith((" ", "\t")):
            break
        selected.append(line)
        n += 1
    return "\n".join(selected)


def slugify(text: str) -> str:
    text = re.sub(r"[`*_~\[\]()]", "", text)
    text = unicodedata.normalize("NFKD", text)
    text = text.lower()
    text = re.sub(r"[^\w\s-]", "", text)
    text = re.sub(r"[\s]+", "-", text).strip("-")
    return text


# ---------------------------------------------------------------------------
# Runner


def run(
    paths: list[Path], root: Path, full_manifest: bool = False
) -> Checker:
    checker = Checker(root)
    docs: list[Doc] = []
    for path in paths:
        if not path.exists():
            checker.add("error", "file-missing", path, 1, "manuscript file is missing")
            continue
        docs.append(parse_document(path))
    for doc in docs:
        checker.check_doc(doc)
        checker.check_sources_heading(doc)
    checker.check_notes(docs)
    if full_manifest:
        found = {path.resolve() for path in paths}
        extras = sorted(
            p
            for p in (root / CHAPTERS).glob("*.md")
            if p.resolve() not in found
        )
        for path in extras:
            checker.add(
                "warning",
                "file-extra",
                path,
                1,
                "file is not part of the stable manifest",
            )
    return checker


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Check the manuscript for structural, citation, table, link, and style problems.",
    )
    parser.add_argument(
        "paths",
        nargs="*",
        help="manuscript files to check; default is the full stable manifest",
    )
    parser.add_argument(
        "--root",
        type=Path,
        default=ROOT,
        help="repository root (default: parent of this script)",
    )
    parser.add_argument(
        "--strict",
        action="store_true",
        help="treat warnings as failures",
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="emit a JSON report",
    )
    parser.add_argument(
        "--quiet",
        action="store_true",
        help="print only errors and the summary",
    )
    args = parser.parse_args(argv)

    root = args.root.resolve()
    if args.paths:
        paths = [
            Path(p) if Path(p).is_absolute() else (root / p) for p in args.paths
        ]
        full_manifest = False
    else:
        paths = expected_files(root)
        full_manifest = True

    checker = run(paths, root, full_manifest)
    errors = [issue for issue in checker.issues if issue.level == "error"]
    warnings = [issue for issue in checker.issues if issue.level == "warning"]
    infos = [issue for issue in checker.issues if issue.level == "info"]
    failed = bool(errors) or (args.strict and bool(warnings))

    if args.json:
        payload = {
            "ok": not failed,
            "root": str(root),
            "stats": {
                "files": checker.stats.files,
                "words": checker.stats.words,
                "notes": checker.stats.notes,
                "tables": checker.stats.tables,
                "links": checker.stats.links,
            },
            "counts": {
                "errors": len(errors),
                "warnings": len(warnings),
                "info": len(infos),
            },
            "issues": [issue.as_dict(root) for issue in checker.issues],
        }
        print(json.dumps(payload, indent=2, ensure_ascii=False))
    else:
        if not args.quiet:
            for issue in checker.issues:
                if issue.level == "info":
                    continue
                try:
                    shown = issue.path.relative_to(root)
                except ValueError:
                    shown = issue.path
                print(
                    f"{issue.level.upper()} {shown}:{issue.line}: "
                    f"[{issue.code}] {issue.message}"
                )
        if errors and not args.quiet:
            print()
        for issue in infos:
            if args.quiet:
                break
            try:
                shown = issue.path.relative_to(root)
            except ValueError:
                shown = issue.path
            print(f"INFO {shown}:{issue.line}: [{issue.code}] {issue.message}")
        print(
            f"{checker.stats.files} file{'s' if checker.stats.files != 1 else ''}, "
            f"{checker.stats.words:,} words, "
            f"{checker.stats.notes} notes, {checker.stats.tables} tables, "
            f"{checker.stats.links} local links; "
            f"{len(errors)} errors, {len(warnings)} warnings"
        )
        if failed:
            print("check_book: FAIL")
        else:
            print("check_book: OK")

    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
