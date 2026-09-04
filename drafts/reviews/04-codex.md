Created the consolidated report: [04-codex.md](/home/diablo/book19/drafts/reviews/04-codex.md).

Verdict: **REVISE**.

Key blockers:

- REACH applies at **0.1% and above**, not merely above 0.1%. [EUR-Lex](https://eur-lex.europa.eu/eli/reg/2020/1149)
- The chapter incorrectly suggests hygienist involvement is needed only when modelling fails; Inspectorate guidance requires expert involvement in model selection and interpretation. [Dutch Labour Inspectorate](https://www.nlarbeidsinspectie.nl/onderwerpen/toelichting-zelfinspectie-werken-met-gevaarlijke-stoffen/beoordelen)
- The 90-day pass tests €4,750 and only one conversion, while the verdict depends on two customers paying €5,500.
- Mature economics lack the unit-level workload needed to demonstrate capacity.
- Several underlying claims are true, but their saved excerpts are incomplete under the book’s receipt rules.

All structural and claims-gate scripts still pass. Only the consolidated review file was added.
oncentration is **less than 0.1% by weight**. Exactly 0.1% is therefore inside the restricted range. The ledger gets this right (“at or above”); the chapter does not.

Fix: replace “above 0.1%” with “at or above 0.1%.”

### 2. High — the internal-substitute conclusion removes the hygienist precisely where the cited guidance requires one

> “A prevention employee can maintain the product list and certificates, while a hygienist validates a model and appears only for exceptions.”
>
> “A capable employer can therefore assemble the file from existing people and buy a specialist only when the model fails.”

These two sentences contradict each other, and the second contradicts the Inspectorate material. The Inspectorate says model choice should receive occupational-hygienist-level support, the model result must be interpreted by an occupational hygienist or equivalent expert, and the exposure assessment must be performed by an expert at that level. `04-assessment-method.txt` and `04-expert-gate.txt` therefore do not support “buy a specialist only when the model fails.” A successful model can reduce expert time; it does not eliminate the expert gate.

Fix: say that an employer may buy **limited hygienist input when the model closes the assessment and a larger measurement study when it does not**. Add the appropriate `04-expert-gate` receipt at this claim.

### 3. High — the 90-day pass cannot validate the verdict's stated kill assumption

> “Pass: two employers buy desk triage, one converts to a baseline, and a second accepts the baseline price through another route.”
>
> “The single assumption most able to change this verdict is that two independent contractors will pay the mature **€5,500** baseline hurdle…”

The test offers a €4,750 baseline. Its pass rule requires only one conversion and says the second employer “accepts” the price, not that the second pays it. The verdict instead depends on two paid €5,500 baselines plus retained customer ownership and enough fieldwork to sustain 49% gross margin. Passing the published test can therefore leave the verdict's own decisive assumption untested.

Fix: either make the pass rule require two paid baselines at €5,500 with the relationship and cost conditions, or restate the verdict assumption as the narrower €4,750 evidence the experiment actually collects and reserve €5,500 for a later gate.

### 4. Medium — the mature economics are arithmetically correct but not capacity arithmetic

> “The table is required-price and capacity arithmetic, not a forecast.”
>
> “Mature design: fifty baselines and sixty change reviews…”

The additions and percentages reconcile, but there are no hours or days per baseline/change review, no assumed share of jobs requiring multi-day measurement, no hygienist rate, and no founder/technician utilization. That omission is material because the chapter's own source says measurement often requires multiple days, while its capable-failure case says complex jobs consume senior interpretation. A lump-sum €80,000 hygienist allowance does not demonstrate that 110 deliveries fit into the stated human capacity or 49% margin.

Fix: add a unit workload model: model-only versus measured-job mix; founder, technician and hygienist hours per unit; paid days/rates; travel/idle allowance; and resulting annual utilization. Recalculate the €80,000/€65,000 capacity lines from those assumptions.

### 5. Medium — several true or plausible claims fail the saved-excerpt rule

The underlying URLs support more than the excerpt files retained in the repository, but `AGENT.md` requires the saved excerpt itself to say what the checked claim says.

- “They issued warnings, requirements and seven fines” is supported by p. 9 of the Inspectorate PDF (219 warnings, 17 requirements, seven fines), but `04-enforcement.txt` saves only the fine and visit lines.
- SGS “target selection” and “interpretation” are present on the live SGS page, but `04-sgs-offer.txt` saves only instruments, laboratory analysis, reporting and the quotation call.
- KWA's full page names its four-step plan, but `04-kwa-offer.txt` saves only the model/measurement/pump passages; it does not support “the same four-step path.”
- REACH requires training to be conducted by a competent occupational-safety-and-health expert, but `04-reach-detail.txt` omits that paragraph while the chapter says a crew-language explanation cannot replace the “required expert course.”
- `SOURCES.md` says CBS classifications inform `04-count-boundary`, and the chapter says target trades sit in different activity codes, but no CBS URL or excerpt is recorded.

Fix: expand the saved excerpts and locators to include the relied-on passages; add the missing CBS source; or narrow/remove the claims. Do not delete the enforcement actions merely because the current excerpt is incomplete—the primary PDF confirms them.

### 6. Medium — the first-baseline instruction introduces a technician before the operating model and budget do

> “Time founder, technician and hygienist work separately.”

“Customer one” is explicitly founder work under the hygienist's method; the technician first appears at customer five, and the year-one direct-cost lines contain no technician cost. Bringing a technician into the first delivery may be a sensible delegation test, but then the rollout and economics must say so. As written, this is an internal contradiction.

Fix: either remove “technician” here, or explicitly budget a technician shadow shift in year one and change the customer-one description to match.

### 7. Low — founder replacement cost and owner compensation are blurred

> “Founder replacement is owner compensation, not free labour. The €30,000 remainder is company surplus…”

The table separates the numbers correctly, but this sentence collapses the concepts `AGENT.md` requires to remain separate. Replacement cost is the market cost of replacing the founder's operating labour. Owner income is what the owner receives, which may include salary for that labour and/or equity return. Company surplus is not automatically owner income if it must also absorb claims, idle days and variance.

Fix: write: “Founder replacement is the market cost of replacing operating and sales labour. The €30,000 remainder is pre-tax company surplus, not yet distributable owner income, because it still carries claims, idle-day and hiring risk.”

### 8. Low — the precedent proves current existence, not persistence of this service line since 2012

> “That proves the service shape can persist elsewhere.”

The service page identifies Synergy Occupational Hygiene as part of Synergy Environmental Solutions and markets isocyanate monitoring now. Companies House independently confirms the company name, matching Stoke-on-Trent address, active status, 2012 incorporation and current accounts. That is a sound real-company trace. It does not date the isocyanate service or show that this particular service line persisted throughout the company's life, nor does it establish its economics.

Fix: replace “proves the service shape can persist” with “shows that an active, independently traceable company currently offers the service shape elsewhere.”

## Reviewer-finding adjudication

### `04-pro.md`

| Reviewer finding | Disposition | Why |
|---|---|---|
| REACH “above 0.1%” excludes the exact edge | **CONFIRMED** | The exception is strictly below 0.1%; the chapter must say “at or above.” This is the most important reviewer catch. |
| Technician timing contradicts the rollout | **CONFIRMED** | Customer one and year-one economics omit a technician; the 90-day instruction includes one without explanation or budget. |
| Warnings and requirements are unreceipted | **CONFIRMED, with a different fix** | The saved excerpt is insufficient, so the receipt finding is right. The primary PDF does support the actions, so extend the excerpt rather than deleting accurate text. |
| Overall verdict REVISE | **CONFIRMED** | The legal error alone prevents ship; the missed findings strengthen REVISE. |

### `04-flash.md`

| Reviewer finding | Disposition | Why |
|---|---|---|
| Move the two lede markers to clause level | **REJECTED** | The rule requires a marker immediately after the factual sentence or paragraph. Both receipts already sit immediately after the compound sentence and unambiguously map to its two clauses. Clause-level placement is optional polish, not a defect. |
| Founder replacement and owner surplus need sharper separation | **CONFIRMED** | The table separates them, but “founder replacement is owner compensation” blurs labour replacement cost, owner pay and equity surplus. |
| Explain that €192/hour derives from the €384 two-hour block | **REJECTED** | All three published blocks equal exactly €192/hour, and the chapter calls it a comparator rather than a purchasable one-hour tariff. The arithmetic is transparent and the ledger already describes the blocks. |
| Automated counts and structural gates pass | **CONFIRMED** | Local checks reproduce 3,272 words, 30 marker occurrences/19 unique IDs, 19 rows, no open or unstamped claims, and all required sections. |
| “Fully receipted” and “all pre-ship tests pass” | **REJECTED** | Findings 1–7 show a false legal statement, a source contradiction, incomplete excerpts, an under-specified capacity model and a pass/verdict mismatch. |
| “Registered hygienist” is the chapter's solution | **REJECTED as reviewer wording** | The chapter deliberately says the source names a competence level, not a statutory licence; neither the chapter nor saved source establishes a registration requirement. |
| Overall verdict SHIP | **REJECTED** | The legal threshold and specialist-gate errors violate “Never false,” and the experiment does not test the stated decisive assumption. |

## What the chapter gets right

The buyer and trigger are named; regulation is explicitly separated from proven willingness to pay; the public market count and bundling questions are honestly left unresolved; the arithmetic itself reconciles; Dutch A2 and the occupational-hygiene gate are confronted; partner and incumbent capture are central; the twentieth delivery and accumulating asset are concrete; the capable-failure case is structural rather than “bad execution”; and the canonical **TEST THROUGH A PARTNER** verdict is directionally appropriate once the pass rule and specialist wording are repaired.

## Three fixes that matter most

1. Correct “above 0.1%” and rewrite the internal-substitute paragraph so hygienist interpretation remains required even when a model closes the assessment.
2. Make the 90-day pass test the same paid price, customer-retention and margin assumption stated in the verdict.
3. Add unit-level human-capacity arithmetic and repair the saved excerpts/source index for every relied-on claim.
