from billability import Billable

class Product(Billable):
    def __init__(self, price:int, quantity:int, discount) -> None:
        self._price = price
        self._quantity = quantity
        self._discount = self._validate_discount(discount)

    @staticmethod
    def _validate_discount(discount) -> int:
        if not 0 <= discount <= 50:
            raise ValueError("Discount must be between 0 and 50")
        return discount

    @property
    def final_price(self) -> float:
        return self._quantity * (self._price - (self._price * self._discount / 100))