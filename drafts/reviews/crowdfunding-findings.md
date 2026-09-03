# Crowdfunding as a paid-demand instrument: EU distribution gaps

**Cut-off: 3 September 2026.** The answer is narrower than the campaign leaderboards suggest. Of the 40 highest-grossing qualifying projects in the published Kickstarter data, 35 already have an established EU route, two sell directly into Europe without a European distributor, and three were not yet in EU retail. The defensible output is five leads for maker outreach and document diligence—not five ready-to-import SKUs.

## Data and method

“Proven elsewhere” means a physical product launched in 2023–2026 by a non-EU creator/platform market, with at least USD 250,000 (or a documented local equivalent) and at least 1,000 backers/supporters. United Kingdom creators remain in scope. Kickstarter's `converted_pledged_amount` supplies USD; the Makuake screen converts JPY using the [ECB cross-rate note](../../resources/sources/method/exchange-rate.md). Campaign location is creator country, not buyer location.

| Platform | Public evidence used | What can and cannot be calculated |
|---|---|---|
| Kickstarter | Web Robots 2023-12-14 baseline and 2026-08-12 latest archive; URLs/MD5 in [data README](../../resources/data/README.md) | Funding, backers and observed completed-project success rate by category/country; 2026 is partial. |
| Indiegogo | Web Robots 2025-10-13 archive and [official 2023 roundup excerpt](../../resources/sources/indiegogo/webrobots-and-top-2023.md) | Category amount and an inferred archive outcome through 2025. `perks_claimed` is blank/zero in this cohort, so backer totals and the two-part product screen are unavailable. |
| Makuake | [Official 2025 annual report/award excerpt](../../resources/sources/makuake/official-2024-2025.md) | Annual total and named leaders; no complete category/success denominator. Three products have enough amount and supporter evidence for the screen. |
| Wadiz | [Public 2023 trend-report excerpt](../../resources/sources/wadiz/2024-trend-report.md) | Editorial trends only. The site prohibits unauthorized crawling, so no project aggregate was built. |
| Zeczec | [Official profile excerpt](../../resources/sources/zeczec/platform-scale.md) | Cumulative platform scale, not a dated project leaderboard with both fields. |
| JD / Modian | [JD closure](../../resources/sources/jd/service-closure.md); [Modian study](../../resources/sources/modian/public-study.md) | JD product crowdfunding ended in 2022. The Modian study reports a project corpus but not a public row-level product table. |
| Gulf | [Official/public landscape excerpt](../../resources/sources/gulf/platform-check.md) | Current measurable scale is mainly equity/debt. A reward platform exists, but no qualifying public product table was found. |

The script and reproducible outputs are [analyze_crowdfunding.py](../../scripts/analyze_crowdfunding.py), [platform-category-summary.csv](platform-category-summary.csv), [kickstarter-category-country.csv](kickstarter-category-country.csv), [proven-elsewhere.csv](proven-elsewhere.csv), [top-40-eu-check.csv](top-40-eu-check.csv), and [analysis-audit.json](analysis-audit.json).

### Kickstarter physical-category snapshot

Amounts and backers below are for successful projects in the observed archive cohort. “Rate” is successful / (successful + failed); live/other projects are excluded. Games here means only tabletop games and playing cards. Art is physical printing. Full year/category rows are in the platform CSV.

| Physical parent | Observed success rate 2023 / 2024 / 2025 / 2026 | Successful pledged USD, 2023–2026 | Backers, 2023–2026 |
|---|---:|---:|---:|
| Technology | 75.00% / 82.47% / 81.81% / 85.81% | $795,131,529 | 2,109,686 |
| Design | 98.60% / 86.54% / 84.05% / 86.84% | $344,389,578 | 2,159,758 |
| Tabletop/playing-card games | 91.39% / 92.95% / 92.12% / 95.31% | $218,327,719 | 2,531,648 |
| Fashion | 77.14% / 59.19% / 50.59% / 53.97% | $34,250,145 | 262,589 |
| Crafts | 44.12% / 44.76% / 43.36% / 48.17% | $5,392,670 | 47,125 |
| Food | 39.13% / 37.06% / 37.08% / 42.25% | $4,154,584 | 47,235 |
| Physical printing under Art | — / 75.00% / 70.00% / 85.71% | $185,950 | 2,243 |

These rates are **not platform-wide rates**. Web Robots documents a Kickstarter category result cap and duplicate appearances across subcategories; the script deduplicates IDs, but cannot recover omitted projects. The unusually high observed Design/Games rates are a warning about discovery-page skew, not a finding that nearly every campaign succeeds.

