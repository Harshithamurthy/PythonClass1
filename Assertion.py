# def KelvinToFarhenheat(temperature):
#     assert (temperature >= 0), "Colder than absolute zero"
#     return ((temperature - 273)*1.8)+32
# print(KelvinToFarhenheat(273))
# print(KelvinToFarhenheat(500.64))
# print(KelvinToFarhenheat(-5))
#
# #OR
#
# import sys
#
# def linux_interaction():
#     assert ('linux' in sys.platform), "Function can only run on Linux systems."
#     print('Doing something.')
#
#
# try:
#     linux_interaction()
# except:
#     pass

List = [24, 25, 26, 27]
List.append(28)
print(List.append(29))