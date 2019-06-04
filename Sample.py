x = 10
y = 15.6
stringvar1 = 'Welcome to Python' \
             ' session'
stringvar2 = "Double " \
             "quotes"

print("The value of x is", x)
print(str(x) + "The value of x is", str(x))
print("{0} The value of x {1} is {2}" .format(x, y, stringvar1))

stringvar3 = '''Assert statement is used to assert whether something is true or false.
This statement is very useful when you want to check the items in the list for true or false function.'''

print("Paragraph :", stringvar3)

print(stringvar1[3])
print(stringvar1[:4])
print(stringvar1[5:10])
print(stringvar1[5:])
print(stringvar1 * 3)


# Collections
# 1.List
# 2.Tuples
# 3.Set
# 4.Dictionary

x = 10

listvar1 = [12, 76, 38, 26, 97, 12]
listvar2 = [4.6, 81, "Ram", 'H',38]


print(listvar1, end = '')
print(listvar2)

print(listvar1, end = '@')
print(listvar2)

# Conditional Statements
# 1. Simple If
# 2. If Else
# 3. Multiple If
# 4. Multiple If Else
# 5. Nested If ELse

a = 22
b = 20

# Simple If
if a > b:
    print("a is greater than b")

# If
if a < b:
    print("a is less than b")

# If Else

if a > b:
    print("a is greater than b")

else:
    print("a is less than b")

category = "Electronics"
if(category == "Electronics"):
    print("You have selected the Fashion category")
elif(category == "Fashion"):
    print("You have selected the Footwear category")
elif(category == "Footwear"):
    print("You have selected the Electronics category")
else:
    print("You have not selected any of the listed category")

x =20
y = 15
z = 25

if x > y:
    if x > z:
        print("x is bigger")
    else:
        print("z is bigger")
elif(y > z):
     print("y is bigger")
else:
    print("z is bigger)")










