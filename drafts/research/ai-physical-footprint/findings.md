# Research Findings: The Physical Footprint of AI in the Netherlands (2026–2030)

**Research date:** 2026-09-04
**Folder:** `drafts/research/ai-physical-footprint`
**Question:** which physical, on-site or licensed work does the AI/data-centre build-out buy in the Netherlands, and which of it could a two-to-ten-person operator sell outside IT?
**Screen:** `drafts/edge-inventory.md` (A2 Dutch, English/Russian/Polish, ~EUR 100k, regulatory literacy, engineering habit, 30k LinkedIn audience); A2 gate and AI gate. Does not re-propose the seven candidates kept in `drafts/notes/2026-09-03-fable-triage.md`; section 4 notes where this instrument strengthens or weakens them.
**Status:** COMPLETE (37 web fetches; 29 saved excerpts).

---

## 1. Sources and their limits

Every figure below traces to a plain-text excerpt in `sources/` (fetch date 2026-09-04). Where a widely quoted number could not be verified on a fetched page, the excerpt says so and the number is not used.

| id | publisher | what it gives |
|---|---|---|
| stb-2023-492-hyperscale-instructieregel | Staatsblad 2023, 492 | Legal definition of a hyperscale datacenter (>10 ha, ≥70 MW); only Het Hogeland and Hollands Kroon allowed; in force 1 Jan 2024 |
| kamerstuk-26643-939-hyperscale-amvb | Tweede Kamer, 8 Nov 2022 | Minister's letter announcing the AMvB locations |
| omgevingsweb-kamervragen-datacenters-2021 | EZK answers, 17 Dec 2021 | 2019 baseline: 2.7 TWh, three hyperscalers, 239 ha, 20–25 projects |
| dda-regeldruk-feb-2025 | Dutch Data Center Association, 12 Feb 2025 | 3.7 TWh = 3.3% of NL electricity; 1 million m3 water; 50 MWth NSA = IPPC; 50 MW cooling discharge permit; competence split Rijk/province/municipality; Amsterdam 2019 moratorium; NIS2 physical-security duties |
| dda-economische-impact | DDA | 6,070 FTE (2025) → 7,710 FTE (2030); supporting functions named |
| dda-state-2026-landing | DDA | Themes only; figures behind registration form |
| datacenterworks-arbeidsmarkt-2019 | trade press / Pb7 | 4,700 staff (2019); no datacenter training route exists |
| hollandskroon-datacenters | Gemeente Hollands Kroon | 500+ permanent jobs; 200–300 temporary construction jobs on average; PWN water; no waste-heat use yet |
| hollandskroon-beleidsregels-huisvesting-2026 | Gemeente Hollands Kroon, in force 17 Apr 2026 | Migrant-housing rules: max 80 per agricultural site, register obligation, SNF, temporary permits |
| emerce-microsoft-middenmeer-2025 | Emerce, 10 Sep 2025 | Microsoft expansion announced, AI as the reason; land bought Sep 2025 |
| rtvnoord-qts-eemshaven | RTV Noord, 13 Jul 2025 | QTS EUR 1.4 bn to 2029; 130 jobs; heat to >10,000 households with WarmteStad in 2026 |
| google-eemshaven-location | Google | EUR 600 m Eemshaven (2014); 28 km water pipeline, EUR 45 m water works; Winschoten and Groningen EUR 600 m+ each (2024) |
| nos-zeewolde-raad-van-state-2023 | NOS, 20 Sep 2023 | Zeewolde zoning plan annulled; Meta withdrew June 2022 |
| haarlemmermeer-datacenterbeleid-2020 | Gemeente Haarlemmermeer, 24 Nov 2020 | 750 MVA cap to 2030, none after; four parks; PUE <1.2; heat delivery if a network exists; rainwater or industrial water for cooling |
| amsterdam-vestigingsbeleid-datacenters-2020 | Gemeente Amsterdam | Policy dates only |
| odnzkg-ams10-schiphol-rijk | ODNZKG, 11 Dec 2025 | EdgeConneX AMS10: three permits, decision early 2026 |
| nos-tennet-goodman-kortgeding | NOS, 29 Apr 2026 | Court: TenneT need not connect Goodman; Vijfhuizen grid reinforced only 2033–2035; Eindhoven/Utrecht all requests wait from 1 July |
| netbeheer-nederland-feiten-en-cijfers | Netbeheer Nederland | End 2025: 15,014 companies waiting for consumption (9,305 MW), 8,687 for injection (5,027 MW); 2025: 2,424 km MV + 2,015 km LV cable, 2,183 transformer stations, 1,298 neighbourhoods; deficit to 2029: 28,000 technicians incl. 23,000 at contractors |
| lan-netcongestie-voortgang-april-2026 | LAN progress report via Duurzaam Ondernemen, 13 Apr 2026 | Waiting list +26% y/y; storage contracts 94 → 237; 281 MW contracted storage; capacity-restriction contracts 18 → 243; block contracts 41 → 142; 56 HV projects delivered |
| cob-30000-vacatures-2030 | COB, 29 Apr 2026 | Netbeheer NL: 30,000 extra jobs for the grid to 2030; Bouwend NL: 312 HBO civil graduates in 2024 |
| tennet-eu401-erkenningsregeling | TenderView mirror of TenneT notice | Qualification system for ≥110 kV line works via Mercell; typical certificates VCA/ISO/CO2-ladder |
| uwv-kansrijke-beroepen-2026-2027 | UWV | Kansrijk: monteurs laag-/midden-/hoogspanning, kabelwerkers datacommunicatie, glasvezelmonteurs, koeltechniek, beveiligingsinstallaties, inspecteurs elektrische installaties, objectbeveiligers, oppermannen GWW |
| rvo-rapportageplicht-datacentra-eed | RVO | EED art. 12: every datacenter ≥500 kW IT reports PUE, water, waste-heat factor annually; 2026 window 16 Mar–15 May |
| drinkwaterplatform-datacenters-2026 | Drinkwaterplatform, 26 Feb 2026 | ≤1 million m3 drinking water/yr (0.088%); rainwater at Agriport, industrial water at Eemshaven |
| powertec-scios-scope4-nsa | inspection-company blog | SCIOS Scope 4/7c mandatory for emergency generators since 1 Jan 2016; 4-yr (20–100 kW) / 2-yr (>100 kW); <500 h/yr = emergency status |
| justis-wpbr-vergunning | Justis | Wpbr licence EUR 600 + EUR 92 per manager; 5 years; staff need mbo Beveiliger diploma; no language or diploma requirement stated for the licence holder |
| svpb-beveiliger-n2-engels | SVPB | Beveiliger N2 exam is Dutch-language; contains an A2 professional-English component |
| veiligheidsbranche-krapte-2020 | Nederlandse Veiligheidsbranche, 30 Jan 2020 | 64,000 security workers; over half of firms report shortage |
| ilt-aeea-weeelabex-cenelec | ILT | AEEA processors need WEEELABEX/CENELEC 50625 conformity; repair/refurb incl. hard-drive replacement is outside certification; Type 0 handling exempt |

