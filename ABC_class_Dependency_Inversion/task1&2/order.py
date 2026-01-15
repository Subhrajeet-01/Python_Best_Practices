# When To Use @classmethod

# Use it when:

# Situation	Use
# Alternative object creation ->	Yes
# Parsing JSON / dict ->	Yes
# Creating from file / DB ->	Yes
# Creating from API ->	Yes
# Just utility function ->	No

from billability import Billable
from product import Product
                      # wrong implementation of Cart class
# class Cart(Billable):
#     def __init__(self, price: Product) -> None:
#         self._price = price
#         self._total = 0

#     @property
#     def final_price(self) -> float:
#         self._total += self._price.final_price
#         return self._total
    
               # correct implementation of Cart class as Order

class Order(Billable):
    def __init__(self, products: list[Product]) -> None:
        self._products = products

    @property
    def final_price(self) -> float:
        return sum(product.final_price for product in self._products)
    
    @classmethod
    def from_dict(cls, data: list[dict]) -> "Order":
        products = [
            Product(
                price=item["price"],
                quantity=item["quantity"],
                discount=item["discount"]
            )
            for item in data
        ]
        return cls(products)
    
    