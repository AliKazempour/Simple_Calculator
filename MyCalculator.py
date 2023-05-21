class Calculator:
    def sum(self, a, b):
        print(f"{a}+{b}={a+b}")

    def subtract(self, a, b):
        print(f"{a}-{b}={a-b}")

    def multiply(self, a, b):
        print(f"{a}*{b}={a*b}")

    def division(self, a, b):
        print(f"{a}/{b}={a/b}")


mycalculator = Calculator()
mycalculator.subtract(2, 5)
mycalculator.multiply(4, 7)
