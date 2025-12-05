FROM ubuntu
ENV DEBIAN_FRONTEND=noninteractive
RUN apt update && apt install -y tzdata 
RUN apt install -y wget apache2 php php-mysql libapache2-mod-php
RUN wget https://cs.utahtech.edu/it/3300/files/WaterPokemon-f22.tgz
RUN tar -xvzf WaterPokemon-f22.tgz && mv water /var/www/html && rm *.tgz
EXPOSE 80
CMD ["apachectl", "-DFOREGROUND"]

