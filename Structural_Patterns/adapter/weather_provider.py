# Step 2: Target Interface

from abc import ABC, abstractmethod
from models import WeatherData

class WeatherProvider(ABC):

    @abstractmethod
    def get_weather(self, city: str) -> WeatherData:
        pass