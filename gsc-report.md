# GSC Report — Good Mushroom — 04 Jul 2026

**Window analysed:** 2026-04-03 → 2026-07-02 (last 90d)
**Property:** `https://goodmushroom.in/`
**Previous baseline:** 31 May 2026 (see git history)

---

## TL;DR — the pivot worked

1. **Traffic ~3× since May 31.** 90d totals: 2,469 impressions / 178 clicks / 5.6% CTR. Previous 4-month window was 856 / 38 / 4.4%.
2. **Farmers page leak: completely fixed.** 609 impr / 32 clicks / 5.3% CTR at pos 5.6, up from 104 / 0 / 0%. The dual-path rebuild and "For Farmers" nav restore both landed.
3. **Homepage is dominant.** 1,122 impr / 124 clicks / 11.1% CTR at pos 5.5. Branded "good mushroom" is 74 impr / 34 clicks / 46% CTR — outreach is generating branded search.
4. **The biggest new opportunity is Ashwagandha bulk queries.** Twelve distinct "bulk ashwagandha / withania somnifera" queries (63+ total impressions) all stuck at position 19-22 with ~0 clicks. Title/meta rewrite to move the page from pos 20 → pos 8-10 is the single highest-ROI SEO fix.
5. **USA is showing us but not converting.** 595 impressions / 1 click / 0.2% CTR. Big untapped market.

---

## 1. Topline (Apr 3 – Jul 2, 2026)

| Metric | Value | vs May-31 baseline |
|---|---|---|
| Clicks | 178 | +368% |
| Impressions | 2,469 | +188% |
| CTR | 5.6% | +1.2pp |
| Avg position (top pages) | 5–12 | improved |

Country split: India 1,559 impr / 164 clicks (10.5% CTR) · USA 595 / 1 (0.2%) · Canada 56 / 2 · Japan 13 / 1 · UAE 12 / 1 · Singapore 12 / 1.

Device split: Mobile 941 impr / 118 clicks (12.5% CTR) · Desktop 1,507 / 54 (3.6%) · Tablet 21 / 6 (28.6%). Mobile continues to convert 3× better than desktop.

---

## 2. Page performance snapshot

| Page | Pos | Impr | Clicks | CTR | Verdict |
|---|---:|---:|---:|---:|---|
| `/` | 5.5 | 1,122 | 124 | 11.1% | Primary engine |
| `/farmers.html` | 5.6 | 609 | 32 | 5.3% | Fully recovered from 0% leak |
| `/products.html` | 9.2 | 408 | 4 | 1.0% | Bleeding — title too generic |
| `/products/cordyceps.html` | 11.7 | 246 | 3 | 1.2% | Missing "wholesale" query |
| `/products/ashwagandha.html` | 14.1 | 176 | 1 | 0.6% | **Biggest opportunity** |
| `/about.html` | 5.1 | 168 | 11 | 6.5% | Healthy |
| `/faq.html` | 5.9 | 133 | 1 | 0.8% | Bleeding |
| `/products/lions-mane.html` | 11.5 | 119 | 3 | 2.5% | Missing "wholesale" |
| `/products/button.html` | 10.4 | 78 | 0 | 0.0% | 78 impressions, zero clicks |
| `/products/reishi.html` | 15.7 | 53 | 0 | 0.0% | Missing "liquid extract" |
| `/products/extracts-dual.html` | 20.3 | 49 | 0 | 0.0% | Title hyphen may be blocking match |
| `/buyers.html` | 7.7 | 40 | 0 | 0.0% | One rank away from clicks |
| `/products/oyster.html` | 14.0 | 33 | 0 | 0.0% | |
| `/products/tulsi.html` | 7.9 | 22 | 0 | 0.0% | |

---

## 3. High-value queries we're already ranking for

### Ashwagandha bulk cluster — the single biggest fixable set

All rank at position 19-22 (page 2-3, no clicks), all landing on `/products/ashwagandha.html`:

| Query | Impr | Pos |
|---|---:|---:|
| bulk ashwagandha root | 12 | 20.9 |
| ashwagandha root bulk | 9 | 20.1 |
| bulk withania somnifera | 7 | 20.1 |
| ashwagandha in bulk | 6 | 22.5 |
| bulk withania somnifera price | 6 | 19.2 |
| bulk ashwagandha | 5 | 22.8 |
| bulk withania somnifera root granules | 5 | 32.2 |
| bulk ashwagandha tablets | 4 | 15.0 |
| bulk ashwagandha root powder | 3 | 24.0 |
| ashwagandha root wholesale | 2 | 19.5 |
| bulk ashwagandha root granules | 2 | 39.0 |
| bulk withania somnifera tablets | 2 | 25.5 |

