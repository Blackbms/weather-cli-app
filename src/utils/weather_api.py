# pylint: disable=C0114,C0115,C0116,R0903
from typing import Any, Dict, Optional

import requests


class WeatherAPI:
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.base_url = "https://api.openweathermap.org/data/2.5/weather"

    def get_weather(self, zip_code: str) -> Optional[Dict[str, Any]]:
        """
        Get weather data for a specific zip code

        Args:
            zip_code: The zip code to get weather data for

        Returns:
            Dict containing weather data or None if request failed
        """
        params = {"zip": zip_code, "appid": self.api_key, "units": "imperial"}

        try:
            # Added connect timeout (5 seconds) and read timeout (10 seconds)
            response = requests.get(self.base_url, params=params, timeout=(5, 10))
            response.raise_for_status()  # Raise exception for 4XX/5XX responses
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error fetching weather data: {e}")
            return None
