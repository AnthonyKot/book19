# The boring-business lens: which small physical businesses in the Netherlands quietly last

Research date: 2026-09-04 (fetch date for all excerpts). Agent: Fable 5.1.
Reader screen: `drafts/edge-inventory.md` (A2 Dutch; English/Russian/Polish; ~EUR 100k; regulatory literacy; engineering habit; 30k LinkedIn). Gates: A2 gate and AI gate. The seven candidates kept in `drafts/notes/2026-09-03-fable-triage.md` are not re-proposed; where this lens strengthens or weakens one, it is said in section 6. Every figure traces to a file in `sources/` (this folder) or, where marked `../succession/sources/`, to the succession run's saved excerpts.

## Answer in one paragraph

Survival in Dutch physical small business is mostly a size effect, not a sector secret. CBS's European-norm demography shows that firms founded in 2018 with 1–5 employees were still alive in 2023 at 72–81% in nearly every physical sector tested (machine repair 80.6%, personal services 80.0%, vehicle trade/repair 79.4%, manufacturing 74.0%, construction 72.4%, trade 72.3%), against 54–65% for zero-employee starters in trade, wholesale, transport and cleaning [A]. Among sectors, the quiet survivors are machine repair and installation (SBI 33: 79.0% five-year survival, 1.9% annual exit of 2–10-person firms, 17 bankruptcies in 2025 on 14,175 firms), specialised construction incl. building installation, specialised vehicle repair, funeral services and laundries (pre-tax margins 12–14% in 2024) [A][B][C][F]. Wholesale and road haulage have the oldest owners but the weakest survival and margins. What is for sale matches the CBS picture only in installation (30 live Brookz profiles), garages (14) and wholesale (94); cleaning, funeral, laundry, courier and waste show 1–6 profiles each [L]. The licences that gate these trades (CO-certificaat, Eurovergunning vakdiploma, ADR, biocide vakbekwaamheid) are person-bound and examined in Dutch; the buyer's design is therefore always the same: keep the licensed Dutch operator, own the system.

## 1. Sources and limits

