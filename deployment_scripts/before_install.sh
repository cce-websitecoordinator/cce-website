#!/bin/bash
set -e

echo "Pruning old, unused Docker images..."

sudo docker image prune -f