from invoice_printer import Invoice_printer
from product import Product
from order import Order

def main() -> None:
    product1 = Product(price=1000, quantity=5, discount=10)
    product2 = Product(price=500, quantity=2, discount=5)

    order = Order(products=[product1, product2])

    printer = Invoice_printer()
    printer.print_invoice(product1)
    printer.print_invoice(product2)
    printer.print_invoice(order)

    data = [
        {"price": 1000, "quantity": 5, "discount": 10},
        {"price": 500, "quantity": 2, "discount": 5},
    ]

    order_from_dict = Order.from_dict(data)
    printer.print_invoice(order_from_dict) 
    
if __name__ == "__main__":
    main()


# Important Design Rules You Just Learned

# @property must be side-effect free

# Aggregates must use composition

# Factories belong in @classmethod

# Domain naming matters

# Interfaces allow extension without modification