from report_templete import ReportTemplete

class SaleReport(ReportTemplete):

    def fetch_data(self) -> None:
        print("Fetching sales data")
    
    def format_data(self) -> None:
        print("Formatting sales data")

    def export(self) -> None:
        print("Exporting sales report")