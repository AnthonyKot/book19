#!/usr/bin/env python3
"""
Analyze Kickstarter Web Robots scrape for 2023-2026 physical products.
Deduplicates projects, filters by date, categorizes physical goods,
computes category and country statistics, and extracts high-demand candidates
(>= $250k pledged, >= 1,000 backers, non-EU).
"""

import zipfile
import csv
import io
import json
import os
import datetime
from collections import defaultdict

# 2023-01-01 00:00:00 UTC to 2026-12-31 23:59:59 UTC
START_TS = 1672531200
END_TS = 1798761599

EU_COUNTRIES = {
    'AT', 'BE', 'BG', 'HR', 'CY', 'CZ', 'DK', 'EE', 'FI', 'FR',
    'DE', 'GR', 'HU', 'IE', 'IT', 'LV', 'LT', 'LU', 'MT', 'NL',
    'PL', 'PT', 'RO', 'SK', 'SI', 'ES', 'SE'
}

# Physical categories definition:
# Parent category -> list of allowed subcategory slugs/names (or None if all allowed)
# Exclude pure digital/services: apps, software, web, makerspaces, events, etc.
PHYSICAL_PARENT_MAP = {
    'Technology': {
        '3d printing', 'camera equipment', 'diy electronics', 'fabric tools',
        'flight', 'gadgets', 'hardware', 'robots', 'sound', 'space exploration',
        'wearables', 'technology'
    },
    'Design': {
        'product design', 'toys', 'design'
    },
    'Fashion': {
        'accessories', 'apparel', 'childrenswear', 'footwear', 'jewelry',
        'pet fashion', 'ready-to-wear', 'fashion'
    },
    'Crafts': {
        'candles', 'crochet', 'diy', 'embroidery', 'glass', 'knitting',
        'pottery', 'printing', 'stationery', 'taxidermy', 'weaving',
        'woodworking', 'crafts'
    },
    'Food': {
        'small batch', 'drinks', 'cookbooks', 'food'
    },
    'Photography': {
        'camera equipment', 'photobooks', 'photography'
    },
    'Games': {
        'tabletop games'  # physical games only
    }
}

DIGITAL_EXCLUDES = {
    'apps', 'software', 'web', 'makerspaces', 'video games', 'gaming hardware',
    'mobile games', 'live games', 'narrative games'
}

def is_physical(parent_name, sub_name, slug):
    slug_lower = (slug or '').lower()
    sub_lower = (sub_name or '').lower()
    parent_lower = (parent_name or '').lower()

    for exc in DIGITAL_EXCLUDES:
        if exc in slug_lower or exc in sub_lower:
            return False

    # Check parent
    for p_key, allowed_subs in PHYSICAL_PARENT_MAP.items():
        if p_key.lower() == parent_lower:
            if allowed_subs is None:
                return True
            for allowed in allowed_subs:
                if allowed in slug_lower or allowed in sub_lower:
                    return True
            return False

    return False

