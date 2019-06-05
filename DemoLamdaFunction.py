# Normal Function

def Add(a, b):
    c = a + b
    print("The Sum is ", c)
    return a, b, c

c = Add(10, 20)
print(c)

# Lambda Function

addLambda = lambda a, b : a + b
print(addLambda(10, 30))

# Normal Function

def Add(a, b, func):
    c = a + b + 10
    d = func(a, b)
    print("The anonymous function value is :", d)
    print("Normal Function is", c)

# Lambda Function

addLambda = lambda a, b : a + b
Add(100, 50, addLambda)


c = 0      # Global Variable
defaultValue = 10
#Normal Function
def Add(a, b):
    c = a + b + defaultValue
    d = 10          # Local Variable
    print("Add result is ", c)


def Sub(a, b):
    c = a - b + defaultValue
    #print(d)   # d is local variable and we cant use it in other functions
    print("Sub result is ", c)


def Mul(a, b):
    c = a * b
    print("Mul result is ", c)


# Lambda Function
Add(100, 50)
Sub(100, 50)
Mul(100, 50)
