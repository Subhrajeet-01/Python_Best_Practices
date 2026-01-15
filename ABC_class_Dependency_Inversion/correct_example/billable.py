from abc import ABC, abstractmethod

class Billable(ABC):
    @property
    @abstractmethod
    def final_price(self) -> float:
        pass