**Limits.** (1) The DDA *State of the Dutch Data Centers 2026* report is behind a registration form; its MW figures were not obtained, and vendor market-report numbers (1.14 GW etc.) are excluded. (2) TenneT's own investment-plan pages are Cloudflare-blocked; the "1,000 projects / 40 new stations" claims in search summaries are therefore NOT used. (3) Indeed's vacancy pages returned 403; no operator or contractor job posting could be saved, so job-board evidence rests on the UWV list and the Hollands Kroon jobs statement. (4) The security-shortage figures are from 2020. (5) The SCIOS 1 Jan 2026 frequency change and the Microsoft "six buildings / 50 ha / H2 2026 application" details were seen only in search summaries and are not used as figures. (6) No TenderNed datacenter-specific tender was fetched; TenneT's contractor qualification system is the only procurement document.

---

## 2. Evidence tables

### 2a. Where the build-out is, and who decides

| site / cluster | status and dates | competent authority | buyers |
|---|---|---|---|
| Hollands Kroon (Agriport A7, Middenmeer) | Microsoft and Google both "bezig met de realisatie van een nieuw datacenter"; Microsoft announced a further expansion 10 Sep 2025, citing AI; 500+ permanent jobs, 200–300 construction jobs on average | Rijk instruction rule (Stb. 2023, 492): one of only two hyperscale areas; municipality for permits and housing | Microsoft, Google, their general contractors |
| Het Hogeland (Eemshaven) | Google EUR 600 m (2014), 28 km water pipeline; QTS EUR 1.4 bn to 2029, 130 jobs, heat to >10,000 households in 2026; Google Winschoten and Groningen EUR 600 m+ each (2024) | Rijk instruction rule; province; Groningen Seaports | Google, QTS, WarmteStad, North Water |
| Haarlemmermeer / Schiphol-Rijk | 750 MVA growth cap to 2030, nothing after; four permitted parks; EdgeConneX AMS10 permits decided early 2026; Vijfhuizen grid only reinforced 2033–2035 | Municipality (<50 MW), province (≥50 MW) | Colocation operators (EdgeConneX and others) |
| Amsterdam | Moratorium 2019; siting policy 2020–2030 | Municipality | Colocation operators |
| Zeewolde | Meta withdrew June 2022; zoning plan annulled 20 Sep 2023 | — | none |

