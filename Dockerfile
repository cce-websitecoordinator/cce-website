# Filename: Dockerfile

# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /app

# Install dependencies
# Copy the requirements file first to leverage Docker cache
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application's code
COPY . .

# Make the entrypoint script executable
RUN chmod +x /app/entrypoint.prod.sh

# The command to run when the container starts
# This will be overridden by docker-compose, but it's good practice
CMD ["/app/entrypoint.prod.sh"]