### Kickstarter creator-country snapshot

The full output has 541 year × country × category rows. The six largest non-EU creator countries by successful pledged amount are shown to keep the table short.

| Creator country | Completed projects | Observed success rate | Successful pledged USD | Backers on successful projects |
|---|---:|---:|---:|---:|
| United States | 10,556 | 78.18% | $857,763,151 | 4,046,338 |
| Hong Kong | 2,391 | 92.89% | $278,757,255 | 998,996 |
| United Kingdom | 2,341 | 82.02% | $63,176,032 | 576,805 |
| Canada | 1,183 | 78.53% | $36,295,762 | 290,933 |
| Australia | 641 | 79.88% | $18,487,767 | 133,379 |
| Singapore | 227 | 73.57% | $16,691,646 | 56,748 |

### Indiegogo category snapshot

This is the archive cohort for 2023–2025, ranked by successful USD. Backers are reported as unavailable, not zero consumers. Non-USD campaigns contribute zero to the USD column; outcome is inferred from close date and funding percentage.

| Physical category | Completed | Inferred success rate | Successful USD | Backers |
|---|---:|---:|---:|---:|
| Travel & Outdoors | 218 | 4.59% | $5,850,229 | unavailable |
| Health & Fitness | 136 | 3.68% | $4,069,439 | unavailable |
| Energy & Green Tech | 40 | 2.50% | $2,247,960 | unavailable |
| Home | 123 | 4.07% | $2,193,081 | unavailable |
| Productivity | 108 | 10.19% | $1,683,628 | unavailable |
| Camera Gear | 17 | 23.53% | $1,646,627 | unavailable |

## Proven elsewhere and EU-seller audit

The machine-readable list contains **647 qualifying rows: 644 Kickstarter projects plus three Makuake projects**. The EU audit covers the top 40 by reference USD. `EU` means an EU shop, named European seller/distributor or EU warehouse route was found; `EU-direct` is the maker's explicit EU sales route; `Direct only` means a non-EU maker accepts EU destinations but no European distributor was found; `No EU retail` means no retail channel was found on the check date. Each search method, date and evidence URL is in the [structured audit](top-40-eu-check.csv) and [saved check excerpt](../../resources/sources/eu-seller-checks/top-40.md). Compliance labels are triage, not legal conclusions.

