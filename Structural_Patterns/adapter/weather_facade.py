# PART 2 — Facade Pattern
# Problem: Client should not know about adapters, models, APIs
# We create a single clean entry point.

from adapters import ThirdPartyWeatherAdapter
from third_party_weather_API import ThirdPartyWeatherAPI

class WeatherServiceFacade:
    def __init__(self) -> None:
        api = ThirdPartyWeatherAPI()
        self._provider = ThirdPartyWeatherAdapter(api)

    def get_weather(self, city: str):
        return self._provider.get_weather(city)
    