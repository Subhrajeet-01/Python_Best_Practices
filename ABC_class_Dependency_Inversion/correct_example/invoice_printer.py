from billable import Billable

class InvoicePrinter:
    def print_invoice(self, item: Billable) -> None:
        print(f"Final price: {item.final_price}")