### 2b. Physical work the build-out buys

| work stream | legal driver / demand evidence (dated) | licence or certificate; exam language | incumbents | entry for a 2–10 person firm |
|---|---|---|---|---|
| Grid extension: cable, trenching, substations | End 2025: 15,014 companies waiting (9,305 MW); 2025 output 2,424 km MV + 2,015 km LV cable, 2,183 transformer stations, 1,298 neighbourhoods; deficit to 2029: 28,000 technicians, 23,000 of them at contractors; 30,000 extra grid jobs to 2030 (Netbeheer NL, Apr 2026) | TenneT ≥110 kV via qualification system EU-401 (Mercell); VCA/ISO/CO2-ladder typical; grid-operator safety designations (BEI/VIAG) NOT verified for language | BAM Infra, ENGIE, KWS, VolkerRail (per mirror) | Only as subcontracted civil crew to a qualified main contractor |
| Battery storage and flexible connections | Storage contracts 94 (2024) → 237 (2025); 281 MW contracted; capacity-restriction contracts 18 → 243; block contracts 41 → 142 | Installation NEN 1010/3140; fire-safety and permit rules not fetched | Green Energy Storage-type developers; installers | Behind-the-meter packages for waiting-list SMEs |
| Datacenter construction and fit-out | Hollands Kroon: 200–300 construction jobs on average; QTS: "honderden of zelfs duizenden" during build | VCA; trade certificates | General contractors of hyperscalers (not named in sources) | Subcontract trades; crew housing (see 2c) |
| Cooling, water, waste heat | EED art. 12 reporting for every DC ≥500 kW (PUE, water, waste-heat factor), window 16 Mar–15 May 2026; Haarlemmermeer requires heat delivery if a network exists and PUE <1.2; Agriport still no heat re-use; ≤1 million m3 drinking water/yr | F-gas (STEK, English exam per regulation run); UWV: koeltechniek kansrijk | ECW Energy (Agriport water), North Water (Eemshaven), WarmteStad | Sub-contract cooling maintenance; too capital-heavy for heat networks |
| Backup power (NSA) | SCIOS Scope 4/7c mandatory since 1 Jan 2016; 2-yr cycle >100 kW; NSA >50 MWth makes the DC an IPPC installation | SCIOS company certificate; Dutch-only exam (regulation run) | Bredenoord, Powertec, Normec van Empel | Acquire a certified inspection microfirm only |
| Fibre and civil works | UWV kansrijk: kabelwerkers datacommunicatie, monteurs glasvezel; oppermannen GWW as entry | none for labour; NEN 3140 for electrical | telecom contractors | Civil crew subcontracting |
| Physical security | DDA: NIS2 requires "Investeringen in beveiliging"; UWV kansrijk: objectbeveiligers, monteurs beveiligingsinstallaties; 64,000 workers, over half of firms short (2020) | Wpbr licence EUR 600, 5 yrs, no diploma for the licence holder; guards need mbo Beveiliger diploma (Dutch exam, A2 English component) | Large guarding firms (not named in sources) | Own Wpbr firm as overflow supplier |
| Commissioning and inspection | UWV kansrijk: inspecteurs elektrische installaties | SCIOS Scope 8/10/12, NEN 3140: Dutch-only (regulation run) | Arepa, DEKRA, Kiwa (regulation run) | cut in triage (L4) — not re-proposed |
| Decommissioning and e-waste | AEEA processors need WEEELABEX/CENELEC 50625 conformity; repair/refurb incl. hard-drive replacement outside certification; Type 0 handling exempt | WEEELABEX (company, per site); VIHB for transport (no exam, per regulation run) | certified ITAD/recyclers | Collection, refurbishment and CEE resale, destruction subcontracted |
| Crew housing and site logistics | Hollands Kroon rules in force 17 Apr 2026: max 80 per agricultural site, register obligation, SNF standards, temporary permits 15–20 yrs | SNF; municipal permit | housing operators around Eemshaven and Agriport (unnamed) | strengthens triage rank 1, not a new candidate |

