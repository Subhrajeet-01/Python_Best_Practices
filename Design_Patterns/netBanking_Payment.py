from payment_method import PaymentMethod

class NetBanking(PaymentMethod):
    def pay(self, amount: float) -> None:
        print(f"Paid {amount} using Net Banking")