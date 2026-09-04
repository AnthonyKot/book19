# AGENT.md — instructions for Book 19 research and writing (ported from Book 18, 2026-09-05)

## Who is reading

An experienced enterprise developer in the Netherlands looking for income outside software over
the next two to five years, as AI progresses. Their edges are in `drafts/edge-inventory.md`:
English, Russian and Polish; Dutch at A2; EU and Dutch regulatory literacy; an engineering
habit; a Polish, Ukrainian and Russian-speaking network on the supply and crew side; about
EUR 100k. Their constraints, confirmed 2026-09-05: hands-on; alongside the job at first; no more
than EUR 50k at risk in year one; retraining of days or weeks in English, no Dutch trade exam.
The book's line: outside software, not outside engineering. They sell installed iron and a
signed file, never a product with a login. They are not asking to be reassured.

## Priority stack

1. **Never false.** Current claims are sourced; proposals are not presented as law; arithmetic
   hypotheses are not presented as observed prices.
2. **Find the buyer and event.** Name the person or function who pays and what happens to make
   this purchase outrank other work.
3. **Make the money legible.** Revenue, gross margin, founder replacement cost, working capital
   and owner income are separate.
4. **Earn scalability.** State which work remains human, what can be delegated, and what asset
   accumulates. Never use "platform" as a magic word.
5. **Attack the idea.** Entrenched vendors, internal teams, consultancies, free tools, standards
   uncertainty and partner capture belong in the main argument.
6. **Leave a cheap next move.** The reader must be able to test the riskiest assumption without
   resigning or buying the full equipment stack.

## Research rules

- Browse because laws, deadlines, standards, products and competitors are current.
- Prefer primary sources for law and technical requirements.
- For competitors, use their own product documentation and pricing where published; label
  marketing claims as marketing claims.
- Record every relied-on URL and its purpose in `resources/sources/NN/SOURCES.md`.
- Write a claim ledger in `checks/claims/NN.tsv` before or alongside prose. Schema:
  `id<TAB>claim<TAB>source_url<TAB>source_locator<TAB>status` where status is `verified`,
  `inference`, or `open`. HTML may ship only with no `open` claims.
- Use `<!-- CHECK: id -->` immediately after the factual sentence or paragraph.
- Save the passage that supports each `verified` row as a text excerpt in
  `resources/sources/NN/excerpts/<slug>.txt` (URL, date fetched, then the verbatim passage),
  and name that file in the `source_locator` column. A `verified` row without an excerpt is
  not verified.
- Do not download or reproduce copyrighted reports unless needed and permitted; links and
  concise paraphrases are normally enough.

## Voice

Plain, adult, analytical. No startup cheerleading, future-of-X throat-clearing, fake scenes,
or inflated market-size paragraphs. Explain technical mechanisms where they change the business
case. The reader should feel that a skeptical operator and a skeptical investor wrote together.

## Required challenge

Each essay must contain at least one credible path by which capable execution still loses. This
is Book 4's counter-case discipline adapted to an opportunity that may not yet have a historical
post-mortem. It must not be a straw man such as "poor sales" or "bad execution."

## Pre-ship test

1. Can the reader name the buyer, purchase event and substitute?
2. Is demand evidence distinct from regulation and market size?
3. Does the economic model pay replacement-cost labour and still reach the owner target?
4. Is the twentieth delivery visibly different from the first?
5. Does the essay name why an incumbent, partner or customer might capture the margin?
6. Is Dutch-language dependence stated for this exact channel, and does the "Why you" section answer it honestly?
7. Is there a bounded 90-day experiment with a price, pass rule and kill rule?
8. Are all external claims receipted and all arithmetic labelled?

## Coordination

Agents edit only their assigned essay HTML, claim TSV, source index and optional draft notes.
The coordinating agent alone edits `CONTEXT.md`, `AGENT.md`, `TEMPLATE.md`, `README.md`,
`index.html`, `about.html`, static assets and cross-essay comparisons.
