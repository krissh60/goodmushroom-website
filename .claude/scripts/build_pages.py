#!/usr/bin/env python3
"""
Generate the top-level pages and product detail pages on the v4 design.

Usage:  python3 .claude/scripts/build_pages.py
"""
from pathlib import Path
import html, json

ROOT = Path(__file__).resolve().parents[2]
WA = "918219599053"
SITE = "https://goodmushroom.in"
GA = "G-3JPKHJHFQM"

GA_BLOCK = '''  <!-- Google tag (gtag.js) -->
  <script async src="https://www.googletagmanager.com/gtag/js?id=G-3JPKHJHFQM"></script>
  <script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){dataLayer.push(arguments);}
    gtag('js', new Date());
    gtag('config', 'G-3JPKHJHFQM');
  </script>'''

FONTS_BLOCK = '''  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Instrument+Serif:ital@0;1&family=Manrope:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet" />'''

# ----- Reusable nav (image-only logo) -----
def nav_html(prefix=''):
    return f'''<nav class="nav" aria-label="Main">
  <div class="nav-inner">
    <a href="{prefix}index.html" class="nav-logo" aria-label="Good Mushroom — home">
      <span class="nav-logo-mark" aria-hidden="true"></span>
      <span>Good Mushroom</span>
      <img src="{prefix}images/logo-nav.png" alt="Good Mushroom" class="brand-img" />
    </a>
    <ul class="nav-links" role="list">
      <li><a href="{prefix}products.html">Products</a></li>
      <li><a href="{prefix}about.html">About</a></li>
      <li><a href="{prefix}buyers.html">Buyers</a></li>
      <li><a href="{prefix}farmers.html">Farmers</a></li>
      <li><a href="{prefix}exports.html">Markets</a></li>
      <li><a href="{prefix}faq.html">FAQ</a></li>
      <li><a href="{prefix}contact.html">Contact</a></li>
    </ul>
    <div class="nav-cta">
      <a href="{prefix}contact.html" class="btn btn-outline btn-sm">Get a quote</a>
      <a href="{prefix}contact.html#buyer" class="btn btn-primary btn-sm">Buy in bulk
        <svg viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M3 8h10M9 4l4 4-4 4"/></svg>
      </a>
      <button class="nav-hamburger" aria-label="Open menu">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 7h16M4 12h16M4 17h16"/></svg>
      </button>
    </div>
  </div>
</nav>

<div class="mobile-menu" role="dialog" aria-label="Mobile menu">
  <div class="mobile-menu-top">
    <span class="nav-logo">
      <span class="nav-logo-mark" aria-hidden="true"></span>
      <span>Good Mushroom</span>
      <img src="{prefix}images/logo-nav.png" alt="Good Mushroom" class="brand-img" />
    </span>
    <button class="mobile-menu-close" aria-label="Close menu">
      <svg viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" stroke-width="2"><path d="M6 6l12 12M18 6L6 18"/></svg>
    </button>
  </div>
  <nav class="mobile-menu-links" aria-label="Mobile">
    <a href="{prefix}products.html">Products <span class="arr">→</span></a>
    <a href="{prefix}about.html">About <span class="arr">→</span></a>
    <a href="{prefix}buyers.html">For Buyers <span class="arr">→</span></a>
    <a href="{prefix}farmers.html">For Farmers <span class="arr">→</span></a>
    <a href="{prefix}exports.html">Export Markets <span class="arr">→</span></a>
    <a href="{prefix}faq.html">FAQ <span class="arr">→</span></a>
    <a href="{prefix}contact.html">Contact <span class="arr">→</span></a>
  </nav>
  <div class="mobile-menu-foot">
    <a href="{prefix}contact.html" class="btn btn-primary btn-lg">Get a quote in 24 hrs →</a>
    <a href="https://wa.me/{WA}" class="btn btn-outline btn-lg">Chat on WhatsApp</a>
    <div class="mobile-menu-meta">
      <span>krish@goodmushroom.in</span>
      <span>+91 8219599053</span>
    </div>
  </div>
</div>'''

def footer_html(prefix=''):
    return f'''<footer class="foot">
  <div class="wrap">
    <div class="foot-grid">
      <div class="foot-brand">
        <img src="{prefix}images/logo-white.png" alt="Good Mushroom" class="brand-img" />
        <h3>Good <em>Mushroom</em></h3>
        <p>India's trusted partner for mushroom trading and export. Connecting farmers with buyers across 40+ countries.</p>
      </div>
      <div class="foot-col">
        <h5>Products</h5>
        <ul>
          <li><a href="{prefix}products/cordyceps.html">Cordyceps</a></li>
          <li><a href="{prefix}products/shiitake.html">Shiitake</a></li>
          <li><a href="{prefix}products/lions-mane.html">Lion's Mane</a></li>
          <li><a href="{prefix}products/reishi.html">Reishi</a></li>
          <li><a href="{prefix}products/extracts-dual.html">Extracts</a></li>
          <li><a href="{prefix}products/ashwagandha.html">Ayurvedic herbs</a></li>
        </ul>
      </div>
      <div class="foot-col">
        <h5>Company</h5>
        <ul>
          <li><a href="{prefix}about.html">About</a></li>
          <li><a href="{prefix}buyers.html">For buyers</a></li>
          <li><a href="{prefix}farmers.html">For farmers</a></li>
          <li><a href="{prefix}exports.html">Export markets</a></li>
          <li><a href="{prefix}faq.html">FAQ</a></li>
          <li><a href="{prefix}contact.html">Contact</a></li>
          <li><a href="{prefix}privacy.html">Privacy</a></li>
        </ul>
      </div>
      <div class="foot-col">
        <h5>Contact</h5>
        <div class="foot-contact">
          <a href="mailto:krish@goodmushroom.in">krish@goodmushroom.in</a>
          <a href="mailto:anmol@goodmushroom.in">anmol@goodmushroom.in</a>
          <a href="https://wa.me/{WA}">+91 8219599053</a>
          <span>Himachal Pradesh, India</span>
          <span>Mon–Sat · 10am–6pm IST</span>
        </div>
      </div>
    </div>
    <div class="foot-bottom">
      <span>© 2026 Good Mushroom PVT LTD · All rights reserved</span>
      <span>Made with care in India</span>
    </div>
  </div>
</footer>

<a class="wa-float" href="https://wa.me/{WA}?text=Hi%20Good%20Mushroom" target="_blank" rel="noopener" aria-label="WhatsApp">
  <span class="wa-icon" aria-hidden="true">
    <svg viewBox="0 0 24 24" width="20" height="20" fill="currentColor"><path d="M17.5 14.4l-.4-.2c-.6-.3-1.5-.7-1.7-.7-.2 0-.5.1-.7.4-.2.2-.6.6-.7.7-.1.1-.3.2-.5.1-.6-.3-1.4-.7-2.4-1.6-.7-.6-1.2-1.4-1.4-1.6-.1-.2 0-.4.1-.5l.4-.4c.1-.2.2-.3.3-.5.1-.2 0-.4 0-.5-.1-.2-.7-1.7-.9-2.3-.2-.6-.5-.5-.7-.5h-.5c-.2 0-.5.1-.8.4-.3.3-1 1-1 2.4 0 1.4 1 2.8 1.2 3 .1.2 2 3.1 4.9 4.2 1.7.7 2.3.7 3.1.6.5-.1 1.5-.6 1.7-1.2.2-.6.2-1.1.2-1.2l-.2-.2zm-5.5 7.6c-1.6 0-3.3-.4-4.7-1.3l-.3-.2-3.5.9.9-3.4-.2-.3c-1-1.5-1.5-3.3-1.5-5.1 0-5.2 4.2-9.4 9.3-9.4 2.5 0 4.8 1 6.6 2.7 1.8 1.8 2.7 4.1 2.7 6.6 0 5.2-4.2 9.5-9.3 9.5zM20 4c-2.1-2.1-5-3.3-8-3.3C5.6.7.6 5.7.6 12c0 2 .5 3.9 1.5 5.6L.5 23.5l5.9-1.5c1.6.9 3.5 1.3 5.4 1.3 6.3 0 11.4-5 11.4-11.3 0-3-1.2-5.9-3.3-8z"/></svg>
  </span>
  <span class="wa-label">WhatsApp</span>
</a>

<nav class="smb" aria-label="Quick contact">
  <a href="{prefix}contact.html#buyer"  class="primary">Buy</a>
  <a href="{prefix}contact.html#seller" class="brand">Sell</a>
  <a href="https://wa.me/{WA}" class="wa">WhatsApp</a>
</nav>

<script src="{prefix}js/main.js" defer></script>'''


