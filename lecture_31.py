"""
OOPs concept:
1. Hierarchy
2. super()
"""


"""INHERITANCE:"""

## Mtd-1
class Person:       # Parent class
    def __init__(self, name):

        self.myname = name

    def display(self):
        print('My name is: ', self.myname)


class Employee:     # Child class
    def __init__(self, name, salary):

        self.msalary = salary
        super().__init__(self, name)

    def personEmployeeInfo(self):

        Person.display(self)


    
obj_emp = Employee('RAMAN', 1500)
obj_emp.personEmployeeInfo()





## Mtd-2
class Person:       # Parent class
    def __init__(self, name):

        self.myname = name

    def display(self):
        print('My name is: ', self.myname)


class Employee(Person):     # Child class
    def __init__(self, name, salary):

        self.msalary = salary
        super().__init__(name)

    def personEmployeeInfo(self):

        Person.display(self)


    
obj_emp = Employee('RAMAN', 1500)
obj_emp.personEmployeeInfo()







    
