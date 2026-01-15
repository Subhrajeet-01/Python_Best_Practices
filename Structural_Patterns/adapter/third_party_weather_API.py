# Adapter Pattern : Use Adapter pattern to solve output of ThirdPartyWeatherAPI by exposes a clean interface to clients, and adds caching & access control.
# Problem: Third-party API mismatch

class ThirdPartyWeatherAPI:
    def fetch(self, city: str) -> dict:
        return {
            "temp_celsius": 30,
            "humidity": 70,
            "city": city
        }

# But your system wants:

# WeatherData(temp, humidity, city)

