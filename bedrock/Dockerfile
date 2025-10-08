FROM debian
ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get -y install \
    apache2 \
    libapache2-mod-php \
    unzip \ 
    python3 \
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
    curl \
    less \
    nodejs \
    npm

WORKDIR /app
COPY install_composer.sh install_composer.sh
RUN bash install_composer.sh && mv composer.phar /usr/local/bin/composer

COPY entry.sh /app/entry.sh
RUN chmod +x /app/entry.sh

RUN curl -O https://raw.githubusercontent.com/wp-cli/builds/gh-pages/phar/wp-cli.phar && \
    chmod +x wp-cli.phar && \
    mv wp-cli.phar /usr/local/bin/wp

CMD "/app/entry.sh"
