#!/usr/bin/env python3
"""Generate 12 product detail pages on the v4 editorial design."""
from pathlib import Path
import html, json, importlib.util

ROOT = Path(__file__).resolve().parents[2]
spec = importlib.util.spec_from_file_location("build_pages", ROOT / ".claude/scripts/build_pages.py")
bp = importlib.util.module_from_spec(spec); spec.loader.exec_module(bp)

WA = bp.WA; SITE = bp.SITE
nav_html = bp.nav_html; footer_html = bp.footer_html
page_head = bp.page_head

PRODUCTS = [
    dict(slug='cordyceps', name='Cordyceps Militaris', latin='Cordyceps militaris',
        category='Medicinal mushroom', image='images/cordyceps.jpg',
        tagline="Lab-cultivated. Cordycepin 5–8%. <em>Fully traceable</em> from substrate to softgel.",
        lede="High-altitude cultivated Cordyceps militaris from Indian farms. Dried fruiting body, mesh-100 powder, and 8:1–20:1 dual extracts. Cordycepin and adenosine verified by HPLC, NABL COA per batch, MOQ 10 kg.",
        keywords="buy cordyceps militaris India, cordyceps wholesale India, cordyceps exporter India, cordyceps powder bulk",
        specs=[
          ('Forms','Dried fruiting body · powder · dual extract 8:1–20:1'),
          ('MOQ','10 kg dried · 5 kg extract first order'),
          ('Lead time','10–14 days from PO'),
          ('Cordycepin','5–8% (HPLC)'),
          ('Adenosine','0.3–0.6%'),
          ('Lab','HPLC actives · ICP-MS heavy metals · micro · pesticides — per batch'),
          ('Certs','FSSAI · NABL COA. Organic / Kosher / Halal on request'),
          ('Packaging','Vacuum-sealed mylar · 5/10/25 kg fibre drums'),
        ],
        faqs=[
          ('Cultivated or wild?','Strictly Cordyceps militaris, indoor cultivated. We do not handle wild C. sinensis (CITES-listed). Cultivated militaris matches or exceeds wild cordycepin in published studies.'),
          ('Can you supply organic-certified?','Yes — NPOP and USDA NOP-equivalent organic batches with 30-day lead time.'),
          ('Do you ship to USA / EU / UAE?','Yes. Air for < 100 kg, sea for larger. Full export docs included (phyto-sanitary, COA, invoice, packing list).'),
        ],
    ),
    dict(slug='shiitake', name='Shiitake', latin='Lentinula edodes',
        category='Culinary + medicinal mushroom', image='images/shiitake.jpg',
        tagline="Donko-grade, koshin, sliced and powdered. <em>Beta-glucan</em> verified.",
        lede="Premium shiitake from Indian farms — fresh cold-chain, dried whole and sliced, mesh-100 powder. Donko thick-cap and koshin flat-cap grades, lentinan present, ergosterol verified.",
        keywords="buy shiitake India, shiitake wholesale India, dried shiitake exporter, shiitake powder bulk India",
        specs=[
          ('Forms','Fresh (cold-chain) · dried whole donko/koshin · sliced · powder'),
          ('MOQ','100 kg fresh/week · 50 kg dried · 25 kg powder'),
          ('Lead time','Fresh 3–5 days · dried 10–14 · powder 14–21'),
          ('Beta-glucan','20–35% (powder)'),
          ('Moisture','Fresh 88–92% · dried < 12%'),
          ('Lab','Heavy metals · microbiology · mycotoxins'),
          ('Certs','FSSAI · COA per shipment · Organic on request'),
          ('Packaging','Fresh 5 kg vented crates · Dried 1–25 kg vacuum, fibre drum'),
        ],
        faqs=[
          ('Donko vs koshin?','Donko are thick-cap, partially-open, cracked tops — premium priced. Koshin are flat, fully-open caps — better for slicing and powder.'),
          ('Supplement-grade powder?','Yes — mesh 80–120, beta-glucan tested, food-grade vacuum in fibre drums.'),
          ('Fresh shiitake export?','By air to UAE, Singapore, GCC. Sea routes too long for fresh — switch to dried for those markets.'),
        ],
    ),
    dict(slug='lions-mane', name="Lion's Mane", latin='Hericium erinaceus',
        category='Medicinal mushroom', image='images/lions-mane.jpg',
        tagline="Whole fruiting body. <em>Hericenones</em> + erinacines verified.",
        lede="Indoor-cultivated Lion's Mane (Hericium erinaceus). White, fully-formed heads dried under controlled conditions. Hericenones from fruiting body, erinacines from mycelium — both HPLC verifiable per batch.",
        keywords="buy lion's mane India, lion's mane extract supplier India, hericium erinaceus wholesale",
        specs=[
          ('Forms','Whole dried · powder · dual extract 8:1'),
          ('MOQ','20 kg dried · 10 kg powder · 5 kg extract'),
          ('Lead time','14–21 days'),
          ('Beta-glucan','25–40%'),
          ('Actives','Hericenones · erinacines verified by HPLC'),
          ('Lab','HPLC actives · heavy metals · micro · pesticides'),
          ('Certs','FSSAI · COA per shipment · Kosher/Organic on request'),
          ('Packaging','Vacuum-sealed 1–25 kg · fibre drum outer'),
        ],
        faqs=[
          ('Powder or extract?','Both. Powder = whole dried mushroom, mesh 100. Extract = 8:1 dual (water + ethanol), >25% beta-glucan.'),
          ('Mycelium or fruiting body?','100% fruiting body. We can source mycelium-on-grain separately if specifically required.'),
          ('Hericenone quantification?','HPLC per batch on request.'),
        ],
    ),
    dict(slug='oyster', name='Oyster Mushrooms', latin='Pleurotus spp.',
        category='Culinary mushroom', image='images/oyster.jpg',
        tagline="Pearl · pink · blue · king. <em>India's most-grown</em> gourmet mushroom.",
        lede="Pearl (P. ostreatus), pink (P. djamor), blue (P. ostreatus var. florida) and king oyster (P. eryngii). Fresh cold-chain for regional buyers, dried and powder for export.",
        keywords="buy oyster mushroom India, oyster mushroom wholesale, pleurotus supplier, king oyster buyer",
        specs=[
          ('Varieties','Pearl · pink · blue · king'),
          ('Forms','Fresh · dried whole · sliced · powder'),
          ('MOQ','100 kg fresh/week · 50 kg dried'),
          ('Shelf life','Fresh 5–7 days at 2–4°C · dried 18 months'),
          ('Beta-glucan','18–30% in dried · ergothioneine present'),
          ('Lab','Heavy metals · microbiology per batch'),
          ('Certs','FSSAI · COA on request'),
          ('Packaging','Fresh 200g/500g/2kg punnets in 5 kg crates · Dried vacuum 1–25 kg'),
        ],
        faqs=[
          ('Which variety to order?','Pearl most versatile. Pink for restaurants. King for premium foodservice — densest texture.'),
          ('Fresh oyster export?','Air to UAE, Singapore, Sri Lanka. Longer routes: switch to dried.'),
          ('Substrate?','Pasteurised straw or supplemented sawdust. Tested for residue.'),
        ],
    ),
    dict(slug='reishi', name='Reishi / Ganoderma', latin='Ganoderma lucidum',
        category='Medicinal mushroom', image='images/reishi.jpg',
        tagline="Whole · sliced · powder · dual extract · <em>CO₂ spore oil</em>.",
        lede="Cultivated Ganoderma lucidum from Indian farms — whole fruiting body, mesh-100 powder, 10:1 dual extract, broken-shell spore powder, and supercritical CO₂ spore oil. Triterpenes and beta-glucan HPLC-verified.",
        keywords="buy reishi India, ganoderma lucidum supplier, reishi extract wholesale, reishi spore oil bulk",
        specs=[
          ('Forms','Whole · sliced · powder · 10:1 extract · broken-shell spore · spore oil'),
          ('MOQ','10 kg whole/sliced · 5 kg powder/extract · 1 kg spore oil'),
          ('Lead time','14–28 days for spore oil · 10–14 for powder'),
          ('Triterpenes','>2% (powder) · >35% (spore oil)'),
          ('Beta-glucan','>25%'),
          ('Lab','HPLC triterpenes · beta-glucan · heavy metals · micro'),
          ('Certs','FSSAI · COA per batch · spore oil softgel-ready'),
          ('Packaging','Vacuum 1–25 kg · spore oil in food-grade HDPE under nitrogen'),
        ],
        faqs=[
          ('Softgel-ready spore oil?','Yes — CO₂ extracted, triterpenes >35%, packaged under N₂. Direct softgel encapsulation suitable.'),
          ('Red, black or shiro?','Primarily red (G. lucidum). Black (G. sinense) and antlered on request, longer lead times.'),
          ('Triterpene profile by HPLC?','Yes per batch — ganoderic acid A, B, C₂, D, F, DM standard markers.'),
        ],
    ),
    dict(slug='button', name='Button & Specialty Mushrooms', latin='Agaricus bisporus',
        category='Culinary mushroom', image='images/button.jpg',
        tagline="White · crimini · portobello. <em>India's largest</em> cultivated category.",
        lede="White button (A. bisporus), crimini (brown button), portobello (mature crimini) from Maharashtra, Punjab and Himachal — India's button mushroom belts. Fresh cold-chain, dried, sliced, powder, canned in brine.",
        keywords="buy button mushroom India, agaricus bisporus wholesale, crimini supplier India, portobello India, canned button mushroom export",
        specs=[
          ('Varieties','White button · crimini · portobello'),
          ('Forms','Fresh whole/sliced · dried · powder · canned in brine'),
          ('MOQ','200 kg fresh/week · 100 kg dried · 50 kg powder'),
          ('Shelf life','Fresh 7–10 days · canned 24 months · dried 18 months'),
          ('Lab','Heavy metals · microbiology · mycotoxins'),
          ('Certs','FSSAI · HACCP-compatible canning'),
          ('Packaging','Fresh 250 g/500 g/1 kg punnets · Canned 400 g/800 g/A10'),
          ('Origin','Maharashtra · Punjab · Himachal'),
        ],
        faqs=[
          ('White, crimini, portobello?','Same species, different maturity. White youngest, portobello fully mature. Pricing rises with maturity.'),
          ('Canned button?','Yes — 400/800 g tins or A10 cans, brine, HACCP facility, 24-month shelf life.'),
          ('Organic substrate?','Available with longer lead time.'),
        ],
    ),
    dict(slug='extracts-dual', name='Dual-Extract Mushroom Powders', latin='Water + alcohol',
        category='Extract', image='images/extract.jpg',
        tagline="8:1 to 20:1. <em>Beta-glucan</em> and triterpenes verified.",
        lede="Bulk dual-extract powders — cordyceps, lion's mane, reishi, chaga, turkey tail, maitake, shiitake. Water + ethanol extraction at 8:1 to 20:1. Spray-dried, mesh 80–120, supplement-ready.",
        keywords="mushroom extract supplier India, dual extract powder India, beta-glucan mushroom extract, supplement-grade mushroom extract bulk",
        specs=[
          ('Species','Cordyceps · Lion\'s Mane · Reishi · Chaga · Turkey Tail · Maitake · Shiitake'),
          ('Ratios','8:1 · 10:1 · 15:1 · 20:1'),
          ('Beta-glucan','20–40% (Megazyme assay)'),
          ('Triterpenes','Reishi >2.5% (others per spec)'),
          ('Form','Spray-dried mesh 80–120 · free-flowing'),
          ('MOQ','5 kg per species per batch'),
          ('Lab','Beta-glucan · heavy metals · micro · pesticide residue'),
          ('Certs','FSSAI · NABL COA · Organic/Kosher/Halal on request'),
        ],
        faqs=[
          ('What does 8:1 mean?','8 kg raw dried mushroom yields 1 kg finished extract. Higher ratios = more concentrated.'),
          ('Beta-glucan vs alpha-glucan?','Beta = active polysaccharide. Alpha = starch residue from substrate. We test for both, report true beta separately.'),
          ('Custom blends?','See the custom-blends product page.'),
        ],
    ),
    dict(slug='extracts-spore-oil', name='Reishi Spore Oil', latin='CO₂ supercritical',
        category='Extract', image='images/reishi.jpg',
        tagline="Triterpenes <em>>35%</em>. Softgel-ready. Packaged under nitrogen.",
        lede="Bulk reishi spore oil from broken-shell Ganoderma spores. CO₂ supercritical extraction — no solvent residue, preserves heat-sensitive triterpenes. Light-yellow oil, packaged under nitrogen.",
        keywords="reishi spore oil bulk India, ganoderma spore oil supplier, softgel-grade spore oil, CO2 spore oil India",
        specs=[
          ('Source','Broken-shell Ganoderma lucidum spores'),
          ('Extraction','Supercritical CO₂'),
          ('Triterpenes','>35% (HPLC per batch)'),
          ('Form','Light-yellow oil · packaged under N₂'),
          ('MOQ','1 kg'),
          ('Lead time','21–30 days'),
          ('Lab','HPLC triterpenes · peroxide value · heavy metals · micro'),
          ('Certs','FSSAI · COA · Halal/Kosher on request'),
        ],
        faqs=[
          ('Why CO₂?','No solvent residue. Preserves heat-sensitive triterpenes. Cleaner than hexane/ethanol.'),
          ('Shelf life?','24 months sealed under N₂, cool + dark. Once opened, refrigerate, use within 6 months.'),
          ('Softgel-ready?','Viscosity, peroxide value and active level all suitable for direct encapsulation.'),
        ],
    ),
    dict(slug='extracts-blends', name='Custom Mushroom Blend Powders', latin='OEM / White-label',
        category='Extract', image='images/extract.jpg',
        tagline="2–8 species. Your <em>formula</em>. Your brand.",
        lede="Custom mushroom blend powders for supplement brands. 2 to 8 species at your specified ratios. Spray-dried, beta-glucan blend total verified, full COA, your branding.",
        keywords="custom mushroom blend India, OEM mushroom powder, white label mushroom supplement India",
        specs=[
          ('Species pool','Cordyceps · Lion\'s Mane · Reishi · Chaga · Turkey Tail · Maitake · Shiitake · Tremella'),
          ('Blend size','2–8 species (we suggest 4–6 for balance)'),
          ('Form','Spray-dried powder · sticks · capsules · finished mix'),
          ('MOQ','25 kg per blend'),
          ('Branding','White-label or OEM packaging'),
          ('Lab','Beta-glucan blend total · heavy metals · micro · pesticides'),
          ('Lead time','21–35 days from approved formula'),
          ('Certs','FSSAI · COA per batch'),
        ],
        faqs=[
          ('Private label finished packs?','Yes — capsules, sachets, pouches. 60-day lead, minimum 500 finished units.'),
          ('How do you decide ratios?','Recommend based on target benefit, or follow your formulator\'s spec exactly.'),
          ("Typical blend?","“Big six”: Lion’s Mane 25 / Reishi 20 / Cordyceps 15 / Chaga 15 / Turkey Tail 15 / Maitake 10."),
        ],
    ),
    dict(slug='ashwagandha', name='Ashwagandha', latin='Withania somnifera',
        category='Ayurvedic herb', image='images/herbs.jpg',
        tagline="Root powder and <em>2.5–5%</em> withanolide extract.",
        lede="Bulk Ashwagandha (Withania somnifera) from Madhya Pradesh and Rajasthan — India's primary belts. Root powder mesh 80 and standardised extract (withanolides 2.5–5% by HPLC). AYUSH-licensed facility, FSSAI.",
        keywords="buy ashwagandha India, withania somnifera supplier, ashwagandha extract wholesale, KSM-66 alternative India",
        specs=[
          ('Forms','Root powder mesh 80 · standardised extract 2.5% · 5%'),
          ('MOQ','50 kg powder · 5 kg extract'),
          ('Active','Withanolides 2.5–5% (HPLC)'),
          ('Source','Madhya Pradesh · Rajasthan'),
          ('Lab','HPLC withanolides · heavy metals · micro · pesticides · aflatoxins'),
          ('Certs','FSSAI · AYUSH-licensed · COA per batch · Organic on request'),
          ('Packaging','Vacuum 1–25 kg · fibre drum'),
        ],
        faqs=[
          ('Equivalent to KSM-66?','We supply our own standardised extract at 2.5–5% withanolides. KSM-66 is a branded extract by Ixoreal Biomed — we can source it on request at brand-set pricing.'),
          ('Powder vs extract?','Powder = whole root, traditional, lower potency. Extract = concentrated, standardised — preferred for capsules.'),
          ('KSM-66 or Sensoril?','We can route those branded extracts on request, with longer lead times.'),
        ],
    ),
    dict(slug='tulsi', name='Tulsi / Holy Basil', latin='Ocimum sanctum',
        category='Ayurvedic herb', image='images/herbs.jpg',
        tagline="Dried leaf · powder · 8:1 extract · <em>steam-distilled oil</em>.",
        lede="Bulk tulsi (Ocimum sanctum) — Krishna and Rama tulsi from Karnataka, Maharashtra and MP. Whole dried leaf, mesh-80 powder, 8:1 hydroethanolic extract, and steam-distilled essential oil. Eugenol verified by GC-MS.",
        keywords="buy tulsi India, holy basil supplier India, tulsi powder bulk, tulsi essential oil exporter",
        specs=[
          ('Forms','Whole dried leaf · powder mesh 80 · 8:1 extract · steam-distilled oil'),
          ('MOQ','25 kg leaf/powder · 5 kg extract · 1 kg oil'),
          ('Actives','Eugenol 60–80% (oil) · Rosmarinic acid (extract)'),
          ('Lab','GC-MS for oil · HPLC for extract · heavy metals · micro'),
          ('Certs','FSSAI · AYUSH-licensed · IFRA-compliant on request'),
          ('Packaging','Vacuum-sealed leaf/powder · oil in food-grade aluminium under N₂'),
          ('Source','Karnataka · Maharashtra · MP'),
        ],
        faqs=[
          ('Krishna vs Rama tulsi?','Both are Ocimum sanctum. Krishna (purple-tinged) higher eugenol. Rama (green) milder. We supply both.'),
          ('Essential oil therapeutic-grade?','GC-MS verified eugenol per batch. IFRA-compliant on request.'),
          ('Tulsi vs sweet basil?','Different species. Tulsi (O. sanctum) sacred Ayurvedic herb. Sweet basil (O. basilicum) culinary. Different chemistry.'),
        ],
    ),
    dict(slug='shatavari-brahmi', name='Shatavari, Brahmi & Other Ayurvedic Herbs', latin='Multiple species',
        category='Ayurvedic herb', image='images/herbs.jpg',
        tagline="Shatavari · Brahmi · Moringa · Neem · Giloy · Amla · <em>Triphala</em> blends.",
        lede="Bulk Ayurvedic herbs from India — Shatavari (Asparagus racemosus), Brahmi (Bacopa monnieri), Moringa, Neem, Giloy, Amla, Triphala blends. AYUSH-licensed facilities, NABL labs, organic on request.",
        keywords="shatavari supplier India, brahmi powder wholesale, moringa exporter India, neem extract bulk, ayurvedic herb supplier",
        specs=[
          ('Herbs available','Shatavari · Brahmi · Moringa · Neem · Giloy · Amla · Triphala'),
          ('Forms','Root/leaf powder · hydroethanolic extracts · freeze-dried · capsule fill'),
          ('MOQ','25–50 kg per herb'),
          ('Actives','Shatavarins · Bacosides · Moringin — HPLC verified'),
          ('Lab','HPLC · heavy metals · micro · pesticides · aflatoxins'),
          ('Certs','FSSAI · AYUSH-licensed · NABL COA'),
          ('Packaging','Vacuum 1–25 kg · fibre drum'),
        ],
        faqs=[
          ('Triphala or other classics?','Yes — Triphala (Amla+Bibhitaki+Haritaki), Trikatu, Chyawanprash bases on request.'),
          ('Wild vs cultivated?','Prefer cultivated for sustainability/consistency. Wild-collected with traceable supplier on request.'),
          ('Bacosides %?','Standard 20% · 50% on request. HPLC verified per batch.'),
        ],
    ),
]