| # | Product | Launch / creator | Raised | Backers | EU status | CE/CRA relevance triage |
|---:|---|---|---:|---:|---|---|
| 1 | eufyMake E1 UV printer | 2025 US | $46,762,258 | 17,822 | EU | electrical, machinery/UV, connected |
| 2 | Official Cyberpunk TCG | 2026 US | $28,353,088 | 50,773 | EU | possible toy |
| 3 | Snapmaker U1 3D printer | 2025 US | $20,614,548 | 20,680 | EU | electrical, machinery, connected |
| 4 | XGIMI Titan Noir projector | 2026 US | $19,372,823 | 6,178 | EU | electrical, radio/connected, laser |
| 5 | AWOL Aetherion projector | 2026 US | $18,649,456 | 7,050 | EU | electrical, radio/connected, laser |
| 6 | NestWorks C500 CNC | 2025 HK | $13,282,869 | 3,541 | **No EU retail** | electrical, machinery, CRA interface triage |
| 7 | Makera Z1 CNC | 2025 HK | $12,407,876 | 8,284 | EU | electrical, machinery, connected |
| 8 | Smith Blade multi-tool | 2025 CA | $11,172,733 | 38,323 | EU | GPSR/packaging |
| 9 | Valerion VisionMaster projector | 2024 US | $10,921,452 | 4,824 | EU | electrical, radio/connected, laser |
| 10 | LiberNovo Omni chair | 2025 HK | $10,232,267 | 11,620 | EU | electrical, connected |
| 11 | UGREEN AI NAS | 2026 US | $8,844,449 | 3,872 | EU | electrical, connected |
| 12 | Nebula X1 Pro projector | 2025 US | $8,243,808 | 2,322 | EU | electrical, radio/connected, laser |
| 13 | Lymow One robot mower | 2024 US | $7,488,321 | 3,415 | EU | electrical, machinery, radio/connected |
| 14 | BB-777 boombox | 2026 US | $7,131,764 | 9,334 | **Direct only** | electrical, radio/connected, battery |
| 15 | Game Changer: Home Edition | 2026 US | $7,018,438 | 48,989 | **No EU retail** | possible toy |
| 16 | UGREEN NASync | 2024 US | $6,678,664 | 13,285 | EU | electrical, connected |
| 17 | JetKVM | 2024 US | $5,927,862 | 45,880 | EU | electrical, connected |
| 18 | AEKE S1 Pro home gym | 2026 US | $5,866,348 | 1,885 | EU | electrical, machinery, connected |
| 19 | Anker SOLIX F3800 | 2023 US | $5,813,434 | 1,570 | EU | electrical, battery |
| 20 | XLASERLAB X1/X1Pro | 2025 HK | $5,233,622 | 1,706 | EU | electrical, machinery, laser |
| 21 | xTool WonderPress | 2026 US | $5,191,321 | 9,251 | EU | electrical, machinery |
| 22 | TIMEMORE electric grinder | 2023 SG | $5,005,317 | 10,836 | EU | electrical |
| 23 | Meticulous Espresso | 2023 US | $4,960,578 | 3,774 | EU | electrical |
| 24 | FibreSeeker 3 | 2025 US | $4,698,825 | 1,539 | EU | electrical, machinery, connected |
| 25 | RingConn Gen 2 | 2024 US | $4,415,966 | 18,428 | EU | electrical, radio/connected, battery |
| 26 | Longer ePrint UV printer | 2025 US | $4,294,357 | 1,621 | EU | electrical, machinery, connected |
| 27 | iGarden Swim Jet X | 2026 US | $4,243,667 | 2,093 | EU | electrical, machinery, battery, connected |
| 28 | Hestia smartphone telescope | 2023 US | $4,129,095 | 13,983 | EU | GPSR/optical product |
| 29 | Titan 2 Elite phone | 2026 HK | $4,079,856 | 8,836 | EU | electrical, radio/connected, battery |
| 30 | Circular Ring 2 | 2025 US | $4,078,500 | 13,695 | EU | electrical, radio/connected, battery |
| 31 | Rokid AI/AR Glasses | 2025 HK | $4,029,730 | 5,875 | EU | electrical, radio/connected, battery |
| 32 | Pongbot Aura sports robot | 2026 HK | $4,014,157 | 4,836 | EU | electrical, machinery, radio/connected, battery |
| 33 | Flux Keyboard | 2023 AU | $3,602,284 | 8,171 | **Direct only** | electrical, connected by USB |
| 34 | ZX Spectrum Next Issue 3 | 2025 GB | $3,541,371 | 7,524 | EU | electrical, data interface |
| 35 | eufy S1 Pro robot vacuum | 2024 US | $3,511,133 | 3,196 | EU | electrical, machinery, radio/connected, battery |
| 36 | Carvera Air CNC | 2024 US | $3,469,320 | 2,098 | EU | electrical, machinery, connected |
| 37 | ELEGOO OrangeStorm Giga | 2023 US | $3,386,996 | 2,005 | EU | electrical, machinery, connected |
| 38 | Kode Dot maker device | 2025 US | $3,360,759 | 16,171 | EU | electrical, data interface, battery |
| 39 | Halliday AI glasses | 2025 US | $3,305,917 | 8,023 | EU-direct | electrical, radio/connected, battery, optical |
| 40 | Night Storm X3 | 2025 US | $3,248,440 | 5,879 | **No EU retail** | electrical, battery, optical/laser, CRA interface triage |

The three Makuake additions are below. Badge counts are lower bounds where marked; the amounts are the exact figures in Makuake's annual report.

| Product | 2025 support purchases | Supporters | EU check on 2026-09-03 |
|---|---:|---:|---|
| il modo Air wallet | JPY 226,212,500 | at least 10,000 | No European seller found; Japan and Taiwan channels found |
| COFO Chair Pro 2 | JPY 208,802,697 | 3,949 | Global USD shop and Japan sellers; no European seller found |
| iFLYTEK AINOTE Air 2 | JPY 129,557,650 | at least 1,000 | Official German shop found |

## Ranked candidate opportunities

The ranking emphasizes channel gap, manufacturer readiness and how much EU regulatory execution can add. It is a contact list, contingent on maker consent and documents—not an invitation to copy products.

### 1. NestWorks C500 desktop CNC

Kickstarter launched 2025-11-04 and records **$13,282,869 from 3,541 backers**. No EU checkout or named reseller was found; the project was still moving through fulfillment. The route is an EU distribution agreement conditional on a technical-file audit, production sample and service-parts plan. Scope likely includes Machinery Directive 2006/42/EC for pre-transition placement and Regulation (EU) 2023/1230 from 2027-01-20, plus EMC 2014/30/EU, RoHS 2011/65/EU, WEEE 2012/19/EU, PPWR 2025/40 and RED/CRA 2024/2847 if its interfaces bring them into scope. **Kill fact:** the maker cannot provide a complete design risk assessment, test evidence and software/update access before the first EU order.

