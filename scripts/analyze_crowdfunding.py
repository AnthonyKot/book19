#!/usr/bin/env python3
"""Build traceable crowdfunding tables from the published Web Robots archives.

No network calls. Python standard library only. Run from the repository root:
    python3 scripts/analyze_crowdfunding.py
"""

from __future__ import annotations

import csv
import io
import json
import re
import sys
import zipfile
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "resources" / "data"
OUT = ROOT / "drafts" / "reviews"
FETCH_CUTOFF = datetime(2026, 9, 3, 23, 59, 59, tzinfo=timezone.utc).timestamp()
EU27 = {
    "AT", "BE", "BG", "HR", "CY", "CZ", "DK", "EE", "FI", "FR", "DE",
    "GR", "HU", "IE", "IT", "LV", "LT", "LU", "MT", "NL", "PL", "PT",
    "RO", "SK", "SI", "ES", "SE",
}

# Explicitly physical subcategories. Broad media categories are not inferred to
# have physical rewards. Tabletop/playing-card campaigns are tangible products.
PHYSICAL_SUBCATEGORIES = {
    "3D Printing", "Accessories", "Apparel", "Bacon", "Beer", "Candles",
    "Ceramics", "Childrenswear", "Coffee", "Cookbooks", "Couture", "Crochet",
    "DIY", "DIY Electronics", "Embroidery", "Fabrication Tools", "Fashion",
    "Footwear", "Gadgets", "Glass", "Hardware", "Jewelry", "Knitting",
    "Pet Fashion", "Playing Cards", "Pottery", "Printing", "Product Design",
    "Quilts", "Ready-to-wear", "Robots", "Small Batch", "Sound", "Stationery",
    "Tabletop Games", "Taxidermy", "Vegan", "Wearables", "Weaving", "Woodworking",
}
PHYSICAL_TECH = {
    "Camera Equipment", "Flight",
}
INDIEGOGO_PHYSICAL = {
    "Audio", "Camera Gear", "Energy & Green Tech", "Fashion & Wearables",
    "Food & Beverages", "Health & Fitness", "Home", "Phones & Accessories",
    "Productivity", "Transportation", "Travel & Outdoors", "Innovative Products",
}
PROVEN_FIELDS = [
    "platform", "project_id", "title", "creator", "country", "year", "category",
    "parent_category", "launched_date", "deadline_date", "raised_usd", "backers", "currency", "state",
    "compliance_flags", "url", "source_archive", "amount_basis", "backers_basis",
]


def as_int(value: str | None) -> int:
    try:
        return int(float(value or 0))
    except (TypeError, ValueError):
        return 0


def as_float(value: str | None) -> float:
    try:
        return float(value or 0)
    except (TypeError, ValueError):
        return 0.0


def unix_year(value: str | None) -> int | None:
    try:
        stamp = float(value or 0)
        if stamp <= 0 or stamp > FETCH_CUTOFF:
            return None
        return datetime.fromtimestamp(stamp, tz=timezone.utc).year
    except (TypeError, ValueError, OSError):
        return None


def unix_date(value: str | None) -> str:
    try:
        stamp = float(value or 0)
        return datetime.fromtimestamp(stamp, tz=timezone.utc).date().isoformat() if stamp > 0 else ""
    except (TypeError, ValueError, OSError):
        return ""


def iso_year(value: str | None) -> int | None:
    if not value or value == "null":
        return None
    match = re.search(r"(20\d{2})", value)
    return int(match.group(1)) if match else None


def json_field(value: str | None) -> dict:
    try:
        result = json.loads(value or "{}")
        return result if isinstance(result, dict) else {}
    except json.JSONDecodeError:
        return {}


def kickstarter_physical(category: dict, title: str) -> bool:
    name = category.get("name", "")
    parent = category.get("parent_name", "")
    title_lc = title.lower()
    return name in PHYSICAL_SUBCATEGORIES or name in PHYSICAL_TECH or (
        parent == "Technology" and name not in {"Apps", "Software", "Web"}
    ) or (name == "Space Exploration" and any(word in title_lc for word in ("telescope", "satellite", "rocket", "hardware")))


