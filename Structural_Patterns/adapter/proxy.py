from weather_provider import WeatherProvider   
from models import WeatherData

class WeatherServiceProxy(WeatherProvider):
    def __init__(self, wrapped: WeatherProvider) -> None:
        self._wrapped = wrapped
        self._cache: dict[str, WeatherData] = {}

    def get_weather(self, city: str) -> WeatherData:
        if city in self._cache:
            print("Returning cached data")
            return self._cache[city]
        
        data = self._wrapped.get_weather(city)
        self._cache[city] = data
        return data

