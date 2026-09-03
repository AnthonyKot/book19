# Crossing flows — review and additions pass (Fable 5.1, 2026-09-04)

Reviewing `ideas.md` (agent B, same day) against the eight-part shape in
`scripts/prompts/idea-metaprompt.md`. The ideation run had no part 8 (precedent); this pass adds it,
re-attempts every figure marked "unverified", re-screens each idea, and tests the crowdfunding
machinery hub the brief asked for. Budget: 25 fetches, searches counted. Every fetched page saved under
`sources/`. Marks: **verified** = saved excerpt; **estimate** = from knowledge, unverified.

Fetch log (appended as spent):

| # | type | target | result | saved as |
|---|---|---|---|---|
| 1 | search | EUDR DDS services for small importers | SaaS and large brokers only | search-01-eudr-services.txt |
| 2 | search | CBAM Beratung KMU (DE) | Ingdilligenz found; COM(2025) 783 dated 16 Dec 2025 | search-02-cbam-de.txt |
| 3 | search | SME sanctions/export-control boutiques | US law firms; two US boutiques | search-03-sanctions-consultancy.txt |
| 4 | search | not-waste file for used machinery | GOV.UK WEEE guidance only | search-04-used-machinery-waste.txt |
| 5 | search | Makera / NestWorks EU dealers | Makera own EU store exists | search-05-makera-eu.txt |
| 6 | fetch | efeca.com | UK policy consultancy, weak fit | precedent-K1.txt |
| 7 | fetch | ingdilligenz.de/cbam-beratung | 20+ consultants, CBAM representative | precedent-K2.txt |
| 8 | fetch | strongandherd.co.uk | 31-year UK SME export-controls firm | precedent-K3.txt |
| 9 | fetch | igo3d.com | German importer-distributor with repair shop | precedent-A1-crowdfunding-hub.txt |
| 10 | fetch | emissieautoriteit.nl/onderwerpen/cbam | 50 t threshold verified | verify-cbam-omnibus.txt |
| 11 | search | Art 12g / 12gb dates | 20 Mar 2024 / 26 Dec 2024 verified | verify-sanctions-12g-12gb.txt |
| 12 | search | ILT used-equipment export | ILT page located; MILON incumbent | verify-ilt-used-eee.txt, precedent-K4.txt |
| 13 | search | Gutachten Gebrauchtmaschinen Export | Mevas, Hiddessen, TÜV | precedent-K4.txt |
| 14 | search | EUDR obsługa importerów (PL) | RECO Gliwice found | precedent-K1.txt |
| 15 | search | Ingdilligenz trace | Creditreform/Cylex; founded 2021 | precedent-K2.txt |
| 16 | fetch | Companies House search | OC318609, inc. 22 Mar 2006 | precedent-K3.txt |
| 17 | search | iGo3D trace | Implisense; 2013; 40–50 staff | precedent-A1-crowdfunding-hub.txt |
| 18 | fetch | NEa cbam-aangifte | 404 | nea-cbam-aangifte-fail.txt |
| 19 | fetch | ILT export gebruikte EEA | per-device test + label + declaration | verify-ilt-used-eee.txt |
| 20 | fetch | baumaschinen-gutachten.de | Mevas, since 2006 | precedent-K4.txt |
| 21 | search | Mevas volumes and price | 700+/yr, from €720, 22+ countries | precedent-K4.txt |
| 22 | fetch | reco.com.pl/rozporzadzenie-eudr | Polish EUDR desk for importers | precedent-K1.txt |
| 23 | search | RECO trace | KRS 0000371220, 3m PLN capital | precedent-K1.txt |
| 24 | search | CBAM omnibus dates | 31 Mar 2026 / 1 Feb 2027 / 30 Sep 2027 | verify-cbam-omnibus.txt |
| 25 | search | Mevas independent trace | Bauforum24 thread only (weak) | precedent-K4.txt |

Budget exhausted at 25. Nothing below rests on an unfetched page unless marked estimate.

## What the verification pass settled

