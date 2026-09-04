**Verdict: REVISE — the thesis survives, but the debt model and several evidence receipts are not yet fit to ship.**

# Consolidated review: Chapter 05

The structural and automated checks pass: 3,117 words, 21 markers covering 16 ledger rows, no open or unstamped claims. Those checks establish completeness, not semantic support.

## Reviewer-finding audit

| Reviewer finding | Disposition | Assessment |
|---|---|---|
| Flash 1 — personal-guarantee headroom | **REJECTED** | The chapter already says the €40k equity plus €10k costs exhausts the €50k limit, permits “no further personal recourse,” and requires total cash plus recourse to remain within €50k. The reviewer’s assertion that lenders “almost never” waive a guarantee is absent from the supplied sources. Qredits says it *asks* directors to sign one; neither excerpt states its amount or waiver frequency. |
| Flash 2 — mature debt-service ambiguity | **CONFIRMED** | The model never defines when “mature” occurs or how the €100k seller-note principal is retired. See Finding 1 below. The reviewer’s proposed repayment schedule is itself unsourced and should be labelled a design hurdle. |
| Flash 3 — mandatory conformity checks in the diagnostic | **UNVERIFIABLE** | None of Chapter 05’s sources supports the reviewer’s CPR, REACH, CLP, PED, CBAM or EN 10204 claims. The categories are also broader than the regulated subsets cited. The chapter already excludes regulated categories without specialist review. This may be a useful operational enhancement, but it is not an evidence-backed defect in this review packet. |
| Flash 4 — mandatory 20%/50% customer thresholds | **REJECTED** | Brookz supports only that customer spread affects valuation. It does not support the proposed thresholds, and the checklist does not require arbitrary universal cut-offs. |
| Flash 5 — missing previous/next links | **REJECTED** | Although `TEMPLATE.md` describes previous/contents/next navigation, the chapter-specific drafting brief expressly instructed authors to retain the two placeholder spans. Every current essay follows that instruction. |
| Pro 1 — false Hammond receipt | **CONFIRMED, but narrowed** | The marker does not support “sector knowledge,” and the earlier paragraph contains additional unsupported precedent descriptions. The reviewer is wrong that institutional support is absent: the excerpt explicitly says Shawbrook supported the transaction. See Finding 3. |
| Pro 2 — undated ABN expectation | **CONFIRMED, low severity** | “Within ten years” needs its December 2025 survey anchor. This is temporal ambiguity rather than a false statistic. |
| Pro 3 — verdict must explicitly say provisional | **REJECTED** | The chapter uses one exact permitted verdict, as required. It repeatedly conditions action on paid, lender and target-record gates and says passing authorises diligence, not a bid. Replacing the verdict with “TEST NOW (PROVISIONAL ACQUIRE)” would violate the exact-verdict rule. |

## Ranked findings

### 1. High — The model never repays the €100,000 seller-note principal

> “Senior-debt stress: €160k, 9.95%, 60 months” appears as €40.7k in both Year 1 and “Mature”; only €5k of seller-note interest is charged.

> “It leaves the €100,000 seller principal unpaid…”

The [KVK excerpt](/home/diablo/book19/resources/sources/05/excerpts/05-seller-finance.txt) gives an illustrative structure in which seller-note repayment begins after the five-year bank loan. It does not supply a maturity, rate or amortisation schedule for this deal.

The table’s arithmetic is correct for the rows shown, but it is not complete acquisition economics. “Mature” could mean years 2–5, after year 5, or an indefinitely refinanced state. Calling €74.3k owner residual without showing the seller principal risks counting cash needed to retire acquisition debt as owner wealth.

**Fix:** Model at least two explicit phases: senior-loan years and seller-note-repayment years. State seller-note interest, maturity, whether interest is paid or accrued, annual principal service, and resulting owner cash. Keep every invented term labelled as a design hurdle.

### 2. High — Replacement labour and owner income are not actually separated

> “Founder labour at replacement cost — €90,000.”

> “The year-one owner receives the €90,000 replacement-cost compensation hurdle and owns the €30,300 residual. That reaches the income objective on paper.”

No source is needed for a labelled hurdle, but the meaning must be internally clear. If €90k is the company’s loaded employment cost, the owner does not receive €90k. If it is gross salary, employer costs are missing. The €30.3k residual is also pre-tax and potentially needed for seller-note principal. Finally, the “income objective” is never stated.

This contradicts the book’s requirement to distinguish replacement labour from owner income even though the table visually separates two rows.

**Fix:** Define the €90k as either gross salary or total employer cost and show the other amount. State the owner-income target explicitly. Label the residual pre-tax and show what remains distributable after the seller-principal reserve.

