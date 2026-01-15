from third_party_weather_API import ThirdPartyWeatherAPI
from weather_provider import WeatherProvider
from models import WeatherData

class ThirdPartyWeatherAdapter(WeatherProvider):
    def __init__(self, api: ThirdPartyWeatherAPI) -> None:
        self._api = api
    
    def get_weather(self, city: str) -> WeatherData:
        data = self._api.fetch(city)
        return WeatherData(
            temperature=data["temp_celsius"],
            humidity=data["humidity"],
            city = data["city"]
        )