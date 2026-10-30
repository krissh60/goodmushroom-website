# Good Mushroom release and rollback

The owner reviews local changes before a GitHub push. A push and VPS deployment are separate steps. This document does not authorize either action.

## Recorded baseline

Active root observed 29 October 2026: `/var/www/goodmushroom`. VPS HEAD: `ae57498e0d29b61541333a6b7a21b0b4b956de79`. Five intentional advisory files outside that commit matched GitHub main `0ee6218344dd25b464326f1f816766b50fd0b7e1`, which is the local recovery branch base. Recheck before releasing: direct VPS changes can happen again.

Private recovery archive: `/root/goodmushroom-before-seo-20261029.tar.gz` (mode 600). It contains runtime configuration; keep it out of GitHub and the public root. Restoration has not been tested.

## Local acceptance

1. Run `node scripts/version-assets.mjs`, `node scripts/verify-site.mjs` and `git diff --check`.
2. Lint `api/contact.php` with PHP 8.3 or the actual supported server version. Test buyer/seller success, validation, delivery failure, honeypot and rate limiting against an isolated mail sink. A sink cannot verify production SMTP or inbox receipt.
3. Review desktop/mobile catalogue, four priority products, contact specification prefill and farmer application. Review the final diff and business claims. Never commit `.env`, private backups, enquiry logs or supplier documents.
4. After owner review, commit on the recovery/release branch, reconcile with current GitHub main and record the exact tested SHA. Push only when authorized. Do not overwrite newer main or VPS edits.

## VPS release after approval

1. Record `git status --short --untracked-files=all`, HEAD, active nginx configuration, PHP version/extensions and file ownership in the active root. Compare against recovery and resolve new changes. Do not use `git reset --hard` or `git clean` to resolve a dirty production tree.
2. Create a new private timestamped backup of current code, runtime and nginx configuration outside the web root. Preserve `api/.env` and enquiry logs and permissions. Verify the archive can be listed; retain previous working code.
3. Fetch the reviewed GitHub branch and verify its exact SHA. Prepare that commit in a separate release directory before touching the active root. Exclude `.git`, `deploy`, `scripts`, internal reports and QA material from public artifacts. Keep the separate advisory host/root intact.
4. Compare the release artifact with the active root using a dry run. Apply only reviewed code/assets in one maintenance operation, preserving runtime/private files. HTML, versioned JS and `api/contact.php` must ship together. Older HTML may remain cached for ten minutes. Do not replace working nginx configuration wholesale with the example.
5. Merge necessary nginx changes after comparing sockets, certificates, hosts and headers. Run `nginx -t` before reload. The example blocks internal reports and deployment material. Apply equivalent protection on any separately configured advisory host.
6. Check `/`, `/products.html`, the four priority product URLs, `/contact.html`, `/farmers.html`, `/robots.txt` and `/sitemap.xml` over HTTPS. Confirm status, canonical, directives, rendered links and versioned asset responses. Check HTTP/www/index redirects, a real missing URL returning 404, and denial of `.git`, `.env`, API logs and internal documents.
7. With a labelled test enquiry, verify buyer mail reaches configured recipients and seller mail reaches its configured destination. Check spam folders. SMTP acceptance alone does not establish receipt.
8. In GA4 DebugView/realtime verify one buyer and supplier event after accepted mail; failure/honeypot must not generate leads. Check action clicks, fixed product/source/request values, absence of personal data, enhanced-measurement duplicates and existing consent settings. Mark intended business events as key events after account review. WhatsApp clicks are intent only.

## Rollback

If forms, routing or key pages regress, restore the previous code tree and corresponding assets/API together. Preserve current `.env` and enquiry logs. Restore nginx only if changed, validate and reload. Recheck routes and mail handling. Never extract a private archive into a public location. Record failed release SHA and cause before retrying.

## Monitoring

Record release time/SHA and GSC last-crawl dates. Check collection/indexing in the first week. Compare the same commercial query/page/country/device cohorts over comparable 28-day windows, using longer windows for low counts. Reconcile received buyer enquiries with qualification, samples, quotes and orders separately from supplier applications. Local tests do not establish traffic or lead growth.
