from billable import Billable

class Subscription(Billable):
    def __init__(self, monthly_price: float, month: int) -> None:
        self._monthly_price = monthly_price
        self._month = month
    
    @property
    def final_price(self) -> float:
        return self._monthly_price * self._month
