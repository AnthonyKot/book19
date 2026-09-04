**REVISE** — the chapter’s evidence chain and €50,000-at-risk acquisition structure need correction before shipping.

Consolidated report: [drafts/reviews/06-codex.md](/home/diablo/book19/drafts/reviews/06-codex.md)

It adjudicates every reviewer finding, challenges their unsupported conclusions, and adds twelve ranked findings—including the funding contradiction, missing end-buyer demand evidence, and future-dated source receipts.
gs are ranked by severity. “Supported” below means supported at the scope required by the book: the marker's ledger row and saved excerpt, not merely text that can be found elsewhere on a website.

## Ranked findings

### 1. High — the EUR 300,000 purchase structure spends the same EUR 50,000 twice (missed by Pro; partly caught by Flash)

> “The acquisition-price hurdle is **€300,000**: no more than €50,000 reader equity at risk, a €200,000 loan and a €50,000 seller earn-out...”
>
> “The €50,000 equity cannot all become goodwill. Legal, financial, tax, employment and certificate diligence, the lender fee and at least one month of payroll must fit inside the purchase structure.”

The three stated purchase-price sources already total EUR 300,000. They leave none of the reader's EUR 50,000 for fees or working capital. The saved Qredits terms also make the 1.5% fee on a EUR 200,000 loan EUR 3,000 before diligence or payroll. The later instruction that these uses must fit inside the same EUR 50,000 is therefore incompatible with the stated acquisition-price funding.

Flash correctly noticed the contradiction, but its proposed EUR 25,000/3,000/4,500/17,500 allocation invents unsourced diligence and payroll amounts and silently adds a further EUR 25,000 of vendor finance. Those numbers are not verified facts and should not be copied into the chapter.

**Fix:** add a sources-and-uses table. Either reduce cash consideration by the exact verified fees and target-derived working-capital reserve, increase explicitly modelled seller finance, or lower the maximum price. Then show that tax, capex and any earn-out cannot force another reader cash injection during year one.

### 2. High — the chapter has no end-buyer demand receipt (missed by both)

> “Buyer behaviour exists but is narrow. HMP says it structurally works with self-employed DIAs and offers regular assignments...”

The Bbl and LAVS excerpts establish obligation and workflow. HMP's vacancy establishes one certified firm's advertised demand for freelance labour. Asdesk establishes an offer and list prices. Brookz establishes listings. None shows a property manager, housing corporation, contractor or other named end buyer actually procuring or paying for an asbestos inventory. Calling HMP's labour recruitment “buyer behaviour” changes which market is being evidenced.

This fails `CONTEXT.md`'s rule that demand be shown by buyer behaviour, enforcement, procurement or filings rather than regulation alone. It also makes the property/project-manager payer in the proposition plausible but unreceipted.

**Fix:** add at least one dated end-buyer procurement, award, framework, invoice/interview record or enforcement-triggered purchase from a named buyer class. If none is available, say explicitly that end-customer demand evidence is still open and make the paid referral the gate before an acquisition verdict.

### 3. High — the evidence trail is dated in the future (missed by both)

Every excerpt and `resources/sources/06/SOURCES.md` says “Fetch date: 2026-09-05,” while this review run and repository context are dated 2026-09-04. A source cannot have been fetched tomorrow. The two reviewers repeat the impossible date and treat the receipts as current.

This is a provenance defect, not an editorial nicety: the ledger uses the same future date in `checked-by:codex:2026-09-05` for nineteen rows.

**Fix:** recover the actual retrieval date from logs if possible. Otherwise re-fetch every relied-on page, save fresh excerpts with the real date, and update the source index and ledger. Do not merely change the string without re-establishing provenance.

### 4. High — the seller-labour normalisation rule is not safe for an owner-DIA (missed by both)

> “If the seller is the only technical final responsible person and their labour is missing from payroll, reported EBITDA must be at least **€150,000 before that normalisation**. Subtract the €75,000 role cost...”

