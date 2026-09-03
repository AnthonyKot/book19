# Trade-Flow Gaps: Netherlands Imports from Poland and Non-EU Partners (2023–2025)

**Cut-off & Fetch Date:** 2026-09-03  
**Author / Reader Context:** Screened against `drafts/edge-inventory.md` (Languages: Polish/Russian/English/Dutch A2; Capital: ~EUR 100k; Regulatory literacy: CRA, CPR, PPWR, Machinery, MDR; Engineering habit; 30k LinkedIn audience).

---

## 1. Sources and Their Limits

This research synthesizes published trade statistics and industrial production data from four primary institutional authorities:
1. **Eurostat Comext (Database DS-045409: EU Trade Since 1988 by HS2-4-6 and CN8)**:
   - *Coverage:* Annual reporting for the Netherlands (`reporter=NL`), import flow (`flow=1`), for partner countries Poland (`PL`) and Extra-EU27 (`EXT_EU27_2020`) across 2023, 2024, and 2025 at full 4-digit Harmonized System (HS4) granularity. Values in Euros (`VALUE_IN_EUROS`).
   - *Limits:* Comext records physical and customs arrivals. In the Netherlands, this is significantly influenced by the 'Rotterdam effect'—goods entering through the Port of Rotterdam or Schiphol Airport cleared for EU transit or intended for re-export (quasi-transit) to Germany and the hinterland. CIF valuation includes freight and insurance.
2. **CBS StatLine (Centraal Bureau voor de Statistiek)**:
   - *Coverage:* Table `85429NED` (Internationale goederenhandel; grensoverschrijding, kerncijfers) and *Nederland Handelsland 2025* (annual macro trade monitor).
   - *Cross-verification:* CBS trade values reconcile with Eurostat (e.g., total NL imports from Poland: €15,650 mln in 2023 and €16,205 mln in 2025; Extra-EU imports: €459,679 mln in 2023 and €445,998 mln in 2025).
   - *Limits:* CBS tables round to nearest million EUR. CBS trade monitor highlights that 35% of total Dutch goods imports (EUR 277B in 2023) are re-exported, meaning import demand combines domestic Dutch absorption and European distribution.
3. **GUS (Główny Urząd Statystyczny / Statistics Poland)**:
   - *Coverage:* *Produkcja wyrobów przemysłowych w 2025 r.* (Tablica 1: physical output volumes; Tablica 5: sold production values by PKWiU division, group, and class across 2023, 2024, and 2025).
   - *Limits:* Tablica 1 covers enterprises with 50+ employees; Tablica 5 covers enterprises with 10+ employees. Domestic reporting is in PLN (converted at market rates where applicable).
4. **PAIH (Polish Investment and Trade Agency) & Industrial Trade Fairs**:
   - *Coverage:* Official export development data (Brand HUB 2024–2029), sector export leaderboards, and contractor attendance at Grupa MTP (BUDMA, Meble Polska) and Targi Kielce (Plastpol).
   - *Limits:* Industry reports provide macro export volumes; individual enterprise capacities require direct commercial vetting.

All source data files, metadata summaries, and text excerpts are preserved locally under `sources/`.

---

## 2. Evidence Tables

### Table 1: Top 40 HS4 Import Lines from Poland into the Netherlands (2023→2025)
Ranked by full-year 2025 value. Values in Euros (€). Compliance flags identify mandatory EU/Dutch regulatory hurdles (CE, Packaging/EPR, Food-contact, CRA).