### Wholesale-intent queries with generic titles

| Query | Impr | Pos | Landing page |
|---|---:|---:|---|
| cordyceps mushroom wholesale | 6 | 36.2 | cordyceps.html |
| lion's mane mushroom wholesale | 6 | 36.2 | lions-mane.html |
| medicinal mushrooms wholesale | 3 | 36.0 | products.html |
| mushroom powder dual extract | 9 | 59.9 | extracts-dual.html |
| dual extract mushroom powder | 2 | 42.5 | extracts-dual.html |
| mushroom products | 9 | 51.1 | products.html |
| reishi ganoderma mushroom liquid extract | 2 | 65.5 | reishi.html |
| ganoderma spore powder | 1 | 32.0 | reishi.html |

### Supplier-side queries (working, keep protecting)

| Query | Impr | Pos | Clicks |
|---|---:|---:|---:|
| where to sell mushroom in india | 9 | 20.4 | 1 |
| where to sell | 6 | 3.8 | 0 |
| cordyceps mushroom buyers | 4 | 1.0 | 0 |
| where to sell cordyceps militaris in india | 2 | 7.5 | 1 |
| who will buy | 3 | 6.7 | 0 |
| any buyers | 1 | 4.0 | 0 |
| cordyceps militaris mushroom buyers in india | 3 | 22.0 | 0 |

---

## 4. Actions shipped in this commit

| # | Change | Target query cluster | Page |
|---|---|---|---|
| 1 | Retitle ashwagandha page around "bulk ashwagandha root wholesale — withania somnifera powder, granules & extract"; meta desc names "bulk", "granules", "tablets", "wholesale", "price" | 12 ashwagandha-bulk queries pos 19-22 | `products/ashwagandha.html` |
| 2 | Retitle cordyceps page to include "Cordyceps Militaris Wholesale — Cordyceps Mushroom Powder Bulk Supplier India" | "cordyceps mushroom wholesale" pos 36, "cordyceps militaris mushroom buyers in india" pos 22 | `products/cordyceps.html` |
| 3 | Retitle lion's mane page to include "Lion's Mane Mushroom Wholesale — Hericium Erinaceus Bulk Supplier India" | "lion's mane mushroom wholesale" pos 36 | `products/lions-mane.html` |
| 4 | Retitle reishi page to include "Reishi Ganoderma Wholesale — Ganoderma Lucidum Powder, Spore & Liquid Extract"; meta desc names spore powder + liquid extract | "reishi ganoderma mushroom liquid extract", "ganoderma spore powder" | `products/reishi.html` |
| 5 | Retitle extracts-dual page to lead with "Mushroom Powder Dual Extract" (matches literal query, hyphen removed from lead) | "mushroom powder dual extract" pos 60, "dual extract mushroom powder" pos 42 | `products/extracts-dual.html` |
| 6 | Retitle products catalogue to "Mushroom Products India — Medicinal Mushrooms Wholesale Catalogue" | "mushroom products" pos 51, "medicinal mushrooms wholesale" pos 36 | `products.html` |
| 7 | Retitle button page around "Button Mushroom Wholesale India — Agaricus Bisporus Fresh, Dried & Canned Bulk Supply" | 78 impressions / 0 clicks bleed | `products/button.html` |
| 8 | Retitle oyster page around "Oyster Mushroom Wholesale India — Pleurotus Pearl, Pink, Blue & King" | 33 impressions / 0 clicks | `products/oyster.html` |
| 9 | Retitle tulsi page around "Bulk Tulsi / Holy Basil Wholesale — Ocimum Sanctum" | 22 impressions / 0 clicks | `products/tulsi.html` |
| 10 | Sharpen buyers.html title with location + turnaround signal | 40 impressions / 0 clicks pos 7.7 | `buyers.html` |
| 11 | Add supplier signal to homepage meta desc without diluting brand primacy | "cordyceps mushroom buyers" pos 1 / 0 clicks | `index.html` |

---

## 5. Not shipped in this commit — needs judgement

- **USA 0.2% CTR (595 impressions).** Snippet reads India-heavy; US buyers may be scrolling past. Need to know which queries are driving those US impressions before we tune country-specific language. Recommend one more GSC pull with `country` + `query` breakdown next week.
- **Country-specific meta on export pages** (`exports/usa.html`, `exports/uk.html`, etc.). GSC impressions on those pages are still small; wait 30-60 days for Google to reindex the current buyer-first content.
- **Body-content tuning on ashwagandha.** Meta rewrite alone can move pos 20 → pos 10-12. To break into top 5 for the bulk-ashwagandha queries we probably need a short "granules / tablets / powder / extract — bulk formats we supply" section on the page itself.