| id | source | what it establishes | limit | excerpt |
|---|---|---|---|---|
| A | CBS StatLine 85200NED, Bedrijvendemografie (Europese norm), 2010–2023 | Births, deaths, survivors by sector and size class; survival ratios computed by the agent (survivors in 2023 "uit 5 jaar eerder" / births 2018; 3-year: 2020 births) | Ends 2023; 4-digit installation/cleaning codes not published; size class is the table's own dimension; European norm excludes mergers and reactivations | `sources/cbs-85200-survival.txt` |
| B | CBS 83149NED (opheffingen by size class) + 81589NED (stock), 2023–2025 | Annual closures of 2–10-person firms divided by stock of 2–10-person firms (exit rate), per SBI code | Closures include mergers and legal-form changes, not only deaths; 2025 provisional | `sources/cbs-83149-81589-closures-stock.txt` |
| C | CBS 82244NED, faillissementen, 2023–2025 | Court bankruptcies per sector | Most small-firm exits are voluntary, not bankruptcies | `sources/cbs-82244-faillissementen.txt` |
| D | CBS 84467NED, zelfstandigen inkomen, 2024 (provisional) | Median income of self-employed with staff (zmp) vs without, per letter sector | CBS publishes income only at letter level; 3-digit rows empty | `sources/cbs-84467-zelfstandigen-inkomen.txt` |
| E | CBS 85077NED, zelfstandigen persoonskenmerken, 2024 | Age distribution of self-employed with staff per letter sector | Persons, not firms; letter level only | `sources/cbs-85077-zelfstandigen-leeftijd.txt` |
| F | CBS 81156ned, arbeids- en financiële gegevens per branche, 2022–2024 (definitive) | Revenue, personnel share, operating and pre-tax margin per 3/4-digit branch | Aggregates over all sizes; large firms dominate transport, wholesale, cleaning; not a small-firm margin | `sources/cbs-81156-financien-per-branche.txt` |
| K | KVK Bedrijvendynamiek jaaroverzicht 2025 (PDF) + press release 2026-01-15 | Starters/stoppers per sector 2024–2025, bankruptcies per sector, owner profile (average age, % foreign-born) per sector | Register counts incl. zzp; no survival | `sources/kvk-bedrijvendynamiek-2025.txt` |
| N | ABN AMRO Sectorprognoses "Bedrijfsopvolging", 2025-12-03 | Top-15 branches by owners 65+ (firms ≥2 persons, CBS-based), Ipsos survey n=519, volume forecasts 2025–2027 | Survey is intent, not supply | `sources/abnamro-sectorprognoses-bedrijfsopvolging-dec2025.txt` |
| BZ | Brookz branche pages (installatie, schoonmaak, transport, koerier, uitvaart, verhuur, handel) | Indicative EBITDA multiple bands, yearly M&A counts, CBS 2025 firm counts by size | Broker marketing; multiples are adviser-survey bands for EUR 0.5–50m firms | `sources/brookz-branche-pages.txt` |
| L | Brookz category listing pages, 12 slugs | Live profile counts and revenue bands per sector on 2026-09-04 | One marketplace, one day; prices behind login | `sources/brookz-listing-counts.txt` |
| P | Brookz listing 39190 (pest control) | One seller-stated deal: revenue ≈EUR 240k, EBITDA ≈EUR 78k, 2–5 FTE, 80% B2B | Unaudited seller claim | `sources/brookz-listing-ongediertebestrijding-39190.txt` |
| S | Brookz kennisbank sectorvisie installatiebranche, 2024-12-17 | 41k installation firms Q4 2024, 173k workers, 5,900 DGA's, EUR 28.7bn, 100 ownership changes 2023, 150–200 expected 2024, consolidators, policy changes | Journalism citing CBS/Techniek Nederland | `sources/brookz-sectorvisie-installatie.txt` |
| T | Installatie Totaal / Techniek Nederland member survey (n=291) | 78% have considered sale, succession, closure or growth by acquisition; for about half within five years | Undated article; member survey | `sources/installatietotaal-overdracht.txt` |
| R1 | NIWO Eurovergunning page | Licence conditions: vakdiploma via six CBR exams, transport manager may be hired or external, EUR 9,000 + EUR 5,000/vehicle risk capital, VOG, fees, 5-year validity | Page text; no approval statistics | `sources/niwo-eurovergunning.txt` |
| R2 | NIWO VIHB page | Waste transporters/collectors need only a VOG; vakdiploma afvalstoffen only for pure traders/brokers | — | `sources/niwo-vihb.txt` |
| R3 | RVO bewijs van vakbekwaamheid (checked 2026-08-24) | Biocide/pest-control competence is per person, examined at green MBO/HBO schools, issued by Bureau Erkenningen; foreign diplomas can be submitted | Does not state exam language explicitly (schools are Dutch) | `sources/rvo-vakbekwaamheid-bestrijding.txt` |
| R4 | Ondernemersplein CO-certificaat | Gas-appliance work requires a company CO-certificate (BRL 6000-25 / K25000 audit) plus a per-mechanic Bewijs van Vakmanschap CO; working without it is punishable for firm and client | — | `sources/ondernemersplein-co-certificaat.txt` |
| R5 | CBR FAQ on exams in another language | ADR: not in English, no interpreter; Ondernemers exams: not in English, interpreter allowed except Calculatie and Financieel Management (Dutch only); reference works for Wegvervoer Goederen not translated | — | `sources/cbr-adr-andere-taal.txt` |
| V | NVPB "over" page | Members represent about 90% of the Dutch pest-management market | No member count on the saved page | `sources/nvpb-over.txt` |
| — | Succession run: Qredits, BMKB, Brookz H1-2026 barometer, dry-cleaning page | Finance envelope (EUR 100k + Qredits max EUR 250k at 9.95%; BMKB starter ceiling EUR 333,333, 67.5% guarantee); average multiple 3.6 at EUR 200k EBITDA; 885 dry cleaners | Cited by path, not refetched | `../succession/sources/finance.txt`, `../succession/sources/valuation_and_transfer.txt`, `../succession/sources/calculations.txt` |

