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