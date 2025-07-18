#!/bin/bash
set -e
echo "Preparing for new deployment..."

# Navigate to the application directory if it exists
if [ -d "/home/ubuntu/cce-website" ]; then
    cd /home/ubuntu/cce-website/
    
    # Stop any running services gracefully
    echo "Stopping existing services..."
    sudo docker-compose -f docker-compose.prod.yml --env-file .env down --remove-orphans || true
    
    # Wait a moment for services to fully stop
    sleep 5
fi

# Clean up Docker resources
echo "Cleaning up Docker resources..."
sudo docker container prune -f || true
sudo docker image prune -f || true
sudo docker volume prune -f || true
sudo docker network prune -f || true

# Clean up any remaining containers that might be stuck
echo "Stopping any remaining containers..."
sudo docker stop $(sudo docker ps -q) || true
sudo docker rm $(sudo docker ps -aq) || true

echo "Before install cleanup completed."