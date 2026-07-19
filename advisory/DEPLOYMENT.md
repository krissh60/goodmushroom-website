# Deploy `advisory.goodmushroom.in` on Hostinger VPS

This branch contains public website code only. It deliberately contains **no** CRM, invoice,
customer, supplier, SMTP or payment credentials.

## Files to copy

Copy the whole `advisory` directory **and replace the existing root `api/contact.php`** with
the version from this branch. Keep the protected `api/.env` file and the `api/lib` directory
exactly where they are; do not copy, move or expose either of them.

```text
/var/www/goodmushroom/
├── api/
│   ├── .env                 # existing; do not copy or expose it
│   ├── contact.php           # replace with this branch's updated file
│   └── lib/                  # existing; retain
├── advisory/
│   ├── index.html
│   └── api/contact.php       # bridge to ../../api/contact.php
└── ...
```

The advisory directory must stay inside that same web root. The root handler update adds
server-side validation and routes advisory enquiries to `info@goodmushroom.in`; the bridge at
`advisory/api/contact.php` then reuses that handler, its protected `api/.env` and its
PHPMailer setup. No credentials belong in the advisory folder.

## Hostinger setup

1. Create the `advisory` subdomain in Hostinger and point its document root to the
   `advisory` directory above.
2. Ensure its DNS points to the same VPS IP as `goodmushroom.in`.
3. Issue/enable SSL for `advisory.goodmushroom.in`.
4. Confirm that PHP is enabled for the subdomain.
5. Do not expose directory listings or copy the parent `api/.env` file into a public folder.

## Verify before announcing it

1. Open `https://advisory.goodmushroom.in/` and check layout on desktop and phone.
2. Open `https://advisory.goodmushroom.in/api/contact.php`. It should return a JSON
   405 error for a browser GET request; that confirms the bridge reaches the shared handler.
3. Submit one controlled test enquiry. It should arrive at `info@goodmushroom.in` with
   subject “New Advisory Enquiry — Good Mushroom”.
4. Confirm the success message appears only after the email handler returns success.
5. Check the existing `goodmushroom.in` buyer, supplier and report forms still work.

## Form behaviour

- Fixed reports use the approved public prices.
- The qualification call is ₹500 for 20 minutes; payment is required before scheduling.
- Custom DPR/project advisory is **price on assessment** and has no public fixed rate.
- The page does not promise yields, profits, funding, licences, buyer placement, purchase or
  supply/offtake outcomes.


## Shared main-site design assets (required for the redesign)

The redesigned advisory pages load the same Good Mushroom CSS, logo, images and JavaScript through same-domain Nginx aliases. Add these locations inside the advisory subdomain server block, before the generic location / block, then run nginx -t and reload only if the test succeeds:

    location ^~ /css/    { alias /var/www/goodmushroom/css/; }
    location ^~ /images/ { alias /var/www/goodmushroom/images/; }
    location ^~ /js/     { alias /var/www/goodmushroom/js/; }

Do not copy or expose api/.env. The advisory folder still uses its local API bridge, which calls the protected shared handler.
