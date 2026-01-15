# Problem: Build CLI / Button based action system

from abc import ABC, abstractmethod

class Command(ABC):

    @abstractmethod
    def execute(self) -> None:
        pass
    