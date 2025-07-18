#!/bin/bash
set -e
echo "Stopping all services..."
cd /home/ubuntu/cce-website/

# Check if docker-compose file exists before trying to stop
if [ -f "docker-compose.prod.yml" ]; then
    # Stop services gracefully
    sudo docker-compose -f docker-compose.prod.yml --env-file .env down --remove-orphans || true
    echo "Services stopped successfully."
else
    echo "No docker-compose.prod.yml found, skipping stop."
fi

# Clean up any dangling containers
sudo docker container prune -f || true