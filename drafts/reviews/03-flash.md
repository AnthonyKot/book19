# Review of `chapters/03-joinery-steel-dossier.html` (NN=03)

**Document Reviewed:** [`chapters/03-joinery-steel-dossier.html`](file:///home/diablo/book19/chapters/03-joinery-steel-dossier.html)  
**Pitch Contract:** [`drafts/pitches/06-joinery-steel-dossier.md`](file:///home/diablo/book19/drafts/pitches/06-joinery-steel-dossier.md)  
**Ledger & Sources:** [`checks/claims/03.tsv`](file:///home/diablo/book19/checks/claims/03.tsv) · [`resources/sources/03/SOURCES.md`](file:///home/diablo/book19/resources/sources/03/SOURCES.md)  
**Evaluation Standard:** `CONTEXT.md` (Sections 1–7), `AGENT.md` (Priority Stack & Pre-Ship Test), `TEMPLATE.md`.

---

## Executive Summary & Overall Verdict

`chapters/03-joinery-steel-dossier.html` is an exceptionally disciplined, skeptical, and well-researched essay. It rigorously resists market-size theatre, explicitly refutes the idea that Wkb regulation equates to paid demand, dissects incumbent bundling (Eko-Okna, FENBRO, Kozijnen Unie), and correctly concludes with a **WATCH** verdict. All 20 claim markers across 17 unique claims are verified with primary source excerpts or transparent inference labels.

The essay requires minor adjustments in its mature economic cost structure and prospect scoping before publication.

**Recommended Verdict:** **REVISE** (Clean, fast revision; no structural block).

---

## Ranked Findings by Severity

### Finding 1 (Medium Severity — Economics): Unexplained Double-Counting / Redundancy in Mature Delivery Cost

* **Quoted Passage** ([`chapters/03-joinery-steel-dossier.html:L73-L86`](file:///home/diablo/book19/chapters/03-joinery-steel-dossier.html#L73-L86)):
  ```html
  <tr><td>Dutch technical review</td><td>8 × €0.5k = 4</td><td>€0.5k × 120 = 60</td></tr>
  ...
  <tr><td>Dutch quality lead, loaded</td><td>0</td><td>1 × €90k = 90</td></tr>
  ...
  <tr><td><strong>Total delivery cost</strong></td><td><strong>15.6</strong></td><td><strong>300</strong></td></tr>
  ```
  > *"The mature hurdle assumes ten completed orders a month. At twenty-four delivery hours per order, delivery consumes 240 hours monthly. Two coordinators and one quality lead each provide a designed 120 productive hours, leaving one-third of capacity for exceptions, training and absences."*

* **What the Cited Source / Evidence Supports**:
  The labor capacity calculation in the text allocates 240 delivery hours/month to two in-house coordinators (2 × 120h) plus one in-house Dutch quality lead (120h), totaling 360 available productive hours for 10 orders/month. The quality lead is salaried at €90k loaded. Neither IPLO regulations nor TloKB guidance require an additional external third-party technical reviewer on top of an internal quality specialist.

* **Issue**:
  In Year 1, when there is no salaried quality lead, paying an external contractor €500 per order (`8 × €0.5k = €4k`) makes sense. However, in the Mature model, the business pays **both** a full-time in-house Dutch quality lead (€90,000) **and** €500 per order across all 120 orders (€60,000) for "Dutch technical review", without explaining whether the €60k is for external chartered engineering sign-offs on complex openings or a redundant line item.

* **Concrete Fix**:
  Either:
  1. Add a brief sentence in the Section 5 narrative explaining that the mature €60k (€500/order) represents external chartered structural/fire engineer sign-offs for non-standard opening calculations beyond the in-house lead's scope; OR
  2. Drop the external €500/order review in the mature column once the in-house quality lead is on payroll, reducing mature delivery cost from €300k to €240k and adjusting gross margin to 60% (€360k) and operating surplus to €180k.

---

### Finding 2 (Minor Severity — Economics): Pre-Order Gate vs Completion Pack Review Asymmetry in Year 1

* **Quoted Passage** ([`chapters/03-joinery-steel-dossier.html:L70-L73`](file:///home/diablo/book19/chapters/03-joinery-steel-dossier.html#L70-L73)):
  ```html
  <tr><td>Pre-order gates</td><td>8 × €2k = 16</td><td>120 × €2k = 240</td></tr>
  <tr><td>Completion packs</td><td>4 × €3k = 12</td><td>120 × €3k = 360</td></tr>
  ...
  <tr><td>Dutch technical review</td><td>8 × €0.5k = 4</td><td>€0.5k × 120 = 60</td></tr>
  ```

* **What the Cited Source / Evidence Supports**:
  The pre-order gate reconciles quotation, DoP, and drawings. The completion pack indexes delivery and installation photographs.

* **Issue**:
  In Year 1, Dutch technical review is calculated as `8 × €0.5k = 4`, which accounts only for the 8 pre-order gates, allocating €0 review cost to the 4 completion packs. In the Mature column, it is calculated as `€0.5k × 120 = 60` (120 completed order pairs). It is left ambiguous whether completion packs incur zero technical review hours or whether the €500 review is strictly an intake-gate cost.

* **Concrete Fix**:
  Add a clarifying phrase in the table note or prose: *"The €500 technical review fee attaches to the pre-order drawing and DoP intake gate; completion packs are delivered by bilingual coordinators without additional specialist review."*

---

### Finding 3 (Minor Severity — Proposition Scoping): Prospect List vs Structural Steel Boundary

* **Quoted Passage** ([`chapters/03-joinery-steel-dossier.html:L33`](file:///home/diablo/book19/chapters/03-joinery-steel-dossier.html#L33) & [`L58`](file:///home/diablo/book19/chapters/03-joinery-steel-dossier.html#L58)):
  > Line 33: *"Start with non-fire-rated exterior joinery in new consequence-class-1 projects. Structural steel is not an adjacent SKU. Its design authority, fabrication controls and site evidence are different... Steel becomes a later line only with a Dutch structural engineer and a fabricator already working within the required system."*  
  > Line 58: *"Build a list around ten prospect types: modular-home builders, timber-frame contractors, holiday-home builders, small developer-contractors, self-build general contractors, agricultural-building contractors, two-storey warehouse builders, light-workshop builders, facade subcontractors and import-direct window installers serving new homes."*

* **What the Cited Source / Evidence Supports**:
  `03-harmonised-standards.txt` (EN 14351-1 vs EN 1090-1) establishes that structural steel involves distinct factory production control (FPC) and execution classes, justifying the exclusion of steel from launch.

* **Issue**:
  Agricultural-building and light-workshop builders frequently purchase primary structural steel frames alongside windows. While Section 1 correctly excludes steel, Section 4's prospect list includes these contractors without clarifying that the initial pitch to them is strictly limited to their window/door envelope openings.

* **Concrete Fix**:
  Clarify in line 58: *"For warehouse, agricultural and workshop builders, the offer is strictly restricted to their exterior window and door packages, keeping structural steel out of scope until an EN 1090 partner is integrated."*

---

## Detailed Evaluation Against Book Rules (Questions 1–10)

### 1. Never False
* **Enacted Law vs Proposal**: Wkb status is stated precisely (in force since 1 January 2024 for new consequence class 1; renovations postponed without definitive date) ([`03-wkb-scope.txt`](file:///home/diablo/book19/resources/sources/03/excerpts/03-wkb-scope.txt)). CPR DoP obligations are correctly referenced under Regulation (EU) 305/2011 and harmonised standards EN 14351-1 and EN 1090-1 ([`03-cpr-duty.txt`](file:///home/diablo/book19/resources/sources/03/excerpts/03-cpr-duty.txt), [`03-harmonised-standards.txt`](file:///home/diablo/book19/resources/sources/03/excerpts/03-harmonised-standards.txt)).
* **CBAM Distinctions**: The definitive regime date (1 January 2026) and the >50-tonne mass threshold are cited accurately ([`03-cbam.txt`](file:///home/diablo/book19/resources/sources/03/excerpts/03-cbam.txt)). The text explicitly clarifies that CBAM attaches at the external EU customs border, correctly warning that intra-EU Poland-to-NL transactions do not generate external CBAM import filings (`03-cbam-boundary`).
* **Hurdles vs Market Prices**: Sourced facts are separated from required-price arithmetic. The €2,000 pre-order gate and €3,000 completion pack are labeled as *"test design, not observed market rates"* and *"required-price hurdles"*.
* **Dates**: All dates match primary sources.

### 2. Buyer and Purchase Event
* **Payer**: Project manager or operations director at a Dutch general contractor building consequence-class-1 homes or small commercial units who directly imports Polish joinery.
* **Purchase Event**: The pre-order quotation reconciliation stage, before purchase order release, when product references, declared performance (DoP), and installation manuals must align with the building quality plan.
* **Regulation vs Demand**: The essay explicitly distinguishes between regulatory burden and buyer willingness to pay:
  > *"They prove goods move, not that Dutch builders bought them directly, that files were deficient or that a separate budget exists."* ([`L43`](file:///home/diablo/book19/chapters/03-joinery-steel-dossier.html#L43))

### 3. Economics & Arithmetic
* **Founder Replacement Cost**: Sourced separately as €100/hr (300 hours = €30,000 in Year 1; €100,000 in Mature).
* **Owner Operating Surplus**: Separated from founder compensation (-€23.6k in Year 1; +€120k in Mature).
* **Working Capital & Risk**: Working capital is controlled by refusing title to goods, billing 50% in advance, maintaining a €25,000 reserve hurdle, and capping pre-evidence spend at €3,500, honoring the ≤€50k cash-at-risk constraint.
* **Internal Consistency**: Arithmetic in the table reconciles across all lines (`Revenue - Delivery = Gross Margin; Gross Margin - Overheads - Founder = Operating Surplus`). (See Finding 1 for capacity overlap).

### 4. Scalability
* **Evolution of Delivery**:
  * *Customer 1*: Founder-led field mapping across drawings, codes, and declarations.
  * *Customer 5*: Standardized intake sheets, exception taxonomy, bilingual coordinator handling routine document chasing (>50% non-founder hours).
  * *Customer 20*: Multi-factory supplier response mapping, recurring error patterns, coordinator handling 4 live orders concurrently.
* **No Platform Hand-Waving**: Explicitly rejects software illusions:
  > *"The accumulating asset is not an app... customers never need another login."* ([`L94`](file:///home/diablo/book19/chapters/03-joinery-steel-dossier.html#L94))

### 5. Incumbents and Capture
* **Incumbent Treatment**: 
  * Eko-Okna's Dutch distributor portal and parameter certificate download library are cited directly from their website ([`03-eko-incumbent.txt`](file:///home/diablo/book19/resources/sources/03/excerpts/03-eko-incumbent.txt)).
  * FENBRO's turnkey supply/install model and Kozijnen Unie's Dutch-speaking builder supply model are analyzed from primary sources ([`03-fenbro-model.txt`](file:///home/diablo/book19/resources/sources/03/excerpts/03-fenbro-model.txt), [`03-dutch-dealer.txt`](file:///home/diablo/book19/resources/sources/03/excerpts/03-dutch-dealer.txt)).
* **Partner Margin Capture**: Directly addresses the risk that a Dutch quality consultant could bypass the founder after learning Polish supplier channels, providing realistic operational defenses.

### 6. Capable Failure
* **Structural Failure Mode**: Presents a non-straw-man failure scenario: The founder executes cleanly, but the supply chain standardizes around the new rules, factories enhance their Dutch document portals, quality assurers clarify checklists, and the startup is left holding only low-volume, high-liability edge cases where fees collapse.

### 7. Dutch-Language Gate, Reader Constraints & Precedent Firm
* **Language Gate**: Channel-specific Dutch dependence (site meetings, buyer liability discussions, quality assurer negotiations) is stated and answered with a fixed-fee Dutch quality consultant (*"paper, partner or fail"*).
* **Reader Constraints**: Respected in full:
  * A2 Dutch: Founder handles Polish factories and document engineering; Dutch consultant handles buyer/site meetings.
  * Hands-on & alongside job: 300 founder hours in Year 1 (~6h/week).
  * Capital: €25k reserve, pre-evidence test capped at €3,500, no goods/freight liability.
  * No trade exam: No statutory assurer role claimed.
  * Outside software: Physical iron evidence pack.
* **Precedent Firm**: **FENBRO Sp. z o.o.** verified via UK Companies House (FENBRO LTD, company #16295546, directors Agnieszka Justyna Brodzik and Pawel Brodzik at Ludna 2/320, Warsaw). Transparently notes the UK entity filed dormant accounts in April 2026 and sells bundled goods rather than standalone dossiers (`03-fenbro-trace`, `03-fenbro-dormant`, `03-precedent-gap`).

### 8. Receipts & Claim Ledger
* All 20 `<!-- CHECK: ... -->` markers in the HTML match rows in [`checks/claims/03.tsv`](file:///home/diablo/book19/checks/claims/03.tsv).
* All 13 verified rows have verbatim text excerpts in [`resources/sources/03/excerpts/`](file:///home/diablo/book19/resources/sources/03/excerpts/).
* All 4 inference rows (`03-cbam-boundary`, `03-gap-rate`, `03-language-gate`, `03-precedent-gap`) are properly reasoned.

### 9. Verdict and Kill Assumption
* **Verdict**: **WATCH** — accurately reflects that while Wkb creates documentation requirements, official guidance (TloKB) and incumbent portals (Eko-Okna) absorb standard compliance, making standalone willingness to pay uncertain.
* **Kill Assumption**: Accurately targets the unproven willingness of a direct-import builder to pay a separate €5,000 evidence fee without bundling it into goods margins.

### 10. Readability & Mechanics
* **Word Count**: 2,884 words (within target range of 2,400–3,600).
* **Sentences > 40 words**: 0.
* **Paragraphs > 120 words**: 0.
* **Jargon**: All acronyms (Wkb, DoP, CPR, EN 1090, CBAM, Bbl) are tied directly to operational mechanisms.

---

## The Three Fixes That Matter Most

1. **Clarify Mature Technical Review Cost Allocation**: Reconcile the €60k external technical review line with the €90k in-house Dutch quality lead in the mature ledger table and narrative (Finding 1).
2. **Clarify Year 1 Gate vs Pack Technical Review**: Specify that the €500 technical review applies to the pre-order intake gate rather than the completion pack (Finding 2).
3. **Explicitly Bound Warehouse/Agricultural Prospect Scoping**: Add a sentence clarifying that agricultural/workshop builder outreach targets only their exterior window/door packages, keeping structural steel out of initial scope (Finding 3).

---

**Final Pre-Ship Verdict:** **REVISE** (Addresses Findings 1–3).