| item | ideas.md status | now | source |
|---|---|---|---|
| CBAM de minimis 50 t/yr | unverified | **verified** (NEa: ">50 ton (gewicht) CBAM-goederen" per calendar year; none for electricity, hydrogen) | verify-cbam-omnibus.txt |
| CBAM authorised-declarant application deadline | unverified | **verified**: before 31 March 2026, imports may continue pending decision (EY, ReedSmith, ICAP concur) | same |
| First certificate sale / first surrender | unverified | **verified**: sales from 1 Feb 2027; surrender by 30 Sep 2027 for 2026 | same |
| CBAM downstream extension | unverified | **verified as a dated proposal**: COM(2025) 783, 16 Dec 2025; content not read | search-02-cbam-de.txt |
| Indirect customs representative as declarant in NL | unverified | still unverified (NEa sub-page 404); German precedent sells a "CBAM-Vertreter" role, which suggests representation is lawful somewhere | precedent-K2.txt |
| Ukraine CBAM derogation | unverified | not found; unverified | — |
| Art 12g no-Russia clause from 20 Mar 2024 | unverified | **verified** (Commission FAQ + five law-firm notes) | verify-sanctions-12g-12gb.txt |
| Art 12gb due diligence from 26 Dec 2024 | unverified | **verified** (same) | same |
| Used EEE export: per-device test, label, exporter declaration | from memory | **verified** (ILT) | verify-ilt-used-eee.txt |
| Used non-electrical machinery under 2024/1157 | unverified | still unverified | — |
| New-CPR authorised-representative clause (R5, already cut) | unverified | not attempted; R5 stays cut | — |
| EUDR dates | verified in run | unchanged | eudr-commission.txt |
| EUDR simplified due diligence for low-risk origin, 1% checks | — | seen in a search snippet for the UK; Ukraine's benchmark status still open | search-01-eudr-services.txt |

## Re-screen of the four kept ideas

### K1. The deforestation file for Ukrainian wood entering the Netherlands — KEEP

1. **Iron plus paper.** A truckload of Ukrainian pallets, pellets, sawn timber or furniture needs a due-diligence statement in the EU Information System, backed by plot geolocation and legality papers. Scope **verified** (Commission page: wood, furniture in scope; Information System live since 4 Dec 2024).
2. **Dated rule.** 30 December 2026 for large and medium operators and for micro/small already under the EUTR; 30 June 2027 for other micro/small. **Verified.** What the December 2025 amendment did to small operators and to downstream traders: still a research question.
3. **Buyers.** Dutch pallet makers, pellet and timber importers, furniture importers of 10–100 staff buying from Ukrainian sawmills. Incumbents seen this pass: Customs Support Group (large Dutch-headquartered broker) and SaaS (TraceX, Coolset, osapiens-class). Verified as present; their SME price still an estimate.
4. **Edge.** Reads the regulation and Ukraine's timber-accounting system; gets polygons from a state forest enterprise by phone; turns the evidence trail into a protocol. No exam. Unchanged.
5. **Price.** Per supplier onboarding and per statement. Test: one importer, one sawmill, three shipments, about €3,000. Step two: a Dutch partner who owns the importers. Step three: importer of record. Unchanged; all estimates.
6. **AI.** Satellite screening raises the number of challenged statements; polygons and permits still come from a forestry office in Zhytomyr. Unchanged.
7. **Kill fact.** Ukraine's state forestry company already issues EUDR-ready geolocation packs with every export contract, free. Not tested this pass (budget went to precedents); open.
8. **Precedent.** **RECO, Gliwice, Poland** (KRS 0000371220, share capital 3m PLN, president Jan Kaźmierczak, per Rejestr.io): a small environmental-compliance consultancy that sells EUDR implementation to importers and traders of wood and the other six commodities: supply-chain mapping, supplier risk assessment by country, "wzory oświadczeń o należytej staranności", supplier-verification procedures, training, contingency procedures, on the same desk as BDO/KOBiZE, CBAM, PPWR and waste paperwork. Price, headcount and founding year not published. Independent trace: the KRS listing. Secondary and weaker: Efeca (Bournemouth, UK), a timber-and-commodities policy consultancy with an EUDR white paper. Nobody found sells the statement itself per shipment as a named small firm; the layer below RECO is SaaS.

