#!/bin/bash
set -e
echo "Starting services..."
cd /home/ubuntu/cce-website/

# Function to check if services are healthy
check_services() {
    local retries=0
    local max_retries=15
    
    while [ $retries -lt $max_retries ]; do
        echo "Checking services health (attempt $((retries + 1))/$max_retries)..."
        
        # Check if containers are running
        app_status=$(sudo docker-compose -f docker-compose.deploy.yml --env-file .env ps app | grep "Up" || echo "")
        db_status=$(sudo docker-compose -f docker-compose.deploy.yml --env-file .env ps db | grep "Up" || echo "")
        proxy_status=$(sudo docker-compose -f docker-compose.deploy.yml --env-file .env ps proxy | grep "Up" || echo "")
        
        echo "App status: $app_status"
        echo "DB status: $db_status" 
        echo "Proxy status: $proxy_status"
        
        if [ -n "$app_status" ] && [ -n "$db_status" ] && [ -n "$proxy_status" ]; then
            echo "All containers are running, checking app connectivity..."
            
            # Simple health check - just check if app container responds
            if sudo docker exec cce-website-app-1 python manage.py check --database default >/dev/null 2>&1; then
                echo "All services are healthy!"
                return 0
            else
                echo "App health check failed, but containers are running..."
            fi
        else
            echo "Some containers are not running yet..."
        fi
        
        echo "Services not ready yet, waiting..."
        sleep 15
        retries=$((retries + 1))
    done
    
    echo "Services failed to become healthy within timeout"
    echo "Final container status:"
    sudo docker-compose -f docker-compose.deploy.yml --env-file .env ps
    return 1
}

# Start services
echo "Starting all services..."
sudo docker-compose -f docker-compose.deploy.yml --env-file .env up -d

# Wait a bit for containers to initialize
echo "Waiting for containers to initialize..."
sleep 10

# Check if services are healthy
if check_services; then
    echo "Deployment successful! All services are running and healthy."
    # Show final status
    sudo docker-compose -f docker-compose.deploy.yml --env-file .env ps
    exit 0
else
    echo "Deployment failed! Services are not healthy."
    echo "Container status:"
    sudo docker-compose -f docker-compose.deploy.yml --env-file .env ps
    echo "App logs:"
    sudo docker logs cce-website-app-1 --tail 50 || echo "Could not get app logs"
    echo "Proxy logs:"
    sudo docker logs cce-website-proxy-1 --tail 50 || echo "Could not get proxy logs"
    echo "DB logs:"
    sudo docker logs cce-website-db-1 --tail 50 || echo "Could not get db logs"
    exit 1
fi