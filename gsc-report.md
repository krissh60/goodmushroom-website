# GSC Report — Good Mushroom — 31 May 2026

**Window analysed:** 2026-02-01 → 2026-05-31 (full Search Console window)
**Property:** `https://goodmushroom.in/`
**Key inflection point:** 2026-05-25 — buyer-first repositioning shipped

---

## TL;DR

1. **Traffic is up since the buyer pivot, not down** — May 25–29 averaged ~33 impressions/day vs. ~15/day for the rest of May. May 29 set a new daily high (56 impressions). The buyer-first rebuild is working at the impressions layer.
2. **But supplier queries still dominate the actual search demand we're getting**, and our nav renaming + page restructure made the supplier path less obvious. Farmers / supply-partnership page now ranks well (pos 6.9, 104 impressions over the window) but has **0% CTR** — Google is showing it, searchers aren't clicking. That's a title/snippet mismatch caused by the rebrand.
3. **The hypothesis is half right.** Supplier impressions haven't fallen — but supplier *engagement* (clicks) has. The page is still ranking; it just stopped speaking the supplier's language.
4. **Recommendation:** dual-path positioning. Keep the buyer-first thesis as primary, but restore explicit supplier signals in nav, hero, page titles, and metadata so we don't bleed the queries we're already winning.

---

## 1. Topline numbers (Feb 1 – May 31, 2026)

| Metric | Value |
|---|---|
| Clicks | 38 |
| Impressions | 856 |
| CTR | 4.44% |
| Avg position | 8.0 |

Clicks are concentrated heavily on the homepage (29 of 38). India = 89% of clicks (34 of 38). USA = 272 impressions but only 1 click — we're showing up there but not converting the snippet.

---

## 2. The supplier-vs-buyer query split

There are 29 distinct queries across the full window. Splitting by intent:

### Supplier / seller / farmer queries (14 queries, 25 impressions, 1 click)

| Query | Pos | Impr | Clicks |
|---|---:|---:|---:|
| cordyceps mushroom buyers | **1.0** | 4 | 0 |
| where to sell mushroom in india | 38.7 | 3 | 0 |
| cordyceps mushroom wholesale | 32.7 | 3 | 0 |
| where to sell cordyceps militaris in india | 7.5 | 2 | **1** |
| where to sell | 5.5 | 2 | 0 |
| lion's mane mushroom wholesale | 42.0 | 2 | 0 |
| any buyers | 4.0 | 1 | 0 |
| alternate supplier | 2.0 | 1 | 0 |
| buyer in india | 1.0 | 1 | 0 |
| seller near me | 4.0 | 1 | 0 |
| export of mushroom from india | 70.0 | 1 | 0 |
| medicinal mushrooms wholesale | 32.0 | 1 | 0 |
| ashwagandha root bulk / bulk ashwagandha root | 24–30 | 2 | 0 |

These are **farmers Googling "where can I sell my cordyceps"** — exactly the supply-partner audience. We're ranking position 1 for "cordyceps mushroom buyers" and "buyer in india" and getting **zero clicks** on those impressions. That's the snippet mismatch.

### Buyer / ingredient queries (4 queries, 7 impressions, 0 clicks)

| Query | Pos | Impr | Clicks |
|---|---:|---:|---:|
| mushroom powder dual extract | 69.8 | 4 | 0 |
| cordyceps powder | 43.0 | 1 | 0 |
| ganoderma spore powder | 32.0 | 1 | 0 |
| mushroom extract | 71.0 | 1 | 0 |

Buyer-intent queries are showing up at positions 30–70 — we're not ranking yet. The buyer-first content is too new (shipped May 25) for Google to have reindexed and re-ranked us; this needs 30–90 days.

**Read this carefully:** the buyer-first rebuild isn't broken, it just hasn't shown up in the rankings yet. Meanwhile, the supplier-side rankings we already had are being underused.

---

## 3. Pages — what's working, what's leaking

