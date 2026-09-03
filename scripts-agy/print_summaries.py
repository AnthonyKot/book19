#!/usr/bin/env python3
import json

with open("drafts/reviews/agy/kickstarter_categories.json") as f:
    cats = json.load(f)

print("=== KICKSTARTER PHYSICAL CATEGORIES (2023-2026) ===")
print(f"{'Category':<15} | {'Projects':>8} | {'Success':>7} | {'Rate %':>7} | {'Total Pledged ($)':>18} | {'Backers':>10} | {'Avg ($)':>8}")
print("-" * 85)
for c in cats:
    print(f"{c['category']:<15} | {c['total_projects']:>8,d} | {c['successful_projects']:>7,d} | {c['success_rate_pct']:>6.1f}% | ${c['total_usd_pledged']:>16,.2f} | {c['total_backers']:>10,d} | ${c['avg_pledge_usd']:>7.2f}")

with open("drafts/reviews/agy/kickstarter_countries.json") as f:
    countries = json.load(f)

print("\n=== KICKSTARTER TOP COUNTRIES (PHYSICAL, 2023-2026) ===")
print(f"{'Country':<7} | {'Status':<7} | {'Projects':>8} | {'Success':>7} | {'Rate %':>7} | {'Total Pledged ($)':>18} | {'Backers':>10}")
print("-" * 80)
for c in countries[:18]:
    eu_str = "EU" if c['is_eu'] else "Non-EU"
    print(f"{c['country']:<7} | {eu_str:<7} | {c['total_projects']:>8,d} | {c['successful_projects']:>7,d} | {c['success_rate_pct']:>6.1f}% | ${c['total_usd_pledged']:>16,.2f} | {c['total_backers']:>10,d}")

with open("drafts/reviews/agy/indiegogo_categories.json") as f:
    igg_cats = json.load(f)

print("\n=== INDIEGOGO PHYSICAL CATEGORIES (2023-2026, NORMALIZED USD) ===")
print(f"{'Category':<22} | {'Projects':>8} | {'Total USD Raised':>18} | {'Avg USD/Project':>16}")
print("-" * 72)
for c in igg_cats:
    print(f"{c['category']:<22} | {c['total_projects']:>8,d} | ${c['total_usd_funds']:>16,.2f} | ${c['avg_usd_per_project']:>14,.2f}")
