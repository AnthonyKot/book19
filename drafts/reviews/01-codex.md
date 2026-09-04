**Verdict: REVISE.**

Consolidated adversarial review written to [drafts/reviews/01-codex.md](/home/diablo/book19/drafts/reviews/01-codex.md).

Main blockers are the misaligned 90-day pass rule, unreproducible/overstated receipts, and incomplete working-capital modelling. Every numbered reviewer finding is marked CONFIRMED or REJECTED with reasons. No chapter files were changed.
he verdict

> “The single assumption that would most change the verdict is that two independent integrators will pay the mature €5,500 hurdle...” (`chapters/01-cell-file.html:121`)
>
> “Pass: two integrators buy desk diagnostics, one converts to a paid site challenge, and one offers a second cell at the mature price.” (`chapters/01-cell-file.html:115`)

The verdict depends on **two independent integrators paying €5,500**, but the pass rule requires only two €1,250 desk purchases, one €4,500 conversion, and a second-cell “offer” from one of them. It can therefore pass with only one integrator buying site work, with nobody paying €5,500, and without proving the two-channel demand needed by the mature model. This contradicts the chapter's own verdict paragraph and `AGENT.md`'s requirement for a priced pass and kill rule. No external source resolves this; these are the chapter's own design conditions.

**Fix:** require deposits or signed paid orders from two unrelated integrators for the same bounded site scope at €5,500, or weaken the verdict paragraph to the smaller fact actually tested. Replace “offers a second cell” with an unambiguous paid commitment.

### 2. High — MISSED BY BOTH: `01-price-boundary` is not reproducible from the chapter's source package

> “The named Dutch integrator and safety-bureau pages reviewed here publish scope but no cell-file price. `<!-- CHECK: 01-price-boundary -->`” (`chapters/01-cell-file.html:63`)

The TSV says this inference spans “Pilz, Yaskawa, D-SC, Olmia and IAB pages,” but supplies only the Pilz URL. `resources/sources/01/SOURCES.md` records Pilz and IAB, not the D-SC or Olmia URLs on which the negative search result expressly relies. There is no excerpt or audit note showing what pages and price fields were checked. Pilz supports only that Pilz markets a broad service scope; it cannot support the wider absence-of-price claim by itself. Under `AGENT.md`, every relied-on URL must be in the source index. As packaged, the cross-provider claim is **UNVERIFIABLE**.

**Fix:** add every relied-on provider URL, access date, and a concise saved record of the price search to `SOURCES.md` and the locator; otherwise narrow the prose and ledger claim to the providers actually receipted. Keep the caveat that absence of a public price does not exclude a private quote.

### 3. High — MISSED BY BOTH: the precedent receipt overclaims the saved excerpt, and the conclusion overclaims Companies House

> “Its site sells cobot risk assessments, force-and-pressure testing and CE/UKCA support. `<!-- CHECK: 01-precedent-offer -->`”
>
> “That proves a small specialist can persist on the shape.” (`chapters/01-cell-file.html:53`)

`excerpts/01-precedent-offer.txt` supports calibrated force/pressure testing and documentation supporting CE/UKCA marking. It does **not** say the firm sells cobot risk assessments. The live page discusses risk assessment as a safety requirement, but the supplied excerpt still fails the rule that the saved passage must say what a checked row says. `excerpts/01-precedent-trace.txt` establishes an active company, incorporation in 2019, recent accounts/confirmation statement, and an engineering-consultancy SIC code. It does not establish revenue, continuous sale of this offer, headcount, or commercial viability. Thus it proves legal continuity plus a current-looking offer, not that the specialist business model has “persisted.”

**Fix:** save the firm's actual risk-assessment offer page if one exists and split the ledger claim by service. Rewrite the conclusion as: “This independently confirms that an active small engineering consultancy currently markets part of the shape; it does not establish revenue, tenure of the offer, Dutch prices or demand.”