def read_kickstarter() -> tuple[dict[str, dict], dict[str, int]]:
    projects: dict[str, dict] = {}
    stats: dict[str, int] = defaultdict(int)
    archives = [
        (DATA / "Kickstarter_2023-12-14.zip", "2023 baseline"),
        (DATA / "Kickstarter_2026-08-12.zip", "2026 latest"),
    ]
    for archive, label in archives:
        with zipfile.ZipFile(archive) as zf:
            for member in zf.namelist():
                if not member.lower().endswith(".csv"):
                    continue
                with zf.open(member) as raw:
                    reader = csv.DictReader(io.TextIOWrapper(raw, encoding="utf-8-sig", newline=""))
                    for row in reader:
                        stats[f"{label}: raw rows"] += 1
                        year = unix_year(row.get("launched_at"))
                        if year is None or not 2023 <= year <= 2026:
                            continue
                        category = json_field(row.get("category"))
                        if not kickstarter_physical(category, row.get("name", "")):
                            continue
                        project_id = row.get("id", "")
                        if not project_id:
                            continue
                        creator = json_field(row.get("creator"))
                        urls = json_field(row.get("urls"))
                        project_url = urls.get("web", {}).get("project", "")
                        record = {
                            "platform": "Kickstarter",
                            "project_id": project_id,
                            "title": row.get("name", "").strip(),
                            "creator": creator.get("name", ""),
                            "country": row.get("country", ""),
                            "year": year,
                            "category": category.get("name", "Unknown"),
                            "parent_category": category.get("parent_name") or category.get("name", "Unknown"),
                            "launched_date": unix_date(row.get("launched_at")),
                            "deadline_date": unix_date(row.get("deadline")),
                            "state": row.get("state", ""),
                            "raised_usd": as_int(row.get("converted_pledged_amount")),
                            "backers": as_int(row.get("backers_count")),
                            "goal_native": as_float(row.get("goal")),
                            "currency": row.get("currency", ""),
                            "launched_at": row.get("launched_at", ""),
                            "deadline": row.get("deadline", ""),
                            "url": project_url,
                            "source_archive": archive.name,
                        }
                        # Baseline is read first; latest replaces it when present.
                        if project_id in projects:
                            stats[f"{label}: duplicate IDs"] += 1
                        projects[project_id] = record
    stats["deduplicated physical Kickstarter projects, 2023-2026"] = len(projects)
    return projects, dict(stats)


def read_indiegogo() -> tuple[dict[str, dict], dict[str, int]]:
    projects: dict[str, dict] = {}
    stats: dict[str, int] = defaultdict(int)
    archive = DATA / "Indiegogo_2025-10-13.zip"
    with zipfile.ZipFile(archive) as zf:
        with zf.open("Indiegogo.csv") as raw:
            reader = csv.DictReader(io.TextIOWrapper(raw, encoding="utf-8-sig", newline=""))
            for row in reader:
                stats["raw rows"] += 1
                category = row.get("category", "").strip()
                if category not in INDIEGOGO_PHYSICAL:
                    continue
                year = iso_year(row.get("open_date")) or iso_year(row.get("close_date"))
                if year is None or not 2023 <= year <= 2026:
                    continue
                project_id = row.get("project_id", "")
                if not project_id:
                    continue
                percent = as_float(row.get("funds_raised_percent"))
                close_date = row.get("close_date", "")
                state = "live/indemand" if close_date in {"", "null"} else ("successful" if percent >= 100 else "failed")
                record = {
                    "platform": "Indiegogo",
                    "project_id": project_id,
                    "title": row.get("title", "").strip(),
                    "creator": row.get("offered_by", "").strip(),
                    "country": "not published in dataset",
                    "year": year,
                    "category": category,
                    "parent_category": category,
                    "launched_date": row.get("open_date", ""),
                    "deadline_date": close_date,
                    "state": state,
                    "raised_usd": as_int(row.get("funds_raised_amount")) if row.get("currency") == "USD" else 0,
                    "raised_native": as_int(row.get("funds_raised_amount")),
                    "backers": as_int(row.get("perks_claimed")),
                    "currency": row.get("currency", ""),
                    "open_date": row.get("open_date", ""),
                    "close_date": close_date,
                    "url": row.get("clickthrough_url", ""),
                    "source_archive": archive.name,
                }
                if project_id in projects:
                    stats["duplicate IDs"] += 1
                projects[project_id] = record
    stats["deduplicated physical Indiegogo projects, 2023-2026"] = len(projects)
    return projects, dict(stats)


def read_manual_proven() -> list[dict]:
    """Read threshold-qualified projects from public pages not in Web Robots."""
    path = DATA / "manual-proven-products.csv"
    with path.open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def read_eu_checks() -> dict[tuple[str, str], dict]:
    path = DATA / "eu-seller-checks.csv"
    with path.open(encoding="utf-8", newline="") as handle:
        rows = list(csv.DictReader(handle))
    return {(row["platform"], row["project_id"]): row for row in rows}


def aggregate(records: list[dict], keys: tuple[str, ...]) -> list[dict]:
    groups: dict[tuple, dict] = {}
    for row in records:
        key = tuple(row[k] for k in keys)
        if key not in groups:
            groups[key] = {k: row[k] for k in keys} | {
                "completed": 0, "successful": 0, "failed": 0, "live_or_other": 0,
                "funded_usd_successful": 0, "backers_successful": 0,
            }
        group = groups[key]
        state = row["state"]
        if state in {"successful", "failed"}:
            group["completed"] += 1
            group[state] += 1
        else:
            group["live_or_other"] += 1
        if state == "successful":
            group["funded_usd_successful"] += row["raised_usd"]
            group["backers_successful"] += row["backers"]
    result = []
    for group in groups.values():
        completed = group["completed"]
        group["success_rate_completed_pct"] = round(100 * group["successful"] / completed, 2) if completed else ""
        result.append(group)
    return sorted(result, key=lambda r: tuple(str(r[k]) for k in keys))


