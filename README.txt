# Good Mushroom Website — Deployment Guide
## goodmushroom.in | Hostinger VPS

---

## WHAT'S IN THIS FOLDER

```
goodmushroom/
├── index.html        ← Homepage (most important for SEO)
├── products.html     ← Full product catalog
├── about.html        ← About us & our story
├── contact.html      ← Lead generation forms (buyers + sellers)
├── sitemap.xml       ← For Google to index your pages
├── robots.txt        ← Tells Google how to crawl
├── css/
│   └── style.css     ← All design / styling
└── js/
    └── main.js       ← Animations, forms, menu etc.
```

---

## STEP 1: Set Up Your Hostinger VPS

1. Log into Hostinger → go to your VPS panel
2. Make sure **Apache** or **Nginx** web server is installed
   - Most Hostinger VPS come with Ubuntu + Apache or Nginx
   - If not, install Apache: `sudo apt update && sudo apt install apache2 -y`
3. Your website files should go to: `/var/www/html/` (Apache) or `/usr/share/nginx/html/` (Nginx)

---

## STEP 2: Upload Your Files

**Option A — Using FileZilla (easiest for beginners)**
1. Download FileZilla (free): https://filezilla-project.org/
2. Connect to your VPS using SFTP:
   - Host: your VPS IP address
   - Username: root (or your VPS user)
   - Password: your VPS password
   - Port: 22
3. Navigate to `/var/www/html/` on the right side
4. Delete the default `index.html` that comes with Apache
5. Upload ALL files from the `goodmushroom/` folder

**Option B — Using terminal (SCP command)**
```bash
scp -r /path/to/goodmushroom/* root@YOUR_VPS_IP:/var/www/html/
```

---

## STEP 3: Point Your Domain to VPS

1. Go to your domain registrar where you bought goodmushroom.in
2. Go to DNS settings
3. Add an A Record:
   - Name: @ (meaning the root domain)
   - Value: YOUR_VPS_IP_ADDRESS
   - TTL: 3600
4. Add another A Record:
   - Name: www
   - Value: YOUR_VPS_IP_ADDRESS
5. Wait 1–24 hours for DNS to propagate (usually 30 minutes)

---

## STEP 4: Set Up Free SSL (HTTPS) — IMPORTANT for SEO

HTTPS is essential for Google ranking. Set it up for free with Certbot:

```bash
# Install Certbot (on Ubuntu with Apache)
sudo apt install certbot python3-certbot-apache -y

# Get free SSL certificate
sudo certbot --apache -d goodmushroom.in -d www.goodmushroom.in

# Auto-renewal (run once — certbot handles renewal after)
sudo certbot renew --dry-run
```

After this, your site will be live at **https://goodmushroom.in** ✅

---

## STEP 5: Set Up Contact Forms (Formspree — FREE)

Currently the forms have placeholder form actions. To make them actually send emails:

1. Go to **https://formspree.io** and create a free account (it's free)
2. Create a new form — you'll get a form ID like `xabcdefg`
3. Open `index.html` and `contact.html`
4. Find this line in BOTH files:
   ```
   action="https://formspree.io/f/YOUR_FORM_ID"
   ```
5. Replace `YOUR_FORM_ID` with your actual Formspree form ID
6. Both forms (buyer + seller) can point to the same Formspree endpoint — or create two separate ones for cleaner email organization

**Alternative: Use a PHP contact form**
If you prefer not to use Formspree, create a simple `mail.php` file and point the form action to it. This requires PHP to be installed on your VPS.

---

## STEP 6: Update Your WhatsApp Number

In `contact.html`, find this line:
```html
<a href="https://wa.me/91XXXXXXXXXX"
```
Replace `XXXXXXXXXX` with your actual WhatsApp number (no spaces, no +, no dashes).
Example: If your number is +91 98765 43210, use: `https://wa.me/919876543210`

---

## STEP 7: Update Email Address

Find all instances of `hello@goodmushroom.in` in the HTML files and make sure this email actually exists and is set up. Create it via Hostinger's email panel or use Google Workspace.

---

## STEP 8: Submit to Google Search Console

After your site is live with HTTPS:
1. Go to: https://search.google.com/search-console
2. Add property: `goodmushroom.in`
3. Verify ownership (DNS method recommended)
4. Submit your sitemap URL: `https://goodmushroom.in/sitemap.xml`

This tells Google to start indexing your pages.

---

## SEO QUICK WINS (Do These First)

1. ✅ SSL certificate (HTTPS) — done above
2. ✅ Submit sitemap to Google Search Console
3. ✅ Create Google Business Profile (even though you're online-only)
4. ✅ Add your website URL to your social media bios (Instagram, LinkedIn)
5. ✅ Update the `<lastmod>` dates in sitemap.xml whenever you make changes
6. ✅ Consider writing a blog about mushroom farming, cordyceps, etc. — great for organic traffic

---

## MAINTENANCE TIPS

- To update text/content: edit the HTML files and re-upload
- To add new products: copy a product card block in `products.html` and change the text
- Backup your files monthly to your computer
- Renew SSL automatically (Certbot handles this)
- Check Google Search Console every 2 weeks for indexing status

---

## NEED HELP?

Email us (ironically): hello@goodmushroom.in
Or ask your developer/web person to follow these steps — they're straightforward.

---

Built with ❤️ and 🍄 for Good Mushroom
