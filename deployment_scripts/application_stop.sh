#!/bin/bash
set -e

echo "Stopping all services defined in docker-compose.prod.yml..."
cd /home/ubuntu/cce-website/

sudo docker-compose -f docker-compose.prod.yml down --remove-orphans