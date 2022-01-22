FROM ubuntu:18.04

RUN mkdir /var/www
WORKDIR /var/www

COPY ./ ./

RUN apt-get update && \
    apt-get install -y \
    curl \
    python3 \
    python3-pip && \ 
    pip3 install -r requirements.txt

RUN chmod 755 -R /var/www
RUN groupadd -g 1000 backend && \
    useradd -m -s /bin/bash -u 1000 -g 1000 backend
USER backend

# CMD ["uwsgi","--ini","/var/www/uwsgi.ini"]