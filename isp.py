from abc import ABC, abstractmethod


class Printer(ABC):
    @abstractmethod
    def print(self):
        pass


class Scanner(ABC):
    @abstractmethod
    def scan(self):
        pass


class MultiFunctionMachine(Printer, Scanner):
    def print(self):
        print("Printing document")

    def scan(self):
        print("Scanning document")


if __name__ == "__main__":
    machine = MultiFunctionMachine()
    machine.print()
    machine.scan()
