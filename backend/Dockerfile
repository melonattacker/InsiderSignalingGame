FROM python:3.9.2-alpine

RUN mkdir /var/www
WORKDIR /var/www

COPY ./ ./

RUN apk add --update \
    curl \
    build-base \
    linux-headers \
    gcc && \
    pip install -r requirements.txt

RUN chmod 755 -R /var/www
RUN adduser -D backend
USER backend

# CMD ["uwsgi","--ini","/var/www/uwsgi.ini"]