"""Assigment on OOPs concept"""

"""
1. Make a python program as classes & objects.
    - Make the class methods name it as "generateNum()" that generates any single number between (0 to 7).
    - Make another class method name it as "getUserInput()" to ask user to enter their own number.
    - Make another class method name it as "Evaluate()" to match both the numbers, 
        -> if match found then print 'number is found' 
        -> else print 'number not found'

    test your class working by creating 2 different class instances(or can say objects)

    
2. Make the python programming as classes and objects.
    - Make the class constructor that takes stores student_name, math_marks
    - Make the class method name it as "stud_info()" that takes and builds the list that stores these variable values and returns that list.

    - Now make the different instances of the class and pass studen_name and math_marks as argument to the constructor
    - Make the different class instances as stud_01, stud_02 and stud_03 and then call stud_info().
    - On stud_info() method by different instances of the class w'll get the list of each instances, now store that list into a dictionary as values and class instances name as key of that dictionary.

    'Example:'
    stud_01 = ['max', 78]
    stud_02 = ['rohan', 99]
    stud_03 = ['raman', 100]

    Final Dictinary must look like:
    stud_dict = {
        'stud_01': ['max', 78],
        'stud_02': ['rohan', 99],
        'stud_03': ['raman', 100]
    }
"""


"""
Q1. Make a python program as classes & objects...
    - Make the class methods name it as "generateNum()" that generates any single number between (0 to 7).
    - Make another class method name it as "getUserInput()" to ask user to enter their own number.
    - Make another class method name it as "Evaluate()" to match both the numbers, 
        -> if match found then print 'number is found' 
        -> else print 'number not found'

    Test your class working by creating 2 different class instances(or can say objects)
"""

# library:
import random


class Generator:


    def generateNum(self):  # randomly generate numbers
        
        x = random.randrange(1, 7)

        print('randomly generated value is: ', x)

        return x



    def getUserInput(self):
        
        userInput = int(input('Enter your number: '))

        return userInput



    def Evaluate(self):
        

        gotX = self.generateNum()

        gotUserinput = self.getUserInput()


        if gotX == gotUserinput:

            print('matched')

        else:
            print('not matched')
    
# myObj = Generator()
# max = Generator()
        
# myObj.Evaluate()
# max.Evaluate()






"""
2. Make the python programming as classes and objects.
    - Make the class constructor that takes stores student_name, math_marks
    - Make the class method name it as "stud_info()" that takes and builds the list that stores these variable values and returns that list.

    - Now make the different instances of the class and pass studen_name and math_marks as argument to the constructor
    - Make the different class instances as stud_01, stud_02 and stud_03 and then call stud_info().
    - On stud_info() method by different instances of the class w'll get the list of each instances, now store that list into a dictionary as values and class instances name as key of that dictionary.

    'Example:'
    stud_01 = ['max', 78]
    stud_02 = ['rohan', 99]
    stud_03 = ['raman', 100]

    Final Dictinary must look like:
    stud_dict = {
        'stud_01': ['max', 78]
        'stud_02': ['rohan', 99]
        'stud_03': ['raman', 100]
        
    }   
"""


class student:

    def __init__(self, student_name, math_marks, object_name):

        self.stud_name = student_name
        self.math_marks = math_marks
        self.mlist = ""
        self.myObjectName = object_name
        

    def studen_info(self):

        self.mlist = [self.stud_name, self.math_marks ] 

        return self.mlist



stud_01 = student('max', 78, 'stud_01')
stud_02 = student('rohan', 99, 'stud_02')
stud_03 = student('raman', 100, 'stud_03')



dic = {

    stud_01.myObjectName : stud_01.studen_info(),
    stud_02.myObjectName: stud_02.studen_info(),
    stud_03.myObjectName: stud_03.studen_info(),
}

print(dic)