def page_head(*, title, description, canonical, image='https://goodmushroom.in/og-image.jpg',
              extra_schema=None, keywords='', prefix=''):
    schema = ''
    if extra_schema:
        schema = f'\n  <script type="application/ld+json">\n{json.dumps(extra_schema, indent=2)}\n  </script>'
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
{GA_BLOCK}

  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover" />
  <title>{html.escape(title)}</title>
  <meta name="description" content="{html.escape(description)}" />
  <meta name="keywords" content="{html.escape(keywords)}" />
  <meta name="robots" content="index, follow" />
  <meta name="google-site-verification" content="54mWXlvRKQmiOaFEhLFs--sTsJ89OZr_VRcmSjOt0hs" />
  <meta name="author" content="Good Mushroom" />
  <meta name="theme-color" content="#162a16" />
  <link rel="canonical" href="{canonical}" />

  <meta property="og:type" content="website" />
  <meta property="og:title" content="{html.escape(title)}" />
  <meta property="og:description" content="{html.escape(description)}" />
  <meta property="og:url" content="{canonical}" />
  <meta property="og:site_name" content="Good Mushroom" />
  <meta property="og:image" content="{image}" />

  <meta name="twitter:card" content="summary_large_image" />
  <meta name="twitter:title" content="{html.escape(title)}" />
  <meta name="twitter:description" content="{html.escape(description)}" />
  <meta name="twitter:image" content="{image}" />

  <link rel="icon" type="image/png" href="{prefix}images/favicon.png" />
  <link rel="apple-touch-icon" href="{prefix}images/favicon.png" />

{FONTS_BLOCK}
  <link rel="stylesheet" href="{prefix}css/style.css" />{schema}
</head>
<body>'''


def page_hero(*, eyebrow, h1, lede, photo, photo_alt, photo_caption, breadcrumb=None, prefix=''):
    crumb = ''
    if breadcrumb:
        items = [f'<a href="{prefix}index.html">Home</a>']
        for txt, href in breadcrumb[:-1]:
            items.append(f'<a href="{prefix}{href}">{html.escape(txt)}</a>')
        items.append(f'<span>{html.escape(breadcrumb[-1][0])}</span>')
        sep = '<span class="sep">/</span>'
        crumb = f'<nav class="breadcrumb">{sep.join(items)}</nav>'
    return f'''<section class="page-hero">
  <div class="wrap">
    {crumb}
    <div class="page-hero-inner">
      <div class="reveal">
        <span class="eyebrow">{html.escape(eyebrow)}</span>
        <h1>{h1}</h1>
        <p class="lede">{html.escape(lede)}</p>
      </div>
      <div class="page-hero-art reveal">
        <img src="{prefix}{photo}" alt="{html.escape(photo_alt)}" loading="eager" />
        <span class="page-hero-art-caption">{html.escape(photo_caption)}</span>
      </div>
    </div>
  </div>
</section>'''


# ============================================================
# Top-level pages
# ============================================================

PAGES = []

# ------ ABOUT ------
PAGES.append({
  'file': 'about.html',
  'title': 'About Good Mushroom — Indian Mushroom Export Company',
  'description': "Good Mushroom is an Indian mushroom trading and export company. We connect farms across Himachal, Uttarakhand and Karnataka with buyers in 40+ countries.",
  'canonical': f'{SITE}/about.html',
  'keywords': 'about Good Mushroom, Indian mushroom export company, Himachal mushroom supplier, mushroom exporter India',
  'schema': {
    "@context": "https://schema.org", "@type": "AboutPage",
    "name": "About Good Mushroom",
    "url": f"{SITE}/about.html",
    "publisher": { "@type": "Organization", "name": "Good Mushroom", "url": SITE }
  },
  'hero': {
    'eyebrow': 'About Good Mushroom',
    'h1': 'Indian mushrooms,<br>handled <em>like wine</em>.',
    'lede': "We're a small, focused trading house: we visit farms, take samples on the spot, run NABL labs on every shipment, and put your name on the documents we ship under.",
    'photo': 'images/about.jpg',
    'photo_alt': 'Mushroom farm in Himachal Pradesh',
    'photo_caption': 'Farm visit · Solan, HP',
    'breadcrumb': [('About', 'about.html')],
  },
  'body': '''<section>
  <div class="wrap">
    <div class="editorial reveal">
      <div class="editorial-image">
        <img src="images/cordyceps.jpg" alt="Cordyceps batch with COA" />
        <span class="editorial-image-caption">Batch QC · cordyceps</span>
      </div>
      <div class="editorial-copy">
        <span class="eyebrow">Our story</span>
        <h2 class="h2" style="margin-top:18px;">Started by two friends in Himachal in <em>2026</em>.</h2>
        <p class="lede" style="margin-top:24px;">After years of seeing Indian farmers get squeezed by middlemen and exporters get shipped substandard product, Krish and Anmol started Good Mushroom to do one thing — connect the two sides directly, with full transparency on quality and price.</p>
        <p>Today we work with 120+ farms across India and ship to buyers in 40+ countries. Every batch is lab-tested. Every contract is direct. Every farmer is paid fairly. Every buyer gets what they ordered.</p>
        <dl class="editorial-stats">
          <div><dt>Farms sourced from</dt><dd>120<span style="color:var(--brand);">+</span></dd></div>
          <div><dt>Lab-verified shipments</dt><dd>100<span style="color:var(--brand);">%</span></dd></div>
          <div><dt>Reorder rate</dt><dd>87<span style="color:var(--brand);">%</span></dd></div>
        </dl>
      </div>
    </div>
  </div>
</section>

