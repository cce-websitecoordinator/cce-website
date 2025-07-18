FROM nginx:1.23.0-alpine

# Copy all your corrected Nginx configuration files
COPY ./nginx/default.conf.tpl /etc/nginx/templates/default.conf.tpl
COPY ./nginx/default-ssl.conf.tpl /etc/nginx/templates/default-ssl.conf.tpl
COPY ./nginx/options-ssl-nginx.conf /etc/nginx/options-ssl-nginx.conf
COPY ./nginx/uwsgi_params /etc/nginx/uwsgi_params

# Copy the startup script
COPY ./run.sh /run.sh
RUN chmod +x /run.sh

# Run the startup script
CMD ["/run.sh"]