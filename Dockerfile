FROM ubuntu:16.04
MAINTAINER Lukas Rist <glaslos@gmail.com>

ENV DEBIAN_FRONTEND noninteractive

## Install dependencies
RUN apt-get update && apt-get install -y \
        build-essential \
        g++ \
        gfortran \
        git \
        libevent-dev \
        liblapack-dev \
        libmysqlclient-dev \
        libxml2-dev \
        libxslt-dev \
        make \
        python-beautifulsoup \
        python-chardet \
        python-dev \
        python-gevent \
        python-lxml \
        python-openssl \
        python-pip \
        python-requests \
        python-setuptools \
        python-sqlalchemy \
        python-mysqldb \
        cython \
        python-dateutil \
        python2.7 \
        python2.7-dev \
        software-properties-common \
        php7.0 \
        php7.0-dev \
    	&& \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

## Install and configure the PHP sandbox
RUN git clone https://github.com/mushorg/BFR.git /opt/BFR && \
    cd /opt/BFR && \
    phpize7.0 && \
    ./configure --enable-bfr && \
    make && \
    make install && \
    echo "zend_extension = "$(find /usr -name bfr.so) >> /etc/php/7.0/cli/php.ini && \
    rm -rf /opt/BFR /tmp/* /var/tmp/*


## Install glastopf from latest sources
RUN git clone https://github.com/mushorg/glastopf.git /opt/glastopf && \
    cd /opt/glastopf && \
    python setup.py install && \
    rm -rf /opt/glastopf /tmp/* /var/tmp/*

## Configuration
RUN mkdir /opt/myhoneypot

EXPOSE 80
WORKDIR /opt/myhoneypot
CMD ["glastopf-runner"]
