# GSC Diagnosis — goodmushroom.in (2026-04-29)

Source: live query of Google Search Console API via service account `emberwood-seo-reader@emberwood-seo.iam.gserviceaccount.com`.

## TL;DR

**There is no crawl failure.** The sitemap reports `errors: 0, warnings: 0`. What you may have seen as "last crawl failed" is actually:

- Sitemap submission says `submitted: 8, indexed: 0` — this counter is misleading/stale; URL Inspection confirms 4 of 8 URLs are in fact `Submitted and indexed`.
- The remaining 4 URLs (`buyers`, `faq`, `about`, `contact`) come back as **"URL unknown to Google"** — Google hasn't crawled them yet. This is a *discovery* problem, not a crawl error.

## Detail

### Property
- URL-prefix property `https://goodmushroom.in/` — service account has `siteFullUser`.
- No domain property (`sc-domain:goodmushroom.in`) exists. Worth adding so subdomains and protocol variants are covered.

### Sitemap
- Path: `https://goodmushroom.in/sitemap.xml`
- Last submitted: 2026-04-19
- Last downloaded: 2026-04-19
- Errors: 0, Warnings: 0
- Submitted: 8, Indexed: 0 *(misleading — see per-URL section below)*

### Per-URL state (live URL Inspection)

| URL | Verdict | Coverage | Last crawl |
|---|---|---|---|
| `/` | PASS | Submitted and indexed | 2026-04-21 |
| `/products.html` | PASS | Submitted and indexed | 2026-04-19 |
| `/farmers.html` | PASS | Submitted and indexed | 2026-03-31 |
| `/privacy.html` | PASS | Submitted and indexed | 2026-04-13 |
| `/buyers.html` | NEUTRAL | **URL is unknown to Google** | never |
| `/faq.html` | NEUTRAL | **URL is unknown to Google** | never |
| `/about.html` | NEUTRAL | **URL is unknown to Google** | never |
| `/contact.html` | NEUTRAL | **URL is unknown to Google** | never |

All 4 indexed pages: `pageFetch=SUCCESSFUL`, `robots=ALLOWED`, `crawledAs=MOBILE`, canonical matches user-declared canonical. No technical issues.

### Search performance (last 28 days)

Total clicks across the whole site: **5** (all to `/`).

Top queries (impressions only, no clicks):
- `where to sell mushroom in india` — pos 43, 2 impressions
- `mushroom herbal products india` — pos 17, 1 impression
- `buyer in india` — pos 1 (1 impression — likely a brand-adjacent click)

Top pages by impressions:
- `/` — 100 impr / 5 clicks
- `/products.html` — 35 impr / 0 clicks
- `/farmers.html` — 28 impr / 0 clicks

The query `where to sell mushroom in india` validates the per-product Sell-to-Us pages we're about to build.

## Why 4 pages are "unknown to Google"

The most likely cause given everything else is healthy: **internal linking strength is low**. Google prefers to discover URLs by crawling links from already-indexed pages, not just from sitemaps. If `buyers.html` is only linked from the nav and footer (which Google sees on many pages but rates low), and there are no in-content links to it from `/`, discovery is slow.

Other contributing factors that are *not* the cause but worth knowing:
- New site (only ~6 weeks of GSC history visible).
- Low overall crawl budget for a freshly verified property.
- Sitemap dates set to `2026-04-19` for every URL — Google sees no recency signal between pages.

## Fixes to apply (in upcoming redesign + deploy)

These are not in scope for this session per your instruction ("diagnose only"), but the redesign work in this same PR will incidentally fix several of them:

1. **Strengthen internal links** — `index.html` already links to `products.html` from hero and product cards; we'll add prominent in-content links to `buyers.html`, `farmers.html`, `faq.html`, `about.html`, `contact.html` from the home page (the redesign already plans this in the trust band + dual CTA strip). Likely the single biggest fix.
2. **Per-page `lastmod`** — when we update pages, we'll set distinct `lastmod` dates in `sitemap.xml` so Google has recency differentiation.
3. **Re-submit sitemap** after deploy so the 12 new product URLs get discovered.
4. **Request indexing manually** for the 4 unknown URLs via the GSC UI ("Inspect URL" → "Request indexing"). The API does not expose this.
5. **Add `sc-domain:goodmushroom.in` domain property** to consolidate any www / non-www / http variants under one report.
6. **Consider an HTML sitemap or "Browse all pages" footer block** — gives crawlers another path.

## Other sites the service account can see

(For your reference — these have nothing to do with the goodmushroom diagnosis.)
- `sc-domain:uyut.in` — siteOwner
- `https://algea.in/` — siteOwner