### 2c. Gate summary

| work stream | A2 gate | AI gate to 2030 |
|---|---|---|
| Grid civil crews | PASS via partner (main contractor owns the Dutch customer; site language mixed) | RAISES (every AI load is a grid connection) |
| Battery/flex packages | PASS (B2B, English/Polish suppliers; grid operator forms in Dutch) | RAISES (congestion is the AI bottleneck) |
| Wpbr security firm | CONDITIONAL (licence has no exam; guards need Dutch diploma) | NEUTRAL (camera analytics cut patrols; access control stays human) |
| ITAD / refurb channel | PASS | RAISES (faster hardware refresh) — volumes unverified |
| SCIOS NSA inspection | FAIL personally; PASS by acquisition | RAISES (more generators, mandatory cycles) |

---

## 3. Ranked candidates

### Rank 1: Grid civil-works crew for the netbeheerders' contractors
- **Opportunity:** a 5–10 person trenching, cabling and transformer-station civil crew, employed by the reader's BV, subcontracted to the main contractors that hold TenneT/Liander/Stedin frames.
- **Demand evidence:** end 2025, 15,014 companies wait for a connection (9,305 MW); 2025 output was 2,424 km MV and 2,015 km LV cable and 2,183 transformer stations; the deficit to 2029 is 28,000 technicians, 23,000 of them at contractors; Netbeheer NL counts 30,000 extra grid jobs to 2030.
- **Edge:** Polish/Ukrainian recruiting; engineering habit for VCA, hours and evidence trails; regulatory literacy for the Wtta/agency line between contracting and labour supply.
- **Gates:** A2 PASS through the main contractor; AI RAISES.
- **First paid test:** one crew, one month, on a Liander neighbourhood job for a qualified contractor, priced per metre.
- **Kill fact:** grid-operator safety designations (BEI/VIAG) are examined in Dutch only and required for every crew member.

### Rank 2: Behind-the-meter battery and flexible-contract packages for waiting-list SMEs
- **Opportunity:** sell foreign-owned or CEE-run SMEs on the waiting list a package: capacity-restriction or block contract with the grid operator, plus a containerised battery sourced from a Polish/CEE maker, with the permit and safety dossier.
- **Demand evidence:** storage contracts rose from 94 (2024) to 237 (2025), contracted storage to 281 MW; capacity-restriction contracts from 18 to 243; block contracts from 41 to 142; the waiting list grew 26% in a year.
- **Edge:** regulatory literacy (ACM framework, Bal, grid codes), CEE supplier access, engineering habit for load profiles.
- **Gates:** A2 PASS (B2B; grid-operator paperwork in Dutch is a partner task); AI RAISES.
- **First paid test:** one paid load-profile and flex-contract study (EUR 2,500) for a Polish-owned logistics firm, then broker its battery.
- **Kill fact:** grid operators or the ACM framework give queued SMEs the same flex products directly, free.