| Rank | HS4 | Description | Value 2023 (€) | Value 2025 (€) | Change (€) | Change (%) | Compliance Flags |
|:---:|:---:|:---|---:|---:|---:|:---:|:---|
| 1 | `8471` | Automatic data-processing machines and units thereof; magnetic or optical readers, machines for transcribing data onto data media in coded form and machines for processing such data, n.e.s. | €1,639,655,350 | €2,018,868,171 | €+379,212,821 | +23.1% | CE (Machinery/EMC/LVD/RED); WEEE/Battery EPR; CRA ((EU) 2024/2847) |
| 2 | `0207` | Meat and edible offal of fowls of the species Gallus domesticus, ducks, geese, turkeys and guinea fowls, fresh, chilled or frozen | €352,383,056 | €421,655,870 | €+69,272,814 | +19.7% | Packaging/EPR (Afvalfonds) |
| 3 | `9401` | Seats, whether or not convertible into beds, and parts thereof, n.e.s. (excl. medical, surgical, dental or veterinary of heading 9402) | €481,124,802 | €406,335,688 | €-74,789,114 | -15.5% | CE (LVD/EMC/GPSR); WEEE/Battery EPR |
| 4 | `9403` | Furniture and parts thereof, n.e.s. (excl. seats and medical, surgical, dental or veterinary furniture) | €271,900,587 | €276,892,697 | €+4,992,110 | +1.8% | CE (LVD/EMC/GPSR); WEEE/Battery EPR |
| 5 | `8517` | Telephone sets, incl. telephones for cellular networks or for other wireless networks; other apparatus for the transmission or reception of voice, images or other data, incl. apparatus for communication in a wired or wireless network {such as a local or wide area network}; parts thereof (excl. than transmission or reception apparatus of heading 8443, 8525, 8527 or 8528) | €116,736,637 | €276,670,635 | €+159,933,998 | +137.0% | CE (Machinery/EMC/LVD/RED); WEEE/Battery EPR; CRA ((EU) 2024/2847) |
| 6 | `8528` | Monitors and projectors, not incorporating television reception apparatus; reception apparatus for television, whether or not incorporating radio-broadcast receivers or sound or video recording or reproducing apparatus | €344,794,450 | €270,617,543 | €-74,176,907 | -21.5% | CE (Machinery/EMC/LVD/RED); WEEE/Battery EPR; CRA ((EU) 2024/2847) |
| 7 | `0201` | Meat of bovine animals, fresh or chilled | €160,668,009 | €268,555,699 | €+107,887,690 | +67.1% | Packaging/EPR (Afvalfonds) |
| 8 | `8708` | Parts and accessories for tractors, motor vehicles for the transport of ten or more persons, motor cars and other motor vehicles principally designed for the transport of persons, motor vehicles for the transport of goods and special purpose motor vehicles of heading 8701 to 8705, n.e.s. | €409,081,607 | €255,001,143 | €-154,080,464 | -37.7% | GPSR / Standard |
| 9 | `3925` | Builders' ware of plastics, n.e.s. | €189,009,174 | €241,935,803 | €+52,926,629 | +28.0% | CE (CPR (EN 14351/EN 1090)) |
| 10 | `2710` | Petroleum oils and oils obtained from bituminous minerals (excl. crude); preparations containing >= 70% by weight of petroleum oils or of oils obtained from bituminous minerals, these oils being the basic constituents of the preparations, n.e.s.; waste oils containing mainly petroleum or bituminous minerals(2002-2500);Petroleum oils and oils obtained from bituminous minerals (excl. crude); preparations containing >= 70% by weight of petroleum oils or of oils obtained from bituminous minerals, these oils being the basic constituents of the preparations, n.e.s.(1988-2001) | €398,423,211 | €224,153,924 | €-174,269,287 | -43.7% | GPSR / Standard |
| 11 | `1806` | Chocolate and other food preparations containing cocoa | €127,516,958 | €210,588,205 | €+83,071,247 | +65.1% | Packaging/EPR (Afvalfonds) |
| 12 | `3002` | Human blood; animal blood prepared for therapeutic, prophylactic or diagnostic uses; antisera and other blood fractions and immunological products, whether or not modified or obtained by means of biotechnological processes; vaccines, toxins, cultures of micro-organisms (excl. yeasts) and similar products | €99,110,887 | €202,820,407 | €+103,709,520 | +104.6% | GPSR / Standard |
| 13 | `8704` | Motor vehicles for the transport of goods, incl. chassis with engine and cab | €283,810,533 | €192,957,618 | €-90,852,915 | -32.0% | GPSR / Standard |
| 14 | `2402` | Cigars, cheroots, cigarillos and cigarettes of tobacco or of tobacco substitutes | €188,919,926 | €184,185,535 | €-4,734,391 | -2.5% | GPSR / Standard |
| 15 | `6204` | Women's or girls' suits, ensembles, jackets, blazers, dresses, skirts, divided skirts, trousers, bib and brace overalls, breeches and shorts (excl. knitted or crocheted, wind-jackets and similar articles, slips, petticoats and panties, tracksuits, ski suits and swimwear) | €175,468,767 | €182,907,137 | €+7,438,370 | +4.2% | GPSR / Standard |
| 16 | `2707` | Oils and other products of the distillation of high temperature coal tar; similar products in which the weight of the aromatic constituents exceeds that of the non-aromatic constituents | €204,219,519 | €166,051,850 | €-38,167,669 | -18.7% | GPSR / Standard |
| 17 | `7308` | Structures and parts of structures "e.g., bridges and bridge-sections, lock-gates, towers, lattice masts, roofs, roofing frameworks, doors and windows and their frames and thresholds for doors, shutters, balustrades, pillars and columns", of iron or steel; plates, rods, angles, shapes, sections, tubes and the like, prepared for use in structures, of iron or steel (excl. prefabricated buildings of heading 9406) | €134,178,660 | €160,013,376 | €+25,834,716 | +19.3% | CE (CPR (EN 14351/EN 1090)) |
| 18 | `3923` | Articles for the conveyance or packaging of goods, of plastics; stoppers, lids, caps and other closures, of plastics | €140,499,670 | €154,309,688 | €+13,810,018 | +9.8% | Packaging/EPR (PPWR/Afvalfonds); Food-contact (EC 1935/2004) |
| 19 | `8473` | Parts and accessories (other than covers, carrying cases and the like) suitable for use solely or principally with machines of heading 8469 to 8472, n.e.s. | €125,810,797 | €153,285,015 | €+27,474,218 | +21.8% | CE (Machinery/EMC/LVD/RED); WEEE/Battery EPR; CRA ((EU) 2024/2847) |
| 20 | `8703` | Motor cars and other motor vehicles principally designed for the transport of <10 persons, incl. station wagons and racing cars (excl. motor vehicles of heading 8702) | €155,978,176 | €151,530,557 | €-4,447,619 | -2.9% | GPSR / Standard |
| 21 | `7610` | Structures and parts of structures "e.g., bridges and bridge-sections, towers, lattice masts, pillars and columns, roofs, roofing frameworks, doors and windows and their frames and thresholds for doors, shutters, balustrades", of aluminium (excl. prefabricated buildings of heading 9406); plates, rods, profiles, tubes and the like, prepared for use in structures, of aluminium | €77,867,541 | €148,271,001 | €+70,403,460 | +90.4% | CE (CPR (EN 14351/EN 1090)) |
| 22 | `9405` | Lamps and lighting fittings, incl. searchlights and spotlights, and parts thereof, n.e.s; illuminated signs, illuminated nameplates and the like having a permanently fixed light source, and parts thereof, n.e.s. | €146,540,815 | €146,707,897 | €+167,082 | +0.1% | CE (LVD/EMC/GPSR); WEEE/Battery EPR; CRA (if IoT/smart control) |
| 23 | `8509` | Electromechanical domestic appliances, with self-contained electric motor; parts thereof (excl. vacuum cleaners, dry and wet vacuum cleaners) | €136,067,881 | €134,776,939 | €-1,290,942 | -0.9% | CE (Machinery/EMC/LVD/RED); WEEE/Battery EPR; Food-contact; CRA (if smart connected) |
| 24 | `0407` | Birds' eggs, in shell, fresh, preserved or cooked | €51,535,630 | €122,784,931 | €+71,249,301 | +138.3% | GPSR / Standard |
| 25 | `2009` | Fruit juices, incl. grape must, and vegetable juices, unfermented, not containing added spirit, whether or not containing added sugar or other sweetening matter | €89,875,071 | €118,991,046 | €+29,115,975 | +32.4% | Packaging/EPR (Afvalfonds) |
| 26 | `6110` | Jerseys, pullovers, cardigans, waistcoats and similar articles, knitted or crocheted (excl. wadded waistcoats) | €79,550,734 | €118,760,818 | €+39,210,084 | +49.3% | GPSR / Standard |
| 27 | `7326` | Articles of iron or steel, n.e.s. (excl. cast articles) | €94,642,016 | €116,475,536 | €+21,833,520 | +23.1% | GPSR / Standard |
| 28 | `2106` | Food preparations, n.e.s. | €63,452,950 | €113,861,038 | €+50,408,088 | +79.4% | Packaging/EPR (Afvalfonds) |
| 29 | `4819` | Cartons, boxes, cases, bags and other packing containers, of paper, paperboard, cellulose wadding or webs of cellulose fibres, n.e.s.; box files, letter trays, and similar articles, of paperboard of a kind used in offices, shops or the like | €83,147,908 | €113,256,961 | €+30,109,053 | +36.2% | Packaging/EPR (PPWR/Afvalfonds); Food-contact (EC 1935/2004) |
| 30 | `6203` | Men's or boys' suits, ensembles, jackets, blazers, trousers, bib and brace overalls, breeches and shorts (excl. knitted or crocheted, wind-jackets and similar articles, separate waistcoats, tracksuits, ski suits and swimwear) | €72,780,462 | €112,255,555 | €+39,475,093 | +54.2% | GPSR / Standard |
| 31 | `8482` | Ball or roller bearings (excl. steel balls of heading 7326); parts thereof | €140,643,819 | €110,673,493 | €-29,970,326 | -21.3% | CE (Machinery/EMC/LVD/RED); WEEE/Battery EPR |
| 32 | `8544` | Insulated "incl. enamelled or anodised" wire, cable "incl. coaxial cable" and other insulated electric conductors, whether or not fitted with connectors; optical fibre cables, made up of individually sheathed fibres, whether or not assembled with electric conductors or fitted with connectors | €126,203,852 | €104,568,542 | €-21,635,310 | -17.1% | CE (Machinery/EMC/LVD/RED); WEEE/Battery EPR |
| 33 | `3920` | Plates, sheets, film, foil and strip, of non-cellular plastics, not reinforced, laminated, supported or similarly combined with other materials, without backing, unworked or merely surface-worked or merely cut into squares or rectangles (excl. self-adhesive products, and floor, wall and ceiling coverings of heading 3918) | €76,378,219 | €102,414,755 | €+26,036,536 | +34.1% | GPSR / Standard |
| 34 | `3303` | Perfumes and toilet waters (excl. aftershave lotions, personal deodorants and hair lotions) | €83,017,249 | €101,966,062 | €+18,948,813 | +22.8% | Packaging/EPR (Afvalfonds) |
| 35 | `6403` | Footwear with outer soles of rubber, plastics, leather or composition leather and uppers of leather (excl. orthopaedic footwear, skating boots with ice or roller skates attached, and toy footwear) | €91,535,599 | €99,328,348 | €+7,792,749 | +8.5% | GPSR / Standard |
| 36 | `8510` | Electric shavers, hair clippers and hair-removing appliances, with self-contained electric motor; parts thereof | €128,620,957 | €99,133,174 | €-29,487,783 | -22.9% | CE (Machinery/EMC/LVD/RED); WEEE/Battery EPR |
| 37 | `0901` | Coffee, whether or not roasted or decaffeinated; coffee husks and skins; coffee substitutes containing coffee in any proportion | €77,870,660 | €99,084,754 | €+21,214,094 | +27.2% | Packaging/EPR (Afvalfonds) |
| 38 | `3304` | Beauty or make-up preparations and preparations for the care of the skin, incl. sunscreen or suntan preparations (excl. medicaments); manicure or pedicure preparations | €78,793,113 | €98,804,016 | €+20,010,903 | +25.4% | GPSR / Standard |
| 39 | `3826` | Biodiesel and mixtures thereof, not containing or containing < 70 % by weight of petroleum oils or oils obtained from bituminous minerals | €45,549,685 | €90,177,217 | €+44,627,532 | +98.0% | GPSR / Standard |
| 40 | `8536` | Electrical apparatus for switching or protecting electrical circuits, or for making connections to or in electrical circuits, e.g., switches, relays, fuses, surge suppressors, plugs, sockets, lamp holders and junction boxes, for a voltage <= 1.000 V (excl. control desks, cabinets, panels etc. of heading 8537) | €81,096,661 | €87,678,991 | €+6,582,330 | +8.1% | CE (Machinery/EMC/LVD/RED); WEEE/Battery EPR |

