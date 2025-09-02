#!/bin/sh
if ! [ -e "/srv/www/wordpress/wp-config.php" ]; then
    python3 /app/gen_php_config.py > /srv/www/wordpress/wp-config.php
    chown www-data /srv/www/wordpress/wp-config.php
fi
apache2ctl -D FOREGROUND
