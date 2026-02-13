# Makefile for managing the Weather CLI App Docker container

# Docker image from GitHub Container Registry
IMAGE_NAME = ghcr.io/blackbms/weather-cli-app:latest

# Pull the latest Docker image from GitHub Container Registry
pull:
	docker pull $(IMAGE_NAME)

# Build the Docker image locally (for development)
build:
	docker build -t weather-cli-app .

# Run the Docker container without API key
run: pull
	docker run -d -p 5000:5000 $(IMAGE_NAME)

# Run the Docker container with API key
run-with-key: pull
	@read -p "Enter Weather API Key: " API_KEY; \
	docker run -d -p 5000:5000 -e WEATHER_API_KEY="$$API_KEY" $(IMAGE_NAME)

# Run with environment file
run-with-env: pull
	docker run -d -p 5000:5000 --env-file .env $(IMAGE_NAME)

# Stop all running containers
stop:
	docker stop $(docker ps -q)

# Remove all stopped containers
clean:
	docker rm $(docker ps -a -q)

# Remove the Docker image
remove-image:
	docker rmi $(IMAGE_NAME)