### 4. Medium — Flash finding 1: CONFIRMED; Pro finding 1: CONFIRMED — the lede's single marker supports neither the whole sentence nor its breadth

> “Dutch integrators already prepare the risk assessment and CE package, and the manufacturer must carry the declaration. `<!-- CHECK: 01-nooteboom -->`” (`chapters/01-cell-file.html:25`)

`excerpts/01-nooteboom.txt` supports **one Dutch case** in which a system integrator handled installation, RI&E, technical dossier, CE marking and delivery. It does not support the general plural “Dutch integrators,” and it does not state the legal declaration duty. That duty is supported separately by `excerpts/01-regulation-duties.txt`. Both reviewers caught the compound-source mismatch, but neither caught the generalisation from one case.

**Fix:** write: “At least one Dutch welding-cobot case shows the integrator preparing the risk assessment, technical dossier and CE marking. `<!-- CHECK: 01-nooteboom -->` The manufacturer remains responsible for the declaration. `<!-- CHECK: 01-regulation-duties -->`”

### 5. Medium — Pro finding 3: CONFIRMED — the payment schedule contradicts the later test wording

> “The integrator pays 50% before the desk review and the balance before the site date.” (`chapters/01-cell-file.html:60`)
>
> “offer the €1,250 desk diagnostic ... 50% in advance. Credit it into the €4,500 site challenge.” (`chapters/01-cell-file.html:111`)

The first passage can naturally mean 50% of the €4,500 total (€2,250) before the desk review; the second means 50% of the €1,250 diagnostic (€625). The chapter therefore has two materially different cash schedules. This matters to both buyer friction and the working-capital claim. No source is involved: it is internal design arithmetic.

**Fix:** state exact invoices and dates—for example, €625 at booking, €625 on desk-review delivery, and €3,250 before the site visit—or explicitly choose 50% of the whole engagement upfront.

### 6. Medium — MISSED BY BOTH: the IAB comparator omits its own staleness warning

> “IAB publishes €6,000 for CE work on a simple machine and about €30,000 for a machinery assembly...” (`chapters/01-cell-file.html:63`)

