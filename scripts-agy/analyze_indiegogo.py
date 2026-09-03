#!/usr/bin/env python3
"""
Analyze Indiegogo Web Robots scrape for 2023-2026 physical products.
Normalizes multi-currency pledges to USD, deduplicates projects,
filters physical categories, computes category statistics,
and identifies candidates with >= $250k raised.
"""

import zipfile
import csv
import io
import json
import os

FX_TO_USD = {
    "USD": 1.0, "EUR": 1.08, "GBP": 1.28, "CAD": 0.74, "AUD": 0.65,
    "HKD": 0.128, "SGD": 0.75, "JPY": 0.0067, "CHF": 1.13, "NZD": 0.60,
    "SEK": 0.095, "NOK": 0.093, "DKK": 0.145, "PLN": 0.25, "MXN": 0.055
}

PHYSICAL_IGG_CATEGORIES = {
    'Health & Fitness', 'Home', 'Fashion & Wearables', 'Travel & Outdoors',
    'Productivity', 'Phones & Accessories', 'Energy & Green Tech',
    'Food & Beverages', 'Audio', 'Transportation', 'Photography', 'Camera Gear'
}

def parse_year(date_str):
    if not date_str or date_str == 'null':
        return None
    try:
        return int(date_str[:4])
    except:
        return None

def main():
    zip_path = "resources/data-agy/Indiegogo_2025-10-13.zip"
    out_dir = "drafts/reviews/agy"
    os.makedirs(out_dir, exist_ok=True)

    unique_projects = {}

    with zipfile.ZipFile(zip_path, 'r') as z:
        with z.open("Indiegogo.csv") as f:
            reader = csv.DictReader(io.TextIOWrapper(f, encoding='utf-8', errors='replace'))
            for r in reader:
                pid = r.get('project_id')
                if not pid or pid in unique_projects:
                    continue

                cat = r.get('category', '')
                if cat not in PHYSICAL_IGG_CATEGORIES:
                    continue

                cur = r.get('currency', '')
                if cur not in FX_TO_USD:
                    continue

                open_d = r.get('open_date', '')
                close_d = r.get('close_date', '')
                y_open = parse_year(open_d)
                y_close = parse_year(close_d)

                # Filter 2023-2026
                in_range = False
                yr = None
                for y in [y_open, y_close]:
                    if y and 2023 <= y <= 2026:
                        in_range = True
                        yr = y
                        break

                if not in_range:
                    continue

                try:
                    raw_funds = float(r.get('funds_raised_amount', 0) or 0)
                except:
                    raw_funds = 0.0

                usd = raw_funds * FX_TO_USD[cur]

                perks_raw = r.get('perks_claimed', '')
                perks = 0
                if perks_raw and perks_raw != 'null':
                    try:
                        perks = int(float(perks_raw))
                    except:
                        perks = 0

                unique_projects[pid] = {
                    'project_id': pid,
                    'title': r.get('title', ''),
                    'tagline': r.get('tagline', ''),
                    'category': cat,
                    'currency': cur,
                    'raw_funds': raw_funds,
                    'usd_pledged': round(usd, 2),
                    'perks_claimed': perks,
                    'year': yr,
                    'open_date': open_d,
                    'close_date': close_d,
                    'product_stage': r.get('product_stage', ''),
                    'clickthrough_url': r.get('clickthrough_url', ''),
                    'source_url': r.get('source_url', '')
                }

    print(f"Unique physical Indiegogo projects (2023-2026): {len(unique_projects)}")

    cat_stats = {}
    for p in unique_projects.values():
        c = p['category']
        if c not in cat_stats:
            cat_stats[c] = {'total': 0, 'usd': 0.0, 'perks': 0}
        cat_stats[c]['total'] += 1
        cat_stats[c]['usd'] += p['usd_pledged']
        cat_stats[c]['perks'] += p['perks_claimed']

    cat_summary = []
    for c, s in sorted(cat_stats.items(), key=lambda x: x[1]['usd'], reverse=True):
        cat_summary.append({
            'category': c,
            'total_projects': s['total'],
            'total_usd_funds': round(s['usd'], 2),
            'total_perks_claimed': s['perks'],
            'avg_usd_per_project': round(s['usd'] / s['total'], 2) if s['total'] > 0 else 0
        })

    with open(os.path.join(out_dir, "indiegogo_categories.json"), "w", encoding="utf-8") as f:
        json.dump(cat_summary, f, indent=2)

    # Candidates: funds >= 250k
    candidates = [
        p for p in unique_projects.values()
        if p['usd_pledged'] >= 250000.0
    ]
    candidates.sort(key=lambda x: x['usd_pledged'], reverse=True)
    print(f"Indiegogo physical candidates (>= $250k USD): {len(candidates)}")

    with open(os.path.join(out_dir, "indiegogo_candidates.csv"), "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=[
            'project_id', 'title', 'category', 'currency', 'raw_funds',
            'usd_pledged', 'perks_claimed', 'year', 'open_date', 'close_date',
            'clickthrough_url', 'tagline'
        ], extrasaction='ignore')
        writer.writeheader()
        for cand in candidates:
            writer.writerow(cand)

    print("Indiegogo analysis complete! Outputs written to drafts/reviews/agy/.")

if __name__ == "__main__":
    main()
