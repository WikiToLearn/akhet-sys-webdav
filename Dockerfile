FROM akhetbase/akhet-base-ubuntu-16-04

MAINTAINER WikiToLearn akhet@wikitolearn.org
ENV DEBIAN_FRONTEND noninteractive
ENV DEBCONF_NONINTERACTIVE_SEEN true

RUN apt-get update && apt-get -y --force-yes install apache2 && rm -f /var/cache/apt/archives/*deb && find /var/lib/apt/lists/ -type f -delete && find /var/log/ -type f -delete
RUN apt-get update && apt-get -y --force-yes install midori && rm -f /var/cache/apt/archives/*deb && find /var/lib/apt/lists/ -type f -delete && find /var/log/ -type f -delete

RUN a2enmod rewrite dav dav_fs
RUN echo > /etc/apache2/mods-available/autoindex.conf
RUN mkdir /webdav

RUN mkdir /var/lock/apache2
RUN chmod 777 /var/lock/apache2
ADD ./apache2.conf    /etc/supervisor/conf.d/
ADD ./midori.conf     /etc/supervisor/conf.d/
ADD ./createlink.conf /etc/supervisor/conf.d/
ADD ./000-default.conf /etc/apache2/sites-available/000-default.conf
ADD ./createlink.py /
ADD ./index.html /index.html
