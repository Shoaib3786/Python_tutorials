"""
OOPs concept:

1. Inheritance based question
"""

"""Problem Statement:

Design a python program that consist of base class which makes a list of dictionaries of the employee data.
Also make child classes as employee class that can access the base class dictionary and add their details into it.
"""
































# class Company:

#     def __init__(self):
#         self.mlist = [{}]

#     def displayDic(self):
#         print('dictionary is: ', self.mlist)


# class Employee(Company):

#     def __init__(self):
#         self.EmployeeDic = {}
#         super().__init__()


#     def AddElement(self, dic):
#         self.EmployeeDic = dic
#         self.mlist.append(self.EmployeeDic)
#         super().displayDic()

# empObj = Employee()
# empObj.AddElement({'name':'sk', 'age':12})


# empObj1 = Employee()
# empObj1.AddElement({'name':'msk', 'age':23})