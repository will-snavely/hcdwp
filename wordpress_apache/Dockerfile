FROM debian
ENV DEBIAN_FRONTEND=noninteractive
ENV WORDPRESS_DB_HOST=""
ENV WORDPRESS_DB=""
ENV WORDPRESS_DB_USER=""
ENV WORDPRESS_DB_PASSWORD_FILE: ""
ENV WORDPRESS_HOME: "/src/www/wordpress"

RUN apt-get update && apt-get -y install apache2 \
	python3 \
	libapache2-mod-php \
        php \
        php-bcmath \
        php-curl \
        php-imagick \
        php-intl \
        php-json \
        php-mbstring \
        php-mysql \
        php-xml \
        php-zip \
        curl
COPY entry.sh /app/entry.sh
RUN chmod +x /app/entry.sh

RUN mkdir -p /srv/www && chown www-data: /srv/www
USER www-data
WORKDIR /srv/www
COPY gen_php_config.py gen_php_config.py
RUN curl https://wordpress.org/latest.tar.gz | tar zx -C /srv/www

USER root
COPY wordpress.conf /etc/apache2/sites-available/wordpress.conf
RUN a2ensite wordpress && a2enmod rewrite && a2dissite 000-default
CMD "/app/entry.sh"