### Table 2: Top 40 HS4 Import Lines from Extra-EU Partners into the Netherlands (2023→2025)
Ranked by full-year 2025 value. Values in Euros (€).

| Rank | HS4 | Description | Value 2023 (€) | Value 2025 (€) | Change (€) | Change (%) | Compliance Flags |
|:---:|:---:|:---|---:|---:|---:|:---:|:---|
| 1 | `2709` | Petroleum oils and oils obtained from bituminous minerals, crude | €59,721,383,345 | €42,108,780,553 | €-17,612,602,792 | -29.5% | GPSR / Standard |
| 2 | `8471` | Automatic data-processing machines and units thereof; magnetic or optical readers, machines for transcribing data onto data media in coded form and machines for processing such data, n.e.s. | €30,320,721,232 | €37,861,625,535 | €+7,540,904,303 | +24.9% | CE (Machinery/EMC/LVD/RED); WEEE/Battery EPR; CRA ((EU) 2024/2847) |
| 3 | `8517` | Telephone sets, incl. telephones for cellular networks or for other wireless networks; other apparatus for the transmission or reception of voice, images or other data, incl. apparatus for communication in a wired or wireless network {such as a local or wide area network}; parts thereof (excl. than transmission or reception apparatus of heading 8443, 8525, 8527 or 8528) | €32,476,656,713 | €32,299,288,278 | €-177,368,435 | -0.5% | CE (Machinery/EMC/LVD/RED); WEEE/Battery EPR; CRA ((EU) 2024/2847) |
| 4 | `2710` | Petroleum oils and oils obtained from bituminous minerals (excl. crude); preparations containing >= 70% by weight of petroleum oils or of oils obtained from bituminous minerals, these oils being the basic constituents of the preparations, n.e.s.; waste oils containing mainly petroleum or bituminous minerals(2002-2500);Petroleum oils and oils obtained from bituminous minerals (excl. crude); preparations containing >= 70% by weight of petroleum oils or of oils obtained from bituminous minerals, these oils being the basic constituents of the preparations, n.e.s.(1988-2001) | €13,375,501,762 | €11,544,368,216 | €-1,831,133,546 | -13.7% | GPSR / Standard |
| 5 | `8542` | Electronic integrated circuits; parts thereof | €14,398,954,902 | €11,279,409,146 | €-3,119,545,756 | -21.7% | CE (Machinery/EMC/LVD/RED); WEEE/Battery EPR |
| 6 | `2711` | Petroleum gas and other gaseous hydrocarbons | €18,832,838,609 | €10,949,898,665 | €-7,882,939,944 | -41.9% | GPSR / Standard |
| 7 | `9018` | Instruments and appliances used in medical, surgical, dental or veterinary sciences, incl. scintigraphic apparatus, other electro-medical apparatus and sight-testing instruments, n.e.s. | €9,298,518,663 | €10,291,520,937 | €+993,002,274 | +10.7% | CE (MDR/EMC) |
| 8 | `3002` | Human blood; animal blood prepared for therapeutic, prophylactic or diagnostic uses; antisera and other blood fractions and immunological products, whether or not modified or obtained by means of biotechnological processes; vaccines, toxins, cultures of micro-organisms (excl. yeasts) and similar products | €7,363,285,100 | €9,952,140,912 | €+2,588,855,812 | +35.2% | GPSR / Standard |
| 9 | `7601` | Unwrought aluminium | €7,027,637,734 | €7,020,886,154 | €-6,751,580 | -0.1% | GPSR / Standard |
| 10 | `9021` | Orthopaedic appliances, incl. crutches, surgical belts and trusses; splints and other fracture appliances; artificial parts of the body; hearing aids and other appliances which are worn or carried, or implanted in the body, to compensate for a defect or disability | €5,892,327,756 | €6,260,336,361 | €+368,008,605 | +6.2% | CE (MDR/EMC) |
| 11 | `1801` | Cocoa beans, whole or broken, raw or roasted | €2,169,169,583 | €6,159,791,532 | €+3,990,621,949 | +184.0% | GPSR / Standard |
| 12 | `8507` | Electric accumulators, incl. separators therefor, whether or not square or rectangular; parts thereof (excl. spent and those of unhardened rubber or textiles) | €4,520,526,363 | €5,553,176,263 | €+1,032,649,900 | +22.8% | CE (Machinery/EMC/LVD/RED); WEEE/Battery EPR |
| 13 | `8473` | Parts and accessories (other than covers, carrying cases and the like) suitable for use solely or principally with machines of heading 8469 to 8472, n.e.s. | €3,401,730,608 | €5,479,642,962 | €+2,077,912,354 | +61.1% | CE (Machinery/EMC/LVD/RED); WEEE/Battery EPR; CRA ((EU) 2024/2847) |
| 14 | `8504` | Electrical transformers, static converters, e.g. rectifiers, and inductors; parts thereof | €6,306,421,497 | €4,985,162,307 | €-1,321,259,190 | -21.0% | CE (Machinery/EMC/LVD/RED); WEEE/Battery EPR |
| 15 | `3004` | Medicaments consisting of mixed or unmixed products for therapeutic or prophylactic uses, put up in measured doses "incl. those for transdermal administration" or in forms or packings for retail sale (excl. goods of heading 3002, 3005 or 3006) | €6,042,109,048 | €4,843,579,766 | €-1,198,529,282 | -19.8% | GPSR / Standard |
| 16 | `8443` | Printing machinery used for printing by means of plates, cylinders and other printing components of heading 8442 (excl. hectograph or stencil duplicating machines, addressing machines and other office printing machines of heading 8469 to 8472); other printers, copying machines and facsimile machines, whether or not combined; parts thereof | €4,686,442,239 | €4,459,093,050 | €-227,349,189 | -4.9% | CE (Machinery/EMC/LVD/RED); WEEE/Battery EPR |
| 17 | `8528` | Monitors and projectors, not incorporating television reception apparatus; reception apparatus for television, whether or not incorporating radio-broadcast receivers or sound or video recording or reproducing apparatus | €3,787,538,356 | €4,087,109,659 | €+299,571,303 | +7.9% | CE (Machinery/EMC/LVD/RED); WEEE/Battery EPR; CRA ((EU) 2024/2847) |
| 18 | `8541` | Diodes, transistors and similar semiconductor devices; photosensitive semiconductor devices, incl. photovoltaic cells whether or not assembled in modules or made up into panels (excl. photovotaic generators); light emitting diodes "LED"; mounted piezoelectric crystals; parts thereof | €10,389,757,311 | €3,624,195,023 | €-6,765,562,288 | -65.1% | CE (Machinery/EMC/LVD/RED); WEEE/Battery EPR |
| 19 | `8703` | Motor cars and other motor vehicles principally designed for the transport of <10 persons, incl. station wagons and racing cars (excl. motor vehicles of heading 8702) | €4,369,991,507 | €3,181,005,081 | €-1,188,986,426 | -27.2% | GPSR / Standard |
| 20 | `2701` | Coal; briquettes, ovoids and similar solid fuels manufactured from coal | €5,621,733,035 | €3,038,233,996 | €-2,583,499,039 | -46.0% | GPSR / Standard |
| 21 | `8523` | Discs, tapes, solid-state non-volatile storage devices, "smart cards" and other media for the recording of sound or of other phenomena, whether or not recorded, incl. matrices and masters for the production of discs (excl. products of chapter 37) | €995,872,387 | €3,008,774,619 | €+2,012,902,232 | +202.1% | CE (Machinery/EMC/LVD/RED); WEEE/Battery EPR; CRA ((EU) 2024/2847) |
| 22 | `9504` | Video game consoles and machines, articles for funfair, table or parlour games, incl. pintables, billiards, special tables for casino games and automatic bowling alley equipment | €5,346,832,205 | €3,008,352,735 | €-2,338,479,470 | -43.7% | CE (Toy Safety); CRA ((EU) 2024/2847) |
| 23 | `8903` | Yachts and other vessels for pleasure or sports; rowing boats and canoes | €1,832,801,964 | €2,849,418,563 | €+1,016,616,599 | +55.5% | GPSR / Standard |
| 24 | `8486` | Machines and apparatus of a kind used solely or principally for the manufacture of semiconductor boules or wafers, semiconductor devices, electronic integrated circuits or flat panel displays; machines and apparatus specified in note 9 C to chapter 84; parts and accessories, n.e.s. | €2,149,756,696 | €2,565,337,471 | €+415,580,775 | +19.3% | CE (Machinery/EMC/LVD/RED); WEEE/Battery EPR |
| 25 | `8411` | Turbojets, turbopropellers and other gas turbines | €2,577,142,428 | €2,442,087,023 | €-135,055,405 | -5.2% | CE (Machinery/EMC/LVD/RED); WEEE/Battery EPR |
| 26 | `8518` | Microphones and stands therefor (excl. cordless microphones with built-in transmitter); loudspeakers, whether or not mounted in their enclosures; headphones and earphones, whether or not combined with a microphone, and sets consisting of a microphone and one or more loudspeakers (excl. telephone sets, hearing aids and helmets with built-in headphones, whether or not incorporating a microphone); audio-frequency electric amplifiers; electric sound amplifier sets; parts thereof | €1,459,085,702 | €2,420,333,871 | €+961,248,169 | +65.9% | CE (Machinery/EMC/LVD/RED); WEEE/Battery EPR |
| 27 | `7202` | Ferro-alloys | €2,817,798,534 | €2,357,385,368 | €-460,413,166 | -16.3% | GPSR / Standard |
| 28 | `2601` | Iron ores and concentrates, incl. roasted iron pyrites | €2,454,068,406 | €2,315,383,428 | €-138,684,978 | -5.7% | GPSR / Standard |
| 29 | `0804` | Dates, figs, pineapples, avocados, guavas, mangoes and mangosteens, fresh or dried | €1,913,049,576 | €2,241,136,638 | €+328,087,062 | +17.1% | Packaging/EPR (Afvalfonds) |
| 30 | `2707` | Oils and other products of the distillation of high temperature coal tar; similar products in which the weight of the aromatic constituents exceeds that of the non-aromatic constituents | €1,573,171,890 | €2,179,289,467 | €+606,117,577 | +38.5% | GPSR / Standard |
| 31 | `8708` | Parts and accessories for tractors, motor vehicles for the transport of ten or more persons, motor cars and other motor vehicles principally designed for the transport of persons, motor vehicles for the transport of goods and special purpose motor vehicles of heading 8701 to 8705, n.e.s. | €2,204,929,995 | €2,116,787,963 | €-88,142,032 | -4.0% | GPSR / Standard |
| 32 | `8802` | Powered aircraft "e.g. helicopters and aeroplanes"; spacecraft, incl. satellites, and suborbital and spacecraft launch vehicles | €2,615,259,807 | €1,898,601,354 | €-716,658,453 | -27.4% | GPSR / Standard |
| 33 | `8525` | Transmission apparatus for radio-broadcasting or television, whether or not incorporating reception apparatus or sound recording or reproducing apparatus; television cameras, digital cameras and video camera recorders | €1,780,437,152 | €1,870,604,535 | €+90,167,383 | +5.1% | CE (Machinery/EMC/LVD/RED); WEEE/Battery EPR; CRA ((EU) 2024/2847) |
| 34 | `6110` | Jerseys, pullovers, cardigans, waistcoats and similar articles, knitted or crocheted (excl. wadded waistcoats) | €1,525,924,792 | €1,758,279,406 | €+232,354,614 | +15.2% | GPSR / Standard |
| 35 | `9403` | Furniture and parts thereof, n.e.s. (excl. seats and medical, surgical, dental or veterinary furniture) | €1,237,398,707 | €1,745,978,156 | €+508,579,449 | +41.1% | CE (LVD/EMC/GPSR); WEEE/Battery EPR |
| 36 | `9027` | Instruments and apparatus for physical or chemical analysis, e.g. polarimeters, refractometers, spectrometers, gas or smoke analysis apparatus; instruments and apparatus for measuring or checking viscosity, porosity, expansion, surface tension or the like; instruments and apparatus for measuring or checking quantities of heat, sound or light, incl. exposure meters; microtomes | €1,787,942,756 | €1,621,163,374 | €-166,779,382 | -9.3% | CE (MDR/EMC) |
| 37 | `8508` | Vacuum cleaners, incl. dry cleaners and wet vacuum cleaners(2007-2500);Electro-mechanical tools for working in the hand, with self-contained electric motor; parts thereof(1988-2001) | €1,072,084,581 | €1,602,263,449 | €+530,178,868 | +49.5% | CE (Machinery/EMC/LVD/RED); WEEE/Battery EPR; CRA (if smart connected) |
| 38 | `6404` | Footwear with outer soles of rubber, plastics, leather or composition leather and uppers of textile materials (excl. toy footwear) | €933,873,884 | €1,600,461,088 | €+666,587,204 | +71.4% | GPSR / Standard |
| 39 | `8429` | Self-propelled bulldozers, angledozers, graders, levellers, scrapers, mechanical shovels, excavators, shovel loaders, tamping machines and roadrollers | €2,208,068,907 | €1,572,839,979 | €-635,228,928 | -28.8% | CE (Machinery/EMC/LVD/RED); WEEE/Battery EPR |
| 40 | `6204` | Women's or girls' suits, ensembles, jackets, blazers, dresses, skirts, divided skirts, trousers, bib and brace overalls, breeches and shorts (excl. knitted or crocheted, wind-jackets and similar articles, slips, petticoats and panties, tracksuits, ski suits and swimwear) | €1,389,183,793 | €1,563,967,041 | €+174,783,248 | +12.6% | GPSR / Standard |

