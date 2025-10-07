FROM debian
ENV DEBIAN_FRONTEND=noninteractive
ARG NODE_VERSION=24.7.0

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
    less

WORKDIR /app
COPY install_composer.sh install_composer.sh
RUN bash install_composer.sh && mv composer.phar /usr/local/bin/composer

COPY entry.sh /app/entry.sh
RUN chmod +x /app/entry.sh

RUN curl -O https://raw.githubusercontent.com/wp-cli/builds/gh-pages/phar/wp-cli.phar && \
    chmod +x wp-cli.phar && \
    mv wp-cli.phar /usr/local/bin/wp

RUN groupadd -r devs && \
    useradd -m -s /usr/bin/bash -r -g devs dev && \
    usermod -aG devs www-data

WORKDIR /home/dev
USER dev
ENV NVM_DIR=/home/dev/.nvm
ENV PATH="$NVM_DIR/versions/node/v$NODE_VERSION/bin:$PATH"
RUN curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.3/install.sh | bash 
RUN bash -c "source $NVM_DIR/nvm.sh && nvm install $NODE_VERSION"

USER root
CMD "/app/entry.sh"
