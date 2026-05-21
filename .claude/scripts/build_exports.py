#!/usr/bin/env python3
"""Generate 8 export-market pages on the v4 design."""
from pathlib import Path
import html, json, importlib.util

ROOT = Path(__file__).resolve().parents[2]
spec = importlib.util.spec_from_file_location("build_pages", ROOT / ".claude/scripts/build_pages.py")
bp = importlib.util.module_from_spec(spec); spec.loader.exec_module(bp)

WA = bp.WA; SITE = bp.SITE
nav_html = bp.nav_html; footer_html = bp.footer_html
page_head = bp.page_head

MARKETS = [
  dict(slug='usa', country='United States', flag='🇺🇸', cities='New York · Los Angeles · Miami',
       regulators='FDA · USDA NOP · USP', freight='Air via DEL/BOM → JFK/LAX 4–6 days · Sea via Nhava Sheva → NY/LA 22–28 days',
       image='images/cordyceps.jpg',
       lede="Active US buyers in supplement, foodservice and retail. We ship to NY, LA, Miami, Chicago and Houston. FDA-aligned documentation, NOP-equivalent organic on request.",
       notes=[
         "FDA Prior Notice filed before each shipment. We provide the FDA Registration of the shipper.",
         "USDA NOP-equivalent organic available via NPOP certification on request — 30-day lead time for the certifier audit.",
         "USP / NSF supplement-grade specs supported. Cordyceps cordycepin, lion's mane hericenones, reishi triterpenes all HPLC-verifiable to your spec.",
         "Customs broker briefing available — we share the import dossier with your broker before goods arrive.",
       ]),
  dict(slug='uk', country='United Kingdom', flag='🇬🇧', cities='London · Manchester · Birmingham',
       regulators='FSA · Soil Association · Defra',
       freight='Air → LHR/MAN 5–7 days · Sea via Felixstowe 24–30 days',
       image='images/shiitake.jpg',
       lede="UK supplement brands and importers in London, Manchester, Birmingham and the South-East. FSA-aligned docs, Soil Association on request.",
       notes=[
         "Post-Brexit GB import documentation handled — we update commercial invoice + COA to current FSA/Defra formats.",
         "Soil Association organic certification arrangeable through certifier partners (60-day lead).",
         "Common shipping route: airfreight Mumbai → Heathrow for sub-100 kg, sea via Felixstowe for full pallets.",
       ]),
  dict(slug='uae', country='United Arab Emirates', flag='🇦🇪', cities='Dubai · Abu Dhabi · Sharjah',
       regulators='ESMA · MoCCAE · Dubai Municipality',
       freight='Air → DXB 3–4 days · Sea via Jebel Ali 14–18 days',
       image='images/extract.jpg',
       lede="Active UAE buyers across Dubai, Abu Dhabi, Sharjah. Halal-certifiable, ESMA-aligned import dossier, fast turnaround thanks to weekly Mumbai-Dubai air freight.",
       notes=[
         "Halal certification routed through certified partners on request.",
         "ESMA conformity (EQM scheme) — we provide pre-aligned product files for supplement-grade products.",
         "Frequent route — air cargo 3–4 days, sea 14–18 days. Reefer available for cold-chain.",
       ]),
  dict(slug='japan', country='Japan', flag='🇯🇵', cities='Tokyo · Osaka · Yokohama',
       regulators='MHLW · JAS · Food Sanitation Act',
       freight='Air → NRT/HND 5–7 days · Sea via Yokohama 20–25 days',
       image='images/reishi.jpg',
       lede="Japan supplement and food markets — Tokyo, Osaka, Yokohama. MHLW-aligned documentation, JAS Organic available on request.",
       notes=[
         "Japan Food Sanitation Act compliance: we test for heavy metals + pesticides to MHLW reference limits and include the lab report.",
         "JAS Organic certification possible through Japanese certifier partners (90-day lead).",
         "Reishi (G. lucidum) and shiitake are particularly active categories in Japan — we have established lab parameters that match common Japanese supplement specs.",
       ]),
  dict(slug='south-korea', country='South Korea', flag='🇰🇷', cities='Seoul · Busan · Incheon',
       regulators='MFDS · KFDA',
       freight='Air → ICN 5–7 days · Sea via Busan 18–22 days',
       image='images/lions-mane.jpg',
       lede="Korean supplement and functional food market — Seoul, Busan, Incheon. MFDS-aligned import dossier, mushroom-extract HPLC specs matching KFDA monograph requirements.",
       notes=[
         "MFDS import declaration handled — we provide product specification, lab tests, ingredient list in KFDA format.",
         "Cordyceps cordycepin and lion's mane hericenones are popular Korean supplement actives — we have HPLC methods aligned to KFDA monograph requirements.",
         "Common route: air via Mumbai/Delhi → Incheon 5–7 days.",
       ]),
  dict(slug='singapore', country='Singapore', flag='🇸🇬', cities='Singapore',
       regulators='SFA · HSA',
       freight='Air → SIN 3–4 days · Sea 8–12 days',
       image='images/oyster.jpg',
       lede="Singapore food, foodservice and supplement market. SFA-aligned, HSA Health Supplements regulatory framework supported.",
       notes=[
         "Singapore is one of our fastest turnaround markets — 3–4 days air, 8–12 days sea, no transhipment.",
         "HSA Health Supplements category supported — we provide product dossiers aligned to current HSA requirements.",
         "Common categories: lion's mane, cordyceps and reishi extracts for HSA-registered supplement brands.",
       ]),
  dict(slug='australia', country='Australia', flag='🇦🇺', cities='Sydney · Melbourne · Brisbane · Perth',
       regulators='TGA · DAFF · FSANZ',
       freight='Air → SYD/MEL 7–9 days · Sea 22–28 days',
       image='images/herbs.jpg',
       lede="Australian importers across Sydney, Melbourne, Brisbane, Perth. TGA-aligned, DAFF biosecurity-ready, FSANZ food standards documented.",
       notes=[
         "DAFF biosecurity inspection at port-of-entry — we package and document to minimise hold-ups (no soil residue, clean fibre drums, full provenance).",
         "TGA Listed Medicine ingredient specs supported — common categories like cordyceps and lion's mane have established AUST-L pathways.",
         "FSANZ food-grade certification for our shiitake / oyster / button categories.",
       ]),
  dict(slug='canada', country='Canada', flag='🇨🇦', cities='Toronto · Vancouver · Montreal',
       regulators='CFIA · Health Canada · NHPD',
       freight='Air → YYZ/YVR 6–8 days · Sea via Vancouver 24–28 days',
       image='images/button.jpg',
       lede="Canadian supplement and natural-health-products market — Toronto, Vancouver, Montreal. CFIA-aligned, NPN registration support on request.",
       notes=[
         "Health Canada NPN (Natural Product Number) registration support — we provide product specification, evidence summary, and CMP-aligned manufacturing data.",
         "CFIA Safe Food for Canadians (SFCR) — we register the export shipment and provide a CFIA-compliant COA.",
         "Active categories: cordyceps, lion's mane, reishi, ashwagandha and triphala blends for NHP brands.",
       ]),
]


