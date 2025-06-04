# Weather CLI App

A simple command-line interface (CLI) application to fetch and display weather information based on a given zip code using a free weather API.

## Features

- Retrieve current weather data for a specified zip code.
- Easy to use command-line interface.

## Requirements

- Python 3.x
- `requests` library

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/weather-cli-app.git
   ```

2. Navigate to the project directory:
   ```
   cd weather-cli-app
   ```

3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## API Key Setup

This application requires an API key from OpenWeatherMap to function properly. You can get a free API key by signing up at [OpenWeatherMap](https://openweathermap.org/).

Once you have your API key, you can set it up in one of the following ways:

1. **Environment Variable**:
   ```
   export WEATHER_API_KEY=your_api_key_here
   ```

2. **Create a .env file**:
   Copy the `.env.example` file to `.env` and replace `your_api_key_here` with your actual API key:
   ```
   cp .env.example .env
   ```

3. **Using Docker**:
   When running with Docker, you can provide the API key as an environment variable:
   ```
   docker run -p 5000:5000 -e WEATHER_API_KEY=your_api_key_here weather-cli-app
   ```
   Or use the Makefile command:
   ```
   make run-with-key
   ```
   (This will prompt you to enter your API key)

## Using `pyenv` to Manage Python Versions

If you need to manage multiple Python versions, you can use `pyenv`:

1. Install `pyenv`:
   ```
   curl https://pyenv.run | bash
   ```

2. Add `pyenv` to your shell:
   ```
   export PATH="$HOME/.pyenv/bin:$PATH"
   eval "$(pyenv init --path)"
   eval "$(pyenv init -)"
   eval "$(pyenv virtualenv-init -)"
   ```

3. Restart your shell or run the commands directly in your terminal.

4. Install the required Python version:
   ```
   pyenv install 3.x.x
   ```

5. Set the local Python version for the project:
   ```
   pyenv local 3.x.x
   ```

6. Verify the Python version:
   ```
   python --version
   ```

## Usage

To get the weather information for a specific zip code, run the following command:

```
python src/main.py <ZIP_CODE>
```

Replace `<ZIP_CODE>` with the desired zip code.

## Weather API

This application uses a free weather API to fetch weather data. Make sure to check the API documentation for any usage limits or additional features.