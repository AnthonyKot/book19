#!/usr/bin/env python3
"""Collect a reproducible, current public-listing sample for the succession note."""

from __future__ import annotations

import csv
import html
import json
import re
import time
import urllib.request
from pathlib import Path

ROOT = Path("/home/diablo/book19/drafts/research/succession")
SOURCES = ROOT / "sources"
FETCH_DATE = "2026-09-03"
UA = "Mozilla/5.0 (compatible; public-research/1.0)"


def fetch(url: str, data: bytes | None = None, headers: dict | None = None) -> str:
    h = {"User-Agent": UA, "Accept-Language": "nl,en;q=0.8"}
    if headers:
        h.update(headers)
    req = urllib.request.Request(url, data=data, headers=h)
    with urllib.request.urlopen(req, timeout=30) as response:
        return response.read().decode("utf-8", "replace")


def textify(raw: str) -> str:
    raw = re.sub(r"(?is)<(script|style|svg).*?</\1>", " ", raw)
    raw = re.sub(r"(?i)<br\s*/?>", "\n", raw)
    raw = re.sub(r"(?i)</(?:p|div|li|h[1-6]|tr)>", "\n", raw)
    raw = re.sub(r"(?s)<[^>]+>", " ", raw)
    raw = html.unescape(raw)
    lines = [re.sub(r"\s+", " ", line).strip() for line in raw.splitlines()]
    return "\n".join(line for line in lines if line)


def compact(s: str, n: int = 900) -> str:
    s = re.sub(r"\s+", " ", s).strip()
    return s[:n] + ("…" if len(s) > n else "")


def retirement(text: str) -> str:
    pats = [
        r"\bpensioen(?:ering|gerechtigd|leeftijd)?\b",
        r"\bpensionering\b",
        r"\bwegens leeftijd\b",
        r"\bvanwege (?:de )?leeftijd\b",
        r"\bgezien (?:de )?leeftijd\b",
        r"\bouderdom\b",
        r"\bbedrijfsopvolging\b",
    ]
    return "yes" if any(re.search(p, text, re.I) for p in pats) else "no"


def retirement_evidence(text: str) -> str:
    for pat in [r"pensioen\w*", r"pensionering", r"wegens leeftijd", r"vanwege (?:de )?leeftijd", r"gezien (?:de )?leeftijd", r"ouderdom", r"bedrijfsopvolging"]:
        match = re.search(pat, text, re.I)
        if match:
            return compact(text[max(0, match.start() - 70) : match.end() + 90], 180)
    return "none"


def next_line(lines: list[str], label: str) -> str:
    for i, line in enumerate(lines):
        if line.strip().casefold() == label.casefold():
            for value in lines[i + 1 : i + 5]:
                if value.strip() and value.strip().casefold() != label.casefold():
                    return value.strip()
    return "not stated"


def json_ld_products(raw: str) -> list[dict]:
    out = []
    for block in re.findall(
        r'(?is)<script[^>]+type=["\']application/ld\+json["\'][^>]*>(.*?)</script>', raw
    ):
        try:
            obj = json.loads(html.unescape(block))
        except Exception:
            continue
        items = obj if isinstance(obj, list) else [obj]
        for item in items:
            if isinstance(item, dict) and item.get("@type") == "Product":
                out.append(item)
    return out


