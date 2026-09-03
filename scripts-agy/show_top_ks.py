#!/usr/bin/env python3
import csv

with open("drafts/reviews/agy/kickstarter_candidates.csv", "r", encoding="utf-8") as f:
    rows = list(csv.DictReader(f))

print(f"Total KS candidates: {len(rows)}")
print("\nTop 40 Kickstarter Candidates (>= $250k, >= 1000 backers, Non-EU, 2023-2026):")
for i, r in enumerate(rows[:40]):
    name = r["name"][:45]
    pcat = r["parent_category"][:12]
    country = r["country"]
    usd = float(r["effective_usd"])
    backers = int(r["backers_count"])
    ldate = r["launch_date"]
    print(f"{i+1:2d}. {name:<45} | {pcat:<12} | {country} | ${usd:>11,.0f} | {backers:>6,} | {ldate}")
