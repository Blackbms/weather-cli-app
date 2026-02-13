# pylint: disable=missing-module-docstring,missing-function-docstring,missing-class-docstring,line-too-long
import os
from datetime import datetime

from flask import Flask, render_template, request

from utils.weather_api import WeatherAPI

# Explicitly set the template folder
app = Flask(
    __name__, 
    template_folder=os.path.join(os.path.dirname(__file__), "../templates"),
    static_folder=os.path.join(os.path.dirname(__file__), "../static")
)

# Get API key from environment variable
WEATHER_API_KEY = os.environ.get("WEATHER_API_KEY", "")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/get_weather", methods=["POST"])
def get_weather():
    error_message = None
    weather_info = {}

    # Check for zip code
    zip_code = request.form.get("zip_code")
    if not zip_code:
        error_message = "Please enter a zip code."
    # Check for API key
    elif not WEATHER_API_KEY:
        error_message = "API key not configured. Please set the WEATHER_API_KEY environment variable."
    else:
        # Try to get weather data
        weather_api = WeatherAPI(WEATHER_API_KEY)
        try:
            weather_data = weather_api.get_weather(zip_code)

            if weather_data:
                # Extract weather information
                city = weather_data.get("name")
                temperature = weather_data.get("main", {}).get("temp")
                wind_speed = weather_data.get("wind", {}).get("speed")
                wind_direction = weather_data.get("wind", {}).get("deg")
                humidity = weather_data.get("main", {}).get("humidity")
                sunrise = weather_data.get("sys", {}).get("sunrise")
                sunset = weather_data.get("sys", {}).get("sunset")

                # Convert timestamps to human-readable format
                sunrise_time = (
                    datetime.fromtimestamp(sunrise).strftime("%Y-%m-%d %H:%M:%S")
                    if sunrise
                    else "N/A"
                )
                sunset_time = (
                    datetime.fromtimestamp(sunset).strftime("%Y-%m-%d %H:%M:%S")
                    if sunset
                    else "N/A"
                )

                # Store weather info in dictionary
                weather_info = {
                    "city": city,
                    "temperature": temperature,
                    "wind_speed": wind_speed,
                    "wind_direction": wind_direction,
                    "humidity": humidity,
                    "sunrise": sunrise_time,
                    "sunset": sunset_time,
                }
            else:
                error_message = "Unable to retrieve weather data."
        except (ValueError, TypeError) as e:
            error_message = f"Error parsing weather data: {e}"
        except ConnectionError as e:
            error_message = f"Connection error: {e}"
        except Exception as e:  # pylint: disable=broad-except
            error_message = f"Unexpected error: {e}"

    # Single return statement at the end
    return render_template("index.html", error=error_message, **weather_info)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
