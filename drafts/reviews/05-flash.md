# Editorial & Evidence Review: Chapter 05 — Owner-Independent Acquisition

**Target File:** [`chapters/05-owner-independent-acquisition.html`](file:///home/diablo/book19/chapters/05-owner-independent-acquisition.html)  
**Pitch Contract:** [`drafts/pitches/03-owner-independent-acquisition.md`](file:///home/diablo/book19/drafts/pitches/03-owner-independent-acquisition.md)  
**Claim Ledger:** [`checks/claims/05.tsv`](file:///home/diablo/book19/checks/claims/05.tsv)  
**Source Index:** [`resources/sources/05/SOURCES.md`](file:///home/diablo/book19/resources/sources/05/SOURCES.md)  
**Review Standard:** `CONTEXT.md` (Sections 1–7), `AGENT.md` (Priority Stack & Pre-Ship Test), and the 10 core editorial gates.

---

## Executive Summary & Final Verdict

**Verdict:** **REVISE**

The essay is an exceptionally disciplined, analytically rigorous chapter that strictly adheres to the book's core philosophy:
- **Separation of money:** Founder replacement labour (€90k/€95k), working capital reserves (€20k/€30k), and owner return (€30.3k/€74.3k) are strictly segregated.
- **Evidence integrity:** All 21 claim markers (16 unique ledger rows) are 100% verified against primary sources or declared as honest inferences.
- **Capable failure:** The counter-case in `div.counter` presents a legitimate working-capital/overtrading failure mode rather than a straw-man "poor execution" excuse.
- **Readability:** Zero sentences exceed 35 words (well below the 40-word limit), the lede is 101 words (under the 130-word cap), and total length is 3,117 words (within the 2,400–3,600 target).

However, **REVISE** is required to resolve three key operational and economic points: (1) making explicit that the €50k cash commitment leaves exactly €0 headroom for personal guarantees under Dutch banking/Qredits practice, (2) clarifying the mature debt-service transition from senior bank annuity to seller-note principal amortisation, and (3) adding regulatory/technical verification (CE/DoP, REACH) to the CEE sourcing diagnostic.

---

## Ranked Findings by Severity

### Finding 1 (Severity: High) — Personal Guarantee Headroom vs. Hard €50k Risk Cap
* **Category:** Reader Constraints & Economic Feasibility (`AGENT.md` §1 & Priority 1/3)
* **Quoted Passage:**
  > *(Lines 64–65)*: "Qredits' currently linked MKB conditions add the critical term. All business assets serve as collateral. When the borrower is a legal person, Qredits asks its directors to sign a guarantee for joint liability. A full €160,000 personal guarantee would put €210,000 at risk after the €50,000 cash commitment. That fails the confirmed risk cap. The Qredits route survives only if the signed offer limits total personal recourse to the remaining headroom."
  > *(Line 122)*: "Pass: one distributor pays €750, and a lender gives a written €160,000 path that keeps total buyer cash and personal recourse within €50,000."
* **What the Source Supports:** 
  - `05-qredits-security.txt` (Article 6.4): Qredits mandates a personal guarantee (*borgtochtovereenkomst voor hoofdelijke aansprakelijkheid*) from directors of legal entities.
  - `05-bmkb.txt`: BMKB provides a 67.5% state guarantee to the lender, but lenders still standardly require director *borgtocht in privé* for residual loss.
* **Problem:** The reader's hard constraint is **≤€50,000 total capital at risk in year one**. The model commits **€40,000 equity cash + €10,000 transaction/diligence cash = €50,000 cash**. Therefore, the "remaining headroom" for any personal guarantee (*borgtocht*) is **€0**. Dutch commercial banks and Qredits almost never extend a €160k acquisition loan to a first-time individual MBI sponsor without *any* director guarantee. 
* **Concrete Fix:** State unequivocally that because the €50,000 cash budget is fully committed on closing (€40k equity + €10k transaction fees), any lender requirement for an unbacked personal guarantee is an immediate **kill event**. The pass rule must require either an explicit non-recourse senior facility, a personal guarantee capped strictly at €0 beyond paid-in equity, or a restructured stack where senior debt is reduced and seller subordinated financing increased.

---

### Finding 2 (Severity: Medium) — Debt-Service Amortisation in the "Mature Hurdle"
* **Category:** Economic Model Consistency (`AGENT.md` Priority 3)
* **Quoted Passage:**
  > *(Lines 78–81, Ledger Table)*:
  > | €000 | Year 1 hurdle | Mature hurdle |
  > | :--- | :--- | :--- |
  > | **Senior-debt stress: €160k, 9.95%, 60 months** | **40.7** | **40.7** |
  > | **Seller-note interest hurdle** | **5** | **5** |
  > | **Surplus after debt and reserves** | **30.3** | **74.3** |
* **What the Source Supports:** 
  - `05-qredits-terms.txt`: 60-month term (5 years) at 9.95% linear/annuity.
  - `05-seller-finance.txt`: KVK example of subordinated seller note repaid *after* bank debt is extinguished.
* **Problem:** The senior debt is a 60-month (5-year) facility with annual debt service of €40,747. In the "Mature hurdle" column, maintaining the exact row label `Senior-debt stress: €160k, 9.95%, 60 months | 40.7` is ambiguous:
  - If "Mature" represents Year 3–4 (within the initial 5-year loan), senior debt is still running at €40.7k.
  - If "Mature" represents Year 6+ (post-senior payoff), senior bank debt is €0, but the €100k seller note principal must now be amortised (e.g. at ~€25k–€35k/year over 3–4 years).
* **Concrete Fix:** Add a parenthetical clarification in the table row or prose: 
  *Change label to:* `Debt-service stress: senior annuity (Y1–5) / seller-note principal amortisation (mature)`. Explain in paragraph 84 that maintaining a ~€40.7k debt-service line in the mature case funds the retirement of the €100k seller note principal once the senior bank loan is extinguished.

---

### Finding 3 (Severity: Medium) — Technical & Regulatory Verification in the Sourcing Diagnostic
* **Category:** Never False & Operational Diligence (`AGENT.md` Priority 1 & 2)
* **Quoted Passage:**
  > *(Lines 53–54)*: "The ten prospect types are distributors of industrial fasteners, bearings and seals, workshop consumables, packaging materials, industrial hose, workwear, cleaning chemistry, adhesives, water-treatment spares and material-handling parts... The offer is a €750 fixed-fee sourcing diagnostic... It covers one named item family, three qualified CEE suppliers, landed-cost comparison, sample coordination and one buyer-approved order route. The existing distributor remains importer and seller of record... The reader supplies no legal opinion and touches no regulated category without specialist review."
* **What the Source Supports:** 
  - General B2B wholesale mechanics; EU product conformity rules (CPR, REACH, CLP, PED, CBAM).
* **Problem:** Several of the 10 named categories (e.g., structural fasteners, industrial cleaning chemicals, industrial hoses, water-treatment spares) are subject to mandatory EU product regulations (CE/DoP under CPR, REACH/CLP safety data sheets, CBAM reporting for iron/steel). Even though the distributor is the importer of record, a sourcing diagnostic that qualifies CEE suppliers without verifying standard manufacturer conformity documentation (e.g., ISO/EN material test certificates 3.1, SDS, CE/DoP) will deliver unviable suppliers that fail the distributor's incoming quality/customs checks.
* **Concrete Fix:** In Section 4, explicitly specify that the diagnostic's "supplier qualification" includes verifying the manufacturer's technical dossier and conformity documentation (e.g., CE mark, Declaration of Performance, REACH/CLP SDS, or EN 10204 3.1 certificates) so the Dutch importer of record can legally accept the product.

---

### Finding 4 (Severity: Minor) — Pre-NDA Customer Concentration Rejection Threshold
* **Category:** Due Diligence Rules (`AGENT.md` §5 & Pre-ship Test)
* **Quoted Passage:**
  > *(Line 57)*: "Send a one-page buy box to accountants, BuyInside, Brookz advisers and owners in the ten categories. Ask for three facts before signing an NDA: staff excluding the seller, percentage of gross profit from the largest five customers, and who approves exceptions when the seller is absent. A listing without those answers is a lead, not an opportunity."
* **What the Source Supports:** 
  - `05-valuation.txt`: Brookz H1-2026 names owner dependence and customer spread (*klantenspreiding*) as primary valuation and deal-breaking factors.
* **Problem:** The text specifies asking for the gross profit percentage of the top 5 customers, but unlike the operational exception test (which has a strict pass/fail criterion), it does not give the reader a hard numerical pass/fail threshold for customer concentration before proceeding.
* **Concrete Fix:** Add an explicit threshold: *"Reject any target where a single customer represents >20% of gross profit, or where the top five customers represent >50%."*

---

### Finding 5 (Severity: Minor) — Chapter Navigation Links
* **Category:** Template Compliance (`TEMPLATE.md` § Navigation)
* **Quoted Passage:**
  > *(Lines 145–149)*:
  > ```html
  > <nav class="chapter-nav" aria-label="Essay navigation">
  >   <span></span>
  >   <a href="../index.html">Contents</a>
  >   <span></span>
  > </nav>
  > ```
* **What the Source Supports:** `TEMPLATE.md` requires: `Navigation: previous / contents / next.`
* **Problem:** The previous and next navigation links are empty placeholder spans instead of linking to `04-spray-crew-file.html` and `06-certified-inspection-microfirm.html`.
* **Concrete Fix:** Replace empty `<span></span>` elements with:
  `<a href="04-spray-crew-file.html">Previous: Spray crew</a>` and `<a href="06-certified-inspection-microfirm.html">Next: Certified inspection</a>`.

---

## Detailed Audit Across the 10 Review Dimensions

### 1. Never False
* **Enacted Law vs. Proposal:** Passed. The chapter does not present any regulation or proposal as compulsory demand. Section 2 explicitly affirms: *"There is no new rule and no compliance deadline. No owner is obliged to sell, no lender is obliged to finance, and no customer has budget because succession exists."*
* **Expectation vs. Deadline:** Passed. The ABN AMRO / Ipsos I&O survey finding (68% expect to step down within 10 years) is properly framed as demographic seller sentiment, not a guaranteed transaction pipeline.
* **Design Hurdle vs. Market Price:** Passed. All non-quoted amounts (€750 diagnostic, €300k acquisition hurdle, €90k replacement CEO labour, €96k pre-debt cash requirement, 1.5× DSCR) are consistently labeled as design hurdles.
* **Source Date Verification:** All dates and figures match primary sources:
  - ABN AMRO Bedrijfsopvolging: December 2025 (`05-succession-demand.txt`, `05-wholesale-age.txt`).
  - CBS StatLine 81156: 2024 full-year wholesale dataset (`05-wholesale-margin.txt`).
  - Brookz Overname Barometer: H1-2026 (`05-valuation.txt`).
  - Qredits Terms & General Conditions: Deposited November 2021, checked September 2024 (`05-qredits-terms.txt`, `05-qredits-security.txt`).
  - RVO BMKB Conditions: Checked August 2024 (`05-bmkb.txt`).

---

### 2. Buyer and Event
* **The 90-Day Test (Diagnostic):**
  - **Payer:** Owner or Purchasing Manager of a Dutch B2B distributor in one of 10 named categories.
  - **Purchase Event:** Stock-out, primary supplier failure, margin compression on a product family, or customer request outside standard catalog.
  - **Deliverable:** €750 fixed-fee diagnostic covering 1 item family, 3 qualified CEE suppliers, landed cost schedule, and sample routing.
* **The Step-Two Path (Acquisition):**
  - **Payer:** The reader (as incoming owner-operator).
  - **Seller:** Retiring founder (65+ years old) without family/staff successors.
  - **Purchase Event:** Succession window closing; founder unwilling to liquidate or unable to attract private equity / strategic consolidators.
  - **Substitute:** For reader: keep developer job. For seller: trade sale to competitor, MBO by staff, liquidation.

---

### 3. Economics & Arithmetic
* **Cash Flow Separation:** Strictly separates:
  1. Replacement-cost founder labour: **€90,000** (Year 1) / **€95,000** (Mature).
  2. Working capital reinvestment: **€20,000** (Year 1) / **€30,000** (Mature).
  3. Owner residual return: **€30,300** (Year 1) / **€74,300** (Mature).
* **Arithmetic Consistency Audit:**

| Metric | Stated Year 1 | Verified Calculation | Stated Mature | Verified Calculation | Status |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Revenue** | €1,600.0k | — | €2,000.0k | — | Exact |
| **COGS (69%)** | €1,104.0k | $1,600 \times 0.69 = 1,104.0$ | €1,380.0k | $2,000 \times 0.69 = 1,380.0$ | Exact |
| **Gross Profit (31%)** | €496.0k | $1,600 - 1,104 = 496.0$ | €620.0k | $2,000 - 1,380 = 620.0$ | Exact |
| **Operating Expenses** | €400.0k | $180 + 110 + 90 + 20 = 400.0$ | €470.0k | $225 + 125 + 95 + 25 = 470.0$ | Exact |
| **Cash Before Debt** | €96.0k | $496.0 - 400.0 = 96.0$ | €150.0k | $620.0 - 470.0 = 150.0$ | Exact |
| **Senior Debt Stress** | €40.7k | Annuity (€160k, 9.95%, 60mo) = €40,747.11/yr | €40.7k | €40,747.11/yr | Exact |
| **Seller Note Interest** | €5.0k | $100k \times 5.0\% = 5.0$ | €5.0k | $100k \times 5.0\% = 5.0$ | Exact |
| **Working Capital Res.** | €20.0k | — | €30.0k | — | Exact |
| **Surplus Residual** | **€30.3k** | $96.0 - 40.747 - 5.0 - 20.0 = 30.253$ | **€74.3k** | $150.0 - 40.747 - 5.0 - 30.0 = 74.253$ | Exact |

* **Pre-Evidence 90-Day Spend:**
  $€600 \text{ (travel/Dutch)} + €1,200 \text{ (samples/checks)} + €1,500 \text{ (normalisation workbook)} + €1,500 \text{ (counsel)} = \mathbf{€4,800}$ (strictly within the ≤€5,000 limit).

---

### 4. Scalability
* **Customer Progression:**
  - **1st Delivery:** Pure transfer exercise; Dutch account owner leads client contact; founder documents every exception, quoting quirk, and delivery requirement.
  - **5th Delivery:** Landed-cost quoting template active; supplier specs and defect logs standardised; warehouse and admin handle routine orders without founder.
  - **20th Delivery:** Repeatable niche catalog; delegated replenishment, invoice matching, and quoting; founder focuses strictly on capital allocation, CEE supplier contracts, and exception resolution.
* **Platform Magic Word Check:** Passed. The word "platform" is never used to explain scaling; scaling is earned through documented item data, supplier credit, approved ranges, and warehouse routines.

---

### 5. Incumbents and Capture
* **Competitor Treatment:**
  - **BuyInside:** Cited fairly from primary marketing copy (15-year specialist MBI search, matchmaking, and advisory platform).
  - **Brookz:** Cited from primary marketplace listings and H1-2026 Overname Barometer.
  - **Strategic Consolidators / MBO:** Explicitly acknowledges that strategic buyers can pay higher multiples by eliminating duplicated back-office/warehouse overhead.
* **Margin-Capture Confrontation:** Directly addresses margin capture risks from:
  1. *Seller:* Demanding goodwill premiums (countered by contingent earn-outs and walk-away price).
  2. *Lender:* Fixed debt claims draining cash (countered by 1.5× DSCR hurdle).
  3. *Account Owner:* Demanding extortionate retention terms post-close (countered by pre-closing employment agreements).
  4. *Customers:* Demanding price cuts during ownership transition (countered by account owner retention and reference calls).

---

### 6. Capable Failure
* **Failure Mechanism:** The scenario in `div.counter` describes a textbook physical distribution failure:
  1. Good execution increases sales and brings in cheaper CEE product.
  2. CEE supplier requires larger batch minimum order quantities (MOQs), trapping cash in 8 weeks of inventory.
  3. Larger Dutch B2B customers demand 60–90 day payment terms in exchange for volume.
  4. Working capital expands faster than operating cash flow, while fixed bank debt amortisation (€3,395/month) continues unabated.
  5. The business experiences a cash crunch despite rising accounting profits.
* **Assessment:** Non-straw-man, highly credible operating failure that directly tests the working-capital dynamics of physical trade.

---

### 7. Language Dependence, Reader Constraints & Precedent
* **Dutch Language Gate:**
  - Diagnosed accurately: A2 Dutch is insufficient for hostile customer calls, employee management, or price negotiation.
  - Solution: Retaining the existing Dutch commercial account manager under contract prior to closing.
  - Test Phase: Sourcing diagnostic executed with export-oriented distributors in English/Polish; Dutch commercial freelancer hired at fixed cost only if requested.
* **Reader Constraints:**
  - *Hands-on:* Yes, transitions to full-time owner-operator on closing day.
  - *Beside the job at first:* Yes, search and €750 diagnostic run alongside enterprise developer job.
  - *Capital ceiling:* €100k net worth, €50k cash committed at closing (€40k equity + €10k fees).
  - *No trade exam:* B2B consumable distribution requires no statutory trade qualifications.
  - *Outside software:* Physical trading business; internal software tools used solely for inventory/costing.
* **Precedent Firm & Trace:**
  - **Company:** Hammond Chemicals Limited.
  - **Transaction:** Euston Ventures MBI acquisition; Jim Ward installed as outside CEO; 3rd generation Hammond family retained in leadership (`05-precedent-deal.txt`).
  - **Independent Trace:** Companies House UK Company 00964829, incorporated 27 Oct 1969, SIC 46750 Wholesale of chemical products (`05-precedent-trace.txt`).

---

### 8. Receipts & Claim Ledger Verification Table

Every `<!-- CHECK: id -->` marker in `05-owner-independent-acquisition.html` traces exactly to a verified row in `checks/claims/05.tsv`:

| Claim ID | Type | Cited Primary Source | Excerpt File / Locator | Summary of Claim vs. Source Support |
| :--- | :--- | :--- | :--- | :--- |
| `05-succession-demand` | Checked | ABN AMRO Sector Report (Dec 2025) | `excerpts/05-succession-demand.txt` | Survey of 519 entrepreneurs: 68% stop steering ≤10 yrs, 22% not started, 20% search without successor. |
| `05-wholesale-age` | Checked | ABN AMRO / CBS Data Table | `excerpts/05-wholesale-age.txt` | 5,210 wholesale/trade owners aged 65+ (15.7% of firms with ≥2 persons). |
| `05-marketplace` | Checked | Brookz Marketplace Snapshot | `excerpts/05-marketplace.txt` | 95 wholesale listings displayed live on Brookz. |
| `05-wholesale-margin` | Checked | CBS StatLine 81156 (2024) | `excerpts/05-wholesale-margin.txt` | SBI 46 revenue €648.435bn, pre-tax €34.481bn (5.3% aggregate margin). |
| `05-language-gate` | Inference | Operating Design Analysis | Proposition-specific inference | A2 Dutch is commercially insufficient for top accounts; account lead retention is mandatory. |
| `05-precedent-deal` | Checked | Shawbrook Bank Case Study | `excerpts/05-precedent-deal.txt` | Euston Ventures acquired Hammond Chemicals; CEO Jim Ward installed, family retained. |
| `05-precedent-trace` | Checked | UK Companies House (00964829) | `excerpts/05-precedent-trace.txt` | Hammond Chemicals Ltd active, inc. 1969, SIC 46750 (Wholesale of chemical products). |
| `05-qredits-terms` | Checked | Qredits MKB Krediet Product Page | `excerpts/05-qredits-terms.txt` | €50k–€250k, 9.95% rate, 1.5% fee, 5–10 yr term, includes business acquisition. |
| `05-qredits-security` | Checked | Qredits MKB General Conditions | `excerpts/05-qredits-security.txt` | Art 6.4 & 11.1: all business assets pledged; director joint liability guarantee required. |
| `05-bmkb` | Checked | RVO BMKB Conditions Page | `excerpts/05-bmkb.txt` | Starter <3 yrs, max loan €333,333, 67.5% state collateral guarantee. |
| `05-public-record-limit` | Inference | Legal/Underwriting Analysis | Evidence boundary inference | Public terms do not prove individual credit approval, recourse waivers, or target EBITDA. |
| `05-seller-finance` | Checked | KVK Bedrijfsovername Guide | `excerpts/05-seller-finance.txt` | Stacked finance mechanics; subordinated seller loan repaid after senior bank debt. |
| `05-diligence` | Checked | KVK Stappenplan Overname | `excerpts/05-diligence.txt` | Due diligence checks on financials, employee salaries/hours, and customer willingness to transfer. |
| `05-ai-line` | Inference | Technical Automation Analysis | AI gate inference | AI streamlines clerical matching/quoting but cannot replace physical inspection, packing, or client repair. |
| `05-buyinside` | Checked | BuyInside Platform Website | `excerpts/05-buyinside.txt` | MBI candidate profiling, deal search, and advisory focused on external succession for 15 yrs. |
| `05-valuation` | Checked | Brookz Overname Barometer H1-2026 | `excerpts/05-valuation.txt` | Survey of 291 M&A advisers: 3.6× EBITDA for €200k EBITDA, 19% deals fail over valuation gaps. |

---

### 9. Verdict & Kill Assumption
* **Stated Verdict:** `<p class="verdict">ACQUIRE, DO NOT BUILD</p>`
* **Verdict Soundness:** Fully earned. Building a B2B distributor from scratch requires creating supplier relationships, credit terms, warehouse operations, and Dutch customer trust with A2 language skills—a near-impossible task under €50k. Buying transfers these existing assets below replacement cost.
* **Kill Criteria:**
  1. Zero paid €750 diagnostics after 10 qualified distributor pitches.
  2. Lender insists on personal guarantee exposure exceeding the €50k total risk cap.
  3. All evaluated targets exhibit irremediable owner dependence on the departing seller.

---

### 10. Readability & Structure
* **Word Count:** 3,117 visible words (passes 2,400–3,600 target).
* **Lede Length:** 101 words (passes ≤130 words limit).
* **Sentence Length Audit:** Maximum sentence length across the essay is **32 words** (passes the ≤40-word rule).
* **Paragraph Density:** All paragraphs are concise (range 35–105 words); zero wall paragraphs.
* **Jargon Clarity:** Terms such as *working-capital peg*, *subordinated note*, *annuity*, *MBI*, and *BMKB* are immediately accompanied by their practical operational or cash mechanisms.

---

## The Three Fixes That Matter Most

1. **Explicit Personal Guarantee Cap in the Pass/Kill Rule (Finding 1):**
   Update lines 64–65 and line 122 to state clearly that because the buyer invests €50,000 cash at closing (€40k equity + €10k fees), there is **€0 remaining headroom** for a director personal guarantee (*borgtocht*). A lender requirement for an unbacked personal guarantee beyond paid-in equity is an automatic kill event.
2. **Clarify Mature Debt Service Allocation (Finding 2):**
   Update the ledger table (line 78) and paragraph 84 to explain that the ~€40.7k annual debt service line in the "Mature hurdle" represents either Year 3–4 debt service or the cash required to amortise the €100k seller note principal once the 5-year senior bank loan is paid off.
3. **Add Conformity/Compliance Verification to Sourcing Diagnostic (Finding 3):**
   Update Section 4 (lines 53–54) to specify that the €750 diagnostic includes verifying manufacturer technical and regulatory compliance dossiers (e.g., CE/DoP, REACH/CLP SDS, or EN 10204 3.1 material certificates) so the Dutch distributor's statutory importer obligations are satisfied.
