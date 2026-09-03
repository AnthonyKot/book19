# Small physical businesses sold on Dutch owner succession

Research date: 2026-09-03  
Reader screen: English/Russian/Polish, A2 Dutch, €100k equity, regulatory literacy, engineering habit and a 30k LinkedIn audience (`drafts/edge-inventory.md`).

## Answer in one paragraph

The investable public-listing seam is not “Dutch retirement businesses” in general. It is small, owner-dependent physical firms whose customer interface can be separated from production: specialist B2B distribution, laundry/textile care, technical workshops, small-batch manufacturing, and event-equipment rental. All appeared below €400k, but only 5 of 60 sampled listings explicitly said retirement/succession. A2 Dutch therefore remains an operating-design gate, not a search filter: buy only where customers work in English/CEE languages or a Dutch-speaking manager/account owner stays. Hospitality, ordinary local retail and regulated care are plentiful but fail that gate more often. AI should lower administrative cost in the five shortlisted profiles without replacing their physical output by 2030; it is more likely to compress undifferentiated retail demand.

## Sources and limits

| Evidence family | What it establishes | Important limit | Saved excerpt |
|---|---|---|---|
| KVK [S1–S3] | Retirement motive, 67+ registrations, older-owner sectors | 2022 survey and register stocks do not predict completed sales | `sources/succession_and_sectors.txt` |
| ING [S6–S7] | Weak pension provision; succession can trigger strategy change | Current ING item is pension research; public succession material found was 2013-era and secondary | `sources/succession_and_sectors.txt` |
| Rabobank [S8–S11] | Wholesale, retail, food-craft and transport structure | Sector totals are not sub-€400k deal counts | `sources/succession_and_sectors.txt` |
| MKB-Nederland [S5] | SME scale, preparation time and older transaction/closure context | Advocacy synthesis; transaction data are from 2023 | `sources/succession_and_sectors.txt` |
| HU/Qredits/ONL [S4], ABN [S12] | Current transfer intent and age cross-check | Intent is not supply; neither study provides a price distribution | `sources/succession_and_sectors.txt` |
| RVO, Qredits, KVK [F1–F4] | Current published acquisition-finance terms | Guarantees and product ceilings are not credit approvals | `sources/finance.txt` |
| Brookz, Bedrijventekoop [V1–V4] | Adviser multiples and branch heuristics | Mostly larger deals; multiples omit deal perimeter and capex | `sources/valuation_and_transfer.txt` |
| KVK, Brookz, Overname Monitor [T1–T3] | Transfer process and first-100-day priorities | Guidance and survey associations, not performance guarantees | `sources/valuation_and_transfer.txt` |
| 60 marketplace profiles | Current asks and seller disclosure | Purposive snapshot; ads are unaudited and may be asset/lease packages | `sources/listings_sample.csv`; platform excerpts in `sources/listings_*.txt` |

The wave is credible but not a count of bargains. KVK found pension age/old age in 69% of relevant stop/transfer responses [S1], and counted 164,001 registered entrepreneurs aged 67+ at 2025-01-01 [S2]. HU/Qredits/ONL says more than one-third of small-business owners—over 500,000 firms—consider a sale within five years [S4]. ABN's current cross-check found more than two-thirds of 519 respondents intend to stop within ten years; 65+ owners rose from 7% in 2010 to 13% in 2025 [S12]. Yet listings show only disclosed seller intent, and retirement is often omitted or anonymised.

## Sector evidence

| Sector signal | Published evidence | Acquisition implication |
|---|---|---|
| Non-food wholesale | €458bn turnover, 420,000 jobs, 75% of value added export-linked; nearly half report labour shortage [S8] | Large B2B/export surface fits languages, but succession does not make a poor distributor valuable |
| Retail | More than half of vacancies hard to fill; retirements exceed entrants; smaller firms struggle with succession [S9] | Supply is plausible, but local Dutch service and AI/omnichannel pressure make generic shops weak fits |
| Food craft | Succession and labour shortages persist; warm bakers are pressured while specialists retain openings [S10] | Only differentiated, manager-run production passes; avoid buying a job |
| Inland shipping | About 70% of vessels pre-1980; about 30% of entrepreneurs older than 58 [S11] | Strong succession signal, rejected here because asset/capex scale does not match this sample |
| SME base | 83% of Dutch employer firms have 2–10 staff; MKB-Nederland says sale preparation needs at least 3–5 years [S5] | Small teams and long seller preparation make owner-dependence and knowledge transfer central risks |

