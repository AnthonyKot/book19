Here are the findings from reviewing `chapters/02-border-files.html` against the book's rules, ranked by severity.

### 1. Hands-on constraint violation and unearned verdict (Severity: High)
* **Rule:** 7 (Reader constraints respected) and 9 (Verdict earned by evidence)
* **Quote:** "The constraint that breaks the fit is the buyer side. [...] If the reader wants physical site work, this also fails personally. It is desk work attached to metal, and the least physical candidate in the book." ... "Verdict: **TEST THROUGH A PARTNER**"
* **What the cited source actually supports:** The essay text openly admits that the proposed business model violates the reader's fixed "hands-on" constraint (which `CONTEXT.md` and `AGENT.md` define as physical site work). A proposition that fundamentally fails the reader's fixed constraints cannot earn a "TEST" verdict without modification.
* **Concrete fix:** Either revise the business model to include a hands-on physical element (e.g., verifying physical shipments at the Dutch port against the supplier's documentary evidence), or change the verdict to **DO NOT ENTER** and cite the failure of the "hands-on" constraint as the kill fact.

### 2. Unsupported claim of "geolocation tools" (Severity: High)
* **Rule:** 8 (Receipts: every CHECK marker's row supports the sentence it follows; every verified row has an excerpt that says what the claim says)
* **Quote:** "More damaging to the original pitch, Ukraine's State Forest Agency says its tracking system already follows batches from harvest to export and provides legality documents and geolocation tools. `<!-- CHECK: 02-ukraine-system -->`"
* **What the cited source actually supports:** The excerpt (`02-ukraine-system.txt`) mentions a tracking system and legality documents ("e-logging permit, the electronic certificate of origin, the electronic waybill with photo documentation, as well as the functionality of the Exporter’s Electronic Cabinet"). Neither the verbatim excerpt nor the TSV claim mentions "geolocation tools."
* **Concrete fix:** Remove "and geolocation tools" from the sentence so it faithfully matches the source, changing it to "and exporter tools" (which matches the TSV) or "and tracing tools."

### 3. Date injection in verified TSV claim (Severity: Medium)
* **Rule:** 8 (Receipts: every verified row has an excerpt that says what the claim says)
* **Quote (from `checks/claims/02.tsv`):** "Ukraine's State Forest Agency says its system traces timber batches from harvest to export, had about 400 active users in April 2026, and provides legality documents and exporter tools."
* **What the cited source actually supports:** The verbatim excerpt in `02-ukraine-system.txt` says "Currently, we have around 400 active users of this system", but does not contain the date "April 2026". A verified row must have an excerpt that explicitly says what the claim says; injecting dates from outside the verbatim passage violates the receipt rule.
* **Concrete fix:** Remove "in April 2026" from the TSV claim to maintain strict receipt discipline, or expand the saved excerpt to include the publication date of the article if it was present in the source text.

***

**Verdict: REVISE**

**The three fixes that matter most:**
1. Revise the business model to incorporate hands-on physical work, or change the verdict to DO NOT ENTER due to failing the reader's fixed constraints.
2. Remove "and geolocation tools" from the Ukraine timber system paragraph so it accurately reflects the cited source.
3. Remove the unsupported "April 2026" date from the `02-ukraine-system` TSV claim so the excerpt fully supports the verification.
