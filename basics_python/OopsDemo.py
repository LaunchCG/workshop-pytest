# self keyword is mandatory for calling variable names into method
# instance and class variables have whole different purpose
# constructor name should be __init__
# new keyword is not required when you create object

class Calculator:
    num = 100

    def __init__(self, a, b):
        self.firstNumber = a
        self.lastNumber = b
        print("Constructor called automatically when the object created")

    def getData(self):
        print("I am executing as method in class")

    def summation(self):
        return self.firstNumber+self.lastNumber+Calculator.num
        # return self.firstNumber+self.lastNumber+self.num


obj = Calculator(2, 3)
obj.getData()
print(obj.summation())

obj1 = Calculator(5, 5)
print(obj1.summation())
print(obj.num)