| figure | value | status |
|---|---|---|
| unit price | €150–400 per statement; €1,500–3,000 per supplier onboarding | estimate, unverified (RECO publishes no prices) |
| entry cost | under €3,000 | estimate |
| capital tied up | under €10,000 | estimate |

Decided by: part 8 satisfied (RECO), part 2 verified. Kept.

### K2. The carbon file for non-EU steel, aluminium and fertiliser imported by Dutch SMEs — KEEP

1. **Iron plus paper.** A lot of Ukrainian, Turkish, Kazakh or Georgian steel, aluminium or fertiliser above 50 t a year cannot be imported without authorised-declarant status, and the 2026 year needs a declaration of embedded emissions per installation, surrendered against certificates. Regime, sectors and threshold **verified**.
2. **Dated rule.** Definitive regime 1 Jan 2026 (**verified**); authorisation applications before 31 March 2026 with imports continuing pending decision (**verified**, professional summaries); certificate sales from 1 Feb 2027 and surrender by 30 Sep 2027 for 2026 goods (**verified**, same); downstream extension proposed 16 Dec 2025, COM(2025) 783 (**verified** as a date; content unread). The 31 March 2026 date has passed: importers who did not apply are today either under 50 t or importing unlawfully, which makes the first sale an emergency, not a plan.
3. **Buyers.** Steel fabricators, trailer builders, façade firms and fertiliser blenders of 10–100 staff. 50 t of steel is two truckloads, so the threshold does not remove them; it removes occasional importers. GTAI snippet: Ukraine and Turkey are the largest exporters of CBAM goods to the EU, about 69% iron and steel (**verified** as a snippet). An IHK Stuttgart survey line, "3 percent get the emissions data they need", is the demand in one figure (snippet, unverified at source).
4. **Edge.** Getting actual emissions out of a mill in Zaporizhzhia, Iskenderun or Temirtau whose energy engineer speaks Russian or Ukrainian; automating the calculation and the evidence trail; NEa works in English. Unchanged.
5. **Price.** Per installation data pack and per annual declaration. Test: one fabricator, one supplier, one quarter, about €4,000. Step two: a Dutch customs broker. Step three: authorised declarant. Whether a third party may be the declarant in NL: still unverified.
6. **AI.** Calculation automates; the person who extracts a verified dataset from a non-EU mill does not, and the scope widens (downstream proposal). Unchanged.
7. **Kill fact.** Restated: the 50 t threshold is verified and does not kill it; the new kill fact is that customs brokers bundle declarant status and default-value declarations into the clearance fee, so the data pack is bought only by importers who want to beat default values. Untested.
8. **Precedent.** **Ingdilligenz GmbH, Würzburg** (founded 2021 per Creditreform/LinkedIn snippets; "20+ consultants", "100+ customer projects"): sells CBAM compliance assessment, supplier questionnaires and data templates, emissions data collection and analysis, quarterly and annual report preparation, and the "CBAM-Vertreter" role, to mid-sized importers in steel and metal processing, heating and building technology. Own site plus Creditreform, Cylex and LinkedIn listings. Prices not published. Closest fit of the pass: same file, same buyer size, one language short.

| figure | value | status |
|---|---|---|
| unit price | €1,500–3,000 per installation data pack; €2,000–5,000 per annual declaration | estimate, unverified |
| entry cost | under €2,000 | estimate |
| capital tied up | under €10,000; none if the reader never holds certificates | estimate |

Decided by: part 8 satisfied (Ingdilligenz), part 2 now fully dated. Kept.

### K3. The sanctions and dual-use file for Dutch machinery going to Central Asia and the Caucasus — WATCH

