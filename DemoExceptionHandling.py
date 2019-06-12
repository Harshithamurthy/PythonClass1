# def Division(a, b):
#     try:
#         c = a/b
#         print(c)
#         list = [10, 20, 30, 40]
#         print(list[5])
#         foo = open("text.txt", 'r')
#         foo.read()
#         foo.close()
#     except ZeroDivisionError:
#         print("Denominator Cannot be zero")
#     except FileNotFoundError:
#         print("Check whether file exists or not")
#     except Exception as e:
#         print("Error occurred, Please contact System Administrator : {0}".format(e))
#     finally:
#         foo.close()
#         print("Completed")
#
# Division(40, 2)
#
#
# #OR
#
# def RaiseException(num):
#     if num <1:
#         raise FloatingPointError("Num is less than Zero")
#     return num
#
# try:
#     var = RaiseException(0)
#     print(var)
# except Exception as e:
#     print(e)


try:
    with open('file.log') as file:
        read_data = file.read()
except:
    print('Could not open file.log')