def build_product(p):
    canonical = f'{SITE}/products/{p["slug"]}.html'
    schema_product = {
      "@context": "https://schema.org", "@type": "Product",
      "name": p["name"], "description": p["lede"],
      "image": f'{SITE}/{p["image"]}',
      "brand": {"@type": "Organization", "name": "Good Mushroom"},
      "category": p["category"], "url": canonical,
      "offers": {"@type":"AggregateOffer","priceCurrency":"INR","availability":"https://schema.org/InStock",
                 "seller":{"@type":"Organization","name":"Good Mushroom","url":SITE}}
    }
    schema_faq = {
      "@context":"https://schema.org","@type":"FAQPage",
      "mainEntity": [{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in p["faqs"]]
    }
    schema_breadcrumb = {
      "@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[
        {"@type":"ListItem","position":1,"name":"Home","item":SITE+"/"},
        {"@type":"ListItem","position":2,"name":"Products","item":SITE+"/products.html"},
        {"@type":"ListItem","position":3,"name":p["name"],"item":canonical},
      ]
    }

    head = page_head(
      title=f'Buy & Sell {p["name"]} in Bulk · Good Mushroom',
      description=p["lede"],
      canonical=canonical,
      image=f'{SITE}/{p["image"]}',
      keywords=p["keywords"],
      prefix='../',
    )

    # add the extra schemas (page_head already has the first if extra_schema given; here we inject all 3)
    extra_scripts = (
        '\n  <script type="application/ld+json">\n' + json.dumps(schema_product, indent=2) + '\n  </script>\n'
        '  <script type="application/ld+json">\n' + json.dumps(schema_faq, indent=2) + '\n  </script>\n'
        '  <script type="application/ld+json">\n' + json.dumps(schema_breadcrumb, indent=2) + '\n  </script>'
    )
    head = head.replace('</head>', extra_scripts + '\n</head>')

    nav = nav_html('../')
    foot = footer_html('../')

    # ---- HERO (dark editorial w/ product image) ----
    hero = f'''<section class="page-hero" style="background:var(--brand-deep); color:var(--bone); border-bottom:1px solid rgba(255,255,255,0.08);">
  <div class="wrap">
    <nav class="breadcrumb" style="color:rgba(255,255,255,0.45);">
      <a href="../index.html" style="color:rgba(255,255,255,0.65);border-color:rgba(255,255,255,0.15);">Home</a>
      <span class="sep" style="color:rgba(255,255,255,0.3);">/</span>
      <a href="../products.html" style="color:rgba(255,255,255,0.65);border-color:rgba(255,255,255,0.15);">Products</a>
      <span class="sep" style="color:rgba(255,255,255,0.3);">/</span>
      <span>{html.escape(p["name"])}</span>
    </nav>
    <div class="page-hero-inner">
      <div class="reveal">
        <span class="eyebrow" style="color:rgba(255,255,255,0.65);">{html.escape(p["category"])}</span>
        <h1 style="color:var(--bone);">{p["tagline"]}</h1>
        <p class="lede" style="color:rgba(255,255,255,0.75);">{html.escape(p["lede"])}</p>
        <div style="margin-top:32px; display:flex; gap:12px; flex-wrap:wrap;">
          <a href="#buy" class="btn btn-on-dark btn-lg">Buy in bulk →</a>
          <a href="#sell" class="btn btn-outline-on-dark btn-lg">Sell to us</a>
        </div>
      </div>
      <div class="page-hero-art reveal">
        <img src="../{p["image"]}" alt="{html.escape(p["name"])}" loading="eager" />
        <span class="page-hero-art-caption">{html.escape(p["latin"])}</span>
      </div>
    </div>
  </div>
</section>'''

    # ---- BUY section ----
    spec_rows = '\n'.join(
      f'      <div class="spec-row"><div class="spec-key">{html.escape(k)}</div><div class="spec-val">{html.escape(v)}</div></div>'
      for k,v in p["specs"]
    )

    buy_section = f'''<section id="buy">
  <div class="wrap">
    <header class="sec-head reveal">
      <div><span class="eyebrow">For buyers</span><h2 class="h2">Buy {html.escape(p["name"])}<br>in <em>bulk</em>.</h2></div>
      <div class="sec-head-end"><p>Export-ready supply with full lab documentation and predictable lead times. Quote within 24 hours.</p></div>
    </header>

    <div class="two-up">
      <div class="reveal">
        <h3 class="h3" style="margin-bottom: 16px;">Specifications</h3>
        <div class="spec-list">
{spec_rows}
        </div>
        <div class="price-callout"><strong>Pricing:</strong> on quote — depends on volume, certifications, packaging. Share your spec via the form and we send a quote within 24 hours.</div>
      </div>

      <div class="reveal">
        <div class="form-card">
          <h3 class="h3" style="margin-bottom:8px;">Request a quote</h3>
          <p style="color:var(--ink-mid); margin-bottom:24px; font-size:var(--step--1);">Pre-filled for {html.escape(p["name"])}.</p>
          <form id="buyer-form" action="/api/contact.php" method="POST" novalidate>
            <input type="hidden" name="_subject" value="Buyer Enquiry — {html.escape(p["name"])} — Good Mushroom" />
            <input type="hidden" name="form_type" value="buyer" />
            <input type="hidden" name="product" value="{html.escape(p["name"])}" />
            <input type="hidden" name="source_page" value="products/{p["slug"]}.html" />
            <input type="text" name="website" tabindex="-1" autocomplete="off" style="position:absolute;left:-9999px;" aria-hidden="true" />
            <div class="form-row">
              <div class="form-group"><label>Full name *</label><input type="text" name="name" required placeholder="Your name" /></div>
              <div class="form-group"><label>Company</label><input type="text" name="company" placeholder="Company (optional)" /></div>
            </div>
            <div class="form-row">
              <div class="form-group"><label>Email *</label><input type="email" name="email" required placeholder="you@email.com" /></div>
              <div class="form-group"><label>WhatsApp / phone</label><input type="tel" name="phone" placeholder="+1 555 123 4567" /></div>
            </div>
            <div class="form-row">
              <div class="form-group"><label>Country *</label>
                <select name="country" required><option value="">Select…</option><option>United States</option><option>United Kingdom</option><option>Germany</option><option>France</option><option>Netherlands</option><option>UAE / Dubai</option><option>Australia</option><option>Canada</option><option>Japan</option><option>South Korea</option><option>Singapore</option><option>India</option><option>Other</option></select>
              </div>
              <div class="form-group"><label>Quantity</label><input type="text" name="quantity" placeholder="e.g. 50 kg / month" /></div>
            </div>
            <div class="form-group"><label>Message *</label><textarea name="message" required placeholder="Spec, certifications needed, packaging, target market, timeline…"></textarea></div>
            <button type="submit" class="btn btn-primary btn-lg btn-block">Send buyer enquiry →</button>
            <p class="form-note">Response within 1 business day</p>
            <div class="success-msg">✓ Thank you. We've received your enquiry and will be in touch within 24 hours.</div>
          </form>
        </div>
      </div>
    </div>
  </div>
</section>'''

    # ---- SELL section (omit for OEM blends) ----
    if p["slug"] in ("extracts-blends", "extracts-spore-oil"):
      sell_section = ''
    else:
      sell_section = f'''<section id="sell" class="sec-dark">
  <div class="wrap">
    <header class="sec-head reveal">
      <div><span class="eyebrow">For farmers</span><h2 class="h2" style="color:var(--bone);">Sell us your<br>{html.escape(p["name"])}.</h2></div>
      <div class="sec-head-end" style="color:rgba(255,255,255,0.65);"><p>We pay fair prices, settle fast, and visit farms across India for in-person QC. Net-7 for recurring suppliers.</p></div>
    </header>

    <div class="two-up">
      <div class="reveal" style="color:rgba(255,255,255,0.85);">
        <h3 class="h3" style="color:var(--bone); margin-bottom: 16px;">How we work with farmers</h3>
        <ul style="list-style:none; display:flex; flex-direction:column; gap:14px;">
          <li style="display:flex; gap:14px; align-items:start;"><span class="mono" style="color:var(--brand);">·</span><span><strong style="color:var(--bone);">Direct purchase.</strong> No middlemen. Export-grade price, not mandi price.</span></li>
          <li style="display:flex; gap:14px; align-items:start;"><span class="mono" style="color:var(--brand);">·</span><span><strong style="color:var(--bone);">Farm visits.</strong> Our team comes to you, samples on the spot, confirms price the same week.</span></li>
          <li style="display:flex; gap:14px; align-items:start;"><span class="mono" style="color:var(--brand);">·</span><span><strong style="color:var(--bone);">Net-7 repeat suppliers.</strong> Pay-on-pickup first orders. Standing agreements available.</span></li>
          <li style="display:flex; gap:14px; align-items:start;"><span class="mono" style="color:var(--brand);">·</span><span><strong style="color:var(--bone);">Help with scale.</strong> Substrate sourcing, drying, certifications — what we learn we share across the network.</span></li>
        </ul>
      </div>

      <div class="reveal">
        <div class="form-card dark">
          <h3 class="h3" style="color:var(--bone); margin-bottom:8px;">Register as a seller</h3>
          <p style="color:rgba(255,255,255,0.65); margin-bottom:24px; font-size:var(--step--1);">Pre-filled for {html.escape(p["name"])}.</p>
          <form id="seller-form" action="/api/contact.php" method="POST" novalidate>
            <input type="hidden" name="_subject" value="Seller Registration — {html.escape(p["name"])} — Good Mushroom" />
            <input type="hidden" name="form_type" value="seller" />
            <input type="hidden" name="product" value="{html.escape(p["name"])}" />
            <input type="hidden" name="source_page" value="products/{p["slug"]}.html" />
            <input type="text" name="website" tabindex="-1" autocomplete="off" style="position:absolute;left:-9999px;" aria-hidden="true" />
            <div class="form-row">
              <div class="form-group"><label>Your name *</label><input type="text" name="name" required placeholder="Rajesh Kumar" /></div>
              <div class="form-group"><label>WhatsApp / phone *</label><input type="tel" name="phone" required placeholder="+91 98765 43210" /></div>
            </div>
            <div class="form-row">
              <div class="form-group"><label>Email</label><input type="email" name="email" placeholder="Optional" /></div>
              <div class="form-group"><label>State *</label>
                <select name="state" required><option value="">Select…</option><option>Himachal Pradesh</option><option>Uttarakhand</option><option>Punjab</option><option>Haryana</option><option>Maharashtra</option><option>Karnataka</option><option>Kerala</option><option>Tamil Nadu</option><option>Madhya Pradesh</option><option>West Bengal</option><option>Other</option></select>
              </div>
            </div>
            <div class="form-row">
              <div class="form-group"><label>Monthly volume</label><input type="text" name="capacity" placeholder="e.g. 200 kg / month" /></div>
              <div class="form-group"><label>Experience</label>
                <select name="experience"><option value="">Select…</option><option>Just starting</option><option>< 1 year</option><option>1–3 years</option><option>3–5 years</option><option>5+ years</option></select>
              </div>
            </div>
            <div class="form-group"><label>About your operation</label><textarea name="message" placeholder="Substrate, growing method, certifications, what support you need…"></textarea></div>
            <button type="submit" class="btn btn-brand btn-lg btn-block">Submit seller registration →</button>
            <p class="form-note">Sourcing team will contact you within 48 hours</p>
            <div class="success-msg">✓ Thank you for registering. Our team will reach out within 48 hours.</div>
          </form>
        </div>
      </div>
    </div>
  </div>
</section>'''

    # ---- FAQ ----
    faq_items = '\n'.join(
      f'      <div class="faq-item"><button class="faq-question">{html.escape(q)}<span class="faq-toggle">+</span></button><div class="faq-answer"><div class="faq-answer-inner">{html.escape(a)}</div></div></div>'
      for q,a in p["faqs"]
    )
    faq_section = f'''<section class="sec-bone-2">
  <div class="wrap">
    <header class="sec-head reveal">
      <div><span class="eyebrow">FAQ — {html.escape(p["name"])}</span><h2 class="h2">Common<br>questions.</h2></div>
      <div class="sec-head-end"><p>Quick answers. Full FAQ on the FAQ page covers everything not here.</p></div>
    </header>
    <div class="faq-list reveal">
{faq_items}
    </div>
    <div style="text-align:center; margin-top:48px;">
      <a href="../faq.html" class="link-arrow">See full FAQ <span class="arr">→</span></a>
    </div>
  </div>
</section>'''

    out = f"{head}\n<body>\n\n{nav}\n\n{hero}\n\n{buy_section}\n\n{sell_section}\n\n{faq_section}\n\n{foot}\n</body>\n</html>\n"
    (ROOT / 'products' / f'{p["slug"]}.html').write_text(out, encoding='utf-8')
    return len(out)


def main():
    print("Product pages:")
    for p in PRODUCTS:
        size = build_product(p)
        print(f"  wrote products/{p['slug']}.html  ({size} bytes)")
    print(f"\n{len(PRODUCTS)} pages")


if __name__ == '__main__':
    main()