1. **Iron plus paper.** A used CNC machine, pump, tractor or parts order to Kazakhstan, Uzbekistan, Georgia, Armenia, Turkey or the UAE needs a dual-use classification, CHP screening, a no-re-export-to-Russia clause, an end-user file and often a CDIU licence. Unchanged.
2. **Dated rule.** Article 12g from 20 March 2024 and Article 12gb from 26 December 2024 (**verified**); 21st package 23 July 2026 (verified in run). The clock runs, but the last dated change is behind us; the rule is tightening by package, not by a deadline the buyer can see.
3. **Buyers.** Dutch pump, machinery and agri-tech firms of 10–100 staff with Central Asian customers. Incumbents: law firms; the CDIU. Unchanged, unverified.
4. **Edge.** Verifies the Kazakh or Uzbek buyer in Russian. Real, and the pass did not touch the reputational question (a Belarusian-born adviser signing sanctions files), which is the part-4 risk.
5. **Price.** Per order file; per end-user verification. Test about €3,000. Unchanged, estimates.
6. **AI.** Screening is a commodity; end-use judgment is signed by a person. Unchanged.
7. **Kill fact.** Forwarders sell the clause and the screening for tens of euros a shipment. Untested.
8. **Precedent.** Partial. **Strong & Herd LLP, Manchester** (OC318609, incorporated 22 March 2006; predecessor company 04492078 from 2002; founder retiring after 31 years): export-controls training, audits, a help-line membership and shipping-office services for SMEs. It proves a small firm can live for two decades on SME export-control compliance. It does not sell the K3 product: per-order end-user verification in Russian for Central Asian buyers. Two searches for that product returned law firms and two US boutiques (Riddle Compliance, CVG Strategy, not fetched). No named small firm earns its living on the specific shape.

| figure | value | status |
|---|---|---|
| unit price | €300–800 per order file; €1,500–3,000 per end-user verification | estimate, unverified |
| entry cost | under €3,000 | estimate |
| capital tied up | under €5,000 | estimate |

Decided by: part 8 only partly met after a fair search, and part 2 has no forward deadline. Downgraded to WATCH. Re-test if a research run finds a German or Polish firm selling end-user verification per order, or if the anti-circumvention tool names a Central Asian country.

### K4. The "not waste" file for used equipment sent from the Netherlands to Ukraine and Moldova — KEEP, reframed

1. **Iron plus paper.** For used electrical equipment the rule is now **verified** at ILT: "Elk apparaat moet getest zijn voordat het mag worden geëxporteerd. En er moet een bewijs van de test aanwezig zijn"; a label per device with identification number, production year, tester, test type, date and result; the exporter "moet verklaren dat de zending geen afval bevat"; missing label or packaging means it "kan als afval worden behandeld"; exporters of used EEE must register and report since 1 January 2021. For non-electrical machinery the used-goods test under Regulation 2024/1157 is still unverified.
2. **Dated rule.** 21 May 2026 (most provisions) and 21 May 2027 (green-listed exports to non-OECD countries only if the country is listed). **Verified** in the run.
3. **Buyers.** Dutch used-agri, construction and medical equipment dealers and refurbishers of 10–100 staff. Incumbent seen this pass: MILON, a Dutch EVOA and end-of-waste consultancy (part 3 confirmed as "consultants at big-firm prices" only by its existence; prices unknown).
4. **Edge.** Reads the Regulation and the ILT rules; designs and runs the function-test protocol; reads the consignee's papers in Ukrainian. Unchanged.
5. **Price.** Per lot, and now with a benchmark: Mevas charges "from €720" per machine for an on-site inspection with function tests. Test: two lots for one dealer, about €2,500. Unchanged otherwise.
6. **AI.** Nobody runs a load test on a 2012 tractor by model. Unchanged.
7. **Kill fact.** Customs and ILT do not stop used-machinery shipments to Ukraine in practice. Untested; the ILT page shows the rule is written and policed for EEE, not that it is policed for tractors.
8. **Precedent.** Partial but instructive. **Mevas (Wolfgang Bühn), Germany**, since 2006: on-site condition reports with function tests on used construction machinery and cranes, "over 700 machines per year", "more than 22 countries starting at prices from €720", for "Käufer, Verkäufer, Versicherungen, Vermieter, Bauunternehmen und Behörden", multilingual team. Own site plus a Bauforum24 trade-forum introduction (weak trace). Same iron, same test, different payer (the buyer, "to ensure they don't purchase scrap") and different file (condition report, not a not-waste declaration). No named firm selling the not-waste file itself was found in three searches.

