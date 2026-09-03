# Source Excerpt: Kickstarter Dataset (Web Robots)

- **URL:** https://webrobots.io/kickstarter-datasets/
- **Dataset File:** `Kickstarter_2026-08-12.zip` (322 MB) & `Kickstarter_2023-12-14.zip` (27 MB)
- **Origin S3 URL:** https://s3.amazonaws.com/weruns/forfun/Kickstarter/Kickstarter_2026-08-12T08_12_02_805Z.zip
- **MD5:** `4f42d193bad8ac669a6416a5c18cebf5`
- **Fetch Date:** 2026-09-03
- **Scope:** Full monthly scrape of all public Kickstarter projects, containing 79 CSV chunks and 244,266 raw records, capturing campaigns launched between 2009 and August 2026.

## Extraction Criteria
- Window: Projects launched between 2023-01-01 and 2026-08-12.
- Categories filtered: Physical products only (Technology hardware/gadgets/tools, Product Design, Fashion apparel/accessories, Food hardware/small-batch, Tabletop Games, Photography equipment, Crafts). Excluded pure digital goods (software, apps, web, video games).
- Total deduplicated physical projects (2023–2026): 28,389 projects.
- Total pledged volume across physical categories: $1,403,584,874.65 USD.
- Non-EU physical candidates with ≥ $250,000 USD pledged and ≥ 1,000 backers: 594 projects.
