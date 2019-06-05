# def Add(a,b):
#     c = a + b
#     print("The Sum is ", c)
#     return a, b, c
#
# c = Add(20,10)
# print(c)

result = 0
def Add(a, b):
    result = a + b
    print("The Sum is ", result)


def Sub(a, b):
    result = a - b
    print("The Sub is ", result)


def Mul(a, b):
    result = a * b
    print("The Mul is ", result)


def Div(a, b):
    result = a / b
    print("The Div is ", result)


print('-' * 100)


result = 0
def Add(a, b):
    'Addition of two numbers'
    result = a + b
    print("The Sum is ", result)


def Sub(a, b):
    'Subtraction of two numbers'
    result = a - b
    print("The Sub is ", result)


def Mul(a, b):
    'Multiplication of two numbers'
    result = a * b
    print("The Mul is ", result)

def Add(a, b):
    'Addition of two numbers'
    result = a + b + 100
    print("The Sum is ", result)

if __name__ == '__main__':
    Add(10, 20)
