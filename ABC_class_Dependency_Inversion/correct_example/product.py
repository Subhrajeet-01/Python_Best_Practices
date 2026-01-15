from billable import Billable

class Product(Billable):
    def __init__(self, price: float, discount: int) -> None:
        self._price = price
        self._discount = self._validation_discount(discount)
    
    @staticmethod
    def _validation_discount(discount: int) -> int:
        if not 0 <= discount <= 50:
            raise ValueError("Discount must be between 0 and 50")
        return discount

    @property
    def final_price(self) -> float:
        return self._price - (self._price * self._discount / 100)