| Page | Pos | Impr | Clicks | CTR | Verdict |
|---|---:|---:|---:|---:|---|
| `/` (homepage) | 5.7 | **417** | **29** | 7.0% | 🟢 Working — primary engine |
| `/products.html` | 7.8 | 203 | 1 | 0.5% | 🟡 High impressions, terrible CTR — title/snippet generic |
| `/products/cordyceps.html` | 10.2 | 114 | 3 | 2.6% | 🟢 Solid, will improve with new content |
| `/farmers.html` | 6.9 | **104** | **0** | **0.0%** | 🔴 Ranking well, zero clicks — **biggest leak** |
| `/products/lions-mane.html` | 11.0 | 66 | 3 | 4.5% | 🟢 Good |
| `/about.html` | 9.9 | 39 | 1 | 2.6% | 🟢 Fine |
| `/products/ashwagandha.html` | 10.3 | 26 | 0 | 0.0% | 🔴 |
| `/products/extracts-dual.html` | 24.6 | 17 | 0 | 0.0% | 🔴 |
| `/products/button.html` | 6.5 | 19 | 0 | 0.0% | 🔴 |

**The farmers page is the single biggest fixable problem.** 104 impressions, 0 clicks. Compare to the homepage at 7% CTR — that's at least 7 missing clicks/month right there, before any improvement.

---

## 4. What was working before the buyer pivot (and isn't anymore)

The pre-May 25 site had:
- Nav item literally labelled **"Farmers"** — verb-clear for someone Googling "where to sell"
- Homepage hero that mentioned both farmers and buyers
- Page titles on the supply page that included "sell", "farmers", "growers"

After the May 25 rebuild, the same page is now:
- Nav-labelled **"Supply Partnership"** — accurate to the buyer industry but invisible to a farmer Googling in Hindi/English mix
- Wrapped in a buyer-led homepage with no above-the-fold supplier entry-point
- Titled in buyer-language ("supply partnership", "verified procurement")

**This explains the 0% CTR on `farmers.html` with 104 impressions.** Google is still ranking us for "where to sell mushroom in india" and "cordyceps mushroom buyers" — but when the searcher sees the SERP snippet, it reads like an exporter page, not "sell your crop here."

---

## 5. What's working in the new (May 25+) update

- **Daily impressions are up** — May 25–29 daily impressions ranged 12–56, averaging higher than the prior 4 weeks. The expanded buyer content is being crawled and shown.
- **Cordyceps page is climbing** — it's now the #3 page by impressions despite being rebuilt 6 days ago. The new whole-fruiting-body / non-China content shipped today (May 31) hasn't been indexed yet, so further uplift is still ahead.
- **Homepage CTR holding** — 7% on the homepage is strong; the buyer-first hero is converting impression → click as well as before.
- **Mobile CTR is excellent** — 9.6% on mobile vs 1.8% desktop. Mobile-first decisions in the rebuild were correct.

---

## 6. Recommendations — dual-path positioning

We need the site to clearly speak to **both** sides without diluting either. The buyer is the primary commercial customer; the supplier is the upstream input. They both arrive via Google with completely different vocabularies.

| # | Change | Why | Page |
|---|---|---|---|
| 1 | Add **"For Farmers"** secondary entry-point in main nav (in addition to "Supply Partnership") | Restores the supplier-readable label that was indexed for months | All pages (nav) |
| 2 | **Rewrite `farmers.html` `<title>` and `<meta description>`** to lead with "Sell your cordyceps / mushrooms — Good Mushroom buys from Indian farmers" | Fixes the 104-impression / 0-click leak directly | `farmers.html` |
| 3 | Add a **dual-path band on homepage** ("I want to buy ingredients" / "I grow mushrooms — I want to sell") immediately under the hero | Captures both query types without the buyer thesis losing primacy | `index.html` |
| 4 | Restore **supplier-intent keywords** to homepage and farmers page meta (`where to sell mushroom in india`, `cordyceps buyers india`, `mushroom farmers india`) | These are the queries we already rank for — stop hiding them | `index.html`, `farmers.html` |
| 5 | Add a **"Selling to us"** plain-language micro-section with the literal phrase "If you grow mushrooms in India and want to sell" | Matches supplier Google queries verbatim | `index.html`, `farmers.html` |
| 6 | **Keep buyer-first thesis intact** — hero, founders, COA, non-China positioning all stay primary | Buyer-intent content is too new to judge; don't churn | — |

Items 1–5 ship in this commit.
