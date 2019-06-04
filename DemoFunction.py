# Without Parameter

def Add():
    c = 10 + 20
    print("The Sum is ", c)

Add()


# With Parameters

def Sub(a, b):
    c = a - b
    print("The Sub is ", c)

Sub(50, 10)

# With Default Parameter

def Add(a, b = 0):
    c = a + b
    print("The Sum is ", c)

Add(12)


def Addition(a=0, b=0):
    c = a + b
    print("The Sum is :", c)

a = 10
b = 20

Addition(a, b)
Addition(20, 30)
Addition(40, 50)
Addition(60, 70)
Addition(90)
Addition()


# With named Parameter

def Employee(id , name):
    print("The Employee Id is ", id)
    print("The Employee Name is ", name)

Employee(12, "Pragim")
Employee("Pragim", 12)
Employee(name="Pragim", id=12)

def Employee(id , name):
    print("Name is ", name)
    print("Id is ", id)
    return "Name of the Employee is{} and the Employee Id is {}".format(name, id)

emp = Employee(name="Kumar", id=10)
print(emp)


# With Variable Length Argument

def VariableLengthAruguments(empName, empid, *tupleVar):
    print("Employee Name :", empName)
    print("Employee ID :", empid)
    print("Tuple Variable", tupleVar)
    # for i in tupleVar:
    #     print(i)


VariableLengthAruguments("Pragim", 1234)
print('-' * 100)
VariableLengthAruguments("Kumar", 4321, "Name", "Value")
print('-' * 100)
VariableLengthAruguments("Ravi", 421, "sdf", "sdg", 1, 2, [23, 45,67], 4, 5, 6)
