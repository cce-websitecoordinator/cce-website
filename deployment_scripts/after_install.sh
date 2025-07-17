#!/bin/bash
set -e

echo "Building Docker images from new source code..."
cd /home/ubuntu/cce-website/

sudo docker-compose -f docker-compose.prod.yml build