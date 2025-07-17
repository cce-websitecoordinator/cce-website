#!/bin/bash
set -e

echo "Building and starting all services..."
cd /home/ubuntu/cce-website/

# Add the --env-file flag to load your variables
sudo docker-compose -f docker-compose.prod.yml --env-file .env up --build -d