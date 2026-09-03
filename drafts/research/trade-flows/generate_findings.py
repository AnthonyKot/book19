import json, csv, os

folder = "/home/diablo/book19/drafts/research/trade-flows"
sources_dir = os.path.join(folder, "sources")

def load_comext(filename):
    with open(os.path.join(sources_dir, filename), "r") as f:
        data = json.load(f)
    prod_idx = data["dimension"]["product"]["category"]["index"]
    prod_label = data["dimension"]["product"]["category"]["label"]
    val = data.get("value", {})
    hs4 = {}
    for code, idx in prod_idx.items():
        if len(code) == 4 and code.isdigit():
            v = val.get(str(idx))
            if v is not None:
                hs4[code] = (v, prod_label.get(code, ""))
    return hs4

pl_2023 = load_comext("comext_PL_2023.json")
pl_2025 = load_comext("comext_PL_2025.json")
eu_2023 = load_comext("comext_EXT_EU_2023.json")
eu_2025 = load_comext("comext_EXT_EU_2025.json")

def get_compliance_flags(code, desc):
    flags = []
    c = int(code[:2])
    ce_types = []
    if c in [84, 85]:
        ce_types.append("Machinery/EMC/LVD/RED")
    elif c in [39, 73, 76] and any(w in desc.lower() for w in ["structure", "builder", "window", "door"]):
        ce_types.append("CPR (EN 14351/EN 1090)")
    elif c in [90]:
        ce_types.append("MDR/EMC")
    elif c == 94:
        ce_types.append("LVD/EMC/GPSR")
    elif c == 95:
        ce_types.append("Toy Safety")
    
    if ce_types:
        ce_s = ", ".join(ce_types)
        flags.append(f"CE ({ce_s})")
        
    if c in [39, 48] and any(w in desc.lower() for w in ["pack", "box", "case", "bottle", "conveyance", "bag"]):
        flags.append("Packaging/EPR (PPWR/Afvalfonds)")
    elif any(w in desc.lower() for w in ["cosmetic", "perfume", "food", "meat", "juice", "beverage", "chocolate", "dates", "fruit", "coffee"]):
        flags.append("Packaging/EPR (Afvalfonds)")
    elif c in [84, 85, 94]:
        flags.append("WEEE/Battery EPR")
        
    if c in [39, 48] and any(w in desc.lower() for w in ["pack", "box", "case"]):
        flags.append("Food-contact (EC 1935/2004)")
    elif c in [84, 85] and any(w in desc.lower() for w in ["domestic", "food", "grind", "beverage"]):
        flags.append("Food-contact")
        
    if code in ["8471", "8517", "8528", "8525", "8523", "9504", "8473"]:
        flags.append("CRA ((EU) 2024/2847)")
    elif code == "9405":
        flags.append("CRA (if IoT/smart control)")
    elif code in ["8508", "8509"]:
        flags.append("CRA (if smart connected)")
        
    return "; ".join(flags) if flags else "GPSR / Standard"

def rank_lines(data23, data25):
    all_codes = set(data23.keys()) | set(data25.keys())
    ranked = []
    for code in all_codes:
        v23, label23 = data23.get(code, (0, ""))
        v25, label25 = data25.get(code, (0, ""))
        label = label25 or label23
        diff = v25 - v23
        pct = (diff / v23 * 100) if v23 > 0 else None
        ranked.append((v25, v23, diff, pct, code, label))
    ranked.sort(reverse=True, key=lambda x: x[0])
    return ranked[:40]

ranked_pl = rank_lines(pl_2023, pl_2025)
ranked_eu = rank_lines(eu_2023, eu_2025)

lines = []
lines.append("# Trade-Flow Gaps: Netherlands Imports from Poland and Non-EU Partners (2023–2025)")
lines.append("\n**Cut-off & Fetch Date:** 2026-09-03  ")
lines.append("**Author / Reader Context:** Screened against `drafts/edge-inventory.md` (Languages: Polish/Russian/English/Dutch A2; Capital: ~EUR 100k; Regulatory literacy: CRA, CPR, PPWR, Machinery, MDR; Engineering habit; 30k LinkedIn audience).")
lines.append("\n---\n")

