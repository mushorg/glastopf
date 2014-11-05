FROM ubuntu:trusty
MAINTAINER Lukas Rist <glaslos@gmail.com>


## setup APT
RUN sed -i '1ideb mirror://mirrors.ubuntu.com/mirrors.txt trusty main restricted universe multiverse' /etc/apt/sources.list
RUN sed -i '1ideb mirror://mirrors.ubuntu.com/mirrors.txt trusty-updates main restricted universe multiverse' /etc/apt/sources.list
RUN sed -i '1ideb mirror://mirrors.ubuntu.com/mirrors.txt trusty-backports main restricted universe multiverse' /etc/apt/sources.list
RUN sed -i '1ideb mirror://mirrors.ubuntu.com/mirrors.txt trusty-security main restricted universe multiverse' /etc/apt/sources.list
RUN apt-get update
ENV DEBIAN_FRONTEND noninteractive


## Install dependencies
RUN apt-get install -y python2.7 python-openssl python-gevent libevent-dev python2.7-dev build-essential make
RUN apt-get install -y python-chardet python-requests python-sqlalchemy python-lxml
RUN apt-get install -y python-beautifulsoup mongodb python-pip python-dev python-setuptools
RUN apt-get install -y g++ git php5 php5-dev liblapack-dev gfortran libmysqlclient-dev
RUN apt-get install -y libxml2-dev libxslt-dev
RUN pip install --upgrade distribute


## Install and configure the PHP sandbox
RUN git clone git://github.com/glastopf/BFR.git /opt/BFR
RUN cd /opt/BFR && phpize && ./configure --enable-bfr && make && sudo make install
RUN echo "zend_extension = "$(find /usr -name bfr.so) >> /etc/php5/apache2/php.ini
RUN echo "zend_extension = "$(find /usr -name bfr.so) >> /etc/php5/cli/php.ini


## Install glastopf from latest sources
RUN git clone https://github.com/glastopf/glastopf.git /opt/glastopf
RUN cd /opt/glastopf && python setup.py install


## Configuration
RUN mkdir /opt/myhoneypot


# Clean up when done.
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*


EXPOSE 80
WORKDIR /opt/myhoneypot
CMD ["glastopf-runner"]

