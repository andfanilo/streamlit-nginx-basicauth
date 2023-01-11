FROM nginx:1.23.0

COPY ./nginx.conf /etc/nginx/conf.d/default.conf
COPY ./htpasswd /etc/nginx/htpasswd

HEALTHCHECK --interval=1m --timeout=2s CMD wget http://localhost/ -O /dev/null || exit 1