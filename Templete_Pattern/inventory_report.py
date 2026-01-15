from report_templete import ReportTemplete

class InventoryReport(ReportTemplete):

    def fetch_data(self) -> None:
        print("Fetching inventory data")
    
    def format_data(self) -> None:
        print("Formatting inventory data")

    def export(self) -> None:
        print("Exporting inventory report")