<section class="sec-bone-2">
  <div class="wrap">
    <header class="sec-head reveal">
      <div><span class="eyebrow">What we stand for</span><h2 class="h2">Three things,<br>repeated.</h2></div>
      <div class="sec-head-end"><p>The rules we wrote ourselves when we started. We still hold to them — they're why our buyers reorder and our farmers stay.</p></div>
    </header>
    <div class="process reveal-stagger">
      <div class="process-step">
        <div class="process-num">01 · Principle</div>
        <h4>Direct, never brokered</h4>
        <p>We buy from farms, not aggregators. We sell to buyers, not other exporters. The chain is two links long. Always.</p>
      </div>
      <div class="process-step">
        <div class="process-num">02 · Principle</div>
        <h4>Lab-verified, every batch</h4>
        <p>NABL-accredited labs. HPLC for actives, ICP-MS for heavy metals, micro panel, pesticide screen. COA in every box.</p>
      </div>
      <div class="process-step">
        <div class="process-num">03 · Principle</div>
        <h4>Transparent pricing</h4>
        <p>Farmers see the export price. Buyers see the farm price. The spread covers QC, processing, logistics — and is the same for everyone.</p>
      </div>
      <div class="process-step">
        <div class="process-num">04 · Promise</div>
        <h4>If it doesn't match, we replace</h4>
        <p>Spec mismatch? Send it back. We replace, no questions, no broker fights. Our reputation is built one batch at a time.</p>
      </div>
    </div>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="quote reveal">
      <div class="quote-mark">"</div>
      <div>
        <p class="quote-text">We visit every farm. We don't sign anyone we haven't met. <em>Our farmers know us by first name</em>, and they trust us with their best harvests.</p>
        <div class="quote-author">
          <span class="quote-avatar" aria-hidden="true">K</span>
          <div><strong>Krish, Co-founder</strong><span>Sourcing &amp; farmer relations</span></div>
        </div>
      </div>
    </div>
  </div>
</section>
'''
})

# ------ CONTACT ------
PAGES.append({
  'file': 'contact.html',
  'title': 'Contact Good Mushroom — Buyer Quote or Farmer Registration (24h Reply)',
  'description': 'Send a buyer enquiry for premium Indian mushrooms and extracts, or register as a mushroom farmer to sell your produce. 24h response.',
  'canonical': f'{SITE}/contact.html',
  'keywords': 'contact Good Mushroom, buy mushrooms India inquiry, sell mushrooms India, mushroom export enquiry, mushroom farmer registration India',
  'schema': {
    "@context": "https://schema.org", "@type": "ContactPage",
    "name": "Contact Good Mushroom", "url": f"{SITE}/contact.html",
    "publisher": { "@type": "Organization", "name": "Good Mushroom", "url": SITE }
  },
  'hero': {
    'eyebrow': 'Get in touch',
    'h1': "Quote in 24 hours.<br>Samples in <em>a week</em>.",
    'lede': "Two short forms below — one for buyers, one for farmers. Or skip them and message us on WhatsApp.",
    'photo': 'images/herbs.jpg',
    'photo_alt': 'Ayurvedic herbs',
    'photo_caption': 'Open · Mon–Sat 10–6 IST',
    'breadcrumb': [('Contact', 'contact.html')],
  },
  'body': '''<section id="contact-forms">
  <div class="wrap">
    <div class="two-up">
      <div class="reveal">
        <div class="contact-tabs">
          <button class="tab-btn active" data-tab="buyer-panel">I'm a Buyer</button>
          <button class="tab-btn" data-tab="seller-panel">I'm a Farmer</button>
        </div>

        <div class="form-panel active" id="buyer-panel">
          <div class="form-card">
            <h3 class="h3" style="margin-bottom:8px;">Request a quote</h3>
            <p style="color:var(--ink-mid); margin-bottom:24px; font-size:var(--step--1);">Tell us what you need, where you ship to, and your timeline.</p>
            <form id="buyer-form" action="/api/contact.php" method="POST" novalidate>
              <input type="hidden" name="_subject" value="New Buyer Enquiry — Good Mushroom" />
              <input type="hidden" name="form_type" value="buyer" />
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
                  <select name="country" required>
                    <option value="">Select country…</option><option>United States</option><option>United Kingdom</option><option>Germany</option><option>France</option><option>Netherlands</option><option>Australia</option><option>Canada</option><option>UAE / Dubai</option><option>Japan</option><option>South Korea</option><option>Singapore</option><option>China</option><option>India</option><option>Other</option>
                  </select>
                </div>
                <div class="form-group"><label>Buyer type</label>
                  <select name="buyer_type"><option value="">Select…</option><option>Importer / Distributor</option><option>Supplement Brand</option><option>Restaurant / Food Service</option><option>Retail / Supermarket</option><option>Wellness / Spa Brand</option><option>Other</option></select>
                </div>
              </div>
              <div class="form-group"><label>Product(s) *</label>
                <select name="product" required>
                  <option value="">Select product…</option><option>Cordyceps Militaris</option><option>Shiitake</option><option>Lion's Mane</option><option>Oyster Mushrooms</option><option>Reishi / Ganoderma</option><option>Button &amp; Specialty</option><option>Dual-Extract Powders</option><option>Reishi Spore Oil</option><option>Mushroom Blends (custom)</option><option>Ashwagandha</option><option>Tulsi</option><option>Shatavari / Brahmi</option><option>Multiple — described below</option>
                </select>
              </div>
              <div class="form-row">
                <div class="form-group"><label>Quantity</label><input type="text" name="quantity" placeholder="e.g. 50 kg / month" /></div>
                <div class="form-group"><label>Frequency</label>
                  <select name="frequency"><option value="">Select…</option><option>One-time trial</option><option>Monthly recurring</option><option>Quarterly</option><option>Annual contract</option><option>Not sure</option></select>
                </div>
              </div>
              <div class="form-group"><label>Message</label><textarea name="message" placeholder="Spec, certifications needed (organic, kosher), packaging, target market, timeline…"></textarea></div>
              <button type="submit" class="btn btn-primary btn-lg btn-block">Send buyer enquiry →</button>
              <p class="form-note">We respond within 1 business day (Mon–Sat, 10am–6pm IST)</p>
              <div class="success-msg">✓ Thank you. We've received your enquiry and will be in touch within 24 hours.</div>
            </form>
          </div>
        </div>

        <div class="form-panel" id="seller-panel">
          <div class="form-card">
            <h3 class="h3" style="margin-bottom:8px;">Register as a seller</h3>
            <p style="color:var(--ink-mid); margin-bottom:24px; font-size:var(--step--1);">Tell us where your farm is and what you grow. Our team will reach out on WhatsApp within 48 hours.</p>
            <form id="seller-form" action="/api/contact.php" method="POST" novalidate>
              <input type="hidden" name="_subject" value="New Farmer Registration — Good Mushroom" />
              <input type="hidden" name="form_type" value="seller" />
              <input type="text" name="website" tabindex="-1" autocomplete="off" style="position:absolute;left:-9999px;" aria-hidden="true" />
              <div class="form-row">
                <div class="form-group"><label>Your name *</label><input type="text" name="name" required placeholder="Rajesh Kumar" /></div>
                <div class="form-group"><label>WhatsApp / phone *</label><input type="tel" name="phone" required placeholder="+91 98765 43210" /></div>
              </div>
              <div class="form-row">
                <div class="form-group"><label>Email</label><input type="email" name="email" placeholder="Optional" /></div>
                <div class="form-group"><label>State *</label>
                  <select name="state" required><option value="">Select state…</option><option>Himachal Pradesh</option><option>Uttarakhand</option><option>Punjab</option><option>Haryana</option><option>Maharashtra</option><option>Karnataka</option><option>Kerala</option><option>Tamil Nadu</option><option>Andhra Pradesh</option><option>Telangana</option><option>Odisha</option><option>West Bengal</option><option>Assam / Northeast</option><option>Madhya Pradesh</option><option>Other</option></select>
                </div>
              </div>
              <div class="form-group"><label>District / tehsil</label><input type="text" name="district" placeholder="e.g. Kullu, Manali area" /></div>
              <div class="form-row">
                <div class="form-group"><label>What do you grow? *</label>
                  <select name="product" required><option value="">Select…</option><option>Oyster Mushrooms</option><option>Shiitake</option><option>Lion's Mane</option><option>Cordyceps Militaris</option><option>Button / Crimini</option><option>Reishi / Ganoderma</option><option>Wild Collected</option><option>Medicinal Herbs</option><option>Multiple — described below</option></select>
                </div>
                <div class="form-group"><label>Monthly volume</label><input type="text" name="capacity" placeholder="e.g. 200 kg/month" /></div>
              </div>
              <div class="form-group"><label>Experience</label>
                <select name="experience"><option value="">Select…</option><option>Just starting out</option><option>Less than 1 year</option><option>1–3 years</option><option>3–5 years</option><option>5+ years</option></select>
              </div>
              <div class="form-group"><label>About your farm</label><textarea name="message" placeholder="Substrate, growing method, current buyers, certifications, what support you'd want from us…"></textarea></div>
              <button type="submit" class="btn btn-brand btn-lg btn-block">Submit seller registration →</button>
              <p class="form-note">Sourcing team will contact you within 48 hours</p>
              <div class="success-msg">✓ Thank you for registering. Our team will reach out within 48 hours.</div>
            </form>
          </div>
        </div>
      </div>

      <aside class="reveal">
        <h3 class="h3" style="margin-bottom:16px;">Or reach out directly.</h3>
        <p style="color:var(--ink-mid); font-size:var(--step--1); margin-bottom:32px;">We're a small team. Email goes to a human within an hour during work hours.</p>

        <div style="display:flex; flex-direction:column; gap: 24px; padding-top: 24px; border-top: 1px solid var(--line);">
          <div>
            <div class="mono" style="color:var(--ink-light); text-transform:uppercase; letter-spacing:0.1em; font-size:var(--step--2); margin-bottom:6px;">Krish · Co-founder</div>
            <a href="mailto:krish@goodmushroom.in" style="font-family:var(--font-display); font-size:var(--step-1); color:var(--ink);">krish@goodmushroom.in</a>
          </div>
          <div>
            <div class="mono" style="color:var(--ink-light); text-transform:uppercase; letter-spacing:0.1em; font-size:var(--step--2); margin-bottom:6px;">Anmol · Co-founder</div>
            <a href="mailto:anmol@goodmushroom.in" style="font-family:var(--font-display); font-size:var(--step-1); color:var(--ink);">anmol@goodmushroom.in</a>
          </div>
          <div>
            <div class="mono" style="color:var(--ink-light); text-transform:uppercase; letter-spacing:0.1em; font-size:var(--step--2); margin-bottom:6px;">WhatsApp</div>
            <a href="https://wa.me/918219599053" style="font-family:var(--font-display); font-size:var(--step-1); color:var(--ink);">+91 8219599053</a>
          </div>
          <div>
            <div class="mono" style="color:var(--ink-light); text-transform:uppercase; letter-spacing:0.1em; font-size:var(--step--2); margin-bottom:6px;">Based in</div>
            <span style="font-family:var(--font-display); font-size:var(--step-1); color:var(--ink);">Himachal Pradesh, India</span>
          </div>
          <div>
            <div class="mono" style="color:var(--ink-light); text-transform:uppercase; letter-spacing:0.1em; font-size:var(--step--2); margin-bottom:6px;">Hours</div>
            <span style="font-family:var(--font-display); font-size:var(--step-1); color:var(--ink);">Mon–Sat · 10am–6pm IST</span>
          </div>
        </div>
      </aside>
    </div>
  </div>
