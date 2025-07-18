FROM nginx:1.23.0-alpine

# Copy the final Nginx config and overwrite the default
COPY ./nginx/production.conf /etc/nginx/conf.d/default.conf

# Copy the helper file for SSL settings
COPY ./nginx/options-ssl-nginx.conf /etc/nginx/options-ssl-nginx.conf