---

## 3. Market Structure Audit: Concentrated vs. Fragmented Sectors

To determine whether an independent distributor, agency, or importer can take a position, each candidate sector is screened against its channel concentration:

| HS Sector | Key Goods | Dutch Channel Structure | Dominated vs. Fragmented | Distributor Feasibility |
|:---|:---|:---|:---|:---|
| **2709, 2710, 2711** | Crude oil, refined fuels, LNG | Oil majors (Shell, BP, Total) and global commodity traders (Vitol, Trafigura); deepwater maritime terminals. | **Dominated** (Oligopoly) | **Unfeasible** (Requires EUR 100M+ credit lines). |
| **8471, 8517 (Consumer)** | Laptops, mobile phones, servers | OEM direct sales & captive plants (Dell factory in Łódź, Poland; Apple, HP, Lenovo). | **Dominated** (Captive OEM) | **Unfeasible** for standard consumer SKUs. |
| **8703, 8704, 8708** | Cars, commercial vans, auto parts | OEM captive assembly (Stellantis Tychy, VW Poznań/Września, MAN Niepołomice); Tier-1 EDI systems. | **Dominated** (Captive OEM) | **Unfeasible** (Multi-year IATF 16949 supplier lock-in). |
| **3002, 3004** | Vaccines, medicaments, blood products | Big Pharma multinationals; strict GDP wholesale distribution licensing (Farmatec). | **Dominated** (Regulated Oligopoly) | **Unfeasible** (Capital & GDP license barriers). |
| **7610, 3925** | Aluminium & PVC architectural joinery | Over 1,500 regional Dutch contractors, gevelbouwers, and modular builders ordering per project. | **Highly Fragmented** | **Prime Candidate** (Project agency & Wkb dossier bridge). |
| **9405** | Commercial & industrial LED luminaires | Installation contractors (Equans, SPIE, Unica) and regional technical wholesalers. | **Fragmented** | **Prime Candidate** (Project specification & photometrics). |
| **7308, 7326** | Structural steel, solar racking, mezzanines | Solar EPCs, warehouse developers, and greenhouse builders buying custom structural fabrications. | **Highly Fragmented** | **Prime Candidate** (EN 1090 / CBAM quality brokerage). |
| **8517, 8471 (Industrial)** | Industrial IoT gateways, DIN-rail edge computers | Automation engineers, systems integrators, and specialized value-added distributors (VADs). | **Fragmented** | **Prime Candidate** (CRA compliance & EU Importer of record). |
| **9401, 9403 (Contract)** | Office acoustic pods, ergonomic seating | Commercial workplace dealers (projectinrichters), facility managers, corporate real estate. | **Moderately Fragmented** | **Prime Candidate** (B2B workplace agency / dealer distribution). |