### 2. COFO Chair Pro 2 / COFO chair family

Makuake's 2025 report records **JPY 208,802,697 and 3,949 supporters**. COFO has Japan retail and a global USD shop, but the dated search found no European seller. This is a lower-technical-risk distribution agreement: EU responsible-person/traceability work under GPSR 2023/988, material declarations under REACH 1907/2006, localized warnings/assembly instructions, PPWR 2025/40 and national packaging EPR. A non-powered chair should not receive CE merely as a sales badge. Local spare parts and returns are the operating moat. **Kill fact:** landed freight plus bulky-product return reserve leaves no wholesale margin at a competitive EU price.

### 3. il modo Air wallet family

The 2025 Makuake result is **JPY 226,212,500 with a badge for at least 10,000 supporters**. The maker's public channels found were Japanese/Taiwanese; no European seller surfaced. Seek an authorized EU distribution and localization agreement, preserving the STATUSY design and brand. Work is GPSR 2023/988 traceability and complaint/recall process, REACH 1907/2006 evidence for leather dyes/metal parts, PPWR 2025/40, country packaging EPR and consumer-law returns; CE is not applicable to an ordinary wallet. The small parcel and no-electronics profile make this the cleanest validation pilot. **Kill fact:** handmade production capacity cannot support wholesale allocation after domestic orders.

### 4. BB-777 boombox

Kickstarter launched 2026-03-24 and records **$7,131,764 from 9,334 backers**. Bumpboxx now accepts EU destinations from its US-dollar shop, but no European distributor was found. An agreement could add EU inventory, repair/returns and compliance ownership. The published specification has Bluetooth, a 97.6 Wh Li-ion battery and 100–240 V AC input, triggering a serious file/test review under RED 2014/53/EU, EMC 2014/30/EU, LVD 2014/35/EU, RoHS, WEEE, Batteries Regulation 2023/1542, CRA 2024/2847, GPSR and PPWR/EPR. **Kill fact:** dangerous-goods freight, product weight and local warranty replacements erase distributor margin.

### 5. Night Storm X3 digital night vision

Kickstarter launched 2025-12-10 and records **$3,248,440 from 5,879 backers**. On the check date DVX called it Kickstarter-only, “not in stores” and said retail comes later: a clear moment to propose an authorized EU channel. The pre-scan must cover EMC, RoHS, WEEE, Batteries Regulation 2023/1542, GPSR, PPWR/EPR and laser/optical safety for the rangefinder. CRA 2024/2847 and RED apply only if the production interface/radio design meets their scope; the public page does not establish that. **Kill fact:** conformity or member-state use review shows the rangefinder/consumer positioning cannot be sold across the target EU markets without redesign or fragmented restrictions.

## What this evidence does not prove

Backers are not necessarily unique consumers, a pledge is not delivered revenue, and a launch spike is not repeat retail demand. The best published delivery-risk check located is an older Kickstarter survey of 47,188 backers estimating about 9% project non-delivery, with a plausible 5%–14% range; it is context, not a 2023–2026 adjustment factor ([saved excerpt](../../resources/sources/method/fulfillment-risk.md)). Campaign data also overrepresent English-language, launch-oriented products; creator country is not buyer geography; add-ons can inflate backer value; category caps omit projects; 2026 is incomplete; and EU availability can change immediately after the dated check. Before outreach becomes inventory, obtain delivered-unit counts, refund/chargeback and defect rates, repeat non-campaign sales, bill of materials, test reports, technical documentation, IP ownership, product-liability coverage, gross-margin schedule and territorial rights.

## Honest answer: ideas or Amazon inventory?

Mostly **things Europe already sells**. Thirty-five of the top 40 already had an established EU route; two more sold direct to Europe, and only three were not yet retail products. FibreSeeker 3 looked like a gap until a Netherlands seller with a euro price surfaced, while iFLYTEK and RingConn were already localized. The cross-platform difference is therefore not a hidden warehouse of easy imports. It is **three credible outreach leads plus two higher-risk channel bets**, with the Japanese non-electrical families providing the cleanest tests and the CNC/audio/optics products providing the strongest regulatory moat. Any of the five can vanish on maker outreach, document review or landed economics.
