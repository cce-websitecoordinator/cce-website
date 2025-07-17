#!/bin/bash
set -e

echo "Starting the application..."
cd /home/ubuntu/cce-website/

sudo docker-compose -f docker-compose.prod.yml up -d