---

## 4. Polish Manufacturing Capacity & Supply-Side Benchmarks

Official production statistics from GUS (*Produkcja wyrobów przemysłowych w 2025 r.*) and PAIH confirm substantial Polish supply capacity across the candidate sectors:

| Sector / Product Group | PKWiU / PRODPOL Code | 2025 Physical Production (GUS Tablica 1) | Sold Production Value (GUS Tablica 5) | Export Scale & Trade Fairs |
|:---|:---:|---:|---:|:---|
| **Plastic Doors & Windows (Joinery)** | `22.23` | **10,894,046 units** (9.71M windows, 337k doors) | **23.58 billion PLN** (steady growth 2023–2025) | #1 EU exporter; €3.9B joinery export (PAIH); BUDMA Poznań (>600 exhibitors). |
| **Aluminium Joinery & Profiles** | `25.12` | **592,774 units** (294k doors, 299k windows) | **5.67 billion PLN** (+12.2% from 2023) | Strong extrusion & fabrication cluster (Aluprof, Aliplast, Yawal). |
| **Structural Metal & Steel Components** | `25.11` | Custom tonnage across heavy fabrication | **30.92 billion PLN** (36.58B PLN for total 25.1) | Primary supplier for Central/Western European logistics and energy infrastructure. |
| **Electric Lighting Equipment** | `27.40` | Architectural/industrial LED luminaires | **4.99 billion PLN** (2025 sold value) | Major indigenous brands (Lena Lighting, LUG, Kanlux) with in-house photometrics. |
| **Office & Contract Furniture** | `31.01` | **5,449,376 units** (+18.9% vs. 2024) | **3.40 billion PLN** (Division 31 total: 50.21B PLN) | #2 global exporter (€16.2B export, PAIH); Meble Polska (71 buyer nations). |
| **Insulated Cables & Optical Fibers** | `27.32` | **545,916 tonnes** (147k t fiber optic cables) | **12.06 billion PLN** (Division 27.3: 19.17B PLN) | Major production hubs (TF Kable, optical fiber cable manufacturing). |

