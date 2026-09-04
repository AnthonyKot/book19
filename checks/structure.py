#!/usr/bin/env python3
"""Local release checks for Book 19 (ported from Book 18). No network access required."""

from __future__ import annotations

import csv
import re
import sys
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ESSAYS = {
    "01": "01-cell-file.html",
    "02": "02-border-files.html",
    "03": "03-joinery-steel-dossier.html",
    "04": "04-spray-crew-file.html",
    "05": "05-owner-independent-acquisition.html",
    "06": "06-certified-inspection-microfirm.html",
}
REQUIRED_CLASSES = (
    "proposition",
    "changed",
    "whyyou",
    "sale",
    "economics",
    "scale",
    "competition",
    "counter",
    "monday",
    "verdict-box",
    "reading",
    "chapter-nav",
)
ALLOWED_VERDICTS = (
    "TEST NOW",
    "TEST THROUGH A PARTNER",
    "WATCH",
    "ACQUIRE, DO NOT BUILD",
    "DO NOT ENTER",
)


class Parser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.classes: set[str] = set()
        self.links: list[str] = []
        self.text: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        values = dict(attrs)
        self.classes.update((values.get("class") or "").split())
        if tag == "a" and values.get("href"):
            self.links.append(values["href"] or "")

    def handle_data(self, data: str) -> None:
        self.text.append(data)


def claim_rows(path: Path) -> dict[str, str]:
    rows: dict[str, str] = {}
    with path.open(newline="", encoding="utf-8") as handle:
        for row in csv.reader(handle, delimiter="\t"):
            if not row or row[0].strip().lower() == "id":
                continue
            if len(row) != 5:
                raise ValueError(f"{path}: expected 5 columns, got {len(row)}")
            claim_id, _, _, _, status = (cell.strip() for cell in row)
            if claim_id in rows:
                raise ValueError(f"{path}: duplicate claim id {claim_id}")
            rows[claim_id] = status
    return rows


def local_target(source: Path, href: str) -> Path | None:
    if not href or href.startswith(("http://", "https://", "mailto:", "#")):
        return None
    return (source.parent / href.split("#", 1)[0]).resolve()


def main() -> int:
    selected = set(sys.argv[1:]) or set(ESSAYS)
    unknown = selected - set(ESSAYS)
    if unknown:
        print(f"unknown essay numbers: {', '.join(sorted(unknown))}")
        return 2

    failures: list[str] = []
    warnings: list[str] = []

    for number in sorted(selected):
        chapter = ROOT / "chapters" / ESSAYS[number]
        ledger = ROOT / "checks" / "claims" / f"{number}.tsv"
        sources = ROOT / "resources" / "sources" / number / "SOURCES.md"
        for needed in (chapter, ledger, sources):
            if not needed.exists():
                failures.append(f"{number}: missing {needed.relative_to(ROOT)}")
        if not all(path.exists() for path in (chapter, ledger, sources)):
            continue

        html = chapter.read_text(encoding="utf-8")
        parser = Parser()
        try:
            parser.feed(html)
        except Exception as exc:
            failures.append(f"{number}: HTML parser error: {exc}")
            continue

        missing_classes = set(REQUIRED_CLASSES) - parser.classes
        if missing_classes:
            failures.append(f"{number}: missing classes {', '.join(sorted(missing_classes))}")

        plain = re.sub(r"\s+", " ", " ".join(parser.text)).strip()
        count = len(re.findall(r"\b[\w'’-]+\b", plain))
        if count < 2400 or count > 3600:
            warnings.append(f"{number}: {count} visible words (target 2400–3600)")

        if not any(verdict in plain for verdict in ALLOWED_VERDICTS):
            failures.append(f"{number}: no exact provisional verdict")

        markers = re.findall(r"<!--\s*CHECK:\s*([A-Za-z0-9._:-]+)\s*-->", html)
        # One claim may support more than one nearby sentence. The ledger id is unique;
        # repeated prose markers are intentional and still resolve to that one row.
        try:
            rows = claim_rows(ledger)
        except ValueError as exc:
            failures.append(str(exc))
            rows = {}
        for claim_id in markers:
            if claim_id not in rows:
                failures.append(f"{number}: CHECK {claim_id} missing from ledger")
        for claim_id, status in rows.items():
            if status not in {"verified", "inference", "open"} and not re.fullmatch(r"checked-by:[^:]+:\d{4}-\d{2}-\d{2}", status):
                failures.append(f"{number}: {claim_id} has invalid status {status!r}")
            if status == "open":
                failures.append(f"{number}: {claim_id} remains open")
        if rows and not markers:
            failures.append(f"{number}: ledger exists but prose has no CHECK markers")

        source_text = sources.read_text(encoding="utf-8")
        if len(re.findall(r"https?://", source_text)) < 3:
            failures.append(f"{number}: source index has fewer than 3 URLs")

        for href in parser.links:
            target = local_target(chapter, href)
            if target is not None and not target.exists():
                failures.append(f"{number}: broken local link {href}")

        print(f"{number}: {count} words, {len(markers)} claim markers ({len(set(markers))} unique), {len(rows)} ledger rows")

    for page in (ROOT / "index.html", ROOT / "about.html", ROOT / "static" / "style.css", ROOT / "static" / "theme.js"):
        if not page.exists():
            failures.append(f"missing shared file {page.relative_to(ROOT)}")

    for warning in warnings:
        print(f"WARNING: {warning}")
    if failures:
        for failure in failures:
            print(f"FAIL: {failure}")
        return 1
    print("Book 18 checks passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