### Rank 3: Wpbr-licensed object-security firm for critical sites
- **Opportunity:** a small licensed guarding firm supplying diploma-holding guards from the diaspora to datacenter, substation and construction sites as overflow for the incumbents.
- **Demand evidence:** UWV 2026–27 lists objectbeveiligers and monteurs beveiligingsinstallaties as kansrijk; DDA names security among the supporting functions and NIS2 investment in security; Hollands Kroon sites carry 500+ permanent jobs; 64,000 security workers, over half of firms short (2020).
- **Edge:** recruiting inside Polish/Ukrainian communities; the licence itself has no exam and costs EUR 600.
- **Gates:** A2 CONDITIONAL (guards must pass the Dutch-language Beveiliger diploma); AI NEUTRAL.
- **First paid test:** licence, three certified guards, one overflow contract with an existing Wpbr firm at Middenmeer.
- **Kill fact:** hyperscalers accept only audited national guarding firms; no overflow subcontracting.

### Rank 4: ITAD collection and refurbished-server channel to CEE
- **Opportunity:** collect decommissioned servers from colocation refreshes, refurbish (hard-drive replacement is outside WEEELABEX scope), sell east; subcontract destruction and depollution to a certified processor.
- **Demand evidence:** every datacenter ≥500 kW now reports under EED art. 12; 6,070 FTE sector (2025); AEEA rules put certification on processors, not on collectors or refurbishers. No volume figure was found.
- **Edge:** Russian/Polish/Ukrainian resale networks; regulatory literacy for Waste Shipment Regulation and used-EEE export tests.
- **Gates:** A2 PASS; AI RAISES (unverified).
- **First paid test:** buy one pallet of decommissioned servers from a colocation operator, refurbish, sell to a Polish reseller with destruction certificates.
- **Kill fact:** hyperscalers and large colos run global ITAD contracts; nothing reaches the open market.

### Rank 5: Acquire a SCIOS Scope 4/7c generator-inspection microfirm
- **Opportunity:** buy a certified inspection company serving emergency generators, including datacenter fleets.
- **Demand evidence:** mandatory since 1 Jan 2016, 2-year cycle above 100 kW; a NSA above 50 MWth makes the datacenter an IPPC installation; UWV lists inspecteurs elektrische installaties as kansrijk.
- **Edge:** capital, process discipline; owner-independence rule from the succession run.
- **Gates:** A2 FAIL personally (Dutch-only SCIOS exam), PASS by acquisition with the certified inspector retained; AI RAISES.
- **First paid test:** broker one inspection contract through a certified firm before buying.
- **Kill fact:** the certified inspector leaves at change of control.

---

## 4. Effect on the seven kept candidates
- **Rank 1 (housing/agency compliance):** strengthened. Hollands Kroon's rules in force 17 Apr 2026 (max 80 per site, register obligation, SNF) sit next to Agriport's 200–300 construction jobs and Eemshaven's QTS build to 2029.
- **Rank 3 (heat-pump/F-gas company):** mildly strengthened: UWV lists koeltechniek installers as kansrijk and datacenter cooling is a B2B customer, but the sources give no datacenter-specific cooling contract evidence.
- **Cut L4 (NEN 3140 service):** unchanged; the build-out buys inspection but through Dutch-only certificates and established firms.

---

## 5. Honest assessment
The build-out is real and dated: two hyperscale zones fixed by Staatsblad since 1 January 2024, QTS's EUR 1.4 bn to 2029, Microsoft's 2025 expansion, and a grid programme short 28,000 technicians. But the physical work is bought through qualification systems, national guarding contracts and global ITAD frames that a two-to-ten-person firm enters only as a subcontractor or labour supplier. Nothing here needs the reader's languages more than a Dutch founder's; the only cross-border angles are crew recruiting and CEE battery or server channels, and both are unproven. This instrument found demand, not an edge. What it could not get: the DDA 2026 figures, TenneT's plan, and a single verified operator job posting.
