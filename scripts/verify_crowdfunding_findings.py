#!/usr/bin/env python3
"""Fail if headline findings drift from the generated crowdfunding outputs."""

from __future__ import annotations

import csv
import re
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "drafts" / "reviews"


def rows(name: str) -> list[dict[str, str]]:
    with (OUT / name).open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def main() -> None:
    findings = (OUT / "crowdfunding-findings.md").read_text(encoding="utf-8")
    proven = rows("proven-elsewhere.csv")
    top = rows("top-40-eu-check.csv")

    assert len(proven) == 647
    assert len(top) == 40
    assert all(int(row["raised_usd"]) >= 250_000 and int(row["backers"]) >= 1_000 for row in proven)
    assert len({(row["platform"], row["project_id"]) for row in proven}) == len(proven)
    assert all(row["eu_check_date"] == "2026-09-03" and row["evidence_url"] for row in top)

    statuses = Counter(row["eu_seller_status"] for row in top)
    established = statuses["established EU channel"] + statuses["established direct EU channel"]
    direct_only = statuses["direct-to-EU only; no EU distributor found"]
    no_retail = statuses["no EU retail found"] + statuses["no EU retail yet"]
    assert (established, direct_only, no_retail) == (35, 2, 3)

    # Compare the 40 displayed amounts/backer counts, in rank order, with CSV.
    displayed = []
    for match in re.finditer(r"^\| (\d{1,2}) \| .*? \| .*? \| \$([\d,]+) \| ([\d,]+) \|", findings, re.MULTILINE):
        rank = int(match.group(1))
        if 1 <= rank <= 40:
            displayed.append((rank, int(match.group(2).replace(",", "")), int(match.group(3).replace(",", ""))))
    assert displayed == [(i, int(row["raised_usd"]), int(row["backers"])) for i, row in enumerate(top, 1)]

    by_id = {row["project_id"]: row for row in proven}
    for project_id in ("870254269", "1461739904", "134218902"):
        row = by_id[project_id]
        amount = f"${int(row['raised_usd']):,}"
        backers = f"{int(row['backers']):,}"
        assert amount in findings and backers in findings and row["launched_date"] in findings

    assert "JPY 208,802,697" in findings and "JPY 226,212,500" in findings
    print("validated 647 qualifying rows, top-40 figures, EU-status counts, and candidate headlines")


if __name__ == "__main__":
    main()