## Listing evidence: 60 offers at or below €400k

Method: purposive, cross-sector snapshot of live public offers on 2026-09-03. Bedrijventekoop: 38 sale offers rechecked in the €0–100k or €100–250k bands. Brookz: seven exact asks, €49.5k–€310k. Marktplaats Zakelijk: 15 exact asks, €5k–€130k. No price-on-request ads were admitted. “Retirement” requires explicit pension/age/succession language; no inference. Quantitative disclosures exclude “confidential” and missing values. Full row-level title, region, ask, revenue, profit, staff, retirement flag and URL are in `sources/listings_sample.csv`.

| Sector (research classification) | n | ≤€100k | €100–250k | >€250–400k | Retirement explicit | Revenue disclosed | Profit disclosed | Staff disclosed |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Wholesale/trade | 9 | 5 | 3 | 1 | 0 | 6 | 6 | 8 |
| Workshop/repair/textile care | 11 | 5 | 5 | 1 | 2 | 6 | 6 | 9 |
| Light manufacturing | 6 | 6 | 0 | 0 | 0 | 3 | 3 | 4 |
| Logistics/rental | 5 | 4 | 1 | 0 | 1 | 3 | 3 | 4 |
| Hospitality | 12 | 9 | 3 | 0 | 0 | 8 | 3 | 8 |
| Care/wellness | 6 | 3 | 3 | 0 | 1 | 5 | 2 | 5 |
| Retail | 11 | 9 | 2 | 0 | 1 | 7 | 5 | 8 |
| **Total** | **60** | **41** | **17** | **2** | **5** | **38** | **28** | **46** |

Platform quality matters. Bedrijventekoop supplied bands for all 38 rows, but some financial bands were “confidential.” Brookz supplied staff for all seven, quantitative revenue for six and profit for five. Marktplaats supplied quantitative revenue for one of 15 and staff for one; several asks appear to cover inventory, equipment, lease transfer or a provincial operating package rather than shares in a going concern. The sample proves availability, not value or closing probability.

## What €100k equity can actually finance

| Route | Published envelope | Practical reading |
|---|---|---|
| Equity only | €100k reader capital | Reaches the 41/60 lowest ask bucket only if transaction costs and working capital are funded separately |
| Equity + Qredits maximum | €100k + €250k = €350k gross; 9.95% fixed, 1.5% fee, average five-year/max ten-year term [F3] | €250k amortises at €5,306/month over five years or €3,297/month over ten; calculations in `sources/calculations.txt` |
| Bank + BMKB | Acquisition allowed; guarantee structure depends on regular/small-credit/starter segment [F1–F2] | BMKB improves lender collateral, not underlying cash flow. Publicly insured care, finance and real estate are excluded |
| Seller loan / earn-out | KVK and HU describe stacked acquisition funding [F4, S4] | Useful for owner-dependent goodwill and knowledge transfer, but only if subordination and repayment leave liquidity |

The €400k search cap is thus a sourcing ceiling, not a safe bid. Qredits' maximum carries a €3,750 closing fee and about €63,667 first-year-equivalent debt service on a five-year amortising schedule. A €280k or €310k ask can fit nominally, but not if normalized EBITDA disappears after replacing the seller, inventory is extra, or machinery needs renewal. Ask for a debt-free/cash-free bridge, normalized owner wage, stock and working-capital peg, maintenance capex, and debt-service downside before discussing price.

## Multiples: valuation cross-check, not a bid formula

| Sector | Brookz H1-2025 low / average / high EBITDA multiple [V2] |
|---|---:|
| Retail | 1.8 / 2.3 / 3.0 |
| Hospitality | 2.8 / 3.1 / 4.1 |
| Automotive, transport & logistics | 3.7 / 4.1 / 4.5 |
| Industry | 4.5 / 5.0 / 5.5 |
| Wholesale | 4.8 / 5.2 / 5.9 |
| Health care | 5.8 / 6.4 / 7.1 |

