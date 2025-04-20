import os
from flask import Flask, request, render_template
from utils.weather_api import WeatherAPI
from datetime import datetime

# Explicitly set the template folder
app = Flask(__name__, template_folder=os.path.join(os.path.dirname(__file__), '../templates'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get_weather', methods=['POST'])
def get_weather():
    zip_code = request.form.get('zip_code')
    if not zip_code:
        return render_template('index.html', error="Please enter a zip code.")

    weather_api = WeatherAPI('d7494fd98b3cf1de4e9edaed6506164c')
    try:
        weather_data = weather_api.get_weather(zip_code)

        if weather_data:
            city = weather_data.get('name')
            temperature = weather_data.get('main', {}).get('temp')
            wind_speed = weather_data.get('wind', {}).get('speed')
            wind_direction = weather_data.get('wind', {}).get('deg')
            humidity = weather_data.get('main', {}).get('humidity')
            sunrise = weather_data.get('sys', {}).get('sunrise')
            sunset = weather_data.get('sys', {}).get('sunset')

            # Convert sunrise and sunset timestamps to human-readable format
            sunrise_time = datetime.fromtimestamp(sunrise).strftime('%Y-%m-%d %H:%M:%S') if sunrise else "N/A"
            sunset_time = datetime.fromtimestamp(sunset).strftime('%Y-%m-%d %H:%M:%S') if sunset else "N/A"

            return render_template('index.html', city=city, temperature=temperature, wind_speed=wind_speed,
                                   wind_direction=wind_direction, humidity=humidity, sunrise=sunrise_time,
                                   sunset=sunset_time)
        else:
            return render_template('index.html', error="Unable to retrieve weather data.")
    except Exception as e:
        return render_template('index.html', error=f"Error retrieving weather data: {e}")

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')