</section>
'''
})

# ------ PRODUCTS ------
PRODUCTS_GRID_FULL = '''
<div class="cat-grid reveal-stagger">
  <a href="products/cordyceps.html" class="cat-card" data-cat="medicinal">
    <div class="cat-card-image"><img src="images/cordyceps.jpg" alt="Cordyceps militaris" loading="lazy" /><span class="cat-card-tag">10 kg MOQ</span></div>
    <div class="cat-card-body"><h3>Cordyceps</h3><span class="cat-card-latin">Cordyceps militaris</span><div class="cat-card-meta"><span>Cordycepin 5–8%</span><span class="arr">→</span></div></div>
  </a>
  <a href="products/shiitake.html" class="cat-card" data-cat="culinary medicinal">
    <div class="cat-card-image"><img src="images/shiitake.jpg" alt="Shiitake" loading="lazy" /><span class="cat-card-tag">Cold-chain</span></div>
    <div class="cat-card-body"><h3>Shiitake</h3><span class="cat-card-latin">Lentinula edodes</span><div class="cat-card-meta"><span>β-glucan 20–35%</span><span class="arr">→</span></div></div>
  </a>
  <a href="products/lions-mane.html" class="cat-card" data-cat="medicinal">
    <div class="cat-card-image"><img src="images/lions-mane.jpg" alt="Lion's Mane" loading="lazy" /><span class="cat-card-tag">Extract 8:1</span></div>
    <div class="cat-card-body"><h3>Lion's Mane</h3><span class="cat-card-latin">Hericium erinaceus</span><div class="cat-card-meta"><span>Hericenones verified</span><span class="arr">→</span></div></div>
  </a>
  <a href="products/oyster.html" class="cat-card" data-cat="culinary">
    <div class="cat-card-image"><img src="images/oyster.jpg" alt="Oyster mushrooms" loading="lazy" /><span class="cat-card-tag">100 kg / wk</span></div>
    <div class="cat-card-body"><h3>Oyster</h3><span class="cat-card-latin">Pleurotus spp.</span><div class="cat-card-meta"><span>Pearl · Pink · King</span><span class="arr">→</span></div></div>
  </a>
  <a href="products/reishi.html" class="cat-card" data-cat="medicinal extract">
    <div class="cat-card-image"><img src="images/reishi.jpg" alt="Reishi" loading="lazy" /><span class="cat-card-tag">Triterpenes &gt;35%</span></div>
    <div class="cat-card-body"><h3>Reishi</h3><span class="cat-card-latin">Ganoderma lucidum</span><div class="cat-card-meta"><span>Dual extract · spore oil</span><span class="arr">→</span></div></div>
  </a>
  <a href="products/button.html" class="cat-card" data-cat="culinary">
    <div class="cat-card-image"><img src="images/button.jpg" alt="Button mushrooms" loading="lazy" /><span class="cat-card-tag">200 kg / wk</span></div>
    <div class="cat-card-body"><h3>Button &amp; Specialty</h3><span class="cat-card-latin">Agaricus bisporus</span><div class="cat-card-meta"><span>Fresh · Dried · Brined</span><span class="arr">→</span></div></div>
  </a>
  <a href="products/extracts-dual.html" class="cat-card" data-cat="extract">
    <div class="cat-card-image"><img src="images/extract.jpg" alt="Extract powder" loading="lazy" /><span class="cat-card-tag">OEM / white-label</span></div>
    <div class="cat-card-body"><h3>Dual-Extract Powders</h3><span class="cat-card-latin">Water + alcohol</span><div class="cat-card-meta"><span>8:1 to 20:1</span><span class="arr">→</span></div></div>
  </a>
  <a href="products/extracts-spore-oil.html" class="cat-card" data-cat="extract">
    <div class="cat-card-image"><img src="images/reishi.jpg" alt="Reishi spore oil" loading="lazy" /><span class="cat-card-tag">Softgel-ready</span></div>
    <div class="cat-card-body"><h3>Reishi Spore Oil</h3><span class="cat-card-latin">CO₂ supercritical</span><div class="cat-card-meta"><span>Triterpenes >35%</span><span class="arr">→</span></div></div>
  </a>
  <a href="products/extracts-blends.html" class="cat-card" data-cat="extract">
    <div class="cat-card-image"><img src="images/extract.jpg" alt="Mushroom blends" loading="lazy" /><span class="cat-card-tag">2–8 species</span></div>
    <div class="cat-card-body"><h3>Custom Blends</h3><span class="cat-card-latin">OEM / White-label</span><div class="cat-card-meta"><span>Your formula</span><span class="arr">→</span></div></div>
  </a>
  <a href="products/ashwagandha.html" class="cat-card" data-cat="herb">
    <div class="cat-card-image"><img src="images/herbs.jpg" alt="Ashwagandha" loading="lazy" /><span class="cat-card-tag">2.5–5% withanolides</span></div>
    <div class="cat-card-body"><h3>Ashwagandha</h3><span class="cat-card-latin">Withania somnifera</span><div class="cat-card-meta"><span>Root powder · Extract</span><span class="arr">→</span></div></div>
  </a>
  <a href="products/tulsi.html" class="cat-card" data-cat="herb">
    <div class="cat-card-image"><img src="images/herbs.jpg" alt="Tulsi" loading="lazy" /><span class="cat-card-tag">Eugenol 60–80%</span></div>
    <div class="cat-card-body"><h3>Tulsi / Holy Basil</h3><span class="cat-card-latin">Ocimum sanctum</span><div class="cat-card-meta"><span>Leaf · Extract · Oil</span><span class="arr">→</span></div></div>
  </a>
  <a href="products/shatavari-brahmi.html" class="cat-card" data-cat="herb">
    <div class="cat-card-image"><img src="images/herbs.jpg" alt="Ayurvedic herbs" loading="lazy" /><span class="cat-card-tag">AYUSH facility</span></div>
    <div class="cat-card-body"><h3>Shatavari · Brahmi · More</h3><span class="cat-card-latin">Bacopa · Asparagus · Moringa</span><div class="cat-card-meta"><span>Powder · Extract</span><span class="arr">→</span></div></div>
  </a>
