from horsecatdog/wordpress_apache:latest
ARG NODE_VERSION=24.7.0

RUN apt-get update && apt-get install unzip
RUN chown -R www-data /var/www && chmod -R 755 /var/www

USER www-data
WORKDIR /var/www
RUN mkdir /var/www/.nvm
ENV NVM_DIR=/var/www/.nvm
RUN curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.3/install.sh | bash 
RUN bash -c "source $NVM_DIR/nvm.sh && nvm install $NODE_VERSION"

USER root
WORKDIR /app
COPY install_composer.sh install_composer.sh
RUN bash install_composer.sh && mv composer.phar /usr/local/bin/composer

WORKDIR /srv/www
ENV PATH="$NVM_DIR/versions/node/v$NODE_VERSION/bin:$PATH"
CMD "/app/entry.sh"
