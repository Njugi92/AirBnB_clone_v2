#!/usr/bin/env bash
# Script that sets up web servers for deployment of web_static

apt-get update
# Install Nginx if not already installed
apt-get install -y nginx
# Create folder /data/ if it doesn't exist
# Create folder /data/web_static/ if it doesn't exist
# Create folder /data/web_static/releases/ if don't exist
# Create /data/web_static/releases/test/ if don't exist
mkdir -p /data/web_static/releases/test/
# Create folder /data/web_static/shared/ if doesn't exist
mkdir -p /data/web_static/shared/
# Create fake HTML file /data/web_static/releases/test/index.html
echo '<html>
        <head>
        </head>
        <body>
         Holberton School
        </body>
        </html>' > /data/web_static/releases/test/index.html
# Create symbolic link /data/web_static/current linked to
# /data/web_static/releases/test/ folder. If symbolic link exist
# it should be deleted and recreated every time script is run
ln -sf /data/web_static/releases/test/ /data/web_static/current
# Give ownership of /data/ folder to ubuntu user and group
chown -R ubuntu /data/
chgrp -R ubuntu /data/
# Update Nginx configuration to serve content of
# /data/web_static/current/ to hbnb_static
sed -i '51 i \\n\tlocation /hbnb_static {\n\talias /data/web_static/current;\n\t}' /etc/nginx/sites-available/default
# Restart Nginx after updating configuration
service nginx restart