| figure | value | status |
|---|---|---|
| unit price | €400–1,200 per lot | estimate; Mevas's €720 per machine is a verified neighbour |
| entry cost | under €2,000 | estimate |
| capital tied up | under €5,000 | estimate |

Decided by: part 8 met for the unit economics (Mevas) and part 1 now verified for EEE. Kept, reframed as "the Mevas report, sold to the exporter, with the ILT declaration bundled": the buyer in Lviv and the exporter in Barneveld both want the same signed function test, and the reader is the only one who can talk to both.

## Verdicts

| idea | verdict | decided by | precedent |
|---|---|---|---|
| K1 EUDR wood file | KEEP | part 8 met; part 2 verified | RECO, Gliwice (PL); Efeca (UK) secondary |
| K2 CBAM data pack and declaration | KEEP | part 8 met; part 2 dates verified | Ingdilligenz GmbH, Würzburg (DE) |
| K3 sanctions / dual-use order file | WATCH | part 8 partial; no forward deadline | Strong & Herd LLP, Manchester (UK), partial |
| K4 not-waste file for used equipment | KEEP (reframed) | part 8 partial but priced; part 1 verified for EEE | Mevas (DE), partial |
| A1 crowdfunding machinery hub (test) | WATCH | part 7 half-true; book line | iGo3D GmbH, Hannover (DE) |
| A2 second addition | none | budget; nothing precedent-led surfaced | — |

## Additions

### A1. EU importer, CE and service hub for machinery-class crowdfunding products, with used greenhouse equipment to CEE as the second line — tested as if in the run — WATCH

