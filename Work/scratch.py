class Employee:

    employeeCount = 0

    def __init__(self, name):
        self.name = name
        Employee.employeeCount += 1

emp1 = Employee('bob')
emp2 = Employee('dan')

print(Employee.employeeCount)

class Employee2:

    employeeCount = 0

    def __init__(self, name):
        self.name = name
        self.employeeCount += 1

emp3 = Employee2('bob')
emp4 = Employee2('dan')

print(Employee2.employeeCount)
print(emp3.employeeCount)