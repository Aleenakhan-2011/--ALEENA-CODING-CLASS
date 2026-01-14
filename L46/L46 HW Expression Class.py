class  Calculator:
    #Define a constructor
    def __init__(self,x,y,z):
        self.num1 = x
        self.num2 = y
        self.num3 = z

    def add(self):
        self.result = self.num1 + self.num2 + self.num3
        print("The sum is:", self.result)

    def subtract(self):
        self.result = self.num1 - self.num2 - self.num3
        print("The difference is:", self.result)

    def multiply(self):
        self.result = self.num1 * self.num2 * self.num3
        print("The product is:", self.result)

    def divide(self):
        if self.num2 == 0:
            print("Cannot divide by zero.")
        else:
            self.result = self.num1 / self.num2
            print("The quotient is:", self.result)

# object which calls the constructor
x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
z = int(input("Enter third number: "))

calc = Calculator(x, y, z)
calc.add()
calc.subtract()
calc.multiply()
calc.divide()
