# Ideation brief — find businesses of one shape (book 19, The Third Engine)

You are generating candidate businesses for one specific reader, from your own knowledge and judgment
first, with a small verification budget second. Read `/home/diablo/book19/CONTEXT.md` and
`/home/diablo/book19/drafts/edge-inventory.md` before anything else. Then read
`/home/diablo/book19/drafts/notes/2026-09-03-fable-triage.md` and
`/home/diablo/book19/drafts/notes/2026-09-04-fable-triage-2.md`: everything kept, held or cut there
is off the table. Do not re-propose or lightly rename any of it.

## The shape

Every idea you return must have all seven parts. Ideas that lack one are not returned.

1. **Iron plus paper.** A physical unit (a machine, a site, an order, an imported product, a crew)
   that cannot legally be used, sold or occupied without a file about it: a risk assessment,
   a CE declaration, a certificate, a technical file, a registration, an inspection report.
2. **A dated rule change**, between now and 2028, that creates that file or tightens it, so the
   market has a deadline and someone who reads the rule early sees the demand before it is priced.
3. **Small B2B buyers**, roughly ten to a hundred staff, who work in English or in Polish, Russian or
   Ukrainian, who cannot afford their own compliance person, and whom the incumbents (notified
   bodies, TÜV-class firms, large integrators, national contractors) price above.
4. **The reader's edge does the work**: regulatory literacy (reads EU and Dutch law directly),
   engineering habit (measures, documents, automates the evidence trail), and a Polish, Ukrainian and
   Russian-speaking network on the supply or crew side. No Dutch-language exam may stand between the
   reader and the first sale; if a personal certificate exists, it must be obtainable in English or
   bought with a firm and its holder.
5. **Priced per unit** (per cell, per site, per order, per product, per crew-month), with a first
   paid test under €5,000 that can run inside ninety days alongside a day job, capital under €50,000,
   and a visible step two (a Dutch-speaking partner or hire) and step three (an acquisition, or
   becoming the operator rather than the adviser).
6. **AI raises or leaves the demand** by 2030, because progress adds units and files and does not
   replace the site visit. Say why in one sentence; "AI-proof" without a mechanism is not accepted.
7. **One checkable kill fact**: a single fact that, if true, ends the idea (an incumbent already
   sells it cheaply, every worker needs a Dutch exam, the demand is carried by a subsidy, the
   product cannot legally be sold in the EU).
8. **A precedent that exists.** A real, named small firm elsewhere (United States, China, Germany,
   Poland, the UK; not the Netherlands) that already earns its living on this shape, found on the
   web and saved as an excerpt: what it sells, to whom, at what price if stated, how big it is, how
   long it has existed. Sources we respect: the firm's own site plus one independent trace (trade
   press, a regulator's register, a court or procurement record, a trade-body directory, a
   published interview). A precedent nobody can find is a reason to doubt the idea, not to invent one.

The line of the book: outside software, not outside engineering. The reader sells installed iron
and a signed file, never a product with a login. Anything that becomes a software business within a
year is cut.

## Your seed

{{SEED}}

Stay inside the seed. The other agent has a different one; overlap wastes both runs.

## Method

Work from knowledge first: list twelve to fifteen raw candidates inside the seed in one line each,
then screen them against the seven parts, then keep the best four to six. Only then spend your
verification budget: at most twenty-five web fetches, used for three things only: the precedent for
each kept idea (part 8, at least one fetch each), the kill fact, and the one number each idea most
depends on. Save every fetched page as a plain-text excerpt under
`/home/diablo/book19/drafts/ideation/{{SLUG}}/sources/<id>.txt` with URL, publisher and fetch date.
Never invent a figure; an unverified figure is written as "estimate, unverified". Do not run git.

## Output

Write `/home/diablo/book19/drafts/ideation/{{SLUG}}/ideas.md` as you go (create it early, append):

- the raw list of twelve to fifteen, one line each, with the part that cut each of the discarded ones;
- four to six kept ideas, each ≤240 words in eight labelled parts matching the shape above, plus
  a small table: unit price, entry cost, capital tied up, all marked verified or estimate;
- for each kept idea, the eight to twelve facts a research run must settle, phrased as checkable
  questions with the likely source;
- ≤120 honest words: whether this seed found anything a Dutch founder with the same reading could
  not, and which single idea you would put your own money into.

Final reply ≤200 words: the kept ideas in one line each, and the one you would fund.
