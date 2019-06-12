class Point:
    # The  __del__() destructor prints the class name of an instance that is about to be destroyed.
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def __del__(self):
        classname = self.__class__.__name__
        print(classname, "Destroyed")

a = Point()
b = a
c = b
print(id(a), id(b), id(c))

del a
del b
del c