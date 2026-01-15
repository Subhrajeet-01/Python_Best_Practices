# Final Wiring

from weather_facade import WeatherServiceFacade
from proxy import WeatherServiceProxy
from logging_proxy import LoggingProxy
from auth_proxy import AuthProxy

def main() -> None:
    # facade = WeatherServiceFacade()
    # proxy = WeatherServiceProxy(facade)
    # logging_proxy = LoggingProxy(proxy)
    # auth_proxy = AuthProxy(logging_proxy)
    # print(auth_proxy.get_weather("Restricted").temperature)
    # print(auth_proxy.get_weather("Delhi").temperature)

    facade = WeatherServiceFacade()

    proxy_chain = AuthProxy(
        LoggingProxy(
            WeatherServiceProxy(facade)
        )
    )

    try:
        proxy_chain.get_weather("Restricted")   
    except PermissionError as e:
        print(e)
    
    print(proxy_chain.get_weather("Delhi").temperature)
    print(proxy_chain.get_weather("Delhi").temperature)  # Should hit the cache

if __name__ == "__main__":
    main()
