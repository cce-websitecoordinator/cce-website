#!/bin/bash
set -e
echo "Starting services..."
cd /home/ubuntu/cce-website/

# Function to check if services are healthy
check_services() {
    local retries=0
    local max_retries=12
    
    while [ $retries -lt $max_retries ]; do
        echo "Checking services health (attempt $((retries + 1))/$max_retries)..."
        
        # Check if all expected containers are running
        if sudo docker-compose -f docker-compose.prod.yml --env-file .env ps | grep -q "Up.*app" && \
           sudo docker-compose -f docker-compose.prod.yml --env-file .env ps | grep -q "Up.*db" && \
           sudo docker-compose -f docker-compose.prod.yml --env-file .env ps | grep -q "Up.*proxy"; then
            
            # Check if the app is actually responding
            if sudo docker exec cce-website-proxy-1 wget -qO- http://app:8000 >/dev/null 2>&1; then
                echo "All services are healthy!"
                return 0
            fi
        fi
        
        echo "Services not ready yet, waiting..."
        sleep 10
        retries=$((retries + 1))
    done
    
    echo "Services failed to become healthy within timeout"
    return 1
}

# Start services
echo "Starting all services..."
sudo docker-compose -f docker-compose.prod.yml --env-file .env up -d

# Check if services are healthy
if check_services; then
    echo "Deployment successful! All services are running and healthy."
    # Show final status
    sudo docker-compose -f docker-compose.prod.yml --env-file .env ps
    exit 0
else
    echo "Deployment failed! Services are not healthy."
    echo "Container status:"
    sudo docker-compose -f docker-compose.prod.yml --env-file .env ps
    echo "App logs:"
    sudo docker logs cce-website-app-1 --tail 50
    echo "Proxy logs:"
    sudo docker logs cce-website-proxy-1 --tail 50
    exit 1
fi