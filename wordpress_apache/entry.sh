#!/bin/sh
if ! [ -e "/srv/www/wordpress/wp-config.php" ]; then
    python3 /srv/www/gen_php_config.py > /srv/www/wordpress/wp-config.php
    chown www-data /srv/www/wordpress/wp-config.php
fi

cd /srv/www/wordpress
if [ "$INSTALL_SITE" = "true" ] && ! wp core is-installed 2>/dev/null; then
    wp core install --title=$SITE_TITLE --admin_user=$SITE_ADMIN_USER --admin_password=$(cat $SITE_ADMIN_PASSWORD_FILE) --admin_email=$SITE_ADMIN_EMAIL
fi

apache2ctl -D FOREGROUND
