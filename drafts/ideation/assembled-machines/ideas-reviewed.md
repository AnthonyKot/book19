# Ideation review — assembled machines (seed A) — Fable 5.1, 2026-09-04

Review of `ideas.md` against the eight-part shape in `scripts/prompts/idea-metaprompt.md`, with the part the
run lacked: part 8, the precedent. Budget twenty-five fetches; every fetched page saved under `sources/`
(precedents as `precedent-<id>.txt`, verifications as `verify-<topic>.txt`). Nothing invented; a figure the
fetch did not confirm stays "unverified". Written incrementally; the fetch log is at the end.

## What the verification pass settled

| claim in `ideas.md` | result | source |
|---|---|---|
| Machinery Regulation 2023/1230 applies 20 Jan 2027; assembler-as-manufacturer; AI safety-function clause | **verified** (date, AI clause); the Art. 3/18 "substantial modification" wording **stays unverified** | `verify-machinery-regulation.txt` (Commission) |
| EN ISO 10218-2:2025 replaces the 2011 text | **verified as published** (Feb 2025, ISO 73934); OJ citation under 2023/1230 **unverified** | `verify-iso-10218-2.txt` |
| Product Liability Directive 2024/2853: modifier = manufacturer, 9 Dec 2026 | **verified** | `verify-product-liability-directive.txt` (Commission) |
| Battery Regulation: labelling 18 Aug 2026, QR/passport 18 Feb 2027 (>2 kWh industrial) | **confirmed by trade summaries**, not the OJ; due-diligence date **conflicting** (2025 in one summary; postponed to 2027 from knowledge) | `verify-battery-regulation-dates.txt`, `verify-battery-regulation-commission.txt` |
| AI Act product rules 2 Aug 2027 | **corrected**: Annex I high-risk applies 2 Aug 2028 per the FLI timeline (Annex III 2 Dec 2027); secondary source | `verify-ai-act-timeline.txt` |
| Incumbent prices €6k / €20k / €30k | verified in the run | `iab-ce-kosten.txt` |
| NL robot installations 2024–25 | **still unverified** (no fetch spent) | — |
| Every unit price, entry cost, capital figure | **estimate**, as before | — |

## Kept ideas, re-screened

### A. The cell file — CE for cells, lines and fleets assembled on the floor — **KEEP**

