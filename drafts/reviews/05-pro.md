Here is the review of `05-owner-independent-acquisition.html` against the project's rules (CONTEXT.md and AGENT.md), ranked by severity.

### 1. High Severity: Receipt Violation (Rule 8)
**Rule:** Receipts: every CHECK marker's row supports the sentence it follows; every verified row has an excerpt that says what the claim says.
**Quote:** "It does not prove affordability. The transaction price and cash flow were not public in the sources used here, and the acquirer had sector knowledge and institutional support. `<!-- CHECK: 05-precedent-deal -->`"
**What the source actually supports:** The `05-precedent-deal` claim in the TSV and the corresponding excerpt (`05-precedent-deal.txt`) only establish that Euston Ventures acquired Hammond Chemicals, Jim Ward became CEO, and the family remained in leadership. They contain no information about the transaction price being withheld, cash flow, or the acquirer's sector knowledge and institutional support. Reusing the marker here creates a false receipt.
**Concrete fix:** Remove the `<!-- CHECK: 05-precedent-deal -->` marker from this sentence entirely, as it is an authorial observation about what the source *lacks*. Alternatively, replace it with a new marker (e.g., `<!-- CHECK: 05-precedent-limits -->`) and add an inference row to `05.tsv` acknowledging that the source omits financial details and that Euston operates as an institutional acquirer.

### 2. Medium Severity: Missing Date for Past Expectation (Rule 1)
**Rule:** Never false: is any proposal presented as enacted law, expectation as deadline... Check dates against the cited primary sources.
**Quote:** "In an ABN AMRO/Ipsos I&O survey of 519 entrepreneurs, 68% expected to stop steering within ten years."
**What the source actually supports:** The excerpt (`05-succession-demand.txt`) supports the numbers, but the URL and provenance note show it was pulled from `sectorprognoses-abn-amro-bedrijfsopvolging-dec-2025.pdf`. Later in the essay, the Brookz survey is explicitly dated "H1-2026", but the ABN AMRO survey is presented without a date. This risks presenting a late-2025 expectation as fully current to September 2026.
**Concrete fix:** Add the date to the sentence to ground the expectation: "In a December 2025 ABN AMRO/Ipsos I&O survey of 519 entrepreneurs..."

### 3. Low Severity: Verdict Provisional Status (CONTEXT.md Section 7)
**Rule:** Common verdict (from book 18): Exactly one per essay... Provisional until customer payment exists.
**Quote:** `<p class="verdict">ACQUIRE, DO NOT BUILD</p>`
**What the source actually supports:** The structural logic of the essay earns the thesis that one should acquire rather than build to inherit supplier credit and trust. However, the evidence rules explicitly state that verdicts are "Provisional until customer payment exists." The essay accurately describes a 90-day test to prove a buyer will pay €750 and a lender will cap risk, acknowledging that the current demographic data "does not prove transferable cash flow." Presenting the verdict as absolute skips the required provisional status.
**Concrete fix:** Explicitly mark the verdict as provisional in the HTML. Either change the tag to `<p class="verdict">TEST NOW (PROVISIONAL ACQUIRE)</p>` or add a sentence immediately below it stating: "This verdict is provisional until a distributor pays the €750 diagnostic fee and a lender clears the risk cap."

***

### Verdict: REVISE

The model's arithmetic is airtight, the "capable failure" (growth breaking the working capital cycle) is exceptionally well-argued, and the constraints (the strict €50k risk cap against standard bank joint liability) are handled perfectly as a pass/fail experiment gate. The essay simply needs its receipts cleaned up.

**The three fixes that matter most:**
1. **Fix the false receipt:** Remove the reused `05-precedent-deal` marker from the sentence about affordability/institutional support, or add a dedicated inference row to the TSV to cover it.
2. **Date the demographic expectation:** Insert "December 2025" into the ABN AMRO survey mention so the timeline is honest.
3. **Respect the provisional rule:** Note in the verdict box that "Acquire" remains provisional pending the €750 test and the lender's risk-cap waiver.