The current H1-2026 overall average is 5.0, but a business at €200k normalized EBITDA averaged 3.6 versus 7.0 at €10m [V1]. Size, owner dependence and capex therefore matter more than the sector headline. Bedrijventekoop explicitly warns that multiples omit investment needs and risk [V3]. Reconcile a multiple with maintainable cash flow after market-rate owner/manager pay, deferred maintenance and taxes.

## A2 and AI gates

| Profile | A2 gate | AI-to-2030 gate | Decision |
|---|---|---|---|
| Specialist B2B distribution | Pass if accounts transact in English/CEE languages, otherwise retain Dutch account owner | Raises productivity; physical sourcing, compliance and fulfilment remain | Rank |
| B2B laundry/textile care | Conditional on Dutch route/account manager | Scheduling/inspection improve; cleaning remains physical | Rank |
| Technical workshop/maintenance | Conditional on Dutch reception/service manager and retained technicians | Diagnostics improve; repair/installation remain physical | Rank |
| Small-batch manufacturing | Pass for export/B2B with Dutch commercial cover | Quoting/design/QA improve; output remains physical | Rank |
| Event-equipment rental | Conditional on Dutch operations/customer lead | Planning improves; live events and assets remain physical | Rank |
| Ordinary hospitality | Fails: constant Dutch staff, guest, landlord and municipal interface | Demand remains, but automation does not remove service burden | Reject |
| Regulated care | Fails absent a licensed Dutch clinical/operating partner; some care is BMKB-excluded | Demand may rise, but liability and language remain | Reject |
| Generic local retail | Usually fails unless manager-run | AI/e-commerce increase price and convenience pressure | Reject |

## Ranked candidates

### 1. Specialist B2B distributor/importer with a Dutch account owner

Nine sampled wholesale/trade offers comprised five asks ≤€100k, three at €100–250k and one at €310k; six disclosed revenue and profit. Public profiles included food, health products, wine, workwear-adjacent goods and physical security. Rabobank sizes non-food wholesale at €458bn and 420,000 jobs, with 75% of value added export-linked [S8]. The edge is Polish/Russian/English sourcing, regulatory diligence, systems thinking and a 30k distribution audience. **A2:** pass only for English/CEE accounts or with a retained Dutch salesperson. **AI:** positive—better prospecting, quoting and inventory; physical fulfilment persists. **Paid test:** broker a paid pilot order between a CEE producer and one Dutch B2B buyer before bidding. **Kill fact:** a top supplier/customer, licence or exclusivity agreement is non-transferable or makes normalized cash flow unable to service acquisition debt.

### 2. B2B laundry, dry-cleaning or textile-care route

The workshop sample had 11 offers: five ≤€100k, five at €100–250k and one at €280k; two explicitly cited retirement. Two Brookz dry-cleaning profiles asked €70k on €183k revenue/€111k EBITDA and €280k on €400k/€120k; these are seller claims, not verified accounts. Brookz counts 885 dry cleaners in 2025, suggests 2.0–3.1× EBITDA and recommends B2B as traditional suit demand declines [V4]. Engineering discipline fits process, energy and routing; LinkedIn can reach hotels, clinics and workwear buyers. **A2:** conditional on a Dutch route/account manager. **AI:** positive/neutral; scheduling and inspection improve, cleaning remains physical. **Paid test:** sell a prepaid pickup contract to an English-speaking hotel or property operator using subcontracted capacity. **Kill fact:** normalized earnings after energy, water/environmental compliance, equipment renewal and manager pay fall below debt service.

### 3. Technical maintenance workshop with retained technicians

