FROM debian
ENV DEBIAN_FRONTEND=noninteractive
ENV WORDPRESS_DB_HOST=""
ENV WORDPRESS_DB=""
ENV WORDPRESS_DB_USER=""
ENV WORDPRESS_DB_PASSWORD_FILE: ""
ENV WORDPRESS_ROOT="/srv/www/wordpress"

RUN apt-get update && apt-get -y install apache2 \
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

WORKDIR /app
COPY install_composer.sh install_composer.sh
RUN bash install_composer.sh && \
    chmod +x composer.phar && \
    mv composer.phar /usr/local/bin/composer

RUN curl -O https://raw.githubusercontent.com/wp-cli/builds/gh-pages/phar/wp-cli.phar && \
	chmod +x wp-cli.phar && \
	mv wp-cli.phar /usr/local/bin/wp

CMD apache2ctl -D FOREGROUND
