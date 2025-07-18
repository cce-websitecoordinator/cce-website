# Filename: ~/cce-website/docker/proxy/Dockerfile

FROM nginx:1.23.0-alpine

# Copy the intelligent startup script
COPY ./run.sh /run.sh

# Copy the Nginx configuration templates and SSL options
COPY ./nginx/default.conf.tpl /etc/nginx/default.conf.tpl
COPY ./nginx/default-ssl.conf.tpl /etc/nginx/default-ssl.conf.tpl
COPY ./nginx/options-ssl-nginx.conf /etc/nginx/options-ssl-nginx.conf

# Make the startup script executable
RUN chmod +x /run.sh

# The CMD instruction tells the container to run this script when it starts.
# This replaces the default Nginx command.
CMD ["/run.sh"]