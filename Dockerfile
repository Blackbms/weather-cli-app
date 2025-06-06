# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 5000 for the Flask app
EXPOSE 5000

# Define environment variables
ENV PYTHONUNBUFFERED=1
# The API key will be provided at runtime
ENV WEATHER_API_KEY=""

# Run the application
CMD ["python3", "src/main.py"]