lines.append("## 1. Sources and Their Limits\n")
lines.append("This research synthesizes published trade statistics and industrial production data from four primary institutional authorities:")
lines.append("1. **Eurostat Comext (Database DS-045409: EU Trade Since 1988 by HS2-4-6 and CN8)**:")
lines.append("   - *Coverage:* Annual reporting for the Netherlands (`reporter=NL`), import flow (`flow=1`), for partner countries Poland (`PL`) and Extra-EU27 (`EXT_EU27_2020`) across 2023, 2024, and 2025 at full 4-digit Harmonized System (HS4) granularity. Values in Euros (`VALUE_IN_EUROS`).")
lines.append("   - *Limits:* Comext records physical and customs arrivals. In the Netherlands, this is significantly influenced by the 'Rotterdam effect'—goods entering through the Port of Rotterdam or Schiphol Airport cleared for EU transit or intended for re-export (quasi-transit) to Germany and the hinterland. CIF valuation includes freight and insurance.")
lines.append("2. **CBS StatLine (Centraal Bureau voor de Statistiek)**:")
lines.append("   - *Coverage:* Table `85429NED` (Internationale goederenhandel; grensoverschrijding, kerncijfers) and *Nederland Handelsland 2025* (annual macro trade monitor).")
lines.append("   - *Cross-verification:* CBS trade values reconcile with Eurostat (e.g., total NL imports from Poland: €15,650 mln in 2023 and €16,205 mln in 2025; Extra-EU imports: €459,679 mln in 2023 and €445,998 mln in 2025).")
lines.append("   - *Limits:* CBS tables round to nearest million EUR. CBS trade monitor highlights that 35% of total Dutch goods imports (EUR 277B in 2023) are re-exported, meaning import demand combines domestic Dutch absorption and European distribution.")
lines.append("3. **GUS (Główny Urząd Statystyczny / Statistics Poland)**:")
lines.append("   - *Coverage:* *Produkcja wyrobów przemysłowych w 2025 r.* (Tablica 1: physical output volumes; Tablica 5: sold production values by PKWiU division, group, and class across 2023, 2024, and 2025).")
lines.append("   - *Limits:* Tablica 1 covers enterprises with 50+ employees; Tablica 5 covers enterprises with 10+ employees. Domestic reporting is in PLN (converted at market rates where applicable).")
lines.append("4. **PAIH (Polish Investment and Trade Agency) & Industrial Trade Fairs**:")
lines.append("   - *Coverage:* Official export development data (Brand HUB 2024–2029), sector export leaderboards, and contractor attendance at Grupa MTP (BUDMA, Meble Polska) and Targi Kielce (Plastpol).")
lines.append("   - *Limits:* Industry reports provide macro export volumes; individual enterprise capacities require direct commercial vetting.")
lines.append("\nAll source data files, metadata summaries, and text excerpts are preserved locally under `sources/`.")
lines.append("\n---\n")

lines.append("## 2. Evidence Tables\n")
lines.append("### Table 1: Top 40 HS4 Import Lines from Poland into the Netherlands (2023→2025)")
lines.append("Ranked by full-year 2025 value. Values in Euros (€). Compliance flags identify mandatory EU/Dutch regulatory hurdles (CE, Packaging/EPR, Food-contact, CRA).\n")
lines.append("| Rank | HS4 | Description | Value 2023 (€) | Value 2025 (€) | Change (€) | Change (%) | Compliance Flags |")
lines.append("|:---:|:---:|:---|---:|---:|---:|:---:|:---|")
for i, (v25, v23, diff, pct, code, label) in enumerate(ranked_pl, 1):
    pct_str = f"{pct:+.1f}%" if pct is not None else "N/A"
    flags = get_compliance_flags(code, label)
    lines.append(f"| {i} | `{code}` | {label} | €{v23:,.0f} | €{v25:,.0f} | €{diff:+,.0f} | {pct_str} | {flags} |")

lines.append("\n### Table 2: Top 40 HS4 Import Lines from Extra-EU Partners into the Netherlands (2023→2025)")
lines.append("Ranked by full-year 2025 value. Values in Euros (€).\n")
lines.append("| Rank | HS4 | Description | Value 2023 (€) | Value 2025 (€) | Change (€) | Change (%) | Compliance Flags |")
lines.append("|:---:|:---:|:---|---:|---:|---:|:---:|:---|")
for i, (v25, v23, diff, pct, code, label) in enumerate(ranked_eu, 1):
    pct_str = f"{pct:+.1f}%" if pct is not None else "N/A"
    flags = get_compliance_flags(code, label)
    lines.append(f"| {i} | `{code}` | {label} | €{v23:,.0f} | €{v25:,.0f} | €{diff:+,.0f} | {pct_str} | {flags} |")

