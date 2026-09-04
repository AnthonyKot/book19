**Verdict: REVISE — the opportunity remains testable, but the chapter currently attaches its offer to the wrong urgent event and fails the book’s receipt rules in several places.**

# Consolidated review: `02-border-files.html`

## Reviewer findings adjudicated

| Reviewer finding | Disposition | Verification |
|---|---|---|
| Flash 1 — default-values marker overclaims its receipt | **CONFIRMED** | The saved [excerpt](/home/diablo/book19/resources/sources/02/excerpts/02-default-route.txt:5) and ledger row cover verification, cost direction and uplifts, but not registry inclusion or the calculator. The underlying [live NEa page](https://www.emissieautoriteit.nl/regelgeving/cbam/cbam-aangifte/cbam-aangifte-met-standaardwaarden) does support those facts, so this is a receipt defect rather than a false factual claim. Expand the ledger claim and excerpt or add a separate claim. |
| Flash 2 — misplaced Ukraine markers | **CONFIRMED** | In the [chapter](/home/diablo/book19/chapters/02-border-files.html:46), `02-ukraine-risk` appears after the following sentence rather than immediately after “Ukraine is classified low-risk.” Move it to the first sentence. |
| Flash 3 — EUDR revision lacks a primary legal source | **CONFIRMED, but its fix is incomplete** | The Commission report accurately summarizes the enacted change, but `AGENT.md` requires primary law. The correct act is [Regulation (EU) 2025/2650](https://eur-lex.europa.eu/legal-content/EN/ALL/?uri=CELEX%3A32025R2650). The consolidated EUDR is already listed in `SOURCES.md`; merely adding another cross-reference would not repair the claim’s source and excerpt. |
| Pro 1 — “hands-on” necessarily means physical site work, so the verdict is unearned | **REJECTED** | Neither [CONTEXT.md](/home/diablo/book19/CONTEXT.md:9) nor [AGENT.md](/home/diablo/book19/AGENT.md:1) defines “hands-on” as physical site work. The proposed test has the founder conduct supplier interviews, mapping and delivery. The chapter honestly flags that it fails if the reader specifically requires site work. Adding port inspection would create a different business and is not justified by the fixed constraint. |
| Pro 2 — “geolocation tools” is unsupported | **CONFIRMED as a receipt defect** | The saved [excerpt](/home/diablo/book19/resources/sources/02/excerpts/02-ukraine-system.txt:5) and TSV claim omit geolocation. The [live agency page](https://forest.gov.ua/en/news/eu-regulation-eudr-how-ukraine-is-preparing-for-new-export-conditions) discusses the geolocation problem before describing its digital services, but does not cleanly state that the named services provide geolocation. Tighten the wording or save a passage that directly supports it. The reviewer also missed the second occurrence at chapter line 96. |
| Pro 3 — “April 2026” is absent from the saved excerpt | **CONFIRMED as a receipt defect** | The live agency page is dated 15 April 2026, so the date is true. It is nevertheless absent from the saved excerpt, contrary to the local verification rule. Add the publication line to the excerpt; removing a true date is unnecessary. |

No reviewer finding was unresolvable from the available record.

## Ranked consolidated findings

### 1. High — The urgent purchase event does not match the product

> “The purchase event is a stopped import, an authorisation review, or the decision between default and actual emissions…”  
> “The business does not clear goods [or] become importer of record…”  
> “A stopped shipment is the urgent event…”

The authorisation source says Customs withholds release when the importer or indirect representative lacks authorised-declarant status. The proposed supplier-evidence diagnostic neither supplies that status nor clears the shipment. Indeed, the chapter itself concedes that enforcement creates urgency for authorisation but does not prove a supplier-data budget.

This conflates the broker’s urgent authorisation service with the entrant’s later emissions-data service. It weakens the buyer/event case and exaggerates near-term urgency before the September 2027 declaration.

**Fix:** Make the actual-versus-default decision before annual declaration the primary event. If a stopped shipment remains, state explicitly that it triggers the broker’s separate authorisation service and may only generate a later referral for the entrant.

### 2. Medium — Twenty-five ledger rows use an invalid status

The required status vocabulary is `verified`, `inference`, or `open` ([AGENT.md](/home/diablo/book19/AGENT.md:36)). The ledger instead has 25 rows marked `checked-by:codex:2026-09-05` and four marked `inference`.

This directly contradicts Flash’s assertion that all status fields are valid.

**Fix:** Change the 25 supported rows to `verified`. If reviewer provenance is needed, store it outside the status field.

### 3. Medium — The Ukraine-system receipt does not support all uses

The same claim supports two chapter statements about geolocation, while its ledger row instead claims “about 400 active users in April 2026.” The saved excerpt supports the user count, tracing and named legality services, but neither the date nor a direct geolocation-tool claim.

**Fix:** Add the page’s publication date and relevant geolocation context to the excerpt, then make the TSV and both prose uses match exactly. Prefer “addresses geolocation evidence” unless a source explicitly identifies the available geolocation function.

### 4. Medium — The EUDR amendment is not receipted from the enacted instrument

The chapter’s dates and downstream simplification appear accurate, but the ledger relies on a 2026 Commission report rather than Regulation (EU) 2025/2650. The same paragraph’s claim that “the deadline has slipped twice” is not supported by the saved excerpt.

**Fix:** Replace the claim URL and excerpt with the amending regulation’s operative provisions. Add a separate receipt for the two prior deferrals or delete “twice.”

### 5. Medium — The precedent date and conclusion are overstated

> “An independent register trace records … incorporation on 17 November 2021…”  
> “This proves that a small firm can persist on the shape.”

The [saved record](/home/diablo/book19/resources/sources/02/excerpts/02-precedent-trace.txt:5) says the articles are dated 17 November and the notice was published on 20 November; it does not call 17 November the incorporation date. A register trace plus a current marketing page proves that the entity and offer exist, not commercial persistence, customers or payment.

Flash repeats the same unsupported “incorporated 17 Nov” interpretation.

**Fix:** Say “articles dated 17 November 2021; register notice published 20 November.” Limit the conclusion to proof of a real small-firm precedent unless trading or filing evidence establishes persistence.

### 6. Medium — Mature capacity is asserted rather than demonstrated

The model requires 375 delivery days across one analyst and one associate: 187.5 billable days each before leave, training, administration, specialist coordination and founder review. Flash’s claimed “420–440 available working days” is its own assumption, not evidence supplied by the chapter.

**Fix:** Add a capacity bridge showing available days, target utilisation, non-delivery time and founder/specialist hours. Either reduce the client load or add delivery capacity if the resulting utilisation is implausible.

### 7. Low — Default-route prose exceeds its saved claim

> “The CBAM registry carries default values, while the Dutch authority publishes a calculator and guidance.”

These facts are present on the live NEa page, but absent from both the ledger claim and saved excerpt.

**Fix:** Expand `02-default-route` and its excerpt to include the registry and calculator passages, or split the tooling statement into its own checked claim.

### 8. Low — Claim-marker placement is inconsistent

At chapter line 46, the low-risk-country marker follows a different sentence. Similar stacked markers appear where EUDR reform and low-risk consequences are combined.

**Fix:** Put each marker immediately after the sentence or clause it supports.

## Checks that pass

The revenue and margin arithmetic is correct; founder replacement labour and residual operating result are separated. The chapter also handles the A2 Dutch gate through a named partner channel, presents a credible capable-failure mechanism, treats incumbents and partner capture seriously, avoids platform rhetoric, supplies a bounded paid experiment, and has no detected sentences over 40 words.

## Three fixes that matter most

1. Re-anchor the sale to the annual emissions-data decision rather than a customs hold the service cannot resolve.
2. Repair the evidence system: valid statuses, complete Ukraine/default excerpts, correctly placed markers and primary EUDR law.
3. Add a defensible mature-capacity bridge and narrow the precedent claims to what the register actually proves.
