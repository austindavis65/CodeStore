FROM ubuntu
ENV DEBIAN_FRONTEND=noninteractive
RUN apt update && apt install -y apache2 iputils-ping
EXPOSE 80
CMD ["/usr/sbin/apachectl", "-DFOREGROUND"]
