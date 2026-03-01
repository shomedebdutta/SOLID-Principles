class Report:
    def __init__(self, content):
        self.content = content

    def generate(self):
        return self.content


class ReportPrinter:
    def print_report(self, report):
        print(report.generate())


if __name__ == "__main__":
    report = Report("Monthly Sales Report")
    printer = ReportPrinter()
    printer.print_report(report)