def main():
    zip_path = "resources/data-agy/Kickstarter_2026-08-12.zip"
    out_dir = "drafts/reviews/agy"
    os.makedirs(out_dir, exist_ok=True)

    print(f"Reading {zip_path}...")
    unique_projects = {}

    with zipfile.ZipFile(zip_path, 'r') as z:
        csv_names = [n for n in z.namelist() if n.endswith('.csv')]
        print(f"Found {len(csv_names)} CSV chunks.")
        for idx, name in enumerate(csv_names):
            if idx % 10 == 0:
                print(f"Processing chunk {idx}/{len(csv_names)}: {name}...")
            with z.open(name) as f:
                reader = csv.DictReader(io.TextIOWrapper(f, encoding='utf-8', errors='replace'))
                for row in reader:
                    pid = row.get('id')
                    if not pid:
                        continue
                    # If already seen, keep latest state_changed_at or deadline
                    if pid in unique_projects:
                        continue
                    
                    try:
                        launched_at = float(row.get('launched_at', 0))
                    except (ValueError, TypeError):
                        continue

                    # Filter date 2023-2026
                    if not (START_TS <= launched_at <= END_TS):
                        continue

                    # Parse category
                    cat_raw = row.get('category', '')
                    parent_name = ''
                    sub_name = ''
                    slug = ''
                    try:
                        c_obj = json.loads(cat_raw)
                        parent_name = c_obj.get('parent_name', '')
                        sub_name = c_obj.get('name', '')
                        slug = c_obj.get('slug', '')
                    except Exception:
                        pass

                    if not is_physical(parent_name, sub_name, slug):
                        continue

                    unique_projects[pid] = {
                        'id': pid,
                        'name': row.get('name', ''),
                        'blurb': row.get('blurb', ''),
                        'parent_category': parent_name or slug.split('/')[0].capitalize(),
                        'sub_category': sub_name,
                        'slug': slug,
                        'country': row.get('country', ''),
                        'currency': row.get('currency', ''),
                        'goal': float(row.get('goal', 0) or 0),
                        'pledged': float(row.get('pledged', 0) or 0),
                        'usd_pledged': float(row.get('usd_pledged', 0) or 0),
                        'converted_pledged_amount': float(row.get('converted_pledged_amount', 0) or 0),
                        'backers_count': int(row.get('backers_count', 0) or 0),
                        'state': row.get('state', ''),
                        'launched_at': launched_at,
                        'deadline': float(row.get('deadline', 0) or 0),
                        'source_url': row.get('source_url', ''),
                        'urls': row.get('urls', '')
                    }

    print(f"Extracted {len(unique_projects)} unique physical-product projects (2023-2026).")

    # Category aggregates
    cat_stats = defaultdict(lambda: {'total': 0, 'successful': 0, 'usd_pledged': 0.0, 'backers': 0})
    # Country aggregates (for Kickstarter)
    country_stats = defaultdict(lambda: {'total': 0, 'successful': 0, 'usd_pledged': 0.0, 'backers': 0})

    proven_candidates = []

    for p in unique_projects.values():
        p_cat = p['parent_category'] or 'Other Physical'
        country = p['country'] or 'Unknown'
        is_succ = (p['state'] == 'successful')
        usd = p['usd_pledged'] if p['usd_pledged'] > 0 else p['converted_pledged_amount']
        backers = p['backers_count']

        cat_stats[p_cat]['total'] += 1
        if is_succ:
            cat_stats[p_cat]['successful'] += 1
        cat_stats[p_cat]['usd_pledged'] += usd
        cat_stats[p_cat]['backers'] += backers

        country_stats[country]['total'] += 1
        if is_succ:
            country_stats[country]['successful'] += 1
        country_stats[country]['usd_pledged'] += usd
        country_stats[country]['backers'] += backers

        # Proven elsewhere criteria:
        # Non-EU, usd >= 250k, backers >= 1000, successful
        if is_succ and (country not in EU_COUNTRIES) and (usd >= 250000.0) and (backers >= 1000):
            # Format launch date
            dt = datetime.datetime.fromtimestamp(p['launched_at'], datetime.timezone.utc).strftime('%Y-%m-%d')
            p_copy = dict(p)
            p_copy['launch_date'] = dt
            p_copy['effective_usd'] = usd
            proven_candidates.append(p_copy)

    # Sort candidates by USD pledged descending
    proven_candidates.sort(key=lambda x: x['effective_usd'], reverse=True)

    print(f"Found {len(proven_candidates)} non-EU physical candidates with >= $250k & >= 1000 backers.")

    # Save category stats
    cat_summary = []
    for c, s in sorted(cat_stats.items(), key=lambda x: x[1]['usd_pledged'], reverse=True):
        rate = (s['successful'] / s['total'] * 100) if s['total'] > 0 else 0
        avg_pledge = (s['usd_pledged'] / s['backers']) if s['backers'] > 0 else 0
        cat_summary.append({
            'category': c,
            'total_projects': s['total'],
            'successful_projects': s['successful'],
            'success_rate_pct': round(rate, 1),
            'total_usd_pledged': round(s['usd_pledged'], 2),
            'total_backers': s['backers'],
            'avg_pledge_usd': round(avg_pledge, 2)
        })

    with open(os.path.join(out_dir, "kickstarter_categories.json"), "w", encoding="utf-8") as f:
        json.dump(cat_summary, f, indent=2)

    # Save country stats
    country_summary = []
    for c, s in sorted(country_stats.items(), key=lambda x: x[1]['usd_pledged'], reverse=True):
        rate = (s['successful'] / s['total'] * 100) if s['total'] > 0 else 0
        country_summary.append({
            'country': c,
            'is_eu': c in EU_COUNTRIES,
            'total_projects': s['total'],
            'successful_projects': s['successful'],
            'success_rate_pct': round(rate, 1),
            'total_usd_pledged': round(s['usd_pledged'], 2),
            'total_backers': s['backers']
        })

    with open(os.path.join(out_dir, "kickstarter_countries.json"), "w", encoding="utf-8") as f:
        json.dump(country_summary, f, indent=2)

    # Save candidates CSV
    candidate_fields = [
        'id', 'name', 'parent_category', 'sub_category', 'country',
        'effective_usd', 'backers_count', 'launch_date', 'blurb', 'urls'
    ]
    with open(os.path.join(out_dir, "kickstarter_candidates.csv"), "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=candidate_fields, extrasaction='ignore')
        writer.writeheader()
        for cand in proven_candidates:
            writer.writerow(cand)

    print("Kickstarter analysis complete! Outputs written to drafts/reviews/agy/.")

if __name__ == "__main__":
    main()