lines.append("\n---\n")

lines.append("## 3. Market Structure Audit: Concentrated vs. Fragmented Sectors\n")
lines.append("To determine whether an independent distributor, agency, or importer can take a position, each candidate sector is screened against its channel concentration:")
lines.append("\n| HS Sector | Key Goods | Dutch Channel Structure | Dominated vs. Fragmented | Distributor Feasibility |")
lines.append("|:---|:---|:---|:---|:---|")
lines.append("| **2709, 2710, 2711** | Crude oil, refined fuels, LNG | Oil majors (Shell, BP, Total) and global commodity traders (Vitol, Trafigura); deepwater maritime terminals. | **Dominated** (Oligopoly) | **Unfeasible** (Requires EUR 100M+ credit lines). |")
lines.append("| **8471, 8517 (Consumer)** | Laptops, mobile phones, servers | OEM direct sales & captive plants (Dell factory in Łódź, Poland; Apple, HP, Lenovo). | **Dominated** (Captive OEM) | **Unfeasible** for standard consumer SKUs. |")
lines.append("| **8703, 8704, 8708** | Cars, commercial vans, auto parts | OEM captive assembly (Stellantis Tychy, VW Poznań/Września, MAN Niepołomice); Tier-1 EDI systems. | **Dominated** (Captive OEM) | **Unfeasible** (Multi-year IATF 16949 supplier lock-in). |")
lines.append("| **3002, 3004** | Vaccines, medicaments, blood products | Big Pharma multinationals; strict GDP wholesale distribution licensing (Farmatec). | **Dominated** (Regulated Oligopoly) | **Unfeasible** (Capital & GDP license barriers). |")
lines.append("| **7610, 3925** | Aluminium & PVC architectural joinery | Over 1,500 regional Dutch contractors, gevelbouwers, and modular builders ordering per project. | **Highly Fragmented** | **Prime Candidate** (Project agency & Wkb dossier bridge). |")
lines.append("| **9405** | Commercial & industrial LED luminaires | Installation contractors (Equans, SPIE, Unica) and regional technical wholesalers. | **Fragmented** | **Prime Candidate** (Project specification & photometrics). |")
lines.append("| **7308, 7326** | Structural steel, solar racking, mezzanines | Solar EPCs, warehouse developers, and greenhouse builders buying custom structural fabrications. | **Highly Fragmented** | **Prime Candidate** (EN 1090 / CBAM quality brokerage). |")
lines.append("| **8517, 8471 (Industrial)** | Industrial IoT gateways, DIN-rail edge computers | Automation engineers, systems integrators, and specialized value-added distributors (VADs). | **Fragmented** | **Prime Candidate** (CRA compliance & EU Importer of record). |")
lines.append("| **9401, 9403 (Contract)** | Office acoustic pods, ergonomic seating | Commercial workplace dealers (projectinrichters), facility managers, corporate real estate. | **Moderately Fragmented** | **Prime Candidate** (B2B workplace agency / dealer distribution). |")

lines.append("\n---\n")