---

## 5. Ranked Candidate Opportunities

Candidates are strictly evaluated as **distribution, agency, or import positions** (not manufacturing), screened against `drafts/edge-inventory.md`, and passed through the A2 Dutch and AI 2030 gates.

### 1. Architectural Aluminium & High-Performance Joinery Systems (HS 7610 / HS 3925)

Exclusive agency and project distribution for Polish architectural aluminium fabricators supplying Dutch commercial and modular builders.
Demand: NL imports of HS 7610 from Poland surged from €77,867,541 in 2023 to €148,271,001 in 2025 (+90.4%); HS 3925 reached €241,935,803 (+28.0%). Poland exported €3.9B in joinery (2024, PAIH); GUS reports 10.89M plastic and 592k aluminium window/door units produced in 2025.
Edge: Polish language accesses fabricators directly; regulatory literacy navigates CPR EN 14351-1, CE execution classes, and Dutch 2024 Wkb technical dossier mandates; engineering habit automates U-value/BENG compliance trails.
Gates: A2 Pass (commercial contractors accept English; partner facade erectors handle on-site Dutch). AI Pass (physical building envelopes and energy retrofits cannot be digitized).
First test: Broker a €30,000 custom window package for a Dutch modular project with complete Wkb dossier for a 10% fee.
Kill fact: Dutch contractor insurer or VMRG mandate strictly requiring local KOMO-certified assembly partners.

