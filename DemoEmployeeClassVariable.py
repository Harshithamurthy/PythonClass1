class Employee:
    'Employee Class Information'
    empcount = 0
    _PrivateVariable ="private Value"

    def __init__(self, empname = "None", empid = 0):
        self.empname = empname           # Attribute
        self.empid = empid
        self.cmpnyname = "Mphasis"        # We can write the common attribute(here company name of employees working in Mphasis) of all employess in init so that it can be accessed in all memeber functions but if we want to change cmpny of each employee we have to go to every func to change hence we use class variables that will be inside class but outside of member function
        Employee.empcount += 1            # This will display the total number of Employees by adding objects created

    def EmployeeDetails(self):
        self.empcount += 1                  # This will display the number of times same object called total of Employees
        print("Employee Name is : ", self.empname)
        print("Employee Id is : ", self.empid)
        print("Employee count is : ", self.empcount)

    def _PrivateMethod(self):                        # Private Method
        print("Private method invoked")

    def EmployeCount(self):
        print("The Total Employees count is : ", Employee.empcount)


E = Employee("Harshitha", 123456)
E.EmployeeDetails()
E.EmployeeDetails()
E.EmployeeDetails()

print("-" * 100)

E1 = Employee("Ram", 197956)
E1.EmployeeDetails()
E1.EmployeeDetails()
print("The Total Employees count is : ", Employee.empcount)

print("-" * 100)

E2 = Employee()
E2.EmployeeDetails()

print("-" * 100)

emp3 = Employee()
emp3.empname = "Ravi"
emp3.empid = 4000
emp3.EmployeeDetails()
print("The Total Employees count is : ", Employee.empcount)

print("-" * 100)

print(hasattr(E, 'empname')) # Returns true if 'empname' attribute exists
print(getattr(E, 'empname')) # Returns value of 'empname' attribute
setattr(E, 'empname', 'Pragim') # Set empName 'Pragim'
print(getattr(E, 'empname')) # Returns value of 'empname' attribute
#delattr(E, 'empname') # Delete attribute 'empname'
print(getattr(E, 'empname')) # Returns value of 'empname' attribute

print('-' * 100)

print("Employee.__doc__:", Employee.__doc__)
print("Employee.__name__:", Employee.__name__)
print ("Employee.__module__:", Employee.__module__)
print ("Employee.__bases__:", Employee.__bases__)
print ("Employee.__dict__:", Employee.__dict__ )

# del emp1
# E1.DisplayEmployee();

print(id(E))
print(id(E2))
print(id(E1))

E4 = E2
print(id(E4))





