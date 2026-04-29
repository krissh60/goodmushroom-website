# Good Mushroom Website

Static marketing and lead-generation site for https://goodmushroom.in.

## What is included

```
index.html              Homepage
products.html           Product catalogue
products/*.html         Product-specific buy/sell landing pages
buyers.html             Buyer information page
farmers.html            Farmer/seller information page
contact.html            Buyer and seller lead forms
faq.html                FAQ page
privacy.html            Privacy policy
api/contact.php         PHP form endpoint for VPS email delivery
api/.env.example        Example VPS-only email environment variables
sitemap.xml             SEO sitemap
robots.txt              Crawl rules
deploy/DEPLOY.md        VPS deployment workflow
deploy/nginx-goodmushroom.conf  Nginx config with PHP endpoint support
```

## Forms and email

Lead forms post to `/api/contact.php`. The endpoint reads real SMTP credentials
from `api/.env` on the VPS. Do not commit the real env file.

Required VPS env keys:

```
RECIPIENT_PRIMARY=krish@goodmushroom.in
RECIPIENT_SECONDARY=anmol@goodmushroom.in
SMTP_HOST=smtp.hostinger.com
SMTP_PORT=465
SMTP_USER=hello@goodmushroom.in
SMTP_PASS=replace_with_real_smtp_password
SMTP_FROM=hello@goodmushroom.in
SMTP_FROM_NAME=Good Mushroom Website
RATE_LIMIT_PER_HOUR=20
```

If the PHP endpoint is unavailable, the frontend falls back to opening a mailto
draft addressed to `krish@goodmushroom.in,anmol@goodmushroom.in`.

## WhatsApp

All WhatsApp CTAs use `+91 6361 621 886` via `https://wa.me/916361621886`.
Mobile pages keep the floating WhatsApp action and sticky mobile bottom bar.

## Deploy

See `deploy/DEPLOY.md` for the full VPS workflow. The short version is:

```
git push origin main
ssh root@YOUR_VPS_IP 'cd /var/www/goodmushroom && sudo git fetch origin && sudo git reset --hard origin/main && sudo chown -R www-data:www-data .'
```

Before reloading Nginx on the VPS, confirm the PHP-FPM socket in
`deploy/nginx-goodmushroom.conf` matches the installed PHP version.

## SEO after deploy

Submit `https://goodmushroom.in/sitemap.xml` in Google Search Console, then
request indexing for the new product pages plus `/buyers.html`, `/faq.html`,
`/about.html`, and `/contact.html`.
