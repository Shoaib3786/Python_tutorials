
#Homework solution:


"""
Q1. Write a Python function to find the maximum of three numbers. [Take 3 user input and find the maximum of it...]
"""

def fun():
    mlist = []
    i = 1
    
    while i <= 3:

        a = int(float(input('Enter value: ')))
        mlist.append(a)

        i += 1   # i = i + 1



    print(mlist)

    mlist.sort()  # sorting in ascending order
    
    print(mlist)

    max_num = mlist[-1]

    return max_num
    

# myValue = fun()

# print('maximum number user input is: ', myValue)

"""
Q2. Write a Python function to sum all the numbers in a list.
Sample List : (8, 2, 3, 0, 7)
"""

def mfun(mlist):
    sum = 0
    
    for i in mlist:
        sum = sum + i
    
    return sum

meralist = [8, 2, 3, 0, 7]

mera_sum = mfun(mlist= meralist)
print('sum of the list element is: ', mera_sum)


"""
Q3. Make two python functions named as "userInput()" and "addition()".
* In userInput() -> Take 2 interger inputs from the user and return the 2 input value.

* In addition() -> Get the user input value from the userInput().
                -> Then add the two user input value and store the addition in the variable called 'sum'.
              
Now find the way to globally print the value of the sum varaible used in addition() function.
"""


def userInput():
    
    userIn_1 = int(input('Enter the value 1: '))
    userIn_2 = int(input('Enter the value 2: '))
    
    return userIn_1, userIn_2

def addition():
    value_01, value_02 = userInput()
    print('Value-1 is: ', value_01)
    print('Value-2 is: ', value_02)


addition()