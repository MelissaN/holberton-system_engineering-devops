#!/usr/bin/env bash
# Fix container given to run as nginx user && listen on all active IPs on port 8080

# update nginx config file with user 'nginx'
sudo sed -i 's/#user www-data/user nginx/' /etc/nginx/nginx.conf

# change ownership and permissions of config file
chmod 700 /etc/nginx/nginx.conf
chown nginx:nginx /etc/nginx/nginx.conf

# update nginx file to listen to 8080
sudo sed -i 's/80 default_server/8080 default_server/' /etc/nginx/sites-available/default

# netstat -lpn shows apache2 is using 8080
pkill apache2
sudo -u nginx service nginx restart
