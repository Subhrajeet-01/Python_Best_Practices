from payment_method import PaymentMethod

class Wallet(PaymentMethod):
    def pay(self, amount: float) -> None:
        print(f"Paid {amount} using Wallet")