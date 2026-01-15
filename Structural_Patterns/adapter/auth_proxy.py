from models import WeatherData
from weather_provider import WeatherProvider

class AuthProxy(WeatherProvider):
    def __init__(self, wrapped: WeatherProvider) -> None:
        self._wrapped = wrapped
    
    def get_weather(self, city: str) -> WeatherData:
        if city == "Restricted":
            raise PermissionError("Access to this city's weather data is restricted.")
        return self._wrapped.get_weather(city)