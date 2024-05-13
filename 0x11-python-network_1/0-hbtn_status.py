#!/usr/bin/env bash
# This script configures Nginx to listen on port 80 of all active IPv4 IPs

# Install nginx if not already installed
apt-get update
apt-get -y install nginx

# Ensure nginx is not already running
service nginx stop

# Modify nginx configuration to listen on port 80
sed -i 's/listen 80 default_server;/listen 80;/g' /etc/nginx/sites-available/default

# Restart nginx
service nginx start