`excerpts/01-incumbent-price.txt` reproduces those figures, so the numbers are quoted correctly. But the [live IAB page](https://iab-ingenieurs.nl/vraag-en-antwoord/ce-markering-machines/machinerichtlijn-ce-markering-machines/wat-zijn-de-kosten-van-een-ce-markering/) warns that posts may be outdated and gives no visible publication date; the saved excerpt omits that warning. The chapter calls the numbers broad anchors, which helps, but later uses them as the only published price evidence around a current €3,000 kill threshold. The source supports an undated published example, not a current market comparator.

**Fix:** include the warning in the excerpt and call the amounts “undated, potentially stale published examples.” Do not use them to validate the €5,500 hurdle; the live two-provider quotes in the 90-day test must do that.

### 7. Medium — MISSED BY BOTH: working capital is asserted, not modelled separately

> “Working capital is light only if the boundary holds.”
>
> “The year-one cash-at-risk hurdle is €15,000...” (`chapters/01-cell-file.html:78`)

The table separates revenue, direct cost, founder replacement labour, overhead and surplus, but it has no working-capital line or timing bridge. “Cash at risk” is not the same measure: the prose does not reconcile the €15,000 to deposits, VAT, receivables, contractor timing or the mature year's €127,000 of direct cost. This fails `AGENT.md`'s requirement to keep working capital separate even though the advance-billing policy plausibly reduces it.

**Fix:** add a small cash bridge for year one and the mature model: invoice milestones, collection days, VAT treatment, supplier/contractor payment dates, peak cash need, contingency, and distributable owner income after that reserve.

### 8. Medium — MISSED BY BOTH: the claim stamps are future-dated and the written status contract disagrees with the gate

As of this review date, 2026-09-04, all 16 sourced rows are stamped `checked-by:codex:2026-09-05`—a verification date in the future. The gate checks only the date's shape, so these rows pass despite impossible chronology. Separately, `AGENT.md` permits only `verified`, `inference`, or `open`, while the executable gates in `checks/claims.py` and `checks/structure.py` explicitly accept—and in the former case require—the `checked-by` form. Thus Flash's statement that there are “16 verified rows” is inaccurate as written, although the automated gate passes all 19 rows.

**Fix:** correct the stamps to the actual verification date, make the gate reject future dates, and have the coordinating agent update `AGENT.md` to document stamped verification (or change the tooling and ledger together). Do not mechanically change the TSV to bare `verified`: the current claim gate treats that as unreviewed and fails it.

### 9. Low — MISSED BY BOTH: the English-training receipt establishes an old offer, not current availability

> “An English-language machinery-safety course is commercially available in the Netherlands...” (`chapters/01-cell-file.html:52`)

`excerpts/01-english-training.txt` says the course “can also be given” in English, but the [source page](https://www.verwey-safety.nl/kennis/nieuws/item/19-training-machinery-safety-and-ce-marking) is dated 24 October 2017. A still-live old announcement does not verify present commercial availability in 2026. It also does not establish course duration, though the chapter does not state one.

**Fix:** obtain a current course page or written provider confirmation with language, duration, dates and price; until then say that a Dutch provider historically advertised English delivery.

## Reviewer findings rejected

### Flash finding 2 — REJECTED

The reviewer says “Founder replacement is below gross margin, as owner compensation rather than free labour” blurs labour pay and owner return. Read with the next sentence—“The €34,000 remainder is company surplus, not additional salary”—the chapter does distinguish replacement-cost labour from equity surplus. The wording can be polished, but it is not an accounting conflation. The actual economics defect is the absent working-capital bridge in finding 7.

### Flash finding 3 — REJECTED

The mature figures are internally consistent rounding to the nearest thousand: €306.25k becomes €306k; minus €127k is €179.25k, shown as €179k; minus €145k is €34.25k, shown as €34k. The displayed 59% is also correct when rounded. An explicit rounding note is optional polish, not a finding.

### Flash finding 4 — REJECTED

The cited prospect-list sentence is 39 words by the reviewer's own count. The checklist asks for sentences **over** 40 words, so being near the threshold is not a defect. The paragraph remains readable.

### Pro finding 2 — REJECTED AS STATED

The claim that “named ... pages reviewed here” is false merely because D-SC and Olmia do not appear in the reader-facing prose does not follow: “here” can refer to the essay's research record, and the TSV locator does name those firms. The real problem is more serious and different: their URLs and evidence are absent from `resources/sources/01/`, making the inference unreproducible (finding 2).

## What survives adversarial review

- The Machinery Regulation application date, manufacturer duties, Article 18 boundary, PLD application date, and prospective Dutch implementation date match the supplied excerpts; the chapter correctly separates enacted EU law from expected Dutch commencement.
- The buyer, commissioning event and substitutes are named, and the chapter openly treats willingness to pay as unproven rather than turning regulation into demand.
- The customer-one/five/twenty progression and capable-failure case are concrete. The partner-learning/capture mechanism is credible and not “poor execution” in disguise.
- The Dutch-language boundary is explicit: the partner owns operator interviews, Dutch instructions and the declaration, or the job fails qualification.
- `TEST THROUGH A PARTNER` is the right provisional verdict if—and only if—the revised experiment tests payment by two independent integrators at the mature scope and price.

## The three fixes that matter most

1. Align the 90-day pass rule with the verdict: two unrelated integrators must make paid €5,500 commitments for the same bounded site scope.
2. Repair the receipts: fully source the negative price search, narrow the Nooteboom generalisation, and split/narrow the precedent claims.
3. Make cash legible: choose one exact invoice schedule and add a year-one and mature working-capital bridge before calling the €34k surplus owner income.
