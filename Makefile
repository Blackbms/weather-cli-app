# Makefile for managing the Weather CLI App Docker container

# Build the Docker image
build:
	docker build -t weather-cli-app .

# Run the Docker container without API key
run:
	docker run -d -p 5000:5000 weather-cli-app

# Run the Docker container with API key
run-with-key:
	@read -p "Enter Weather API Key: " API_KEY; \
	docker run -d -p 5000:5000 -e WEATHER_API_KEY="$$API_KEY" weather-cli-app

# Run with environment file
run-with-env:
	docker run -d -p 5000:5000 --env-file .env weather-cli-app

# Stop all running containers
stop:
	docker stop $(docker ps -q)

# Remove all stopped containers
clean:
	docker rm $(docker ps -a -q)

# Remove the Docker image
remove-image:
	docker rmi weather-cli-app
