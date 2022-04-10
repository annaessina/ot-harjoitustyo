
class Calculator:
    def __init__(self):
        self.number1 = self.number2 = 0

    def start(self):
        temp = "+"

        while temp == "+" or temp == "-" or temp == "*" or temp == "/":
            print("Select any operation from +, -, *, /: ")

            temp = str(input())

            if temp != "+" and temp != "-" and temp != "*" and temp != "/":
                print("Incorrect command")
                break

            print("Type in numbers?")
            self.number1 = int(input("number1: "))
            self.number2 = int(input("number2: "))

            if temp == "+":
                print(self.add())

            if temp == "-":
                print(self.dist())

            if temp == "*":
                print(self.mult())

            if temp == "/":
                print(self.div())



    def add(self):
        result = self.number1 + self.number2
        return result

    def dist(self):
        result = self.number1 - self.number2
        return result

    def mult(self):
        result = self.number1 * self.number2
        return result

    def div(self):
        result = self.number1 / self.number2
        return result

if __name__ == "__main__":
    Calculator = Calculator()
    Calculator.start()