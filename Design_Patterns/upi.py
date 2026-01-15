from payment_method import PaymentMethod

class UPI(PaymentMethod):
    def pay(self, amount: float) -> None:
        print(f"Paid {amount} using UPI")
        