lines.append("## 4. Polish Manufacturing Capacity & Supply-Side Benchmarks\n")
lines.append("Official production statistics from GUS (*Produkcja wyrobów przemysłowych w 2025 r.*) and PAIH confirm substantial Polish supply capacity across the candidate sectors:")
lines.append("\n| Sector / Product Group | PKWiU / PRODPOL Code | 2025 Physical Production (GUS Tablica 1) | Sold Production Value (GUS Tablica 5) | Export Scale & Trade Fairs |")
lines.append("|:---|:---:|---:|---:|:---|")
lines.append("| **Plastic Doors & Windows (Joinery)** | `22.23` | **10,894,046 units** (9.71M windows, 337k doors) | **23.58 billion PLN** (steady growth 2023–2025) | #1 EU exporter; €3.9B joinery export (PAIH); BUDMA Poznań (>600 exhibitors). |")
lines.append("| **Aluminium Joinery & Profiles** | `25.12` | **592,774 units** (294k doors, 299k windows) | **5.67 billion PLN** (+12.2% from 2023) | Strong extrusion & fabrication cluster (Aluprof, Aliplast, Yawal). |")
lines.append("| **Structural Metal & Steel Components** | `25.11` | Custom tonnage across heavy fabrication | **30.92 billion PLN** (36.58B PLN for total 25.1) | Primary supplier for Central/Western European logistics and energy infrastructure. |")
lines.append("| **Electric Lighting Equipment** | `27.40` | Architectural/industrial LED luminaires | **4.99 billion PLN** (2025 sold value) | Major indigenous brands (Lena Lighting, LUG, Kanlux) with in-house photometrics. |")
lines.append("| **Office & Contract Furniture** | `31.01` | **5,449,376 units** (+18.9% vs. 2024) | **3.40 billion PLN** (Division 31 total: 50.21B PLN) | #2 global exporter (€16.2B export, PAIH); Meble Polska (71 buyer nations). |")
lines.append("| **Insulated Cables & Optical Fibers** | `27.32` | **545,916 tonnes** (147k t fiber optic cables) | **12.06 billion PLN** (Division 27.3: 19.17B PLN) | Major production hubs (TF Kable, optical fiber cable manufacturing). |")

lines.append("\n---\n")

lines.append("## 5. Ranked Candidate Opportunities\n")
lines.append("Candidates are strictly evaluated as **distribution, agency, or import positions** (not manufacturing), screened against `drafts/edge-inventory.md`, and passed through the A2 Dutch and AI 2030 gates.\n")

lines.append("### 1. Architectural Aluminium & High-Performance Joinery Systems (HS 7610 / HS 3925)\n")
lines.append("""Exclusive agency and project distribution for Polish architectural aluminium fabricators supplying Dutch commercial and modular builders.
Demand: NL imports of HS 7610 from Poland surged from €77,867,541 in 2023 to €148,271,001 in 2025 (+90.4%); HS 3925 reached €241,935,803 (+28.0%). Poland exported €3.9B in joinery (2024, PAIH); GUS reports 10.89M plastic and 592k aluminium window/door units produced in 2025.
Edge: Polish language accesses fabricators directly; regulatory literacy navigates CPR EN 14351-1, CE execution classes, and Dutch 2024 Wkb technical dossier mandates; engineering habit automates U-value/BENG compliance trails.
Gates: A2 Pass (commercial contractors accept English; partner facade erectors handle on-site Dutch). AI Pass (physical building envelopes and energy retrofits cannot be digitized).
First test: Broker a €30,000 custom window package for a Dutch modular project with complete Wkb dossier for a 10% fee.
Kill fact: Dutch contractor insurer or VMRG mandate strictly requiring local KOMO-certified assembly partners.""")

lines.append("\n### 2. Commercial & Industrial Smart LED Luminaires (HS 9405)\n")
lines.append("""Value-added distribution and project specification for Polish commercial/industrial LED luminaires targeting Dutch logistics warehouses, greenhouses, and retrofit real estate.
Demand: NL imports of HS 9405 from Poland were €146,540,815 (2023) and €146,707,897 (2025). GUS 2025 lighting sold production was 4.99 billion PLN. Fluorescent bans drive massive retrofit demand across Dutch installation contractors (Fedet/NLA).
Edge: Polish technical liaison with factory photometric labs; regulatory literacy audits Ecodesign/EPREL, WEEE/LightRec, and CRA rules for smart DALI controllers; 30k LinkedIn audience reaches facility directors.
Gates: A2 Pass (technical procurement with Dutch electrical installers is English-ready). AI Pass (physical lighting required in every building; AI building automation boosts smart DALI luminaire demand).
First test: Supply a €15,000 luminaire pilot with DIALux photometrics for a logistics hall retrofit.
Kill fact: Major Dutch installers refuse to order outside existing wholesaler accounts (Technische Unie/Rexel).""")