Not obtained: Rabobank sector monitors (site returned "tijdelijk niet beschikbaar" to curl and 403 to the fetcher twice); the Brookz H1-2026 sector multiple table (the branche pages give the current bands instead); CBS income at 3-digit level (not published); a firm count for pest control (SBI 8129 "overige reiniging" mixes it with other cleaning); Bedrijventekoop counts per sector (POST endpoint, not re-queried; the succession run's 60-listing sample stands).

## 2. Evidence table 1 — survival, exit, bankruptcy (CBS)

Five-year survival = 2018 births still alive in 2023; three-year = 2020 births alive in 2023 [A]. Exit rate = 2025 closures of 2–10-person firms / stock of 2–10-person firms at 2025 Q1 [B]. Bankruptcies 2023 → 2025 [C].

| sector (SBI) | 5-yr survival, all | 5-yr survival, 1–5 employees | 5-yr survival, 0 employees | 3-yr survival, all | exit rate 2–10 wp 2025 | stock 2–10 wp 2025 | bankruptcies 2023→2025 |
|---|---:|---:|---:|---:|---:|---:|---:|
| 33 Reparatie/installatie machines | 79.0% | 80.6% | 79.0% | 85.6% | 1.9% | 2,080 | 31 → 17 |
| F Bouw (all) | 74.5% | 72.4% | 74.5% | 81.4% | 3.2% | 29,950 | 479 → 488 |
| 43 Gespecialiseerde bouw | n/p | n/p | n/p | n/p | 3.1% | 18,085 | 224 → 286 |
| 432 Bouwinstallatie | n/p | n/p | n/p | n/p | 3.4% (2.3% in 2023) | 5,970 | 98 → 133 (168 in 2024) |
| C Industrie | 71.3% | 74.0% | 71.2% | 81.4% | 3.4% | 16,560 | 270 → 292 |
| 10 Voedingsmiddelen | n/p | n/p | n/p | n/p | 5.7% | 2,025 | 25 → 53 |
| 96 Overige persoonlijke diensten (incl. laundries, funeral) | 70.5% | 80.0% | 70.3% | 81.7% | 3.2% | 10,705 | 48 → 39 |
| 81 Schoonmaak/hoveniers | 69.5% | 68.1% | 69.6% | 78.8% | 4.4% | 8,220 | 46 → 83 |
| 812 Schoonmaakbedrijven | 64.2% | 62.7% | 64.4% | 75.6% | 5.9% (3.6% in 2023) | 4,840 | 29 → 61 |
| 45 Autohandel en -reparatie | 65.1% | 79.4% | 64.2% | 76.2% | 3.1% | 11,920 | 47 → 68 |
| 452 Gespecialiseerde autoreparatie | n/p | n/p | n/p | n/p | 4.1% | 2,170 | 8 → 14 |
| 52 Opslag/dienstverlening vervoer | 65.2% | 59.1% | 65.6% | 78.9% | 3.2% | 2,210 | 47 → 54 |
| 521 Opslag | n/p | n/p | n/p | n/p | 3.2% | 310 | 3 → 7 |
| 773 Zakelijke verhuur goederen | 65.3% | 57.1% (n=7) | 65.8% | 76.8% | 2.9% | 860 | 6 → 15 |
| 49 Vervoer over land | 63.2% | 67.5% | 63.0% | 77.8% | 5.0% | 6,375 | 137 → 142 |
| 494 Goederenvervoer over de weg | n/p | n/p | n/p | n/p | 4.8% | 4,585 | 121 → 114 (174 in 2024) |
| I Horeca | 62.9% | 70.2% | 60.4% | 74.3% | 5.0% | 29,900 | 267 → 347 |
| H Vervoer en opslag | 61.8% | 66.8% | 61.5% | 76.8% | 4.5% | 11,985 | 237 → 224 |
| G Handel | 56.3% | 72.3% | 55.2% | 67.7% | 5.9% | 81,260 | 682 → 706 |
| 77 Verhuur roerende goederen | 55.6% | 63.3% | 55.3% | 73.2% | 5.1% | 2,720 | 17 → 42 |
| 46 Groothandel | 54.9% | 67.7% | 53.8% | 71.4% | 2.9% | 22,365 | 297 → 352 |
| 38 Afvalbehandeling/recycling | n/p | n/p | n/p | n/p | 2.0% | 245 | 5 → 2 |
| A–U all | — | — | — | — | 4.2% | 355,190 | 3,272 → 3,635 |

n/p = not published at that level in 85200NED. Solo-firm exit rates are roughly double: 8.1% overall in 2025, 14.1% in cleaning, 12.6% in road haulage, 6.1% in machine repair [B]. KVK's register tells the same story for 2025: starters −10%, stoppers +18%, stoppers up in every sector; construction starters −18% and stoppers +25%, transport −18%/+17%, industry stoppers +19%, trade +8%; bankruptcies −21% overall (construction 603→471, transport 310→228, industry 367→291) [K].

## 3. Evidence table 2 — margins, income, owner age

Margins are branch aggregates over all firm sizes, 2024 [F]. Income is the 2024 median "inkomen als zelfstandige" (EUR thousand) for self-employed with staff (zmp) vs without (zzp) [D]; the all-sector zmp median is 64.0k against 40.8k for zzp. Age is the share of zmp aged 55+ in 2024 [E]; the ABN/CBS column is the share of owners 65+ among firms with ≥2 persons [N]; KVK gives the average owner age and the share born outside NL on 1 Jan 2026 [K].

| branch | net revenue 2024 (EUR m) | personnel share | pre-tax margin 2022→2024 | revenue per worker (kEUR) | zmp median income (letter) | zmp 55+ (letter) | owners 65+ (ABN/CBS) | KVK avg age / % foreign-born (letter) |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| 432 Bouwinstallatie | 33,174 | 29.3% | 10.5 → 12.6% | 174 | F: 66.5k | F: 28.1% | gespec. bouw 9.8% | F: 44 / 31% |
| 4322 Loodgieters/installatie | 14,605 | 27.1% | 10.8 → 12.9% | 179 | F: 66.5k | F: 28.1% | — | F: 44 / 31% |
| 43 Gespecialiseerde bouw | 67,916 | 25.3% | 15.0 → 15.7% | 159 | F: 66.5k | F: 28.1% | 9.8% (3,060 owners) | F: 44 / 31% |
| 33 Reparatie/installatie machines | 17,671 | 25.9% | op. margin 9.2 → 8.6% (pre-tax n/p) | 256 | C: 66.5k | C: 39.0% | — | C: 46 / 17% |
| 452 Gespecialiseerde autoreparatie | 5,211 | 24.3% | 9.5 → 13.1% | 151 | G: 60.0k | G: 38.3% | autohandel/-reparatie 12.6% (2,470) | G: 44 / 17% |
| 45 Autohandel en -reparatie | 131,834 | 5.6% | 4.3 → 4.3% | 729 | G: 60.0k | G: 38.3% | 12.6% | G: 44 / 17% |
| 46 Groothandel | 648,435 | 6.6% | 5.8 → 5.3% | 881 | G: 60.0k | G: 38.3% | 15.7% (5,210) — highest non-farm | G: 44 / 17% |
| 812 Schoonmaakbedrijven | 9,243 | 52.6% | 14.3 → 16.2% | 49 | O n/p | — | schoonmaak/hoveniers 8.5% (1,270) | O: 42 / 24% |
| 8121 Interieurreiniging | 6,252 | 58.7% | 11.7 → 14.5% | 41 | — | — | — | — |
| 494 Goederenvervoer weg | 32,460 | 27.8% | 8.8 → 6.8% | 189 | H: 60.7k | H: 31.5% | vervoer over land 10.5% (1,470) | H: 43 / 36% |
| 521 Opslag | 11,912 | 20.4% | 2.8 → 12.2% | 281 | H: 60.7k | H: 31.5% | — | H: 43 / 36% |
| 77 Verhuur roerende goederen | 28,953 | 9.8% | 15.7 → −2.8% (op. 13.4%) | 516 | — | — | — | — |
| 38 Afvalbehandeling/recycling | 10,540 | 17.4% | 8.9 → 5.9% | 382 | — | — | — | E: 43 / 28% |
| 381 Inzameling van afval | 3,206 | 25.1% | 9.5 → 5.3% | 252 | — | — | — | — |
| 10 Voedingsmiddelenindustrie | 108,126 | 11.5% | 6.0 → 5.8% | 540 | C: 66.5k | C: 39.0% | — | C: 46 / 17% |
| 9601 Wasserijen | 1,139 | 40.4% | 8.2 → 12.3% | 102 | — | — | — | T: 45 / 21% |
| 9603 Uitvaartbranche | 1,472 | 28.1% | 10.6 → 13.7% | 120 | — | — | — | T: 45 / 21% |
| I Horeca | 41,288 | 28.9% | 10.3 → 11.9% | 59 | I: 51.0k | I: 28.2% | eet-/drinkgelegenheden 7.9% | I: 45 / 32% |

Reading: owners are oldest where survival is weakest (wholesale 15.7% aged 65+, vehicle trade 12.6%, road transport 10.5%) and youngest in the trades that survive (specialised construction 9.8%, cleaning 8.5%); construction and transport owners are also the most foreign-born (31%, 36%) [K][N]. ABN's Ipsos survey (n=519): 68% intend to stop steering within ten years; 22% of them have not begun succession, 20% search without a successor; 12.7% of owners of ≥2-person firms are 65+, up from just over 7% in 2010 [N].

## 4. Evidence table 3 — what is for sale and at what multiple

| sector | live Brookz profiles 2026-09-04 [L] | revenue bands seen [L] | Brookz indicative EBITDA multiple band [BZ] | Brookz/CBS M&A count per year 2015→2024 [BZ] | CBS firm count 2025 by size (Brookz rendering) [BZ] |
|---|---:|---|---|---|---|
| Installatiebedrijf | 30 | EUR 23k–5.5m; most 1–3m with 2–20 FTE; one EUR 230k security installer 2–5 FTE; one EUR 1.0m "met servicecontracten" 2–5 FTE | 4.3–5.5 (bouw & installatietechniek); sector average rose 3.9 (2022) → 4.8 (2025) | 90, 110, 85, 100, 130, 115, 150, 195, 105, 140 | ~41k firms Q4 2024, 173k workers, 5,900 DGA's, EUR 28.7bn [S] |
| Autogarage | 14 | not extracted | 3.9–4.7 (automotive, transport & logistics) | — | — |
| Groothandel/handelsonderneming | 94 | EUR 102k–3.6m | 4.8–5.9 (groothandel; average 5.2 in 2025) | 1,095 … 1,630 (2022 peak), 1,040 (2024) | 297,210 trading firms, of which 43,035 with 2 staff, 21,025 with 3–5, 15,180 with 5–10 |
| Transportbedrijf | 9 | EUR 800k–24.5m | 3.9–4.7 | 180 … 285 (2022), 170 (2024) | — |
| Verhuurbedrijf | 9 | EUR 15.6k–3.0m | 4.6–5.7 (zakelijke dienstverlening) | 35–55 typical, 75 in 2022 | 11,770 firms; 1,800 with 2 staff, 605 with 3–5, 425 with 5–10 |
| Schoonmaakbedrijf | 6 | EUR 0–50k, 200–250k (×2), 2–3m, 10–15m | 4.6–5.7 | 30 … 55 (2022), 35 (2024) | 27,400 firms; 21,555 solo, 3,080 with 2, 1,160 with 3–5, 745 with 5–10 |
| Wasserij | 4 | EUR 150–200k, 400–450k, 600–700k | (stomerij 2.0–3.1, `../succession` V4) | — | — |
| Uitvaartbedrijf | 2 | on request; EUR 700–800k; one sold at 200–250k | 4.6–5.7 | 60 … 105 (2021), 60 (2024) | 2,975 firms; 2,290 solo, 325 with 2, 165 with 3–5, 120 with 5–10 |
| Koeriersbedrijf | 1 | EUR 1.3m, 1 FTE, conditioned transport | 3.9–4.7 | 5–15 per year | 8,655 firms; 7,430 solo |
| Afvalinzamelaar | 1 | EUR 0–50k; one sold at 2–3m | — | — | — |
| Ongediertebestrijding / opslagbedrijf | no category | one pest-control listing: revenue ≈240k, EBITDA ≈78k, 2–5 FTE, 80% B2B, ~200 clients [P] | — | — | NVPB members ≈90% of market [V] |

Finance envelope (succession run, cited by path): EUR 100k equity + Qredits maximum EUR 250k at 9.95% fixed (EUR 5,306/month over five years) = EUR 350k gross; BMKB starter ceiling EUR 333,333 with 67.5% guarantee; the Brookz barometer's average multiple at EUR 200k normalised EBITDA is 3.6 [`../succession/sources/finance.txt`, `calculations.txt`, `valuation_and_transfer.txt`]. At 3.6–4.5× a firm with EUR 78–100k EBITDA prices at EUR 280–450k, i.e. the top of the envelope; the pest-control listing above sits exactly there.

## 5. Licence and gate table

| sector | licence held by | exam language / route | A2 gate | AI gate to 2030 |
|---|---|---|---|---|
| Building installation, gas work | Company CO-certificaat (BRL 6000-25 or K25000 audit, quality manual, register) + per-mechanic Bewijs van Vakmanschap CO [R4]; F-gas per person (licences run) | Dutch trade exams; company certificate is procedural — the reader's regulatory literacy applies to the quality manual, not the exam | Fails personally; passes as owner with certified mechanics and a Dutch service desk | Demand physical and policy-driven (2026 hybrid obligation dropped; salderingsregeling ends 1 Jan 2027; office label A 2030) [S]; AI touches quoting and scheduling only |
| Road haulage / courier | Eurovergunning: transport manager with vakdiploma (six CBR exams), may be an employee or hired external manager (max 4 firms / 50 vehicles); EUR 9,000 + 5,000 per vehicle risk capital; VOG ≤2 months; 5-year validity; EUR 255 application [R1] | Ondernemers exams: no English; interpreter allowed except Calculatie and Financieel Management (Dutch only); reference works not translated [R5] | Passes by hiring the transport manager; drivers and dispatch can run in Polish/Russian | Neutral to negative: routing/dispatch automation favours scale; margins 6.8% [F] |
| ADR (dangerous goods) | Per driver; ADR certificate 5 years [R5] | No English, no interpreter — Dutch only [R5] | Fails personally; drivers with certificates from other ADR states are recognised [R5] | Neutral |
| Waste transport/collection (VIHB) | Only VOG for transporters/collectors; vakdiploma afvalstoffen only if purely trader/broker [R2] | No exam for the operator | Passes | Neutral; margins thin (5.3–5.9%) [F] |
| Pest control (biocides) | Bewijs van vakbekwaamheid per person, exam at green MBO/HBO school, issued by Bureau Erkenningen; foreign diplomas can be submitted [R3] | Dutch schools; language not stated on RVO page | Fails personally unless a foreign diploma is recognised; passes as owner of certified technicians | Positive: IPM rules add paperwork per job (regulatory literacy); demand is regulatory (food, housing) |
| Machine repair/industrial maintenance | No general operator licence found (specific ones may apply per plant: not researched) | — | Passes for industrial B2B customers who work in English; technicians speak Dutch/Polish | Positive: predictive maintenance creates field-service work; repair stays physical |
| Cleaning (specialised) | No operator licence found (industry keurmerk voluntary; not researched) | — | Conditional: facility-manager customers in Dutch; crews often CEE | Negative for interior cleaning (robots, 58.7% labour share); neutral for specialised/industrial |
| Funeral, laundry, storage | No licence found in this run | — | Funeral fails without Dutch/diaspora front; laundry and storage pass as B2B | Neutral/positive |

## 6. Ranked candidates (new to this run)

### 1. Buy a machine-repair / industrial-maintenance microfirm (SBI 33)
The quietest survivor in the data: 79.0% of 2018 starters alive in 2023 (80.6% with 1–5 employees), the lowest small-firm exit rate of any sector tested (1.9% in 2025), 17 bankruptcies in 2025 on 14,175 firms, operating margin 8.6%, revenue per worker EUR 256k, and 2,080 firms in the 2–10-person class [A][B][C][F]. Owners in industry are old: 39.0% of employers aged 55+ [E]. Edge: engineering habit, English with OEMs and plant managers, Polish technician and parts supply. **A2:** passes for industrial customers; the technicians and site safety briefings are Dutch. **AI:** positive — predictive maintenance generates field calls; nothing digital fixes a pump. **First paid test:** sell one paid maintenance-audit-plus-spares-sourcing job to an English-speaking plant through an existing repair firm before bidding. **Kill fact:** no Brookz category exists and the sample shows no listing; if the skill sits in the seller alone, there is no firm to buy.

### 2. Buy a specialised-cleaning contractor (SBI 8122/8129), not an interior-cleaning firm
Cleaning has the best margins of the physical services tested (812 pre-tax 16.2% in 2024, up from 14.3%) but the worst churn (2–10-person exit rate 3.6% → 5.9%, bankruptcies 29 → 61) and a 52.6% labour share [B][C][F]; interior cleaning is where robots and the labour share bite (58.7%). Specialised cleaning births rose from 403 (2018) to 493 (2020) [A]. Six Brookz profiles, two at EUR 200–250k revenue; multiple band 4.6–5.7; consolidators buy [L][BZ]. Edge: crews are often Polish/Ukrainian-speaking and the reader can run them; 24% of sector-O owners are foreign-born [K]. **A2:** conditional on a Dutch account manager for facility contracts. **AI:** neutral for specialised, negative for interior. **First paid test:** subcontract one post-construction or industrial clean for a Polish-owned contractor (31% of construction owners are foreign-born) [K]. **Kill fact:** a cost base at 52.6% wages cannot absorb debt service if a CAO rise lands after closing.

### 3. Acquire a pest-control microfirm with its certified technicians
The one listing found states revenue ≈EUR 240k, EBITDA ≈EUR 78k, 2–5 FTE, 80% B2B, ~200 clients [P] — at the barometer's 3.6× for small EBITDA this is ≈EUR 280k, inside the EUR 100k + Qredits envelope [`../succession/sources`]. Demand is regulatory (biocide use requires per-person competence; NVPB members hold ~90% of the market, so independents are rare and small) [R3][V]. Edge: regulatory literacy for IPM documentation, Polish/Russian-speaking client base in housing and food. **A2:** fails personally — the exam runs through Dutch green schools; passes only if the certificate-holders stay [R3]. **AI:** positive — inspection and reporting get cheaper; the work stays physical. **First paid test:** broker three annual contracts from CEE-owned food or housing operators to an existing certified firm for a fee. **Kill fact:** the seller is the only certificate-holder (CBS gives no firm count for 8129 to size the pool).

### 4. B2B fleet workshop for CEE-owned transport and construction firms (SBI 452)
Specialised vehicle repair earns 13.1% pre-tax (2024, up from 9.5%), EUR 151k revenue per worker, 5-year survival of 79.4% for 1–5-employee firms, 12.6% of owners aged 65+, and 14 garages live on Brookz [A][F][N][L]. The demand angle is the reader's: 36% of transport and 31% of construction owners are foreign-born [K], and their vans need MOT, tachograph and maintenance in Polish. **A2:** passes only as a B2B desk in Polish/Russian with a Dutch chief mechanic; the APK inspector licence is a Dutch RDW/IBKI exam (not fetched — verify). **AI:** neutral; EV transition reduces maintenance per vehicle (judgment, no source). **First paid test:** sell ten prepaid fleet-service vouchers through Polish agencies and fulfil at a partner garage. **Kill fact:** garage revenue in the 45 aggregate is 4.3% margin — if the target's income is vehicle trade, not repair, the margin story collapses.

### 5. Small road haulage with a hired transport manager (SBI 494) — tested, weak
Eurovergunning is buyable: the transport manager may be an employee or an external hire, risk capital is EUR 9,000 + 5,000 per vehicle, application EUR 255 [R1]. Nine transport profiles are live, multiple band 3.9–4.7 [L][BZ], and drivers can be run in Polish. But 2–10-person exit is 4.8%, solo exit 12.6%, bankruptcies 121/174/114 in 2023–25, pre-tax margin 8.8% → 6.8%, and the Ondernemers and ADR exams exclude English [B][C][F][R5]. **Verdict:** DO NOT ENTER at EUR 100k; the data shows a sector where survival is the exception.

### Where this lens moves the seven kept candidates
- **Heat-pump/installation company by hiring or acquisition (triage #3): strengthened as a buy, weakened as a build.** 41k firms, 100 ownership changes in 2023 and 150–200 expected for 2024, 30 live Brookz profiles, multiple 4.3–5.5 and rising, 78% of Techniek Nederland respondents thinking about sale/succession, half within five years [S][L][BZ][T]; margins 12.6–12.9% [F]. Against: 2–10-person exit rose from 2.3% to 3.4% and bankruptcies from 98 to 133 in two years [B][C]; the CO-certificaat makes gas work a company-plus-person certification [R4]; hybrid obligation dropped and saldering ends 2027 [S].
- **Owner-independent B2B acquisition (triage #2): supply confirmed, survival warned.** Wholesale has the oldest owners (15.7% aged 65+, 5,210 people) and 94 live profiles, but 54.9% five-year survival, 5.3% margin [N][L][A][F]. Laundries: 12.3% margin on EUR 1.1bn, four profiles [F][L].
- **Funeral desk (triage #6): strengthened.** 9603 pre-tax margin 13.7% and rising, 2,975 firms of which 2,290 solo, sector-96 survival 80.0% for 1–5-employee firms [F][BZ][A].
- **Asbestos survey (#5), housing compliance (#1), Polish joinery agency (#4), CRA importer (#7):** no new evidence in this run.

## 7. Honest result

This instrument found a ranking a Dutch founder could produce in an afternoon from the same StatLine tables; nothing here is hidden. Its real finding is structural: survival is bought by having employees (72–81% at five years for 1–5-employee starters against 54–65% solo), and the sectors that survive best — machine repair, specialised construction, personal services — are exactly the Dutch-language, licence-bound trades. Owner income is only published at letter level (employers' median EUR 60–66k against EUR 41k solo), so "above-median owner income by niche" cannot be shown from public data. Listings are thin outside installation, garages and wholesale. The reader's edge is not sector choice but the crew: CEE-speaking technicians and B2B customers, and the paperwork Dutch owners avoid.