</div>
'''

PAGES.append({
  'file': 'products.html',
  'title': 'Products — Indian Mushrooms, Extracts & Ayurvedic Herbs | Good Mushroom',
  'description': "Wholesale Indian mushrooms — Cordyceps, Shiitake, Lion's Mane, Reishi, Oyster, Button. Plus dual-extract powders, reishi spore oil, custom OEM blends, and Ayurvedic herbs.",
  'canonical': f'{SITE}/products.html',
  'keywords': 'buy cordyceps India, shiitake wholesale India, lion\'s mane extract India, mushroom export catalogue',
  'schema': {
    "@context":"https://schema.org","@type":"CollectionPage",
    "name":"Products — Good Mushroom","url":f"{SITE}/products.html",
  },
  'hero': {
    'eyebrow': 'Catalogue',
    'h1': "What we<br><em>trade</em>.",
    'lede': "Twelve product lines across mushrooms, extracts and Ayurvedic herbs. Each has its own page with specs, MOQ, lab values, certifications and a quote form.",
    'photo': 'images/reishi.jpg',
    'photo_alt': 'Reishi mushroom',
    'photo_caption': 'Reishi · whole · sliced',
    'breadcrumb': [('Products', 'products.html')],
  },
  'body': f'''<section class="sec-bone-2">
  <div class="wrap">
    <div class="cat-toolbar reveal">
      <div class="cat-filters">
        <button class="cat-filter active" data-filter="all">All</button>
        <button class="cat-filter" data-filter="medicinal">Medicinal</button>
        <button class="cat-filter" data-filter="culinary">Culinary</button>
        <button class="cat-filter" data-filter="extract">Extracts</button>
        <button class="cat-filter" data-filter="herb">Ayurvedic herbs</button>
      </div>
      <div class="cat-count">12 products</div>
    </div>
    {PRODUCTS_GRID_FULL}
  </div>
</section>
'''
})

# ------ BUYERS ------
PAGES.append({
  'file': 'buyers.html',
  'title': 'For Buyers — Indian Mushroom Wholesale Supplier | Good Mushroom',
  'description': "Bulk Indian mushroom and extract supplier for global buyers. Cordyceps, Shiitake, Lion's Mane, Reishi. MOQ from 5 kg extract / 50 kg dried. Full export documentation.",
  'canonical': f'{SITE}/buyers.html',
  'keywords': 'mushroom wholesale India, buy Indian mushrooms bulk, mushroom exporter buyer, supplement brand sourcing India',
  'schema': {"@context":"https://schema.org","@type":"WebPage","name":"For Buyers","url":f"{SITE}/buyers.html"},
  'hero': {
    'eyebrow': 'For buyers',
    'h1': 'Cross-border B2B,<br>not a <em>marketplace</em>.',
    'lede': "Supplement brands, importers, restaurant groups, retail chains — we source directly, certify everything, and put your name on the documents we ship under.",
    'photo': 'images/cordyceps.jpg',
    'photo_alt': 'Cordyceps for export',
    'photo_caption': 'Sample · 10 kg pack',
    'breadcrumb': [('For Buyers', 'buyers.html')],
  },
  'body': '''<section class="sec-dark">
  <div class="wrap">
    <header class="sec-head reveal">
      <div><span class="eyebrow">From spore to shipment</span><h2 class="h2" style="color:var(--bone);">How a quote<br>becomes a&nbsp;container.</h2></div>
      <div class="sec-head-end" style="color:rgba(255,255,255,0.65);"><p>Four steps, predictable timing. The clock starts the minute you send us a brief — most buyers receive samples within seven days and full containers inside six weeks.</p></div>
    </header>
    <div class="process reveal-stagger">
      <div class="process-step"><div class="process-num">01 · Day 0</div><h4>Brief &amp; quote</h4><p>You send species, grade, MOQ and destination. We come back within 24 hours with farm options, indicative pricing and a sample plan.</p></div>
      <div class="process-step"><div class="process-num">02 · Day 3–7</div><h4>Sample &amp; spec</h4><p>10 kg sample air-freighted to your facility. Full NABL COA — actives by HPLC, heavy metals, microbiology, pesticides — included.</p></div>
      <div class="process-step"><div class="process-num">03 · Week 2–4</div><h4>Production</h4><p>On-farm QC, processing at our HACCP facility, packaging to your spec. Status updates in WhatsApp every Thursday.</p></div>
      <div class="process-step"><div class="process-num">04 · Week 5–6</div><h4>Ship &amp; clear</h4><p>Phyto-sanitary, APEDA, packing list, invoice. Sea or air. We answer customs questions before your broker asks them.</p></div>
    </div>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="editorial reveal">
      <div class="editorial-image"><img src="images/extract.jpg" alt="Mushroom extract powder" /><span class="editorial-image-caption">OEM · supplement-grade</span></div>
      <div class="editorial-copy">
        <span class="eyebrow">What we do for you</span>
        <h2 class="h2" style="margin-top:18px;">Documentation,<br>done.</h2>
        <p class="lede" style="margin-top:24px;">FSSAI · APEDA · Phyto-sanitary · Certificate of Origin · NABL COA · Packing list · Commercial invoice. Sea or air freight. Customs questions answered before your broker asks them.</p>
        <ul style="list-style:none; display:flex; flex-direction:column; gap:14px; margin-top:24px;">
          <li style="display:flex; gap:14px; align-items:start;"><span class="mono" style="color:var(--brand); padding-top:2px;">·</span><span><strong>Spec lock.</strong> What you order is what you get — or it goes back. No "close enough."</span></li>
          <li style="display:flex; gap:14px; align-items:start;"><span class="mono" style="color:var(--brand); padding-top:2px;">·</span><span><strong>Lab on demand.</strong> Need a custom test (e.g. specific cordycepin range)? We arrange it before dispatch.</span></li>
          <li style="display:flex; gap:14px; align-items:start;"><span class="mono" style="color:var(--brand); padding-top:2px;">·</span><span><strong>Repeat-order discounts.</strong> Standing contract = better pricing + locked production windows.</span></li>
          <li style="display:flex; gap:14px; align-items:start;"><span class="mono" style="color:var(--brand); padding-top:2px;">·</span><span><strong>WhatsApp QC photos.</strong> Mid-production shots from the floor. You see what's being packed.</span></li>
        </ul>
        <div style="margin-top:32px;"><a href="contact.html#buyer" class="btn btn-primary">Request a buyer quote →</a></div>
      </div>
    </div>
  </div>
