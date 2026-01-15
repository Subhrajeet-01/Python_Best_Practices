from abc import ABC, abstractmethod

class ReportTemplete(ABC):

    def generate(self) -> str:
        self.fetch_data()
        self.format_data()
        self.export()

    @abstractmethod
    def fetch_data(self) -> None:
        pass

    @abstractmethod
    def format_data(self) -> None:
        pass

    @abstractmethod
    def export(self) -> None:
        pass