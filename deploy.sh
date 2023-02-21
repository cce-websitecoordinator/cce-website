#!/bin/bash

# Load environment variables from .env file
source cce/.env

# Log in to ECR
$(aws ecr get-login --no-include-email --region $AWS_REGION)

# Pull the updated Docker image from ECR
docker pull $AWS_ACCOUNT_ID.dkr.ecr.$AWS_REGION.amazonaws.com/$IMAGE_NAME

# Stop and remove the old container (if it exists)
docker stop $CONTAINER_NAME || true
docker rm $CONTAINER_NAME || true

# Run the new container
docker run -d --name $CONTAINER_NAME -p 80:8000 $AWS_ACCOUNT_ID.dkr.ecr.$AWS_REGION.amazonaws.com/$IMAGE_NAME
