import os
import secrets

auth_keys = [
    'AUTH_KEY',
    'SECURE_AUTH_KEY',
    'LOGGED_IN_KEY',
    'NONCE_KEY',
    'AUTH_SALT',
    'SECURE_AUTH_SALT',
    'LOGGED_IN_SALT',
    'NONCE_SALT'
] 


config_template = """
<?php

define('DB_NAME', getenv('WORDPRESS_DB'));
define('DB_USER', getenv('WORDPRESS_DB_USER'));
define('DB_HOST', getenv('WORDPRESS_DB_HOST'));
define('DB_PASSWORD', trim(file_get_contents(getenv('WORDPRESS_DB_PASSWORD_FILE'))));
define('DB_CHARSET', 'utf8');
define('DB_COLLATE', '');

{auth_settings}

$table_prefix = 'wp_';
define('WP_DEBUG', false);

if(!defined('ABSPATH')) {{
    define('ABSPATH', __DIR__ . '/');
}}
require_once ABSPATH . 'wp-settings.php';
"""

def get_php_config():
    define_template = "define('{}', '{}');"
    auth_defines = [
            define_template.format(key, secrets.token_urlsafe(32))
            for key in auth_keys
            ]
    config = config_template.format(auth_settings="\n".join(auth_defines))
    return config

if __name__ == "__main__":
    print(get_php_config())

