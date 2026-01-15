# step1 : Domain Model
class WeatherData:
    def __init__(self, temperature: float, humidity: int, city: str) -> None:
        self.temperature = temperature
        self.humidity = humidity
        self.city = city
