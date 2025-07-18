#!/bin/bash
set -e
echo "Building Docker images from new source code..."
cd /home/ubuntu/cce-website/

# Stop any running services before rebuilding
echo "Stopping existing services..."
sudo docker-compose -f docker-compose.prod.yml --env-file .env down --remove-orphans || true

# Clean up old images to free space
echo "Cleaning up old images..."
sudo docker image prune -f || true

# Build new images
echo "Building new Docker images..."
if sudo docker-compose -f docker-compose.prod.yml build --no-cache; then
    echo "Docker images built successfully."
    
    # Verify images were created
    echo "Verifying built images:"
    sudo docker images | grep cce-website
    
    exit 0
else
    echo "Failed to build Docker images."
    exit 1
fi