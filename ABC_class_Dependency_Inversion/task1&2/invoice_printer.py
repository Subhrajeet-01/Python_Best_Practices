from billability import Billable

class Invoice_printer:
    def print_invoice(self, item: Billable):
        print(f"Final Price: {item.final_price}")