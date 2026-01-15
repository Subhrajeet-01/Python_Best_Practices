from payment_method import PaymentMethod

# Decorator Pattern
class LoggingPayment(PaymentMethod):
    def __init__(self, wrapped: PaymentMethod) -> None:
        self._wrapped = wrapped
    
    def pay(self, amount: float) -> None:
        print(f"Logging: Initiating payment of {amount}")
        self._wrapped.pay(amount)
        print(f"Logging: Payment of {amount} completed")