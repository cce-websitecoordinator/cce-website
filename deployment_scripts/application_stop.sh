#!/bin/bash
set -e

echo "Stopping all services defined in docker-compose.prod.yml..."
cd /home/ubuntu/cce-website/

# Add the --env-file flag here as well
sudo docker-compose -f docker-compose.prod.yml --env-file .env down --remove-orphans