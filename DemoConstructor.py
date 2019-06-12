class Calculator:
    result = 0

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def Add(self):
        result = self.a + self.b
        print("The sum is : ", result)

    def Sub(self):
        result = self.a - self.b
        print("The sub is : ", result)

    def Mul(self):
        result = self.a * self.b
        print("The Mul is : ", result)

    def Add(self):
            result = self.a + self.b + 20
            print("The sum is : ", result)


c = Calculator(60, 40)
c.Add()
c.Sub()
c.Mul()
print("-" * 100)
c.__init__(80, 40)
c.Add()
c.Sub()
c.Mul()

