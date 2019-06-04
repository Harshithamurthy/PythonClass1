# Pass By Value

def PassByValue(valueType):
    valueType = "NewValue"
    print("Printing after the value gets modified:", valueType)

valueType = "Intial Value"
print("valueType : Initial :",valueType)

PassByValue(valueType)
print(valueType)


# Pass By Reference

def PassByReference(refType):
    print("The reference type value is :", refType)
    refType[2] = "Pragim"
    print("The reference type value is :", refType)

refType = [10,20,30,40,50]
print("The reference type value is 1:", refType)
PassByReference(refType)
print("The reference type value is 5:", refType)

x = [10, 20, 30, 40, 50]
y = [60, 70, 80]
x = y
y[0] = "Pragim"
print(x)
x[2] = "New Value"
print(x)
print(y)




