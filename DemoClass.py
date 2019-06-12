class Calculator:

    # Data Member - Variable Initialization
    # Global Variable
    # Class Variable
    result = 0

    # Self ==> The Current Object

    def Add(self, a, b):
        Calculator.result = a + b
        self.result = a + b
        print("The result is {}:".format(self.result))

calc = Calculator()
Calculator.result = 20
calc.Add(10,20)
calc.Add(20,30)
calc.Add(30,40)

calc2 = Calculator()
calc2.Add(50,60)
print("Global Variable : ", Calculator.result)

print(type(calc2))

# x = 10
# y = "Welcome"
#
# print(type(x))
# print(type(y))
# print(dir(int))

print('-' * 100)

class Demo:

    result = 0

    def Add(self, a, b):
        Demo.result = 10
        self.result = a + b
        print("With in the function", self.result)
        self.result = 70
        print("The Sum is {}".format(self.result))

c = Demo()
Demo.result = 100
c.Add(20, 30)
c.Add(50, 60)





