# Deploying updates to the VPS

The site lives at `/var/www/goodmushroom` on the Hostinger VPS. The simplest
reliable workflow is: keep a git clone on the VPS and `git pull` on each deploy.

## First-time setup (run once on the VPS)

```bash
# SSH in
ssh root@YOUR_VPS_IP

# Install nginx + certbot if missing
sudo apt update
sudo apt install -y nginx certbot python3-certbot-nginx git

# Clone the site
sudo git clone https://github.com/YOUR_USER/goodmushroom.git /var/www/goodmushroom
sudo chown -R www-data:www-data /var/www/goodmushroom

# Drop in the nginx config
sudo cp /var/www/goodmushroom/deploy/nginx-goodmushroom.conf /etc/nginx/sites-available/goodmushroom
sudo ln -sf /etc/nginx/sites-available/goodmushroom /etc/nginx/sites-enabled/goodmushroom
sudo rm -f /etc/nginx/sites-enabled/default

# Get SSL (answer the prompts)
sudo certbot --nginx -d goodmushroom.in -d www.goodmushroom.in

# Reload
sudo nginx -t && sudo systemctl reload nginx
```

## Deploying a new change (the "fetch on VPS" command)

After you `git push` from your laptop:

```bash
ssh root@YOUR_VPS_IP
cd /var/www/goodmushroom
sudo git fetch origin
sudo git reset --hard origin/main
sudo chown -R www-data:www-data .
sudo systemctl reload nginx      # only needed if nginx config changed
```

Or as a one-liner you can run locally without SSHing in:

```bash
ssh root@YOUR_VPS_IP 'cd /var/www/goodmushroom && sudo git fetch origin && sudo git reset --hard origin/main && sudo chown -R www-data:www-data .'
```

## Verifying security headers after deploy

```bash
curl -skI https://goodmushroom.in | grep -iE 'strict-transport|content-security|x-frame|referrer|permissions|coop'
```

All of these should come back non-empty. If any are missing, `sudo nginx -t`
and check the config.

## Re-running Lighthouse

After the config is live, re-run Lighthouse on https://goodmushroom.in —
Best Practices should jump into the 90s (HTTPS, HSTS, CSP, COOP, XFO all
now set), and Performance should improve from the long cache lifetimes +
gzip.
