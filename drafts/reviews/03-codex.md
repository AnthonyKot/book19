**Verdict: REVISE — the thesis can stand, but the evidence ledger, central source characterizations, experiment design, and economic narrative are not yet shippable.**

# Reviewer adjudication

| Reviewer finding | Decision | Why |
|---|---|---|
| Flash 1: mature Dutch review and quality-lead costs are double-counted | **CONFIRMED, narrowly** | The two costs may represent different work, so double-counting is not proved. However, the model never explains why it needs both €60k of per-order review and a €90k quality lead. The reviewer’s suggested structural/fire-engineer explanation is invented and conflicts with the launch scope. |
| Flash 2: completion packs receive no Year-1 technical review | **REJECTED** | The four completion packs are a subset of eight order engagements. Nothing says the €500 review is charged per stage rather than per order. Eight reviews for eight orders is internally possible; the reviewer inferred twelve review events without evidence. |
| Flash 3: agricultural/workshop prospects contradict the steel exclusion | **REJECTED** | A contractor’s sector does not define the product being offered. The chapter expressly limits launch to exterior joinery. Moreover, official IPLO scope includes qualifying two-storey industrial buildings such as warehouses, livestock buildings and workshops in consequence class 1. The reviewer’s claim that these prospects “frequently” buy primary steel is unsourced, and the cited standards excerpt says nothing about “execution classes” or factory-production controls. [IPLO scope](https://iplo.nl/regelgeving/regels-voor-activiteiten/technische-bouwactiviteit/kwaliteitsborging/bouwwerken-gevolgklasse/) |
| Pro 1: reuse between the private and authority dossiers is unsupported | **CONFIRMED** | [03-consumer-dossier.txt](/home/diablo/book19/resources/sources/03/excerpts/03-consumer-dossier.txt:6) establishes contents and separation of the parties, but not that material can be reused. The clause needs another receipt or an explicit inference marker; deletion is not the only valid fix. |
| Pro 2: Kozijnen Unie “project guidance” is unsupported | **CONFIRMED** | [03-dutch-dealer.txt](/home/diablo/book19/resources/sources/03/excerpts/03-dutch-dealer.txt:6) supports supply, Dutch-speaking staff and installation. “Clear communication” is not evidence of project guidance. |
| Pro 3: FENBRO “quotation” bundle is unsupported | **CONFIRMED** | [03-fenbro-model.txt](/home/diablo/book19/resources/sources/03/excerpts/03-fenbro-model.txt:9) says product, delivery, installation and warranty—not quotation. |

# Consolidated ranked findings

## 1. High — The central public counter-case overstates two sources

> “correct manufacturer instructions may already give the quality assurer sufficient proof.”

The TloKB source says proof is sufficient when the builder **installs the product according to** the manufacturer’s instructions. Possessing “correct instructions” is not itself enough. The chapter states the mechanism correctly later, but the lede changes it in a way that exaggerates how easily the substitute absorbs the work. [TloKB guidance](https://www.tlokb.nl/wet-kwaliteitsborging/bouwproducten-verwerken-in-een-bouwwerk)

Likewise:

> “This is the kill fact in public view. The factory can place documents next to the order without a specialist intermediary.”

[03-eko-incumbent.txt](/home/diablo/book19/resources/sources/03/excerpts/03-eko-incumbent.txt:6) proves that Eko-Okna markets a distributor platform, a document-library category and a Dutch business-contact channel. It does not show that documents are matched to individual orders, complete for Dutch project requirements, or usable without an intermediary. The lede also generalizes from one manufacturer to “Large factories.”

**Fix:** Correct the lede to require installation according to the instructions. Describe Eko-Okna as evidence that incumbents possess relevant distribution and document surfaces—not as proof they already close the project-specific evidence gap. Make actual first-review adequacy the kill fact.

## 2. High — The experiment mixes the excluded steel business into the joinery pass rule

> “review ten recent Polish-origin joinery or steel orders each”

> “require the quality-assurer sample to show at least four material first-review gaps in twenty Polish-origin orders.”

The launch explicitly excludes structural steel because its evidence and authority chain differ. A mixed sample could pass solely because four steel files were deficient, even if every target window-and-door file was adequate. The cited standards excerpt establishes different standards; it does not justify combining their failure rates.

**Fix:** Sample only non-fire-rated exterior joinery in new consequence-class-1 projects. If steel is investigated, give it a separate denominator, pass rule and later-line decision.

## 3. High — The claim ledger fails the required schema and is future-dated

AGENT.md requires the status field to be exactly `verified`, `inference`, or `open`. Thirteen rows instead use values such as:

> `checked-by:codex:2026-09-05`

See [03.tsv](/home/diablo/book19/checks/claims/03.tsv:2). The source index and excerpts say 2026-09-04, while the verification metadata is dated 2026-09-05—after the declared current date. Flash’s statement that all thirteen rows are “verified” is therefore false as a schema claim.

**Fix:** Change the thirteen supported statuses to `verified`; retain reviewer/date metadata in a separate column or note, using a non-future date.

## 4. Medium — The economic prose contradicts the table and capacity model

> “Cash loss is lower because that labour is not a payroll cheque”

The table yields €6,400 positive cash operating result before founder compensation: €28k − €15.6k − €6k. It shows an economic loss after imputing founder labour, not a smaller cash loss.

> “If average delivery exceeds thirty hours, gross margin falls below the intended level”

At 30 hours × 10 orders, the operation uses 300 of the stated 360 monthly productive hours. The table’s payroll and gross margin do not change; only contingency capacity falls. Separately, the 90-day test permits 48 hours per order, which would require 480 monthly hours at mature volume—33% more than stated capacity.

**Fix:** State the €6.4k pre-founder cash result explicitly. Replace the unsupported 30-hour margin assertion with a capacity threshold, and distinguish an acceptable first-pilot time from the ≤24-hour mature target.

## 5. Medium — The completion paragraph outruns its saved excerpt

> “the quality assurer checks the work during construction and issues a statement when there is justified confidence that the building meets the technical rules.”

The `03-completion-dossier` excerpt begins with the completion notification and does not contain either the construction-stage inspection or “justified confidence” support. The current official pages support these facts, but the required saved receipt does not. [Chapter passage](/home/diablo/book19/chapters/03-joinery-steel-dossier.html:40)

**Fix:** Add the relevant official passages to a saved excerpt and split the marker if necessary; update the ledger claim to cover every receipted sentence.

## 6. Medium — Mature technical-review economics are unexplained

> “Dutch technical review … €60k”  
> “Dutch quality lead, loaded … €90k”

This confirms the useful core of Flash finding 1: readers cannot tell what the external €500 buys once a Dutch quality lead is employed, or whether its hours sit inside or outside the 24-hour order estimate.

**Fix:** Define each role, its hours and whether the €500 is external independent review. If it duplicates the lead, remove it and recalculate; do not invent structural or fire sign-offs outside the stated scope.

## 7. Medium — The precedent trace follows a different legal entity

The website identifies **FENBRO Sp. z o.o.**; the independent excerpt identifies **FENBRO LTD**, a UK entity that filed dormant accounts. Matching name, address and directors is corroboration, but it does not independently establish that the Polish website entity is the operating precedent. Pro’s statement that Companies House verifies FENBRO Sp. z o.o. is too strong.

**Fix:** Add an official Polish KRS extract for the Polish company and identify the relationship, if any, between it and the dormant UK company.

## 8. Medium — Private-dossier reuse is unreceipted

This is Pro finding 1. The source supports dossier separation and contents, not reuse across submissions.

**Fix:** Remove the reuse clause, add a source, or separate it under an `inference` claim.

## 9. Low — Two competitor descriptions exceed their excerpts

- Replace “quotation” with “product” in the FENBRO bundle.
- Remove “project guidance” from the Kozijnen Unie description unless a supporting passage is saved.
- Update the corresponding ledger rows so they exactly match the repaired prose.

The buyer and purchase event, anti-platform scalability discussion, Dutch-language gate, capable-failure case and overall **WATCH** chapter verdict otherwise survive review. The three fixes that matter most are the central-source corrections, a joinery-only experiment, and repair of the claim ledger.