def bt_sample() -> tuple[list[dict], str]:
    chosen = {
        110900: "light manufacturing", 110498: "light manufacturing",
        110435: "light manufacturing", 110199: "light manufacturing",
        110960: "wholesale/trade", 110715: "wholesale/trade",
        110711: "wholesale/trade", 110482: "wholesale/trade",
        110560: "wholesale/trade", 110942: "wholesale/trade",
        111004: "workshop", 110637: "workshop", 110512: "workshop",
        110554: "workshop", 108778: "workshop",
        110281: "logistics", 109363: "logistics", 109819: "logistics",
        110726: "care", 110610: "care", 110708: "care",
        110344: "care", 111029: "care",
        111059: "hospitality", 111036: "hospitality", 110990: "hospitality",
        110922: "hospitality", 110917: "hospitality", 110799: "hospitality",
        110678: "hospitality",
        111063: "retail", 111006: "retail", 110984: "retail",
        110953: "retail", 110906: "retail", 110672: "retail",
        110469: "retail", 110742: "retail",
    }
    endpoint = "https://www.bedrijventekoop.nl/listings-post"
    idmap = {}
    response_sizes = []
    for page_no in range(1, 6):
        payload = {
            "type": 1,
            "sectors": ["1", "2", "3", "4", "6", "7", "8", "9", "10", "13"],
            "regions": [], "turnovers": [], "askingprice": ["1", "2"],
            "typeofacquisition": [], "legalentity": [], "typeoftransaction": [],
            "employees": [], "lifephaseenterprise": [], "platform": [], "search": "",
            "movable": False, "page": page_no, "limit": 60, "archive": False,
        }
        raw = fetch(endpoint, json.dumps(payload).encode(), {"Content-Type": "application/json"})
        response_sizes.append(len(raw.encode()))
        for item in json.loads(raw).get("items", []):
            if item.get("id") in chosen:
                idmap[item["id"]] = "https://www.bedrijventekoop.nl" + item["listingUrl"]

    missing = set(chosen) - set(idmap)
    if missing:
        raise RuntimeError(f"Bedrijventekoop IDs missing from current filtered API: {sorted(missing)}")

    rows, notes = [], []
    for n, listing_id in enumerate(chosen, 1):
        url = idmap[listing_id]
        raw = fetch(url)
        page = textify(raw)
        lines = page.splitlines()
        id_index = next(i for i, x in enumerate(lines) if x.startswith(f"#{listing_id} "))
        title = lines[id_index - 2]
        main_end = next((i for i in range(id_index + 1, len(lines)) if lines[i] == "Persoonlijke gegevens"), id_index + 30)
        desc = "\n".join(lines[id_index + 1 : main_end])
        ask = next_line(lines, "Indicatie overnamebedrag")
        if ask == "not stated":
            ask = next_line(lines, "Overname")
        revenue = next_line(lines, "Omzet indicatie")
        if revenue == "not stated":
            revenue = next_line(lines, "Omzet")
        if ask not in {"€ 0 - € 100.000", "€ 100.000 - € 250.000"}:
            raise RuntimeError(f"Selected listing {listing_id} no longer has an eligible public asking-price band: {ask}")
        row = {
            "sample_id": f"BT{n:02d}", "platform": "Bedrijventekoop.nl",
            "listing_id": listing_id, "title": title, "sector": chosen[listing_id],
            "region": next_line(lines, "Regio"),
            "asking_price_eur_or_band": ask,
            "revenue": revenue,
            "profit": next_line(lines, "Resultaat voor belasting").replace("Resultaat voor belasting", "").strip(),
            "staff": next_line(lines, "Aantal medewerkers (in FTE)").replace("Aantal medewerkers (in FTE)", "").strip(),
            "retirement_stated": retirement(desc), "url": url, "fetch_date": FETCH_DATE,
        }
        rows.append(row)
        notes.append(
            f"ID: {row['sample_id']} / listing {listing_id}\nURL: {url}\nPublisher: Bedrijventekoop.nl\n"
            f"Fetch date: {FETCH_DATE}\nTitle: {title}\nExtracted fields: region={row['region']}; "
            f"ask={row['asking_price_eur_or_band']}; revenue={row['revenue']}; profit={row['profit']}; "
            f"staff={row['staff']}; retirement stated={row['retirement_stated']}\n"
            f"Retirement evidence: {retirement_evidence(desc)}\n"
            f"Public listing excerpt: {compact(desc)}\n"
        )
        time.sleep(0.05)
    meta = (
        f"Dataset endpoint: {endpoint}\nPublisher: Bedrijventekoop.nl\nFetch date: {FETCH_DATE}\n"
        "Query: all five result pages (60/page), sale offers only, selected physical sectors, asking-price bands €0–100k and €100–250k. "
        f"Response sizes (bytes): {response_sizes}; combined={sum(response_sizes)}. Responses were processed, not retained. "
        "Every selected asking-price band was rechecked on its public profile.\n"
    )
    return rows, meta + "\n" + "\n".join(notes)