Note first: triage 1 (#7) and triage 2 (#8) parked "EU importer of record for crowdfunding-proven makers" as IT-adjacent. The brief asked for the machinery-class cut of it to be tested on all eight parts anyway; this is that test, not a re-proposal.

1. **Iron plus paper.** A desktop CNC mill, laser cutter, 3D printer or robot mower from a Hong Kong or US maker cannot be placed on the EU market without CE marking (machinery, LVD/EMC, RED where wireless, laser safety), a technical file, an EU-established responsible operator named on the product, and WEEE, battery and packaging registrations. The connected ones also fall under the CRA. Rule set from `drafts/reviews/crowdfunding-findings.md` and `-agy.md` (their triage, not re-fetched).
2. **Dated rule.** Machinery Regulation 2023/1230 applies from 20 January 2027 (date as cited in crowdfunding-findings.md; not re-fetched this pass); CRA reporting duties from September 2026 and full application December 2027; PPWR from August 2026. All from the earlier runs, marked estimate here.
3. **Buyers.** Two kinds, and this is the weak part: the makers (HK/US firms of roughly 10–100 staff that raised $3–13m and have no EU route: NestWorks C500, XLASERLAB X1, FibreSeeker 3, AEKE S1 Pro, Pongbot Aura, per the agy audit) pay for the file and the channel; EU B2B users (schools, makerspaces, small workshops) pay for a VAT invoice, a warranty and a repair bench. The makers work in English; the EU users in Dutch, German, Polish.
4. **Edge.** Regulatory literacy (the machinery and CRA books), engineering habit (service, spares, the technical file), a Polish network for the repair bench and for CEE resale. No Dutch exam. The reader is not an electronics retailer, which is the honest gap.
5. **Price.** Per product CE and technical-file audit (€3,000–8,000, estimate) plus per-unit importer margin (15–25%, estimate). Test under €5,000: one maker, one file audit, five demo units on consignment. Capital under €50,000 only on consignment; buying stock of €3–6k machines breaks it. Step two: a Dutch partner with a webshop and a workshop. Step three: exclusive EU distributor and service centre, the iGo3D shape.
6. **AI.** Cheaper design tools mean more crowdfunded machines every year; each one needs a physical file and a repair bench; a model does not change a spindle. Mechanism, not slogan.
7. **Kill fact.** Half true already. The largest raisers sell direct into the EU from own-brand EU stores: Makera runs eu.makera.com with Carvera Air and Z1 pages (**verified** this pass); Snapmaker, xTool (Makeblock Europe B.V.), Lymow, Longer and ELEGOO have EU shops or entities (agy audit, not re-fetched). The gap is only the mid-tier, and a maker that raised $13m can open a Shopify EU store in a week. Second kill fact untested: the connected ones are CRA products, which is the book-line objection that parked #8.
8. **Precedent.** **iGo3D GmbH, Hannover**, founded 2013, "40 employees" (another listing: about 50), "own logistics center, a certified repair workshop", a reseller network, distributing Formlabs, Desktop Metal, Bambu Lab, Prusa, Creality, Anycubic, Flashforge and Elegoo; explicitly took the distributor role because "the market lacked a distributor capable of supplying resellers". Own site plus Implisense, 3Druck dealer directory and lieferanten.de listings. The strongest precedent of the pass: a small German firm that lives on importing, servicing and reselling non-EU desktop machines. Its existence also says the Netherlands does not need a second iGo3D; it needs a service bench for the products iGo3D does not carry.

**Second line, used greenhouse equipment to CEE.** Dismantled Dutch glasshouse kit (screens, boilers, irrigation, lighting) sold to Polish and Ukrainian growers travels on the same not-waste paperwork as K4 (functionality record per lot, used-goods declaration) and, for the electrical part, on the ILT per-device test verified above. No precedent fetched (budget); the trade is dominated by Dutch dismantlers, so the reader's line would be the paperwork and the CEE buyer, not the crane. Estimate, unverified.

| figure | value | status |
|---|---|---|
| unit price | €3,000–8,000 per product file; 15–25% per unit | estimate, unverified |
| entry cost | under €5,000 on consignment | estimate |
| capital tied up | €20,000–50,000 if stock is bought | estimate |

Decided by: part 7 half-confirmed (Makera's EU store, verified) and the book line on connected products. WATCH: a research run should list the machinery-class raisers of the last 24 months without an EU entity, and settle whether a WiFi-enabled CNC is a CRA product for this book's purposes.

### A2. Second precedent-led addition

None. The budget went to precedents and verification for the four kept ideas plus A1. The one lead that surfaced without being chased is the Mevas shape sold to CEE buyers of Dutch used machinery (inspection for the buyer in Poland or Ukraine, in their language), which is K4 with the payer switched; it is noted inside K4 rather than added.

## Facts a research run must still settle (delta to ideas.md)

- K1: unchanged list; add "does RECO or any Polish firm file statements per shipment for a fee, and at what price?" (call RECO, +48 662 018 291).
- K2: items 1, 2 settled; item 3 (third-party declarant in NL) still open, NEa page 404; add "how many Dutch importers applied before 31 March 2026 and how many CBAM-goods importers over 50 t did not?" (NEa, Douane).
- K3: items 1 and 7 partly settled (12g, 12gb dates); add "name one German or Polish small firm selling end-user verification per order" as the gate to leave WATCH.
- K4: item 1 settled for EEE, open for non-electrical machinery; add "what does MILON charge a dealer for a used-goods opinion?" and "what does Mevas charge for a Dutch inspection with a Ukrainian-language report?".
- A1: "list machinery-class campaigns over $3m, 2024–2026, with no EU entity on the check date" and "is a WiFi CNC a CRA product for the book line?".

## What the precedent test changed (≤120 words)

It sorted the four by how real the trade already is. K2 and K1 have named small firms living on the same file for the same buyers (Ingdilligenz, RECO), so they stand. K4 has a firm proving the per-unit inspection pays at €720 a machine, which is better evidence than the run had, even though the payer differs. K3 found only a general SME export-control shop and law firms; the specific product has no visible precedent, so it goes to WATCH. The verification pass moved five figures from memory to verified without changing any verdict, and made the CBAM idea more urgent: the 31 March 2026 deadline has passed. The crowdfunding hub found the best precedent (iGo3D) and the worst kill fact (Makera already sells into the EU).
