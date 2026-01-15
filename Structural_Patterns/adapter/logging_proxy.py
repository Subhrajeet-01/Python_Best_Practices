from models import WeatherData
from weather_provider import WeatherProvider

class LoggingProxy(WeatherProvider):
    def __init__(self, wrapped: WeatherProvider) -> None:
        self._wrapped = wrapped

    def get_weather(self, city: str) -> WeatherData:
        print(f"Fetching weather data for {city}")
        data = self._wrapped.get_weather(city)
        print(f"Retrieved data: Temperature={data.temperature}, Humidity={data.humidity}")
        return data