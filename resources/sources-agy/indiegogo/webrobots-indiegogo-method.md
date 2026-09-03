# Source Excerpt: Indiegogo Dataset (Web Robots)

- **URL:** https://webrobots.io/indiegogo-dataset/
- **Dataset File:** `Indiegogo_2025-10-13.zip` (3.9 MB, uncompressed `Indiegogo.csv` 18.5 MB)
- **Origin S3 URL:** https://s3.amazonaws.com/weruns/forfun/Indiegogo/Indiegogo_2025-10-13T07_42_28_311Z.zip
- **MD5:** `ad26819d187b6ca525c6a330a3b8b732`
- **Fetch Date:** 2026-09-03
- **Scope:** 28,587 raw campaign records, covering trending and category scrapes on Indiegogo through late 2025.

## Extraction Criteria & Data Nuances
- Deduplicated records with valid recognized currency: 5,520 campaigns (12,038 records held placeholder `'FAKE_CURRENCY'` from pre-launch landing pages).
- Physical categories: Travel & Outdoors, Productivity, Home, Phones & Accessories, Health & Fitness, Fashion & Wearables, Camera Gear, Energy & Green Tech, Transportation, Audio, Food & Beverages, Photography.
- 2023–2026 physical campaigns: 951 deduplicated campaigns.
- Total normalized funds raised across physical categories: $118,591,010.82 USD.
- Candidates with ≥ $250,000 USD funds raised: 117 campaigns.
- Data quirk: `perks_claimed` field is frequently null in Web Robots Indiegogo crawls; backer demand is validated via funds raised, average pledge tiers, and public campaign page inspection.