The 11 workshop offers included garages, watersport maintenance, copy/passport production and textile care; five asked ≤€100k, five €100–250k and one €280k. Nine disclosed staff and two explicitly cited retirement. The edge is an engineering habit, regulatory literacy and process documentation—not doing every repair personally. **A2:** conditional: a Dutch-speaking service adviser must own reception, estimates and complaints while the buyer runs systems and B2B growth. **AI:** positive/neutral; diagnostics, parts search and scheduling improve, while installation and repair stay local and physical. **Paid test:** sell one paid fleet or marina inspection day through the incumbent team before exclusivity. **Kill fact:** the seller is the only certified technician or personally owns the customer relationships, so replacement wages erase maintainable EBITDA.

### 4. Small-batch physical manufacturer serving B2B/export

All six sampled light-manufacturing offers were ≤€100k; three disclosed quantitative revenue and profit. Profiles spanned small boats, plastics, modular products, a bakery concept and production equipment. Brookz's H1-2025 industry range was 4.5–5.5× EBITDA, but its current research shows materially lower multiples for small EBITDA firms [V1–V2]. Engineering and automation discipline fit quoting, job costing and quality; Polish/Russian/English helps suppliers and export. **A2:** pass for export/B2B only with Dutch commercial cover. **AI:** positive—design, quoting and QA get cheaper, while fabrication remains physical. **Paid test:** obtain a paid contract-production batch from an English-speaking customer using the seller's team under a pre-close cooperation agreement. **Kill fact:** profit is unpaid owner labour, or near-term machinery, food-safety/environmental or premises investment consumes the €100k equity reserve.

### 5. Event-equipment rental and delivery operation

Five rental/logistics profiles produced four asks ≤€100k and one at €100–250k; one explicitly cited retirement. A Brookz tent-rental profile asked €75k, stated €86,363 revenue and one FTE; profit was not stated. The edge is operational engineering, multilingual suppliers, B2B LinkedIn reach and route/utilisation analytics. **A2:** conditional on a Dutch booking/operations lead; English-speaking corporate events help. **AI:** positive/neutral through quoting, dispatch and utilisation, while assets and setup remain physical. **Paid test:** pre-sell a paid corporate-event package and fulfil it with rented inventory before acquisition. **Kill fact:** verified utilisation, damage/insurance cost and seasonal cash flow cannot support manager pay, fleet replacement and debt amortisation.

## First 100 days after closing

| Timing | Minimum transfer work |
|---|---|
| Before close | Buyer profile and investment thesis; sales memorandum; LOI with exclusivity/conditions; financial, tax, legal, HR, permit, environmental, cyber and commercial due diligence; financing and purchase agreement [T1] |
| Day 1 | Seller and buyer jointly address staff; call key customers and suppliers; state what remains unchanged; confirm decision rights, banking, insurance, payroll and emergency contacts [T2] |
| Days 1–30 | Listen and shadow. Build a weekly 13-week cash view, customer/supplier concentration map, owner-task inventory and maintenance/permit calendar. Retain Dutch customer owners and scarce technicians. Do not force a rebrand |
| Days 31–60 | Resolve employment-contract, trademark and old-receivable issues; validate job/customer margins, stock, recurring orders and service backlog; document pricing, quality and complaints [T2] |
| Days 61–100 | Transfer seller relationships and tacit know-how; run only low-risk pilots in quoting, scheduling and CEE sourcing; set operating KPIs and board/lender cadence; agree seller-support exit milestones |

The handover should be priced as part of the deal. In the Overname Monitor, 37% of buyers continued immediately without the seller; the figure was 53% without an adviser versus 30% with one, while advised buyers more often retained sellers for six to twelve months [T3]. This association is not causal, but it supports using seller finance/earn-out and documented transition milestones where goodwill is personal.

## Honest result

This instrument found a disciplined shortlist, not a secret unavailable to a Dutch founder. Every category and listing is public, and a native Dutch buyer would screen customer language and municipal obligations faster. The useful edge is cross-border: CEE sourcing and languages, regulatory/process discipline, and a 30k audience can improve a B2B distributor or physical service firm after purchase. But only 5/60 ads explicitly disclosed retirement, figures were unaudited, and Marktplaats disclosure was especially thin. The defensible insight is therefore the rejection rule—owner-independent cash flow plus retained Dutch customer ownership—not privileged deal discovery.