def compliance_flags(row: dict) -> str:
    text = f"{row['title']} {row['category']} {row['parent_category']}".lower()
    flags = []
    electrical = row["parent_category"] == "Technology" or any(
        word in text for word in ("electric", "battery", "charger", "camera", "printer", "light", "audio", "smart", "robot")
    )
    connected = any(word in text for word in ("smart", "wifi", "wi-fi", "bluetooth", " app", "ai ", "camera", "wearable", "tracker"))
    toy = row["category"] in {"Tabletop Games", "Playing Cards"} or any(word in text for word in ("toy", "children", "kids"))
    ppe = any(word in text for word in ("helmet", "respirator", "protective", "ppe", "safety mask"))
    if electrical:
        flags.append("electrical/electronic")
    if connected:
        flags.append("connected/CRA-triage")
    if toy:
        flags.append("possible toy")
    if ppe:
        flags.append("possible PPE")
    return "; ".join(flags) or "GPSR/packaging only (initial triage)"


def write_csv(path: Path, rows: list[dict], fieldnames: list[str] | None = None) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if fieldnames is None:
        fieldnames = list(rows[0]) if rows else []
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames, extrasaction="ignore", lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def main() -> int:
    ks, ks_stats = read_kickstarter()
    igg, igg_stats = read_indiegogo()
    ks_rows = list(ks.values())
    igg_rows = list(igg.values())

    write_csv(OUT / "kickstarter-category-country.csv", aggregate(ks_rows, ("year", "country", "parent_category")))
    write_csv(OUT / "platform-category-summary.csv", aggregate(ks_rows + igg_rows, ("platform", "year", "parent_category")))

    proven = []
    for row in ks_rows + igg_rows:
        if row["state"] != "successful" or row["raised_usd"] < 250_000 or row["backers"] < 1_000:
            continue
        if row["platform"] == "Kickstarter" and row["country"] in EU27:
            continue
        item = dict(row)
        item["compliance_flags"] = compliance_flags(row)
        item["amount_basis"] = "Web Robots converted_pledged_amount (USD)" if row["platform"] == "Kickstarter" else "Web Robots USD-denominated row"
        item["backers_basis"] = "Web Robots backers_count" if row["platform"] == "Kickstarter" else "Web Robots perks_claimed"
        proven.append(item)
    for row in read_manual_proven():
        row["year"] = as_int(row["year"])
        row["raised_usd"] = as_int(row["raised_usd"])
        row["backers"] = as_int(row["backers"])
        proven.append(row)
    proven.sort(key=lambda r: (-r["raised_usd"], -r["backers"], r["title"]))
    write_csv(OUT / "proven-elsewhere.csv", proven, PROVEN_FIELDS)

    eu_checks = read_eu_checks()
    top_40 = []
    for row in proven[:40]:
        key = (row["platform"], str(row["project_id"]))
        if key not in eu_checks:
            raise ValueError(f"missing EU seller check for {key}")
        check = eu_checks[key]
        item = dict(row)
        if check.get("compliance_flags"):
            item["compliance_flags"] = check["compliance_flags"]
        item.update({k: v for k, v in check.items() if k not in {"platform", "project_id", "compliance_flags"}})
        top_40.append(item)
    check_fields = PROVEN_FIELDS + [
        "eu_seller_status", "eu_check_method", "eu_check_date", "evidence_url", "check_note",
    ]
    write_csv(OUT / "top-40-eu-check.csv", top_40, check_fields)

    audit = {
        "generated_at": "2026-09-03",
        "cutoff_utc": datetime.fromtimestamp(FETCH_CUTOFF, tz=timezone.utc).isoformat(),
        "kickstarter": ks_stats,
        "indiegogo": igg_stats,
        "qualifying_proven_elsewhere": len(proven),
        "manual_public_page_projects": len(read_manual_proven()),
        "top_40_rows": min(40, len(proven)),
        "notes": [
            "Kickstarter baseline is read first; a matching project in the latest archive replaces it.",
            "Success-rate denominator is successful + failed only.",
            "Kickstarter converted_pledged_amount is treated as USD; Indiegogo qualifies only USD rows.",
            "Indiegogo inferred outcome uses close_date plus funds_raised_percent because the archive has no state field.",
            "Indiegogo perks_claimed is blank/zero in the qualifying cohort, so it yields no threshold-qualified products and its backer totals are unavailable.",
            "Makuake JPY amounts are converted through the 2026-09-02 ECB cross-rate (EUR/USD 1.1578; EUR/JPY 184.78); badge counts are recorded as lower bounds.",
            "Compliance flags are keyword/category triage and are not legal conclusions.",
        ],
    }
    (OUT / "analysis-audit.json").write_text(json.dumps(audit, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps(audit, indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main())
