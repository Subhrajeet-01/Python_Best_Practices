# Initial Implementation

def calculate_price(price, discount):
    if discount < 0 or discount > 50:
        raise ValueError("Invalid discount")
    return price - (price * discount / 100)


def print_invoice(final_price):
    print(f"Final price: {final_price}")


price = calculate_price(1000, 10)
print_invoice(price)

# --------------------------------------------------------------
# Key Rules You Must Remember (Non-Negotiable)      CORRECT IMPLEMENTATION IN task1.py

# Domain classes never print

# No executable code outside main.py

# Static methods do not use self

# Validation lives inside the owning class

# Derived values should be properties, not stored state
# --------------------------------------------------------------

# Task 1
# Product.py                        # Wrong Implementation
class Product:
    def __init__(self, price: int, discount: int) -> None:
        self.price = price
        self.discount = discount
        self.final_price = calculate_price(price, discount)     # If discount changes, final_price becomes stale.Derived data should be computed, not stored.
    
    def calculate_price(self, price: int, discount: int) -> int:
        if discount < 0 or discount > 50:
            raise ValueError("Invalid discount")
        return price - (price * discount / 100)

    def print_invoice(self, final_price : int) -> None:
        print(f"Final price: {final_price}")

product = Product(1000, 10)
product.print_invoice(final_price)


# Task 2
# Product.py                     # Correct Implementation but logic is wrongly placed.                    
class Product:
    def __init__(self, price: int, discount: int) -> None:
        self.price = price
        self.discount = discount
        self.final_price = calculate_price(price, discount)
    
    @property
    def calculate_price(self, price: int, discount: int) -> int:
        if discount < 0 or discount > 50:
            raise ValueError("Invalid discount")
        return price - (price * discount / 100)

# final_price.py
class InvoicePrinter:
    def print_invoice(self, product: Product) -> None:
        print(f"Final price: {product.final_price}")

#main.py
from product import Product
from final_price import InvoicePrinter

final_price = Product(1000, 10)
invoice = InvoicePrinter()

invoice.print_invoice(final_price)