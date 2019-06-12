class Parent:
    attr = 60
    def __init__(self):
        print("Calling Parent Constructor")

    def ParentMethod(self):
        print("Calling Parent method")

    def Setattr(self, attr):
        Parent.attr = attr

    def Getattr(self):
        print("The attr is : ", Parent.attr)

    def Hasattr(self):
        print("Yes the attribute exists")

class Child(Parent):
    def __init__(self):
        print("Calling child Constructor")

    def ChildMethod(self):
        print("Calling Child Method")

c = Child()
c.ChildMethod()
c.ParentMethod()
c.Setattr(70)
c.Getattr()





