FROM mback2k/simple-cgi-server

USER root

RUN apk --no-cache --update upgrade && apk --no-cache add mercurial

ADD hgweb.cgi /var/www/hgweb.cgi
ADD hgweb.config /var/www/hgweb.config
ENV HGWEB_CONFIG /var/www/hgweb.config

USER serve

ADD simple-cgi-server.yaml /etc/simple-cgi-server/simple-cgi-server.yaml

WORKDIR /var/www
