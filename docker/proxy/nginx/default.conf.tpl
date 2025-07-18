server {
    listen 80;
    server_name ${DOMAIN} www.${DOMAIN};

    # This location handles the Let's Encrypt challenge
    location /.well-known/acme-challenge/ {
        root /vol/www;
    }

    # This location forwards all other traffic to your Django app
    location / {
        proxy_pass http://app:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}