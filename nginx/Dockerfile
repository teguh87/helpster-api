FROM nginx
RUN rm -f /etc/nginx/conf.d/default.conf
ADD api.conf /etc/nginx/conf.d
ADD .  /usr/share/nginx/html/web
ADD . /var/www/html/web