def build_market(m):
    canonical = f'{SITE}/exports/{m["slug"]}.html'
    schema = {
      "@context":"https://schema.org","@type":"WebPage",
      "name": f'Mushroom Export to {m["country"]}',
      "url": canonical,
      "publisher": {"@type":"Organization","name":"Good Mushroom","url":SITE}
    }

    head = page_head(
      title=f'Mushroom Export to {m["country"]} · Good Mushroom',
      description=m["lede"],
      canonical=canonical,
      image=f'{SITE}/{m["image"]}',
      extra_schema=schema,
      keywords=f"mushroom export {m['country']}, {m['country']} mushroom importer, Indian mushroom supplier {m['country']}",
      prefix='../',
    )
    nav = nav_html('../')
    foot = footer_html('../')

    notes_html = '\n'.join(
      f'      <li style="display:flex; gap:14px; align-items:start;"><span class="mono" style="color:var(--brand); padding-top:2px;">·</span><span>{html.escape(n)}</span></li>'
      for n in m["notes"]
    )

    hero = f'''<section class="page-hero">
  <div class="wrap">
    <nav class="breadcrumb">
      <a href="../index.html">Home</a><span class="sep">/</span>
      <a href="../exports.html">Export Markets</a><span class="sep">/</span>
      <span>{html.escape(m["country"])}</span>
    </nav>
    <div class="page-hero-inner">
      <div class="reveal">
        <span class="eyebrow">Export market</span>
        <h1>{html.escape(m["country"])}<br><em>{m["flag"]} · {html.escape(m["cities"])}</em></h1>
        <p class="lede">{html.escape(m["lede"])}</p>
        <div style="margin-top: 32px; display:flex; gap:12px; flex-wrap:wrap;">
          <a href="../contact.html#buyer" class="btn btn-primary">Get a quote for {html.escape(m["country"])} →</a>
          <a href="https://wa.me/{WA}" class="btn btn-outline">WhatsApp us</a>
        </div>
      </div>
      <div class="page-hero-art reveal">
        <img src="../{m["image"]}" alt="Export to {html.escape(m['country'])}" loading="eager" />
        <span class="page-hero-art-caption">Shipping · {html.escape(m["cities"].split(' · ')[0])}</span>
      </div>
    </div>
  </div>
</section>'''

    body = f'''<section>
  <div class="wrap">
    <div class="two-up">
      <div class="reveal">
        <span class="eyebrow">Compliance &amp; routing</span>
        <h2 class="h2" style="margin-top: 20px;">What we handle<br>for {html.escape(m["country"])}.</h2>
        <p style="color:var(--ink-mid); margin-top: 24px; max-width: 50ch;">Every shipment leaves with a complete, country-specific compliance pack. Your broker doesn't have to chase anything.</p>
        <div class="spec-list" style="margin-top: 28px;">
          <div class="spec-row"><div class="spec-key">Regulators</div><div class="spec-val">{html.escape(m["regulators"])}</div></div>
          <div class="spec-row"><div class="spec-key">Freight</div><div class="spec-val">{html.escape(m["freight"])}</div></div>
          <div class="spec-row"><div class="spec-key">Cities served</div><div class="spec-val">{html.escape(m["cities"])}</div></div>
        </div>
      </div>
      <div class="reveal">
        <h3 class="h3" style="margin-bottom: 24px;">Country notes</h3>
        <ul style="list-style:none; display:flex; flex-direction:column; gap:18px;">
{notes_html}
        </ul>
      </div>
    </div>
  </div>
</section>

<section class="sec-bone-2">
  <div class="wrap">
    <header class="sec-head reveal">
      <div><span class="eyebrow">Most-shipped to {html.escape(m["country"])}</span><h2 class="h2">What buyers<br>order most.</h2></div>
      <div class="sec-head-end"><p>The four product lines that move most consistently into {html.escape(m["country"])}. Each links to its product page with full specs.</p></div>
    </header>
    <div class="cat-grid reveal-stagger">
      <a href="../products/cordyceps.html" class="cat-card">
        <div class="cat-card-image"><img src="../images/cordyceps.jpg" alt="Cordyceps" loading="lazy" /><span class="cat-card-tag">10 kg MOQ</span></div>
        <div class="cat-card-body"><h3>Cordyceps</h3><span class="cat-card-latin">Cordyceps militaris</span><div class="cat-card-meta"><span>Cordycepin 5–8%</span><span class="arr">→</span></div></div>
      </a>
      <a href="../products/lions-mane.html" class="cat-card">
        <div class="cat-card-image"><img src="../images/lions-mane.jpg" alt="Lion's Mane" loading="lazy" /><span class="cat-card-tag">Extract 8:1</span></div>
        <div class="cat-card-body"><h3>Lion's Mane</h3><span class="cat-card-latin">Hericium erinaceus</span><div class="cat-card-meta"><span>Hericenones verified</span><span class="arr">→</span></div></div>
      </a>
      <a href="../products/reishi.html" class="cat-card">
        <div class="cat-card-image"><img src="../images/reishi.jpg" alt="Reishi" loading="lazy" /><span class="cat-card-tag">Triterpenes &gt;35%</span></div>
        <div class="cat-card-body"><h3>Reishi</h3><span class="cat-card-latin">Ganoderma lucidum</span><div class="cat-card-meta"><span>Dual extract · spore oil</span><span class="arr">→</span></div></div>
      </a>
      <a href="../products/extracts-dual.html" class="cat-card">
        <div class="cat-card-image"><img src="../images/extract.jpg" alt="Dual extract" loading="lazy" /><span class="cat-card-tag">OEM / white-label</span></div>
        <div class="cat-card-body"><h3>Dual-Extract Powders</h3><span class="cat-card-latin">8:1 to 20:1</span><div class="cat-card-meta"><span>OEM / supplement-ready</span><span class="arr">→</span></div></div>
      </a>
    </div>
  </div>
</section>

<section class="sec-dark">
  <div class="wrap">
    <div class="reveal" style="max-width: 760px; margin: 0 auto; text-align: center;">
      <span class="eyebrow">Start your {html.escape(m["country"])} order</span>
      <h2 class="h1" style="color: var(--bone); margin-top: 20px;">Quote in 24 hours.<br><em>Samples in a week</em>.</h2>
      <p class="lede" style="color: rgba(255,255,255,0.7); margin: 24px auto 0; max-width: 56ch;">Tell us what you need and we'll come back with pricing, lead time and the {html.escape(m["country"])}-specific compliance pack inside one business day.</p>
      <div style="margin-top: 36px; display: flex; gap: 12px; justify-content: center; flex-wrap: wrap;">
        <a href="../contact.html#buyer" class="btn btn-on-dark btn-lg">Request a quote →</a>
        <a href="https://wa.me/{WA}" class="btn btn-outline-on-dark btn-lg">WhatsApp us</a>
      </div>
    </div>
  </div>
</section>'''

    out = f"{head}\n<body>\n\n{nav}\n\n{hero}\n\n{body}\n\n{foot}\n</body>\n</html>\n"
    (ROOT / 'exports' / f'{m["slug"]}.html').write_text(out, encoding='utf-8')
    return len(out)


def main():
    print("Export-market pages:")
    for m in MARKETS:
        size = build_market(m)
        print(f"  wrote exports/{m['slug']}.html  ({size} bytes)")

if __name__ == '__main__':
    main()
