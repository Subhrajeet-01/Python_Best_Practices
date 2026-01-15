from payment_method import PaymentMethod

class PaymentService:
    def __init__(self, method: PaymentMethod) -> None:
        self._method = method
    
    def process(self, amount: float) -> None:
        self._method.pay(amount)