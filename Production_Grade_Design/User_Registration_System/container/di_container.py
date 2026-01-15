from typing import Type, Dict, Callable, Any

class DIContainer:
    def __init__(self) -> None:
        self._providers: Dict[Type, Callable[[], Any]] = {}

    def register(self, interface: Type, provider: Callable[[], Any]) -> None:
        self._providers[interface] = provider
    
    def resolve(self, interface: Type) -> Any:
        provider = self._providers.get(interface)
        
        if not provider:
            raise ValueError(f"No provider registered for {interface}")
        return provider()