### 2. Commercial & Industrial Smart LED Luminaires (HS 9405)

Value-added distribution and project specification for Polish commercial/industrial LED luminaires targeting Dutch logistics warehouses, greenhouses, and retrofit real estate.
Demand: NL imports of HS 9405 from Poland were €146,540,815 (2023) and €146,707,897 (2025). GUS 2025 lighting sold production was 4.99 billion PLN. Fluorescent bans drive massive retrofit demand across Dutch installation contractors (Fedet/NLA).
Edge: Polish technical liaison with factory photometric labs; regulatory literacy audits Ecodesign/EPREL, WEEE/LightRec, and CRA rules for smart DALI controllers; 30k LinkedIn audience reaches facility directors.
Gates: A2 Pass (technical procurement with Dutch electrical installers is English-ready). AI Pass (physical lighting required in every building; AI building automation boosts smart DALI luminaire demand).
First test: Supply a €15,000 luminaire pilot with DIALux photometrics for a logistics hall retrofit.
Kill fact: Major Dutch installers refuse to order outside existing wholesaler accounts (Technische Unie/Rexel).

### 3. CRA-Compliant Industrial IoT Gateways & Edge Networking (HS 8517 / HS 8471 / HS 8473)

Authorized EU Importer and technical distributor for non-EU or Polish industrial IoT gateways, DIN-rail edge computers, and rugged network appliances.
Demand: NL imports of HS 8517 from Poland jumped from €116,736,637 in 2023 to €276,670,635 in 2025 (+137.0%); Extra-EU imports reached €32,299,288,278. HS 8473 grew +21.8% to €153,285,015.
Edge: Regulatory literacy masters Cyber Resilience Act (CRA (EU) 2024/2847) mandatory importer liability, CE, and RED; engineering habit audits firmware SBOM and CVE processes; English/Russian/Polish bridges hardware makers.
Gates: A2 Pass (Dutch automation engineers and systems integrators operate in English). AI Pass (edge AI and sensor data collection drive rugged hardware demand).
First test: Contract a €5,000 CRA technical file audit and importer-of-record retainer for one manufacturer.
Kill fact: Manufacturer firmware contains unmaintained open-source components incapable of meeting CRA vulnerability-remediation standards.

