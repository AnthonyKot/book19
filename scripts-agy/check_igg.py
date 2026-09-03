#!/usr/bin/env python3
import zipfile, csv, io

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

projects = {}
with zipfile.ZipFile("resources/data-agy/Indiegogo_2025-10-13.zip") as z:
    with z.open("Indiegogo.csv") as f:
        reader = csv.DictReader(io.TextIOWrapper(f, encoding="utf-8", errors="replace"))
        for r in reader:
            pid = r.get("project_id")
            if not pid or pid in projects:
                continue
            cur = r.get("currency")
            if cur not in FX_TO_USD:
                continue
            try:
                raw_funds = float(r.get("funds_raised_amount", 0) or 0)
            except:
                continue
            usd = raw_funds * FX_TO_USD[cur]
            op = r.get("open_date", "")
            cl = r.get("close_date", "")
            yr = None
            for d in [op, cl]:
                if d and d != "null":
                    try:
                        yr = int(d[:4])
                        break
                    except:
                        pass
            projects[pid] = {
                "title": r.get("title"),
                "cat": r.get("category"),
                "cur": cur,
                "raw": raw_funds,
                "usd": usd,
                "year": yr,
                "stage": r.get("product_stage"),
                "url": r.get("clickthrough_url"),
                "tagline": r.get("tagline")
            }

all_2023 = [p for p in projects.values() if p['year'] and 2023 <= p['year'] <= 2026]
phys_2023 = [p for p in all_2023 if p['cat'] in PHYSICAL_IGG_CATEGORIES]
phys_top = sorted([p for p in phys_2023 if p['usd'] >= 250000], key=lambda x: x['usd'], reverse=True)

print(f"Total deduplicated IGG with currency: {len(projects)}")
print(f"2023-2026 all: {len(all_2023)}, physical: {len(phys_2023)}")
print(f"Physical >= $250k: {len(phys_top)}")
for p in phys_top[:25]:
    print(f"{p['title'][:45]:<45} | {p['cat']:<18} | ${p['usd']:>11,.0f} ({p['cur']} {p['raw']:>12,.0f}) | yr: {p['year']}")