def brookz_sample() -> tuple[list[dict], str]:
    selected = [
        (42192, "https://www.brookz.nl/bedrijven-te-koop/importeur-argentijnse-wijn-eu-1/42192", "wholesale/trade"),
        (42850, "https://www.brookz.nl/bedrijven-te-koop/autogarage-overname-met-lage-huurkosten/42850", "workshop"),
        (42802, "https://www.brookz.nl/bedrijven-te-koop/uniek-mobiel-horecaconcept-voor-de-evenementenmarkt/42802", "hospitality"),
        (42848, "https://www.brookz.nl/bedrijven-te-koop/verhuurbedrijf-feesttenten-flevolandt-gooi/42848", "logistics"),
        (42460, "https://www.brookz.nl/bedrijven-te-koop/stomerij-en-kledingreiniging/42460", "workshop"),
        (41294, "https://www.brookz.nl/bedrijven-te-koop/stomerij-1/41294", "workshop"),
        (40421, "https://www.brookz.nl/bedrijven-te-koop/familiebedrijf-beveiliging-cameras-toegang-artikelbeveiliging/40421", "wholesale/trade"),
    ]
    rows, notes = [], []
    for n, (listing_id, url, sector) in enumerate(selected, 1):
        raw = fetch(url)
        products = json_ld_products(raw)
        if not products:
            raise RuntimeError(f"No Product JSON-LD on {url}")
        p = products[0]
        props = {x.get("name"): x.get("value") for x in p.get("additionalProperty", []) if isinstance(x, dict)}
        price = p.get("offers", {}).get("price", "not stated")
        full = textify(raw)
        lines = full.splitlines()
        marker = f"#{listing_id}"
        start = next((i for i, x in enumerate(lines) if x.strip().startswith(marker)), 0)
        end = next((i for i in range(start + 1, len(lines)) if lines[i].startswith("Gratis verder lezen")), min(start + 120, len(lines)))
        main = "\n".join(lines[start:end])
        revenue = props.get("Omzet", next_line(main.splitlines(), "Omzet"))
        profit = props.get("EBITDA", props.get("Winst", next_line(main.splitlines(), "Winst")))
        row = {
            "sample_id": f"BR{n:02d}", "platform": "Brookz", "listing_id": listing_id,
            "title": p.get("name", "not stated"), "sector": sector,
            "region": props.get("Regio", "not stated"),
            "asking_price_eur_or_band": f"€{int(float(price)):,}".replace(",", ".") if str(price).replace(".", "", 1).isdigit() else str(price),
            "revenue": revenue, "profit": profit,
            "staff": props.get("FTE", props.get("Aantal medewerkers", "not stated")),
            "retirement_stated": retirement(main), "url": url, "fetch_date": FETCH_DATE,
        }
        rows.append(row)
        notes.append(
            f"ID: {row['sample_id']} / listing {listing_id}\nURL: {url}\nPublisher: Brookz\n"
            f"Fetch date: {FETCH_DATE}\nTitle: {row['title']}\nExtracted fields: region={row['region']}; "
            f"ask={row['asking_price_eur_or_band']}; revenue={row['revenue']}; profit={row['profit']}; "
            f"staff={row['staff']}; retirement stated={row['retirement_stated']}\n"
            f"Retirement evidence: {retirement_evidence(main)}\n"
            f"Public listing excerpt: {compact(main)}\n"
        )
        time.sleep(0.05)
    return rows, "\n".join(notes)


