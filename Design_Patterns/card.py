from payment_method import PaymentMethod

class Card(PaymentMethod):
    def pay(self, amount: float) -> None:
        print(f"Paid {amount} using Card")