</section>

<section class="sec-bone-2">
  <div class="wrap">
    <header class="sec-head reveal">
      <div><span class="eyebrow">Common questions</span><h2 class="h2">Before you<br>write to us.</h2></div>
      <div class="sec-head-end"><p>The questions buyers ask in their first email. Quick answers; the full FAQ has more.</p></div>
    </header>
    <div class="faq-list reveal">
      <div class="faq-item"><button class="faq-question">What is your minimum order quantity?<span class="faq-toggle">+</span></button><div class="faq-answer"><div class="faq-answer-inner">5 kg for extract powders and reishi spore oil. 10 kg for cordyceps dried. 50 kg for most dried whole mushrooms. 100–200 kg / week for fresh cold-chain. Smaller sample orders available before commitment.</div></div></div>
      <div class="faq-item"><button class="faq-question">Do you ship to my country?<span class="faq-toggle">+</span></button><div class="faq-answer"><div class="faq-answer-inner">We export to 40+ countries — US, EU, UAE, UK, Australia, Canada, Japan, South Korea, Singapore, China and more. Send your destination on the form and we'll confirm freight routes + any country-specific import requirements.</div></div></div>
      <div class="faq-item"><button class="faq-question">Can I get a sample before committing?<span class="faq-toggle">+</span></button><div class="faq-answer"><div class="faq-answer-inner">Yes — paid samples (cost + air freight). Typical 100 g – 500 g per spec. We send the full COA with the sample so you can verify before placing a production order.</div></div></div>
      <div class="faq-item"><button class="faq-question">What certifications can you provide?<span class="faq-toggle">+</span></button><div class="faq-answer"><div class="faq-answer-inner">FSSAI, APEDA, NABL COA (standard). Organic / kosher / halal / non-GMO available on request — add 2–3 weeks lead time and we'll route through the appropriate certifier.</div></div></div>
    </div>
    <div style="text-align:center; margin-top:48px;"><a href="faq.html" class="link-arrow">See full FAQ <span class="arr">→</span></a></div>
  </div>
</section>
'''
})

# ------ FARMERS ------
PAGES.append({
  'file': 'farmers.html',
  'title': 'For Farmers — Sell Your Mushrooms to Good Mushroom | Direct Buyer',
  'description': 'Indian mushroom farmers — sell your produce directly to Good Mushroom. No middlemen. In-person farm QC. Net-7 for repeat suppliers.',
  'canonical': f'{SITE}/farmers.html',
  'keywords': 'sell mushrooms India, mushroom farmer buyer India, mushroom direct purchase, Indian mushroom export market',
  'schema': {"@context":"https://schema.org","@type":"WebPage","name":"For Farmers","url":f"{SITE}/farmers.html"},
  'hero': {
    'eyebrow': 'For farmers',
    'h1': "Sell direct.<br>Settle <em>fast</em>.",
    'lede': "Tunnel growers, organic cooperatives and herb collectors across India — we visit your farm, take samples, and confirm price the same week.",
    'photo': 'images/oyster.jpg',
    'photo_alt': 'Oyster mushroom farm',
    'photo_caption': 'Supplier · Karnataka',
    'breadcrumb': [('For Farmers', 'farmers.html')],
  },
  'body': '''<section>
  <div class="wrap">
    <div class="editorial reverse reveal">
      <div class="editorial-copy">
        <span class="eyebrow">Why farmers stay with us</span>
        <h2 class="h2" style="margin-top:18px;">Real prices.<br>Real relationships.</h2>
        <p class="lede" style="margin-top:24px;">Most exporters buy through brokers, who buy through aggregators, who buy from you. By the time you see a price, 3–4 hands have taken a cut. We cut that out.</p>
        <ul style="list-style:none; display:flex; flex-direction:column; gap:14px; margin-top:24px;">
          <li style="display:flex; gap:14px; align-items:start;"><span class="mono" style="color:var(--brand); padding-top:2px;">01</span><span><strong>Export-grade pricing.</strong> You get the price the buyer pays, minus our QC + logistics. Not the mandi price.</span></li>
          <li style="display:flex; gap:14px; align-items:start;"><span class="mono" style="color:var(--brand); padding-top:2px;">02</span><span><strong>In-person QC.</strong> Our team visits HP, UK, Punjab, Maharashtra and Karnataka. We sample on the spot.</span></li>
          <li style="display:flex; gap:14px; align-items:start;"><span class="mono" style="color:var(--brand); padding-top:2px;">03</span><span><strong>Net-7 for repeat suppliers.</strong> Pay-on-pickup for first orders. Standing agreements for steady supply.</span></li>
          <li style="display:flex; gap:14px; align-items:start;"><span class="mono" style="color:var(--brand); padding-top:2px;">04</span><span><strong>Help with scale.</strong> Substrate sourcing, drying tips, certification routing — we share what we learn across the network.</span></li>
        </ul>
        <div style="margin-top:32px; display:flex; gap:12px; flex-wrap:wrap;">
          <a href="contact.html#seller" class="btn btn-primary">Register as a seller →</a>
          <a href="https://wa.me/918219599053" class="btn btn-outline">WhatsApp us</a>
        </div>
      </div>
      <div class="editorial-image"><img src="images/hero.jpg" alt="Farmer in mushroom tunnel" /><span class="editorial-image-caption">Tunnel grower · Solan, HP</span></div>
    </div>
  </div>
</section>

<section class="sec-bone-2">
  <div class="wrap">
    <header class="sec-head reveal">
      <div><span class="eyebrow">What we look for</span><h2 class="h2">Quality first.<br>Volume second.</h2></div>
      <div class="sec-head-end"><p>The kind of farms we already buy from. If you grow even one of these consistently, we want to talk.</p></div>
    </header>
    <div class="process reveal-stagger">
      <div class="process-step"><div class="process-num">·</div><h4>Cordyceps</h4><p>Lab-cultivated militaris. Cordycepin verified by HPLC. Minimum 5 kg / month consistent supply.</p></div>
      <div class="process-step"><div class="process-num">·</div><h4>Shiitake</h4><p>Donko-grade dried or fresh oak-log grown. 50 kg / month dried, 100 kg / week fresh.</p></div>
      <div class="process-step"><div class="process-num">·</div><h4>Lion's Mane</h4><p>Indoor cultivated. White fully-formed heads dried under controlled conditions. 20+ kg / month.</p></div>
      <div class="process-step"><div class="process-num">·</div><h4>Oyster</h4><p>Pearl, pink, blue, king. Cold-chain ready fresh or sun-dried. 50–200 kg / week.</p></div>
    </div>
  </div>