The table separately charges EUR 75,000 per DIA and EUR 85,000 for founder replacement. But the screening prose subtracts only the senior-DIA role when the departing seller may also perform management, sales or account ownership. Conversely, if EUR 85,000 founder labour means the buyer's own paid operating role rather than replacement of seller work, the chapter never says so. A single EUR 150,000 pre-normalisation threshold cannot cover all those cases.

The arithmetic inside the operating table is correct; the bridge from a seller's reported EBITDA to that table is not defined. This undercuts the kill rule and the Brookz multiple comparison.

**Fix:** show a target-specific normalisation bridge: reported EBITDA; add back actual seller compensation; subtract each missing seller role at its replacement cost; subtract buyer/founder labour if distinct; then debt service, tax, capex and earn-out. Apply the multiple only to the resulting like-for-like EBITDA measure.

### 5. Medium — the acquisition preserves neither the certificate nor operations on the evidence shown (missed by both)

> “The buyer takes the shares, the team, the quality system, the work history and the trading name.”
>
> “A share purchase can preserve the legal entity, but it does not make change of control invisible.”

The scheme excerpt proves only that director, management, owner and UBO changes must be reported immediately. It does not state what the certification body does after a share transfer, a technical-final-responsible change or an employee departure. The Advies Lieren announcement does not disclose transaction form, and the Ascert register proves only that both named entities had valid certificates after the announced date. The ninety-day plan correctly asks certification bodies to settle the point; the proposition speaks as if it is already settled.

**Fix:** recast certificate continuity as an explicit open transaction condition, or add written certification-body guidance showing the consequences and timing for the exact share-transfer/TEV scenario. Make continued certificate validity a closing condition rather than an acquired asset assumed in the opening proposition.

### 6. Medium — “losing the employed DIA is operationally fatal” overstates the rule for the proposed two-DIA target (missed by both)

> “The scheme confirms that losing the employed DIA is operationally fatal until another qualifying employee is in place.”

Article 6 requires at least one DIA under an employment contract, and Article 19 requires inventory work to be performed by a DIA. Those provisions make loss of the **last employed DIA** a certification problem. They do not say that either departure from a two-employed-DIA target stops production. A departing technical final responsible person can stop signatures if the remaining DIA does not qualify for that role, but that is a different dependency supported by Article 9.

**Fix:** distinguish three failure modes: loss of the last employed DIA, loss of the sole qualifying technical final responsible person, and ordinary capacity loss. Align the title, lede, kill fact and retention test with those separate facts.

### 7. Medium — several claims are true in the live sources but fail the required ledger/excerpt chain (caught incompletely by both)

The automated strict check passes because IDs match; it does not test semantic scope. The following markers do not have a saved excerpt and ledger claim broad enough for the sentence they follow:

