from payment_method import PaymentMethod
from card import Card
from upi import UPI
from wallet import Wallet
from netBanking_Payment import NetBanking

class PaymentFactory:                       # Factory Pattern

    _methods = {
        "upi": UPI,
        "card": Card,
        "wallet": Wallet,
        "net_banking": NetBanking
    }

    @classmethod
    def create(cls, method: str) -> PaymentMethod:
        try:
            return cls._methods[method]()
        except KeyError:
            raise ValueError(f"Unknown payment method: {method}")
        