</section>

<section class="sec-dark">
  <div class="wrap">
    <div class="reveal" style="max-width: 760px; margin: 0 auto; text-align:center;">
      <span class="eyebrow">Register your farm</span>
      <h2 class="h1" style="color:var(--bone); margin-top: 20px;">A 48-hour conversation<br>away from <em>your first order</em>.</h2>
      <p class="lede" style="color:rgba(255,255,255,0.7); margin: 24px auto 0; max-width: 56ch;">Fill out the registration form and our sourcing team will reach out on WhatsApp within 48 hours. We'll talk about your farm, your volumes, and what you need from us.</p>
      <div style="margin-top:36px; display:flex; gap:12px; justify-content:center; flex-wrap:wrap;">
        <a href="contact.html#seller" class="btn btn-on-dark btn-lg">Register as a seller →</a>
        <a href="https://wa.me/918219599053" class="btn btn-outline-on-dark btn-lg">WhatsApp us</a>
      </div>
    </div>
  </div>
</section>
'''
})

# ------ FAQ ------
FAQ_DATA = [
  ('Minimum order quantity?', 'Depends on the product. 5 kg for extract powders and reishi spore oil. 10 kg for cordyceps dried fruiting body. 20 kg for lion\'s mane. 25 kg for ashwagandha powder. 50 kg for most other dried mushrooms. 100–200 kg / week for fresh cold-chain.'),
  ('Which countries do you export to?', 'Active buyers in 40+ countries — US, EU (Germany, France, Netherlands, UK), UAE, Saudi, Australia, Canada, Japan, South Korea, Singapore, China, and more. We handle export documentation for every destination.'),
  ('Can I see lab tests before ordering?', "Yes. Every batch ships with a NABL-accredited COA — actives by HPLC, heavy metals by ICP-MS, microbiology, pesticide residue, mycotoxins where applicable. We share recent batch COAs with the quote so you can verify before sample."),
  ('What certifications do you have?', "FSSAI, APEDA, AYUSH-licensed facility (for herbs and extracts), HACCP-compatible processing. Organic / kosher / halal / non-GMO routed through certified partners on request — typically 2–3 weeks added lead time."),
  ('Do you offer samples?', "Yes, paid samples (product cost + air freight). Typical sample size 100 g – 500 g. We include full COA with the sample so you can fully verify before placing a production order. Sample cost is creditable against your first commercial order."),
  ('Sea or air freight?', "Both. Small orders (< 100 kg) usually air for speed. Larger orders go sea. We give indicative timelines for both at quote stage so you can choose."),
  ('How do I register as a supplier?', "Fill out the farmer registration form on the Contact page. Our sourcing team will reach out on WhatsApp within 48 hours to schedule a call or farm visit."),
  ('Do you buy from small farms?', "Yes. We work with farms of all sizes. Even a 100 sq ft cultivation unit can be a supplier. What matters is consistency and quality, not scale."),
  ('How are prices agreed?', "Prices are agreed upfront based on quality grade, species, and committed monthly volume. We review pricing quarterly and share export market movements with our suppliers transparently."),
  ('Do I need to dry mushrooms before selling?', "We buy both fresh and dried — depends on the species and our current buyer orders. We have processing capacity and can often accept fresh produce if you're located near our operations."),
]

faq_html = '<div class="faq-list reveal">\n'
for q, a in FAQ_DATA:
    faq_html += f'  <div class="faq-item"><button class="faq-question">{html.escape(q)}<span class="faq-toggle">+</span></button><div class="faq-answer"><div class="faq-answer-inner">{html.escape(a)}</div></div></div>\n'
faq_html += '</div>'

PAGES.append({
  'file': 'faq.html',
  'title': 'FAQ — Mushroom Export from India | Good Mushroom',
  'description': 'Common questions about buying Indian mushrooms in bulk and selling to us as a farmer. MOQ, certifications, shipping, lab tests, pricing.',
  'canonical': f'{SITE}/faq.html',
  'keywords': 'mushroom export FAQ India, mushroom MOQ, mushroom lab tests COA, Indian mushroom certifications',
  'schema': {
    "@context": "https://schema.org", "@type": "FAQPage",
    "mainEntity": [{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in FAQ_DATA]
  },
  'hero': {
    'eyebrow': 'Frequently asked',
    'h1': 'The questions<br>buyers <em>and farmers</em> ask.',
    'lede': "Everything we'd want to know before sending an enquiry. If yours isn't here, message us on WhatsApp.",
    'photo': 'images/shiitake.jpg',
    'photo_alt': 'Shiitake mushrooms',
    'photo_caption': 'Open · we read everything',
    'breadcrumb': [('FAQ', 'faq.html')],
  },
  'body': f'''<section>
  <div class="wrap">
    {faq_html}
    <div style="text-align:center; margin-top:48px;">
      <p style="color:var(--ink-mid); margin-bottom: 20px;">Still have questions?</p>
      <a href="contact.html" class="btn btn-primary">Get in touch →</a>
    </div>
  </div>