1. **Iron plus paper.** A cobot cell, palletiser, AMR fleet or packing line assembled from CE-marked parts is a new machine; whoever installs it owes risk assessment, technical file and declaration. *(Shape verified by two integrators' own pages: Olympus "the integrator is normally the manufacturer"; Nooteboom case delivered "CE-markering voor het samenstel".)*
2. **Dated rule.** 20 Jan 2027, Regulation 2023/1230 **(verified)**; EN ISO 10218-2:2025 published, OJ citation pending **(partly verified)**.
3. **Buyers.** SME manufacturers of 10–100 staff and small integrators, Polish ones included. Incumbents €6,000 per machine, €30,000 per assembly **(verified)**.
4. **Edge.** Reads the Regulation; a templated evidence trail with measured force and stopping distance; Polish integrator channel. No Dutch exam **(the UK precedent's only credential is a private "Certified Machinery Safety Expert" badge, not a state exam)**.
5. **Per unit.** €1,500–3,000 per cell, €4–8k per line **(estimate)**; first test three cells for one integrator ≈ €4,500; measuring set €5–10k **(estimate)**. Step two: Dutch safety engineer. Step three: see addition E.
6. **AI.** Every cheaper cobot is one more assembly; the force measurement is a person with a meter at the cell.
7. **Kill fact.** A distributor bundles the cell file free, or a bureau sells it at ≤€1,500. **Not triggered by what was found**: Olmia does the risk analysis "samen met jou" and does not advertise a CE file; Automise had its RI&E "beoordeeld door een extern deskundige".
8. **Precedent — found.** *Cobots and Machinery Safety Ltd*, Corby, UK: one engineer (Matt Androsiuk), incorporated 10 July 2019, company 12096383, active; sells "Cobot Risk Assessments", "Cobot Force and Pressure Testing", "UKCA and CE Marking", light-curtain testing and EN ISO 10218-2 training to "UK manufacturers"; no prices published. Second, older: *Machine Safety Specialists*, Ohio, "since 1977", industrial and collaborative robot safety assessments and validation to ANSI/RIA and ISO standards. Third-tier: *CE-CON GmbH*, Bremen, 20+ years, but half software. (`precedent-A-*.txt`)

Decided by: part 8 found, part 7 not triggered. The exit line is also visible: `laidler.co.uk`, a UK CE consultancy's domain, now serves a TÜV SÜD certificate (lead, not verified).

### B. The old iron — the substantial-modification file — **KEEP**

1. **Iron plus paper.** A machine retrofitted or recommissioned; if the change adds a hazard the modifier becomes manufacturer and owes a new file; if not, a signed memo.
2. **Dated rule.** PLD 2024/2853: "The person that has made the modification becomes a manufacturer", applies to products placed on the market from 9 Dec 2026 **(verified)**; Machinery Regulation 20 Jan 2027 **(verified)**; Art. 18 wording **(unverified)**.
3. **Buyers.** Polish- and Ukrainian-owned metal, wood and food workshops of 10–100 staff; Polish retrofit shops. Incumbent €20,000 per large machine **(verified)**.
4. **Edge.** Reads the Directive and Regulation; a modification register; Polish channel. No Dutch exam.
5. **Per unit.** €900 memo; €2,500–5,000 re-CE **(estimate)**; first test five machines in one workshop ≈ €4,500; capital <€5k **(estimate)**. Step three: buy the retrofit shop (fits triage #3).
6. **AI.** Retrofit is how AI reaches old plants; each retrofit is a question answered at the guard.
7. **Kill fact.** Like-for-like swaps never count, or inspectors never enforce. **Not tested this pass.**
8. **Precedent — found at trade level.** Poland has a whole small-firm trade in "dostosowanie maszyn do wymagań minimalnych": *Farem Poland*, Czechowice-Dziedzice, sells "ogólny audyt bezpieczeństwa – w tym ocena ryzyka wynikającego z eksploatacji", the safety components, the modernisation and the CE after modification; a February 2026 sponsored piece in 300Gospodarka by a second firm (Engineering Shield) describes the same service line; the search surfaced six more (InTime Automation, Automatech, MTA, Raccord, EcoMS, Cert Partner). No firm published a per-machine price, size or age; no firm-level independent trace was fetched. (`precedent-B-*.txt`)

Decided by: part 8 (trade exists, and it is the reader's own Polish network); the Polish firms also show step three: they sell the retrofit, not only the memo.

### C. The pack — CE and passport file for battery packs assembled in NL — **WATCH**

1. **Iron plus paper.** A lithium pack assembled from cells is a battery placed on the market by its assembler: CE, declaration, technical file, label, QR, passport above 2 kWh.
2. **Dated rule.** Labelling 18 Aug 2026; QR and passport 18 Feb 2027 for industrial batteries >2 kWh **(confirmed by trade summaries, not OJ)**; due diligence date **(conflicting, unverified)**.
3. **Buyers.** Electric-boat yards, AGV builders, forklift electrifiers, Polish pack assemblers. Incumbent €10–30k test-and-CE per model **(estimate)**.
4. **Edge.** Reads the Regulation and the passport acts; cell-to-pack traceability template. No Dutch exam.
5. **Per unit.** €2,500–5,000 per model; €5–20 per pack **(estimate)**; first test one yard's model ≈ €4,000.
6. **AI.** Robots, AMRs and drones carry packs; each model is a file with a physical test behind it.
7. **Kill fact.** The module supplier's passport covers the pack, or the passport makes it software. **Untested.**
8. **Precedent — not found.** A fair search found the incumbents (TÜV SÜD, Intertek, UL), a German testing-and-engineering firm (*BatterieIngenieure GmbH*, Aachen, ISO 9001/14001/27001, TISAX; no regulatory line on its page) and a generic UK CE consultancy (*Conformance Ltd*, Buxton) with an information page and no stated battery service. No small firm anywhere was found earning its living on per-pack files. (`precedent-C-*.txt`)

Decided by: part 8. Downgraded to WATCH per the brief's rule; the shape may be real but nobody visible lives on it yet, and the passport half sits on the book's software line.

### D. The learning machine — notified-body file for AI safety functions — **CUT**

1–3 as in the run. 2. **Dated rule.** Machinery Regulation 20 Jan 2027 **(verified, incl. the AI safety-function clause)**; AI Act Annex I date **corrected to 2 Aug 2028** (secondary source), so the second deadline slips past the book's 2028 window.
4. **Edge.** The evidence is data-validation work: the book's IT line.
5–6 as in the run. 7. **Kill fact** (no SME integrator uses ML safety functions in 2027): **not disproved**; every result found was a vendor or a large body.
8. **Precedent — not found** after a fair search (`precedent-D-search.txt`).

Decided by: part 8 and part 4 together; part 2 weakened.

## Verdicts

| id | idea | verdict | decided by |
|---|---|---|---|
| A | The cell file | **KEEP** (TEST NOW) | part 8 found (UK one-engineer firm, 2019, active); kill fact not triggered |
| B | The old iron | **KEEP** (TEST NOW) | part 8 found at trade level in Poland; part 2 now verified via PLD |
| C | The pack | **WATCH** | part 8 not found; passport half is software-adjacent |
| D | The learning machine | **CUT** | part 8 not found; part 4 (data work); AI Act date slipped to 2028 |
| E | Cell file → one-application integration (addition, tested) | **TEST THROUGH A PARTNER** as step three of A | part 5 (capital) fails as an entry; part 8 found |

## Additions

### E. The one-application cell — palletising or machine-tending, installed and signed (the brief's test idea)

1. **Iron plus paper.** A palletising or machine-tending cobot cell, supplied "complete, installed" and put into service: the supplier "is normally the manufacturer" (Olympus, verbatim) and owes the whole file.
2. **Dated rule.** Same as A: 20 Jan 2027 **(verified)**; the assembler-as-manufacturer rule makes the file the product, not an extra.
3. **Buyers.** SME manufacturers and pack-houses of 10–100 staff buying a first cell; in the UK such a cell sells at "£65,000 to £115,000", of which "approximately 65%" is hardware and 35% integration, safety sensors and commissioning (Olympus guide, **verified as a UK list price**; NL equivalent **estimate**).
4. **Edge.** The file and the measurement are the reader's; the mechanical build is subcontracted to a Polish integrator (part of the reader's channel in A). No Dutch exam.
5. **Per unit.** The 35% share is £23–40k per cell (derived); the reader's margin on it **(estimate)**. First paid test under €5,000: impossible as an integration; possible only as the file-plus-validation slice of a partner's cell. Capital: hardware on the client's purchase order, else >€50k **(fails part 5 as an entry)**. Step two: Dutch-speaking partner integrator. Step three: this idea itself.
6. **AI.** Palletising and tending cells are the first application of every cheaper cobot; each is one assembly, one file, one measurement.
7. **Kill fact.** Dutch distributors sell packaged palletiser cells with the file included at list price, leaving no slice for a third party. **Untested**; one of three "Cobots ..." companies on the UK register was dissolved within three years (Companies House), so dealer churn is real.
8. **Precedent — found, firm site only.** *Olympus Technologies*, Huddersfield: "an innovative robotic integrator, specialising in delivering high quality bespoke turnkey projects", publishes cell prices and takes the manufacturer role; size and age not on the pages fetched; no independent trace within budget. (`addition-olympus-*.txt`)

**Do Dutch cobot dealers subcontract CE today?** Two data points, no survey: Olmia (Tiel) does the risk analysis "samen met jou" and does not advertise CE; Automise wrote Nooteboom's RI&E with the customer's safety officer and had it "beoordeeld door een extern deskundige" (MetaalNieuws, 2021). So dealers do the analysis in-house and, at least sometimes, buy an external review. The external review is A's slot; E is what A grows into. Verdict: not an entry, a step three. (`addition-*.txt`)

### Second addition: none proposed

The fetches produced one lead without a fetch to spare: *Cobots and Machinery Safety* also sells "Light Curtain Testing", a recurring per-cell safety-function verification. Whether Dutch bureaus already sell periodic safety-function verification cheaply was not checked, so it is a lead for a research run, not an idea.

## What the precedent test changed (≤120 words)

It sorted the four ideas by whether anyone lives on them. A has a one-engineer precedent seven years old and active, plus a US firm that has done the same since 1977; B has an entire Polish small-firm trade behind it, which is also the reader's own network; C and D have nobody visible. The pass also corrected one date (AI Act Annex I to 2028) and verified three (Machinery Regulation, PLD, ISO 10218-2 publication). The one thing it could not show is a price: no precedent publishes what it charges per cell or per machine, so every unit price in this file is still an estimate, and the first phone call of the research run is "what did you pay for the file?"

## Fetch log (25 of 25)

1 Commission machinery page · 2 Commission batteries page · 3 Commission PLD page · 4 FLI AI Act timeline · 5 ce-con.de · 6 laidler.co.uk (failed, TLS) · 7 machinesafetyspecialists.com · 8 batterieingenieure.de · 9 robotobor.nl · 10 search: cobot integrator CE · 11 cobotsmachinerysafety.co.uk · 12 Olympus CE guide · 13 Olympus palletiser cost · 14 search: Dutch dealers CE · 15 search: battery dates · 16 search: Poland minimum requirements · 17 search: battery consultancy · 18 search: ML safety functions · 19 Companies House · 20 MetaalNieuws Nooteboom · 21 Olmia diensten · 22 farempoland.pl · 23 300gospodarka · 24 conformance.co.uk · 25 search: ISO 10218-2.
Not fetched: EUR-Lex (any form), NL robot counts, a Polish per-machine price, an independent trace for Farem or Olympus.