### 3. Medium — The Hammond precedent is materially over-described

> “Search-fund entrepreneur Jim Ward became chief executive…”

> “It proves the operating shape: an outside CEO, lender-backed succession…”

> “The acquirer had sector knowledge and institutional support.” `<!-- CHECK: 05-precedent-deal -->`

The [Shawbrook excerpt](/home/diablo/book19/resources/sources/05/excerpts/05-precedent-deal.txt) supports:

- Euston Ventures acquired Hammond Chemicals;
- Jim Ward became CEO;
- third-generation family members remained in leadership;
- Shawbrook supported the transaction;
- Hammond blended, packaged and distributed industrial solvents.

It does **not** establish that Ward was a search-fund entrepreneur, that he was an outsider, that succession motivated the transaction, or that the acquirer had sector knowledge. The [Companies House excerpt](/home/diablo/book19/resources/sources/05/excerpts/05-precedent-trace.txt) proves only the firm’s existence, age, active status and SIC code. The Pro reviewer caught only the last paragraph and incorrectly denied the supported Shawbrook involvement.

**Fix:** Delete the unsupported characterisations or add dedicated ledger rows and excerpts. Rewrite “proves” as “illustrates, according to the lender’s case study,” because the independent trace does not verify the transaction structure.

### 4. Medium — A Qredits marker is being used to receipt negative evidence it does not record

> “It does not publish an approval formula for this first-time buyer or promise ten years for an acquisition.” `<!-- CHECK: 05-qredits-terms -->`

The [Qredits excerpt](/home/diablo/book19/resources/sources/05/excerpts/05-qredits-terms.txt) supports the published amount, rate, fee, repayment choices, average and maximum terms, acquisition use, and individual assessment. The `05-qredits-terms` ledger row does not claim that the site was exhaustively checked for an absent formula or acquisition-specific ten-year promise.

**Fix:** Move these negative claims under `05-public-record-limit`, or create a dedicated inference row stating exactly what the reviewed public record did not settle.

### 5. Medium — The €4,800 experiment may sit outside the stated €50,000 risk cap

> “Lender fees, due diligence and transaction work have a separate €10,000 hurdle. Cash committed is €50,000…”

> “Total pre-evidence spend is capped at €4,800.”

It is unclear whether the €4,800 is included in the €10,000 transaction-cost allocation or precedes it. Some items—travel, translation and sourcing samples—are not obviously acquisition transaction costs. If additional, maximum first-year cash at risk becomes €54,800 before accounting for diagnostic revenue.

**Fix:** State that all ninety-day spending is debited from the €10k non-equity allowance, leaving at most €5,200 for later lender, diligence and closing costs. Otherwise reduce the closing equity or cost budget.

### 6. Low — The succession horizon needs a survey date

> “In an ABN AMRO/Ipsos I&O survey of 519 entrepreneurs, 68% expected to stop steering within ten years.”

The source is ABN AMRO’s December 2025 report. Without that anchor, “within ten years” has no visible starting point.

**Fix:** Begin: “In a December 2025 ABN AMRO/Ipsos I&O survey…”

### 7. Low — The wholesale-age excerpt is not self-contained

> “5,210 owners aged 65 or older … or 15.7% of owners of firms with at least two working people.”

The [saved excerpt](/home/diablo/book19/resources/sources/05/excerpts/05-wholesale-age.txt) contains the table title, the “two or more working people” qualification, and the row `5.210 15,7`, but omits the column heading that identifies `15,7` as a percentage and its denominator.

**Fix:** Extend the saved excerpt to include the table’s column headings. The prose need not change if those headings confirm the ledger wording.

## Areas that pass

- The buyer, signer, acquisition event, sourcing-test payer and purchase triggers are explicit.
- Demand evidence is properly distinguished from regulation, budgets and completed deals.
- The capable-failure case is credible and not disguised poor execution.
- The first/fifth/twentieth-customer progression identifies delegated work and accumulating assets.
- Incumbent, strategic-buyer, lender, employee and customer capture risks receive a fair turn.
- The Dutch A2 gate and the requirement to leave the software job at closing are explicit.
- Readability passes: no substantive prose sentence exceeds 40 words, and paragraph density is controlled.
- `checked-by:codex:2026-09-05` is valid under the live claims gate and chapter drafting brief, despite the older status wording in `AGENT.md`.

## Three fixes that matter most

1. Add a complete, time-phased repayment model for both senior debt and seller principal.
2. Define loaded CEO cost, owner pay, taxes/reserves and the actual owner-income target.
3. Repair the semantic receipts for Hammond and Qredits, then add the missing table header to the wholesale-age excerpt.