</section>
'''
})

# ------ EXPORTS landing ------
PAGES.append({
  'file': 'exports.html',
  'title': 'Export Markets — Where We Ship | Good Mushroom',
  'description': "Active buyers in 40+ countries. Dedicated pages for our biggest export markets — US, UK, Germany, UAE, Japan, Singapore, Australia, Canada, South Korea.",
  'canonical': f'{SITE}/exports.html',
  'keywords': 'mushroom export USA, mushroom export UK, mushroom export Germany, mushroom export UAE, mushroom export Japan, India mushroom shipping',
  'schema': {"@context":"https://schema.org","@type":"WebPage","name":"Export Markets","url":f"{SITE}/exports.html"},
  'hero': {
    'eyebrow': 'Where we ship',
    'h1': 'Active in <em>40+ countries</em>.<br>And growing.',
    'lede': "Country-specific pages with the certifications, shipping routes and import notes we know for each market.",
    'photo': 'images/lions-mane.jpg',
    'photo_alt': 'Lion\'s Mane for export',
    'photo_caption': 'Shipped · Berlin, Tokyo, Dubai',
    'breadcrumb': [('Export Markets', 'exports.html')],
  },
  'body': '''<section class="sec-bone-2">
  <div class="wrap">
    <div class="cat-grid reveal-stagger">
      <a href="exports/usa.html" class="cat-card">
        <div class="cat-card-image"><img src="images/cordyceps.jpg" alt="USA" loading="lazy" /><span class="cat-card-tag">FDA · USDA</span></div>
        <div class="cat-card-body"><h3>United States</h3><span class="cat-card-latin">FDA-aligned, USDA NOP-equivalent</span><div class="cat-card-meta"><span>NY · LA · Miami</span><span class="arr">→</span></div></div>
      </a>
      <a href="exports/uk.html" class="cat-card">
        <div class="cat-card-image"><img src="images/shiitake.jpg" alt="UK" loading="lazy" /><span class="cat-card-tag">FSA · Soil Assoc.</span></div>
        <div class="cat-card-body"><h3>United Kingdom</h3><span class="cat-card-latin">FSA-aligned, Soil Association ready</span><div class="cat-card-meta"><span>London · Manchester</span><span class="arr">→</span></div></div>
      </a>
      <a href="exports/uae.html" class="cat-card">
        <div class="cat-card-image"><img src="images/extract.jpg" alt="UAE" loading="lazy" /><span class="cat-card-tag">ESMA · Halal</span></div>
        <div class="cat-card-body"><h3>United Arab Emirates</h3><span class="cat-card-latin">ESMA-aligned, Halal-certifiable</span><div class="cat-card-meta"><span>Dubai · Abu Dhabi</span><span class="arr">→</span></div></div>
      </a>
      <a href="exports/japan.html" class="cat-card">
        <div class="cat-card-image"><img src="images/reishi.jpg" alt="Japan" loading="lazy" /><span class="cat-card-tag">MHLW · JAS</span></div>
        <div class="cat-card-body"><h3>Japan</h3><span class="cat-card-latin">MHLW-aligned, JAS Organic on request</span><div class="cat-card-meta"><span>Tokyo · Osaka</span><span class="arr">→</span></div></div>
      </a>
      <a href="exports/south-korea.html" class="cat-card">
        <div class="cat-card-image"><img src="images/lions-mane.jpg" alt="South Korea" loading="lazy" /><span class="cat-card-tag">MFDS</span></div>
        <div class="cat-card-body"><h3>South Korea</h3><span class="cat-card-latin">MFDS-aligned import dossier</span><div class="cat-card-meta"><span>Seoul · Busan</span><span class="arr">→</span></div></div>
      </a>
      <a href="exports/singapore.html" class="cat-card">
        <div class="cat-card-image"><img src="images/oyster.jpg" alt="Singapore" loading="lazy" /><span class="cat-card-tag">SFA</span></div>
        <div class="cat-card-body"><h3>Singapore</h3><span class="cat-card-latin">SFA-aligned, HSA for supplements</span><div class="cat-card-meta"><span>Singapore</span><span class="arr">→</span></div></div>
      </a>
      <a href="exports/australia.html" class="cat-card">
        <div class="cat-card-image"><img src="images/herbs.jpg" alt="Australia" loading="lazy" /><span class="cat-card-tag">TGA · DAFF</span></div>
        <div class="cat-card-body"><h3>Australia</h3><span class="cat-card-latin">TGA-aligned, DAFF biosecurity ready</span><div class="cat-card-meta"><span>Sydney · Melbourne</span><span class="arr">→</span></div></div>
      </a>
      <a href="exports/canada.html" class="cat-card">
        <div class="cat-card-image"><img src="images/button.jpg" alt="Canada" loading="lazy" /><span class="cat-card-tag">CFIA · NPN</span></div>
        <div class="cat-card-body"><h3>Canada</h3><span class="cat-card-latin">CFIA-aligned, NPN on request</span><div class="cat-card-meta"><span>Toronto · Vancouver</span><span class="arr">→</span></div></div>
      </a>
    </div>
  </div>
</section>
'''
})

# ------ PRIVACY ------
PAGES.append({
  'file': 'privacy.html',
  'title': 'Privacy Policy — Good Mushroom',
  'description': "Good Mushroom's privacy policy. We only use the information you share to respond to enquiries and ship orders.",
  'canonical': f'{SITE}/privacy.html',
  'keywords': 'Good Mushroom privacy policy',
  'schema': {"@context":"https://schema.org","@type":"WebPage","name":"Privacy Policy"},
  'hero': {
    'eyebrow': 'Privacy',
    'h1': 'Privacy <em>policy</em>.',
    'lede': "Short version: we use the information you share to respond to your enquiry and ship your order. We don't sell or share data.",
    'photo': 'images/about.jpg',
    'photo_alt': 'Privacy at Good Mushroom',
    'photo_caption': 'Last updated · 2026-04-19',
    'breadcrumb': [('Privacy', 'privacy.html')],
  },
  'body': '''<section>
  <div class="wrap" style="max-width: 760px;">
    <div class="reveal" style="font-size: var(--step-0); line-height: 1.7; color: var(--ink-mid);">
      <h2 class="h3" style="color:var(--ink); margin-top: 0; margin-bottom: 12px;">What we collect</h2>
      <p style="margin-bottom: 24px;">When you fill out a form on this site, we collect: your name, email, phone number (if provided), company name, country, product interest, and any message you write. For farmers, we additionally collect your state/district and growing experience.</p>

      <h2 class="h3" style="color:var(--ink); margin-bottom: 12px;">Why we collect it</h2>
      <p style="margin-bottom: 24px;">Solely to respond to your enquiry and run our trading operations — sending quotes, arranging samples, coordinating shipments, paying suppliers. That's it.</p>

      <h2 class="h3" style="color:var(--ink); margin-bottom: 12px;">Who sees your data</h2>
      <p style="margin-bottom: 24px;">Only the Good Mushroom team (currently Krish, Anmol, and our sourcing assistants). We do not sell, share, or licence your data to any third party. Form submissions are emailed to our internal addresses (<a href="mailto:krish@goodmushroom.in">krish@goodmushroom.in</a>, <a href="mailto:anmol@goodmushroom.in">anmol@goodmushroom.in</a>) and stored in our SMTP provider (Hostinger). We use Google Analytics (anonymised, cookie-based) to understand site traffic.</p>

      <h2 class="h3" style="color:var(--ink); margin-bottom: 12px;">How long we keep it</h2>
      <p style="margin-bottom: 24px;">Active buyer/supplier records: as long as our business relationship continues. One-off enquiries that don't go anywhere: 24 months, then deleted. You can ask us to delete your data anytime — write to <a href="mailto:krish@goodmushroom.in">krish@goodmushroom.in</a>.</p>

      <h2 class="h3" style="color:var(--ink); margin-bottom: 12px;">Cookies</h2>
      <p style="margin-bottom: 24px;">We use Google Analytics (gtag.js) which sets a small set of cookies for traffic measurement. No advertising cookies, no behavioural retargeting. You can block analytics with any standard browser extension or your privacy settings.</p>

      <h2 class="h3" style="color:var(--ink); margin-bottom: 12px;">Your rights</h2>
      <p style="margin-bottom: 24px;">Under Indian law (DPDP Act, 2023) and GDPR for EU residents: you have the right to access, correct, or delete your data, and to withdraw consent. Email <a href="mailto:krish@goodmushroom.in">krish@goodmushroom.in</a> with your request and we'll respond within 14 days.</p>

      <h2 class="h3" style="color:var(--ink); margin-bottom: 12px;">Contact</h2>
      <p>Good Mushroom PVT LTD · Himachal Pradesh, India · <a href="mailto:krish@goodmushroom.in">krish@goodmushroom.in</a></p>
    </div>
  </div>
</section>
'''
})


# ------ Build top-level pages ------
def build_top_page(p):
    head = page_head(
        title=p['title'], description=p['description'], canonical=p['canonical'],
        extra_schema=p.get('schema'), keywords=p.get('keywords',''),
        prefix='',
    )
    hero = page_hero(**p['hero'], prefix='')
    out = f"{head}\n\n{nav_html('')}\n\n{hero}\n\n{p['body']}\n\n{footer_html('')}\n</body>\n</html>\n"
    (ROOT / p['file']).write_text(out, encoding='utf-8')
    print(f"  wrote {p['file']:20s}  ({len(out)} bytes)")


def main():
    print("Top-level pages:")
    for p in PAGES:
        build_top_page(p)

if __name__ == '__main__':
    main()
