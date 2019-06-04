# LIST

listvar1 = [10, 20, "Ram", 13.4, 70]
# listvar2 = [30, 40, 50]
#
# print(listvar1[2])
# print(listvar1[:2])
# print(listvar1[2:])
# print(listvar1[2:4])
# print(listvar1 * 3)
# print(listvar1 + listvar2)
#
# listvar1.append(True)          # Adding a value gets appended at the last
# print(listvar1)
# #print(listvar1.append(True))              # o/p as none
# #print(listvar1.insert(3, 'New Value'))       # Adds the value at the position or index mentioned(o/p as none)
# listvar1.insert(3, "New Value")
# print(listvar1)
# #listvar1.clear()                     # Empties or clears the list
# #print(listvar1)
listvar3 = listvar1.copy()             # Shallow Copy
listvar1[2] = "XYZ"
print(listvar1)
print(listvar3)

listvar4 = listvar1          # Deep Copy(0x111000)
listvar1[2] = "XXX"
print(listvar4)
listvar4[1] = 'listvar4'
print(listvar1)
print(listvar4)

listvar5 = [10, 20, 30, 40, 50, 60, 70, 20, 40, 60, 20, 50]
y = 20
x = listvar5.count(y)
print("Items occurrence :", x)

extends = ["Rajesh", "Mahesh"]
print(listvar5 + extends)

# extendedvar = (listvar5.extend(extends))
# print(extendedvar)

print(listvar5)

print("POP without Index", listvar5.pop())           # Removes item at the end of the list
print(listvar5)
print("POP with Index", listvar5.pop(3))
print(listvar5)

print("Length of List is :", len(listvar5))
listvar5.remove(60)
print("Remove an item :", listvar5)

listvar5.reverse()       # Reverse the complete list
print(listvar5)

listvar5.sort()          # Sorts the list in ascending order
print(listvar5)

listvar5.sort(reverse=True)          # Sorts the list in descending order
print(listvar5)