lines.append("\n### 3. CRA-Compliant Industrial IoT Gateways & Edge Networking (HS 8517 / HS 8471 / HS 8473)\n")
lines.append("""Authorized EU Importer and technical distributor for non-EU or Polish industrial IoT gateways, DIN-rail edge computers, and rugged network appliances.
Demand: NL imports of HS 8517 from Poland jumped from €116,736,637 in 2023 to €276,670,635 in 2025 (+137.0%); Extra-EU imports reached €32,299,288,278. HS 8473 grew +21.8% to €153,285,015.
Edge: Regulatory literacy masters Cyber Resilience Act (CRA (EU) 2024/2847) mandatory importer liability, CE, and RED; engineering habit audits firmware SBOM and CVE processes; English/Russian/Polish bridges hardware makers.
Gates: A2 Pass (Dutch automation engineers and systems integrators operate in English). AI Pass (edge AI and sensor data collection drive rugged hardware demand).
First test: Contract a €5,000 CRA technical file audit and importer-of-record retainer for one manufacturer.
Kill fact: Manufacturer firmware contains unmaintained open-source components incapable of meeting CRA vulnerability-remediation standards.""")

lines.append("\n### 4. Engineered Structural Steel Subassemblies & Solar/Agri-Racking (HS 7308 / HS 7326)\n")
lines.append("""Procurement agency and quality-assurance distribution for Polish EN 1090-certified structural steel fabricators supplying Dutch solar mounting, logistics mezzanines, and greenhouse infrastructure.
Demand: NL imports of HS 7308 from Poland expanded from €134,178,660 in 2023 to €160,013,376 in 2025 (+19.3%); HS 7326 rose to €116,475,536 (+23.1%). GUS recorded 30.92 billion PLN in structural metal production (2025).
Edge: Polish coordinates directly with Silesian fabricators; regulatory literacy verifies CPR EN 1090 EXC2/EXC3, 3.1 material certs, and CBAM carbon accounting; engineering habit checks CAD/CAM weld tolerances.
Gates: A2 Pass (Dutch solar EPCs and structural project managers negotiate in English). AI Pass (load-bearing steel structures for energy transition cannot be digitized).
First test: Broker a €25,000 trial order of solar racking beams with 3.1 test certs for 7% commission.
Kill fact: Road freight surcharges and steel price swings eliminate the 25% Polish fabrication discount.""")

lines.append("\n### 5. Acoustic Meeting Pods & Ergonomic Contract Workstations (HS 9401 / HS 9403)\n")
lines.append("""Exclusive Dutch agency for Polish acoustic meeting pods and ergonomic contract workstations supplying commercial office project-furnishers.
Demand: Polish furniture exports reached €16.2B (2024, PAIH). GUS data shows Polish office furniture production rose +18.9% in 2025 to 5.45M units (sold value 3.40B PLN). Combined NL imports of HS 9401 and 9403 from Poland totaled €683,228,385 in 2025.
Edge: Polish secures exclusive agency terms; regulatory literacy manages EUDR deforestation tracing, PPWR, and ESPR/DPP; 30k LinkedIn audience drives corporate tenant inbound leads.
Gates: A2 Pass (Dutch commercial workplace dealers and facility heads operate in English). AI Pass (acoustic isolation for remote work is human-centric physical infrastructure).
First test: Place two demo acoustic pods in a Dutch co-working space on a 60-day paid pilot with purchase option (<€20k).
Kill fact: Major Dutch fit-out dealers remain locked into framework agreements with Nordic incumbent brands.""")

lines.append("\n---\n")

lines.append("## 6. Honest Appraisal: Did This Instrument Find Anything a Dutch Founder Could Not?\n")
lines.append("""The macro trade data found no secret consumer product: high-value trade flows are dominated by multinational captive supply chains (Dell, automakers, oil majors). A Dutch founder with local networks can easily buy wholesale. What this instrument isolated that a Dutch founder cannot easily replicate is cross-border regulatory arbitrage. By combining native Polish/CEE supplier access with direct mastery of technical EU legislation—specifically the 2024 Dutch Wkb construction dossier mandate, CPR EN 1090 execution classes, and the September 2026 Cyber Resilience Act (CRA)—it identifies five B2B niches where mid-sized manufacturers have strong production capacity but are blocked by compliance complexity. The moat is not sourcing; it is technical file liability and bilingual engineering operations.""")

with open(os.path.join(folder, "findings.md"), "w") as f:
    f.write("\n".join(lines) + "\n")

print("Generated findings.md successfully.")