- **Report handoff:** “The report must reach the contractor before removal.” The saved `06-bbl-duty.txt` omits this. The live [IPLO page](https://iplo.nl/regelgeving/regels-voor-activiteiten/sloopactiviteit/asbestinventarisatieplicht/) does support it: the commissioning party must give the contractor a copy before asbestos removal. Pro's allegation that the law lacks the timing is therefore wrong in substance, but the local receipt is still incomplete.
- **Other Bbl exceptions:** “specified exceptions” is broader than the excerpt, which saves only the post-1 January 1994 exception. The live IPLO page also links the non-certified-company and private-removal exceptions. Extend the receipt or narrow the prose and ledger claim.
- **Annual file review:** `06-change-control.txt` saves Article 63(1), not Article 63(2). The live [official scheme](https://zoek.officielebekendmakingen.nl/stcrt-2026-29952.html) supports a dossier review of at least four completed inventories. Both reviewers found the receipt gap, but Flash wrongly assigns the file review to Article 64; it belongs to Article 63(2).
- **Audit thresholds and announced/unannounced scrutiny:** `06-audit-load.txt` saves only three table columns. The prose's “or” rule and “announced and unannounced” language require Article 64(1), (2) and (4), which say to use whichever criterion yields the higher assessment count. Save those provisions.
- **Tritium breadth:** `06-dia-salary.txt` omits the team claim and its ledger row covers only salary, hours and project scale. The live [Tritium vacancy](https://vacatures.creongroep.nl/o/deskundig-inventariseerder-asbest-dia) does describe soil, environmental and sustainability research. Add that passage and broaden/split the ledger row instead of deleting a true claim.
- **Asdesk promises:** `06-retail-price.txt` is only the price PDF. Asdesk's homepage supports the experienced certified inspector, accredited laboratory and clear-report promises, but that page is absent from the source index, ledger and excerpts. Add a marketing-claim row and excerpt, clearly labelled as the firm's promise, or remove the sentence.
- **Gross salary:** neither the saved excerpt nor the live Tritium vacancy labels EUR 2,500–4,375 as gross. Remove “gross” or source it.

### 8. Medium — the A2 conclusion is an unlabelled inference (missed by both)

> “At A2, the reader does not inspect or sign.”

ProXia says a candidate must command Dutch in speech and writing and describes the exam components. It does not map that requirement to CEFR levels or say A2 necessarily fails. The conclusion is sensible risk management, but it is still an inference. Flash goes further and says “Native Dutch is mandatory,” which neither the chapter nor source says.

**Fix:** write “Treat A2 as a fail unless the exam provider confirms eligibility and the reader obtains the DIA certificate,” and record that inference honestly. Retain the separate, well-supported fact that only a DIA performs the inventory and the qualifying technical final responsible person signs.

### 9. Medium — the ledger violates the stated status schema (missed by both)

`AGENT.md` permits `verified`, `inference`, or `open`. Nineteen rows instead say `checked-by:codex:2026-09-05`; only `06-retention-boundary` says `inference`. Flash's statement that the ledger contains “19 verified” rows is therefore not true under the declared schema, even though the verification script accepts them.

**Fix:** after correcting provenance and receipt scope, set each row to the allowed status. Preserve reviewer identity/date in a separate field or note if desired; do not overload `status`.

### 10. Low — the two Brookz markers are stacked after the wrong sentence (caught by Flash)

> “Brookz's ... 4.3–5.5 EBITDA multiple. Its visible asbest page showed ... €850,000 revenue and 6–10 staff. `06-sale-pool` `06-multiple`”

`06-multiple.txt` supports the first sentence and `06-sale-pool.txt` the second. The markers appear together after the second sentence, in reverse order, with more paragraph text following. That is not “immediately after” each factual sentence as required.

**Fix:** put `06-multiple` after the first sentence and `06-sale-pool` after the second.

### 11. Low — earn-out timing is omitted (caught by Flash)

The first-year table leaves EUR 19,000 before tax, capex and earn-out, while the purchase structure includes a EUR 50,000 earn-out with no payment date or cash formula. The omission prevents the reader from checking whether year-one cash needs another capital injection. Flash is right about the ambiguity, but its 19% tax calculation is unreceipted and its years-two-to-four schedule is arbitrary.

**Fix:** tie each earn-out tranche to both retained staff/customer gross profit and available post-tax, post-capex cash, with no payment that breaches a minimum cash balance or the reader's year-one risk ceiling.

### 12. Low — “training records” is not supported as written (caught by both)

> “The scheme requires ... training records...”

The cited quality-system excerpt supports defined roles and replacement arrangements, document control, internal reviews, procurement controls, safety instructions, corrective action and ten-year report retention. It does not list training records, and the current scheme does not use that term. Other provisions require particular instruction certificates and personnel-file records, but those were not cited.

**Fix:** replace “training records” with an element in the excerpt, or add the exact provision and receipt for the particular instruction record meant.

## Disposition of every reviewer finding

| Reviewer finding | Disposition | Why |
|---|---|---|
| Flash 1 — Brookz marker stacking/inversion | **CONFIRMED** | The two excerpts support different sentences; marker order and placement are wrong. |
| Flash 2a — annual review/file-sample receipt | **CONFIRMED, narrowly** | The saved excerpt omits the dossier review. The underlying law supports it under Article 63(2), not Article 64 as Flash says. Expand the receipt; deletion is unnecessary. |
| Flash 2b — “training records” | **CONFIRMED** | Neither the cited excerpt nor Article 12 supports that phrase. |
| Flash 3 — closing cash waterfall | **CONFIRMED** | The same EUR 50,000 funds price and non-price uses. Flash's exact replacement allocation is unverified and adds unstated vendor finance. |
| Flash 4 — earn-out timing | **CONFIRMED** | A EUR 50,000 contingent payment is omitted from the only year-one cash view. The proposed timing and tax figure are unverified. |
| Pro 1 — annual review/file-sample claim | **CONFIRMED, narrowly** | It is a receipt defect, not a false-law defect: the live official source expressly requires at least four dossier reviews. |
| Pro 2 — “training records” | **CONFIRMED** | Same issue as Flash 2b. |
| Pro 3 — Tritium team scope | **CONFIRMED, narrowly** | The saved excerpt/ledger row do not support it, but the live cited vacancy does. Expand the receipt rather than treating the claim as false. |
| Pro 4 — Asdesk marketing promises | **CONFIRMED** | The marked price PDF supports prices only. A different Asdesk page supports the promises but is not indexed or receipted. |
| Pro 5 — report before removal | **CONFIRMED as a receipt gap; REJECTED as a factual objection** | The saved excerpt omits timing, while the live IPLO source explicitly requires the copy before removal. The correct repair is to extend the receipt and ledger claim. |
| Pro 6 — salary described as gross | **CONFIRMED** | Neither saved nor live vacancy text says gross. |

## Reviewer assertions that do not survive checking

- **Flash's overall SHIP verdict — REJECTED.** Passing `./verify.sh 06 --strict` confirms marker/row mechanics (25 markers, 20 unique IDs, 20 rows, no ID mismatch); it does not validate whether the prose is supported by each excerpt. The semantic failures above remain.
- **Flash's “19 verified rows” — REJECTED.** Nineteen statuses are `checked-by:...`, outside the declared schema, and multiple excerpts are narrower than the prose.
- **Flash's “sourced kill fact settles” — REJECTED.** The chapter itself correctly says retention, package, customer continuity and an affordable transaction cannot be settled from the public record. The essay contract permits saying the record cannot settle them; the reviewer should not claim otherwise.
- **Flash's “Native Dutch is mandatory” — REJECTED.** The source requires command of written and spoken Dutch, not native proficiency.
- **Both reviewers' clean economics assessment — REJECTED.** The operating-table additions are correct, but the purchase sources-and-uses and seller-role normalisation are not.

## What works

The chapter names a plausible purchase event and substitutes, separates standing obligation from project timing, treats public prices as comparators rather than market averages, gives the incumbent and partner capture a real turn, describes a credible strategic-buyer failure mode, distinguishes the first/fifth/twentieth customer, respects the no-Dutch-exam and beside-the-job constraints before closing, and uses the required verdict string. The lede and prose also pass the mechanical readability checks. These strengths justify **REVISE**, not **BLOCK**, provided the evidence and financing defects are repaired before shipping.

## Three fixes that matter most

1. Replace the acquisition paragraph with a complete sources-and-uses and year-one cash schedule that stays within EUR 50,000 total reader capital at risk.
2. Add direct end-buyer demand evidence and written confirmation of certificate treatment at change of control; until then, label both as open gates.
3. Rebuild the receipts with real fetch dates and exact supporting passages, then fix ledger statuses and marker placement.
