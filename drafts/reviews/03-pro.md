Here is the review of `03-joinery-steel-dossier.html` against the book's rules, ranked by severity.

### Findings

**1. Unsupported claim in receipted sentence (Severity: High, Rule 8)**
*   **Passage:** "The municipality and quality assurer are not parties to that private dossier, although some material can be reused for the completion notification. `<!-- CHECK: 03-consumer-dossier -->`"
*   **What the source actually supports:** The excerpt (`03-consumer-dossier.txt`) and TSV verify that the municipality and quality assurer are not involved, and list the mandatory contents of the consumer dossier. It does not state or imply that material can be reused for the completion notification. 
*   **Concrete fix:** Delete the unsupported clause so the sentence ends at "private dossier." 

**2. Excerpt mismatch for competitor claim (Severity: Low, Rule 8)**
*   **Passage:** "A Dutch wholesaler such as Kozijnen Unie markets Dutch-speaking staff, supply, project guidance and its own installation team. `<!-- CHECK: 03-dutch-dealer -->`"
*   **What the source actually supports:** The excerpt (`03-dutch-dealer.txt`) confirms Dutch-speaking staff, supply to contractors/builders, and its own installation team. It does not explicitly mention "project guidance" (it mentions clear communication).
*   **Concrete fix:** Remove "project guidance" from the sentence and update the corresponding TSV row.

**3. Minor word substitution in competitor bundle (Severity: Low, Rule 8)**
*   **Passage:** "FENBRO bundles quotation, delivery, installation and warranty around Polish joinery. `<!-- CHECK: 03-fenbro-model -->`" *(Second usage in text)*
*   **What the source actually supports:** The excerpt (`03-fenbro-model.txt`) states they offer "a complete service: product + delivery + installation, with full warranty". It does not explicitly use the word "quotation".
*   **Concrete fix:** Change "quotation" to "the product" to mirror the excerpt exactly: *"FENBRO bundles the product, delivery, installation and warranty..."*

***

### General Rule Compliance

*   **Rule 1 (Never false):** Passed. Proposals and hurdles are clearly labelled as test designs ("required-price hurdle", "not observed market rates"). Implementation dates for Wkb and CBAM are accurate.
*   **Rule 2 (Buyer and event):** Passed. The buyer is the project manager/operations director; the event is needing evidence before purchase order release to avoid acceptance delays.
*   **Rule 3 (Economics):** Passed. The arithmetic is internally consistent. Founder replacement cost (€100k) is strictly separated from operating surplus (€120k). Working capital is credibly controlled by billing 50% in advance.
*   **Rule 4 (Scalability):** Passed. The essay explicitly avoids the "platform" magic word, correctly describing the 20th-customer asset as a "verified supplier-document map" and "trained coordinators."
*   **Rule 5 (Incumbents and capture):** Passed. Eko-Okna acting as an incumbent is treated fairly as the "kill fact in public view." Partner margin capture is explicitly confronted.
*   **Rule 6 (Capable failure):** Passed. It outlines a highly credible non-straw-man scenario where the founder executes perfectly, but the structural willingness to pay evaporates once coordination gaps close.
*   **Rule 7 (Constraints & Precedent):** Passed. Respects the A2 Dutch limit by enforcing a fixed-fee Dutch consultant partner. Cash at risk stays under €50k. The precedent firm (FENBRO) is independently traced to UK Companies House.
*   **Rule 9 (Verdict):** Passed. **WATCH** is the earned verdict because incumbent bundling makes independent demand doubtful without further evidence. The €5k separate fee kill assumption is exactly right.
*   **Rule 10 (Readability):** Passed. No sentences over 40 words (the longest is 34), no wall paragraphs, and no jargon without an explained mechanism.

***

### Verdict

**REVISE**

The three fixes that matter most:
1. Delete the "although some material can be reused..." clause in the `03-consumer-dossier` sentence.
2. Remove "project guidance" from the Kozijnen Unie sentence.
3. Change "quotation" to "the product" in the FENBRO bundle sentence.
