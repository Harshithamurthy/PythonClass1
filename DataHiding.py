# Data Hiding - Not able to print the attributes which are made private

class Counting:
    __count = 0      # Private Attribute

    def counter(self):
        self.__count += 1
        print(self.__count)

c = Counting()
c.counter()
c.counter()
print(c.__count)


#OR

class Counting:
    __count = 0      # Private Attribute

    def counter(self):
        self.__count += 1
        print(self.__count)

c = Counting()
c.counter()
c.counter()
print(c._Counting__count)   # We can access private attribute as Object._className__AttributeName

