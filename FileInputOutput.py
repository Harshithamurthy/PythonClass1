foo = open("Test.txt", 'w')
foo.write("Python is a very easy language to learn.\nIt is like reading normal English \n")   # It will overwrite what ever is their in the test file and print what ever we have written here
foo = open("Test.txt", 'a')    # append(a) will write the text to the file without overriding it
foo.write("Hello world")
foo = open("Test.txt", 'r')
print(foo.read(12))
print(foo.read(8))
print(foo.read(6))
print(foo.tell())    # It will tell current pointer or cursor position
foo.seek(0)           # It will reposition the pointer or cursor to the starting position of file
print(foo.read(30))
print(foo.closed)      # Checks whether the file is closed or not
foo.close()             # It will close the opened file
print(foo.closed)


