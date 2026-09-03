# Research job — crowdfunding as a demand instrument (repo ~/book19)

Question: which physical products proved paid demand on crowdfunding platforms outside the EU
(and in the US/UK) in 2023–2026 but have no European distributor, and would need EU compliance
work (CE, packaging/EPR, and for connected devices the Cyber Resilience Act) that a Netherlands-
based operator with book-18-style regulatory knowledge could supply as the EU distribution partner?

Do, saving as you go (commit only your own files after each milestone, message "WIP crowdfunding: <what>"):
1. Data. Use published datasets and public pages only; do not scrape against a site's terms.
   - Kickstarter: the Web Robots monthly Kickstarter dataset (webrobots.io/kickstarter-datasets)
     — download the most recent full scrape you can and, if available, one from ~2023 for a
     baseline; save to `resources/data/` (gzip if large; do not commit files > 50 MB — note the
     URL and md5 instead).
   - Indiegogo: any published dataset or the public "top funded"/category pages.
   - Asia: Makuake (Japan), Wadiz (Korea), Zeczec (Taiwan), JD Crowdfunding / Modian (China):
     public top-funded / ranking pages and any published statistics; save what you read as
     text excerpts under `resources/sources/<platform>/`.
   - Gulf: check whether any reward-crowdfunding platform of scale exists (Zoomaal, others);
     if the answer is "mostly equity platforms", say so with a source and move on.
   - Save every page you rely on as an excerpt with URL and fetch date.
2. Analysis (write scripts under `scripts/`, keep outputs under `drafts/reviews/`):
   - By platform and, for Kickstarter, by country: funded amount, backer count and success rate
     by category, 2023–2026; physical-product categories only (exclude games/film/music/publishing
     unless physical).
   - A "proven elsewhere" list: physical products with ≥ USD 250k (or local equivalent) raised
     and ≥ 1,000 backers on a non-EU platform, 2023–2026.
   - For the top 40 of those: does an EU seller exist (maker's own EU shop, Amazon.de/.nl listing,
     a named distributor)? Record how you checked and the date. Mark EU-CE-relevant categories
     (electrical, toys, PPE, connected devices).
3. Output `drafts/reviews/crowdfunding-findings.md`:
   - The category tables (short), with the datasets and their limits stated (backers ≠ consumers;
     delivery-failure rates; platform skew).
   - The proven-elsewhere list with the EU-seller check.
   - 3–5 candidate opportunities, each ≤ 150 words: the product or product family, the platform
     evidence (amount, backers, date), the EU status, the compliance work required (name the
     regulation), the plausible route (EU distribution agreement with the maker; not copying),
     and the single fact that would kill it. Rank them.
   - An honest paragraph on whether the cross-platform difference is "3–5 ideas" or "things
     Amazon already sells".
Never invent a number; every figure in the findings must trace to a saved dataset or excerpt.
Final reply ≤ 200 words: the ranked candidates and the honest paragraph.
