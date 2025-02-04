from griptape.artifacts import TextArtifact, ErrorArtifact
from griptape.core import BaseTool
from griptape.core.decorators import activity
from schema import Schema, Literal
from attr import define, field
from typing import Optional
import requests
import logging


@define
class OpenWeatherClient(BaseTool):
    BASE_URL = "http://api.openweathermap.org/data/2.5/weather"
    api_key: str = field(kw_only=True)
    units: Optional[str] = field(default="imperial", kw_only=True)

    @activity(
        config={
            "description": "Can be used to fetch weather data for a given city using the OpenWeather API. Temperatures are returned in {self.units} by default.",  # Modified description
            "schema": Schema({
                Literal(
                    "city_name",
                    description="Name of the city to fetch weather data for."
                ): str
            }),
        }
    )
    def _get_weather_by_city(self, params: dict):
        city_name = params["values"].get("city_name")

        request_params = {
            'q': city_name,
            'appid': self.api_key,
            'units': self.units
        }

        try:
            response = requests.get(self.BASE_URL, params=request_params)
            if response.status_code == 200:
                data = response.json()
                return TextArtifact(str(data))
            else:
                logging.error(f"Error fetching weather data. HTTP Status Code: {response.status_code}")
                return ErrorArtifact("Error fetching weather data from OpenWeather API")
        except Exception as e:
            logging.error(f"Error fetching weather data: {e}")
            return ErrorArtifact(f"Error fetching weather data: {e}")
