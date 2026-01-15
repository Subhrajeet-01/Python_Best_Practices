# Task 2                                 # Correct Implementation of main.py
# Product.py
class Product:
    def __init__(self, price: int, discount: int) -> None:
        self.price = price
        self.discount = self._discount(discount)
        
    @staticmethod
    def _discount(discount: int) -> int:
        if discount < 0 or discount > 50:
            raise ValueError("Invalid discount")
        return discount

    @property
    def calculate_price(self) -> int:
        return self.price - (self.price * self.discount / 100)

# final_price.py
class InvoicePrinter:
    def print_invoice(self, product: Product) -> None:
        print(f"Final price: {product.calculate_price}")

# #main.py
# from product import Product
# from final_price import InvoicePrinter

if __name__ == "__main__":
    product = Product(price=1000, discount=10)
    printer = InvoicePrinter()

    printer.print_invoice(product)