### 4. Engineered Structural Steel Subassemblies & Solar/Agri-Racking (HS 7308 / HS 7326)

Procurement agency and quality-assurance distribution for Polish EN 1090-certified structural steel fabricators supplying Dutch solar mounting, logistics mezzanines, and greenhouse infrastructure.
Demand: NL imports of HS 7308 from Poland expanded from €134,178,660 in 2023 to €160,013,376 in 2025 (+19.3%); HS 7326 rose to €116,475,536 (+23.1%). GUS recorded 30.92 billion PLN in structural metal production (2025).
Edge: Polish coordinates directly with Silesian fabricators; regulatory literacy verifies CPR EN 1090 EXC2/EXC3, 3.1 material certs, and CBAM carbon accounting; engineering habit checks CAD/CAM weld tolerances.
Gates: A2 Pass (Dutch solar EPCs and structural project managers negotiate in English). AI Pass (load-bearing steel structures for energy transition cannot be digitized).
First test: Broker a €25,000 trial order of solar racking beams with 3.1 test certs for 7% commission.
Kill fact: Road freight surcharges and steel price swings eliminate the 25% Polish fabrication discount.

### 5. Acoustic Meeting Pods & Ergonomic Contract Workstations (HS 9401 / HS 9403)

Exclusive Dutch agency for Polish acoustic meeting pods and ergonomic contract workstations supplying commercial office project-furnishers.
Demand: Polish furniture exports reached €16.2B (2024, PAIH). GUS data shows Polish office furniture production rose +18.9% in 2025 to 5.45M units (sold value 3.40B PLN). Combined NL imports of HS 9401 and 9403 from Poland totaled €683,228,385 in 2025.
Edge: Polish secures exclusive agency terms; regulatory literacy manages EUDR deforestation tracing, PPWR, and ESPR/DPP; 30k LinkedIn audience drives corporate tenant inbound leads.
Gates: A2 Pass (Dutch commercial workplace dealers and facility heads operate in English). AI Pass (acoustic isolation for remote work is human-centric physical infrastructure).
First test: Place two demo acoustic pods in a Dutch co-working space on a 60-day paid pilot with purchase option (<€20k).
Kill fact: Major Dutch fit-out dealers remain locked into framework agreements with Nordic incumbent brands.

---

## 6. Honest Appraisal: Did This Instrument Find Anything a Dutch Founder Could Not?

The macro trade data found no secret consumer product: high-value trade flows are dominated by multinational captive supply chains (Dell, automakers, oil majors). A Dutch founder with local networks can easily buy wholesale. What this instrument isolated that a Dutch founder cannot easily replicate is cross-border regulatory arbitrage. By combining native Polish/CEE supplier access with direct mastery of technical EU legislation—specifically the 2024 Dutch Wkb construction dossier mandate, CPR EN 1090 execution classes, and the September 2026 Cyber Resilience Act (CRA)—it identifies five B2B niches where mid-sized manufacturers have strong production capacity but are blocked by compliance complexity. The moat is not sourcing; it is technical file liability and bilingual engineering operations.
