# Makefile for managing the Weather CLI App Docker container

# Build the Docker image
build:
	docker build -t weather-cli-app .

# Run the Docker container
run:
	docker run -d -p 5000:5000 weather-cli-app

# Stop all running containers
stop:
	docker stop $(docker ps -q)

# Remove all stopped containers
clean:
	docker rm $(docker ps -a -q)

# Remove the Docker image
remove-image:
	docker rmi weather-cli-app
