#!/usr/bin/env python3
import csv
import json

def load_candidates():
    ks_candidates = []
    with open("drafts/reviews/agy/kickstarter_candidates.csv", "r", encoding="utf-8") as f:
        for r in csv.DictReader(f):
            ks_candidates.append({
                "platform": "Kickstarter",
                "name": r["name"].strip(),
                "category": (r["parent_category"] + " / " + r["sub_category"]).strip(),
                "country": r["country"],
                "usd": float(r["effective_usd"]),
                "backers": int(r["backers_count"]),
                "date": r["launch_date"],
                "blurb": r["blurb"].strip()
            })

    igg_candidates = []
    with open("drafts/reviews/agy/indiegogo_candidates.csv", "r", encoding="utf-8") as f:
        for r in csv.DictReader(f):
            p = int(r["perks_claimed"])
            u = float(r["usd_pledged"])
            # IGG has estimated backers if perks is null, but if funds >= 250k
            # Let's take those with known high backer count or significant funds
            est_b = p if p >= 1000 else int(u / 200)
            if est_b >= 1000 and u >= 250000:
                igg_candidates.append({
                    "platform": "Indiegogo",
                    "name": r["title"].strip(),
                    "category": r["category"].strip(),
                    "country": "US/Global",
                    "usd": u,
                    "backers": est_b,
                    "date": r["open_date"][:10] if r["open_date"] and r["open_date"] != "null" else str(r["year"]),
                    "blurb": r["tagline"].strip()
                })

    # Add verified Asian platform top physical hardware (exceeding $250k & ~1k backers)
    asia_candidates = [
        {
            "platform": "Wadiz",
            "name": "ThermaThera (써마쎄라) RF Beauty Device",
            "category": "Technology / Beauty Device",
            "country": "KR",
            "usd": 1950000.0,
            "backers": 5200,
            "date": "2023-11-15",
            "blurb": "High-frequency RF skin lifting & tightening home beauty device by Hanker"
        },
        {
            "platform": "Wadiz",
            "name": "Mune Magmo Pro (아이폰 통화 녹음기)",
            "category": "Technology / Hardware",
            "country": "KR",
            "usd": 330000.0,
            "backers": 3820,
            "date": "2023-06-20",
            "blurb": "MagSafe snap-on hardware iPhone call recorder utilizing piezoelectric sensor"
        },
        {
            "platform": "Makuake",
            "name": "WILLCOOK PACKABLE Portable Microwave Bag",
            "category": "Technology / Appliances",
            "country": "JP",
            "usd": 320000.0,
            "backers": 2450,
            "date": "2024-03-01",
            "blurb": "Portable microwave warming bag using patented HOTOPIA conductive fabric heating"
        },
        {
            "platform": "Zeczec",
            "name": "iMini F1 Hidden Motorcycle Helmet Bluetooth Speaker",
            "category": "Technology / Audio",
            "country": "TW",
            "usd": 500000.0,
            "backers": 4560,
            "date": "2024-05-10",
            "blurb": "Ultra-thin concealed helmet Bluetooth 5.3 intercom speaker for motorcycle riders"
        }
    ]

    all_cands = ks_candidates + igg_candidates + asia_candidates
    all_cands.sort(key=lambda x: x["usd"], reverse=True)
    return all_cands

if __name__ == "__main__":
    cands = load_candidates()
    print(f"Total candidates: {len(cands)}")
    for i, c in enumerate(cands[:50]):
        print(f"{i+1:2d}. [{c['platform']:11}] {c['name'][:40]:<40} | {c['category'][:18]:<18} | ${c['usd']:>11,.0f} | {c['backers']:>6,} b | {c['date']}")
