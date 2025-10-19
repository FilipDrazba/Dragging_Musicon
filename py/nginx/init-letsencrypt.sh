#!/bin/bash
set -e

domains=(musicon.ddns.net www.musicon.ddns.net)
email="twojemail@example.com"
webroot="/etc/nginx/html"

mkdir -p $webroot/.well-known/acme-challenge

for domain in "${domains[@]}"; do
  if [ ! -f "/etc/letsencrypt/live/$domain/fullchain.pem" ]; then
    certbot certonly --webroot -w "$webroot" -d "$domain" --email "$email" --agree-tos --non-interactive
  fi
done

nginx -g 'daemon off;'