def marktplaats_sample() -> tuple[list[dict], str]:
    chosen = {
        "m2438622080": "hospitality", "m2409418478": "hospitality",
        "m2437939485": "retail", "m2427605173": "workshop",
        "m2267297828": "logistics", "m2406440342": "hospitality",
        "m2396550266": "workshop", "m2385733998": "workshop",
        "m2434627891": "retail", "m2391296179": "light manufacturing",
        "m2428641482": "hospitality", "m2415763818": "wholesale/trade",
        "m2435451734": "light manufacturing", "m2415409915": "retail",
        "m2348097226": "care",
    }
    base = "https://www.marktplaats.nl/l/zakelijke-goederen/exploitaties-en-overnames/"
    itemmap = {}
    sizes = []
    category_urls = []
    for page_no in range(1, 7):
        url = base if page_no == 1 else base + f"p/{page_no}/"
        raw = fetch(url)
        sizes.append(len(raw.encode()))
        category_urls.append(url)
        m = re.search(r'<script[^>]+id="__NEXT_DATA__"[^>]*>(.*?)</script>', raw, re.S)
        if not m:
            raise RuntimeError(f"No Next data at {url}")
        obj = json.loads(html.unescape(m.group(1)))
        def walk(x):
            if isinstance(x, dict):
                if str(x.get("itemId", "")) in chosen and x.get("vipUrl"):
                    itemmap[str(x["itemId"])] = x
                for value in x.values():
                    walk(value)
            elif isinstance(x, list):
                for value in x:
                    walk(value)
        walk(obj)
        time.sleep(0.1)
    missing = set(chosen) - set(itemmap)
    if missing:
        raise RuntimeError(f"Marktplaats IDs missing from first 6 current pages: {sorted(missing)}")

    rows, notes = [], []
    for n, (listing_id, sector) in enumerate(chosen.items(), 1):
        item = itemmap[listing_id]
        url = item["vipUrl"]
        if url.startswith("/"):
            url = "https://www.marktplaats.nl" + url
        raw = fetch(url)
        products = json_ld_products(raw)
        p = products[0] if products else {}
        desc_match = re.search(
            r'(?is)Description-module-description[^>]*>.*?data-collapsable="description"[^>]*>(.*?)</div>', raw
        )
        desc = textify(desc_match.group(1)) if desc_match else str(p.get("description", ""))
        ask_raw = item.get("priceInfo", {}).get("priceCents")
        if isinstance(ask_raw, int):
            ask = f"€{ask_raw / 100:,.0f}".replace(",", ".")
        else:
            ask = str(p.get("offers", {}).get("price", "not stated"))
        money_tail = r"(?:€\s*\d[\d.,]*|\d[\d.,]*\s*(?:euro|k\b|mln\b))"
        revenue_match = re.search(r"(?i)\bomzet\b.{0,50}" + money_tail, desc)
        profit_match = re.search(r"(?i)\b(?:winst|resultaat|EBITDA)\b.{0,50}" + money_tail, desc)
        staff_match = re.search(r"(?i)(?:\b\d+\s*(?:parttime\s+)?(?:fte|medewerkers?|personeelsleden?|werknemers?)\b|\b(?:fte|medewerkers?|personeelsleden?|werknemers?)\s*[:=-]?\s*\d+)", desc)
        if listing_id == "m2267297828":
            revenue_match = None  # the €10k phrase is the package price, not historical turnover
        location = item.get("location", {})
        if isinstance(location, dict):
            region = location.get("cityName") or location.get("city") or location.get("countryName") or "not stated"
        else:
            region = str(location) if location else "not stated"
        row = {
            "sample_id": f"MP{n:02d}", "platform": "Marktplaats Zakelijk",
            "listing_id": listing_id, "title": item.get("title") or p.get("name", "not stated"),
            "sector": sector, "region": region, "asking_price_eur_or_band": ask,
            "revenue": compact(revenue_match.group(0), 100) if revenue_match else "not stated",
            "profit": compact(profit_match.group(0), 100) if profit_match else "not stated",
            "staff": staff_match.group(0) if staff_match else "not stated",
            "retirement_stated": retirement(desc), "url": url, "fetch_date": FETCH_DATE,
        }
        rows.append(row)
        notes.append(
            f"ID: {row['sample_id']} / listing {listing_id}\nURL: {url}\nPublisher: Marktplaats\n"
            f"Fetch date: {FETCH_DATE}\nTitle: {row['title']}\nExtracted fields: region={row['region']}; "
            f"ask={row['asking_price_eur_or_band']}; revenue={row['revenue']}; profit={row['profit']}; "
            f"staff={row['staff']}; retirement stated={row['retirement_stated']}\n"
            f"Retirement evidence: {retirement_evidence(desc)}\n"
            f"Public listing excerpt: {compact(desc)}\n"
        )
        time.sleep(0.05)
    meta = (
        "Category-page URLs: " + ", ".join(category_urls) + "\nPublisher: Marktplaats\n"
        f"Fetch date: {FETCH_DATE}\nResponse sizes (bytes): {sizes}; combined={sum(sizes)}. "
        "Pages were processed, not retained as datasets.\n"
    )
    return rows, meta + "\n" + "\n".join(notes)


def main() -> None:
    SOURCES.mkdir(parents=True, exist_ok=True)
    bt, bt_notes = bt_sample()
    br, br_notes = brookz_sample()
    mp, mp_notes = marktplaats_sample()
    rows = bt + br + mp
    if len(rows) != 60:
        raise RuntimeError(f"Expected 60 listings, got {len(rows)}")
    fields = [
        "sample_id", "platform", "listing_id", "title", "sector", "region",
        "asking_price_eur_or_band", "revenue", "profit", "staff",
        "retirement_stated", "url", "fetch_date",
    ]
    with (SOURCES / "listings_sample.csv").open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)
    for name, body in [
        ("listings_bedrijventekoop.txt", bt_notes),
        ("listings_brookz.txt", br_notes),
        ("listings_marktplaats.txt", mp_notes),
    ]:
        (SOURCES / name).write_text(body, encoding="utf-8")
    print(f"Wrote {len(rows)} listings: BT={len(bt)}, Brookz={len(br)}, MP={len(mp)}")


if __name__ == "__main__":
    main()
