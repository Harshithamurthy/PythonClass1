# # Operator Overloading
#
# class vector:
#     def Add(self, a, b):
#         self.c = a + b
#         print("The result is ", self.c)
#
# v1 = vector()
# v1.Add(25, 27)
# v1.Add("Hello", " World")
# v1.Add(24.56, 67.84)
#
# v2 = vector()
# v2.Add(27, 28)
#
# v = v1 + v2         # Showing error because we can't add two objects
# print(v)

#OR

class vector:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return 'vector(%d, %d)' %(self.a, self.b)

    def __add__(self, other):              # To add two objects
        v = vector(self.a + other.a, self.b + other.b)            #v = vector(10+30=40, 20+40=60)
        return v
        #return vector(self.a + other.a, self.b + other.b)         #v = vector(40, 60)

v1 = vector(10, 20)
v2 = vector(30, 40)
v = v1 + v2
print(v)


class vector:
    def __init__(self, a, b):
        self.a = a
        self.b = b


    def __add__(self, other):              # To add two objects
        v = vector(self.a + other.a, self.b + other.b)            #v = vector(10+30=40, 20+40=60)
        return v
        #return vector(self.a + other.a, self.b + other.b)         #v = vector(40, 60)

v1 = vector(10, 20)
v2 = vector(30, 40)
v = v1 + v2
print(v1.a + v2.a, v1.b + v2.b)


