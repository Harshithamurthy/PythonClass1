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

