class Base:
    def Singer(self):
        print("I am not a professional singer")


class Child(Base):
    def Singer(self):
        print("I am a professional singer")

ch = Child()
ch.Singer()
b = Base()
b.Singer()

#OR

class Base:
    def Singer(self, a, b = 0):
        print("The value of a is", a)
        print("The value of b is", b)
        print("I am not a professional singer")


class Child(Base):
    def Singer(self):
        print("I am a professional singer")

b = Base()
b.Singer(32)
b.Singer(12, 20)
ch = Child()
ch.Singer()