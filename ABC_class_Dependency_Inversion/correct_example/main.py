from product import Product
from invoice_printer import InvoicePrinter
from subsciption import Subscription

def main() -> None:
    printer = InvoicePrinter()
    product = Product(price=1000, discount=10)
    subscription = Subscription(monthly_price=300, month=3)

    printer.print_invoice(product)
    printer.print_invoice(subscription)


if __name__ == "__main__":
    main()