
#*******************************LECTURE****************************

## Variables:
#   - varaible declaration
# a = 'Hello world'
# print('My variable: ', a)


#   - varaibe naming culture
        # - camel Case - myVariableName = "John"
        # - Pascal case - MyVaraibleName = "John" 
        # - snake case - my_varaibe_name = "John"


#   - Take input from the user.
# age = int(input(" Plz enter age: "))
# print('my age is = ',age)


#   - Global varaibles



## Datatypes:  *For Knowing the type of the varaible use type()*
# int: 2,3.13
# float: 10.98, 2.33
# string: "John" or 'y47s'

# name = "shoaib"
# print(name)

# boolean: True/Fase 

# Sequence: List, Tuple

# Mapping: dic
# a = {'age':10}



## Typecasting:
# a = 2.0
# print('value: ', a)
# print('datatype: ',type(a))

# a = 10
# print(a)

# b = 2.0 typecaste to str


# contraints
a = int(input('please enter your age: '))
print('My age is:',a)



# **********************ASSIGNMENT SOLUTIONS*****************************


print('***************')
print('Program 1')
print('***************'+'\n')

# solution of Assign_01:

# Q1. Write python program to print any random paragraph 
# (randomly picked from google wikipedia).

# SOLUTION:
print('''*****Printing text*****'''+ '\n' +'''Artificial intelligence (AI) is intelligence demonstrated by machines, as opposed to intelligence displayed by humans or by other animals. "Intelligence" encompasses the ability to learn and to reason, to generalize, and to infer meaning.[1] Example tasks in which this is done include speech recognition, computer vision, translation between (natural) languages, as well as other mappings of inputs.[2]''')

# *NOTE* -> '\n' indicates leave a line.  [YOU TRY ABOVE PRINT STATEMENT WITHOUT '\n' TO UNDERSTAND EVEN BETTER]


# *******************************************

print('\n')
print('***************')
print('Program 2')
print('***************'+'\n')


# Q2. create a program to take an input from user (say user's age) 
# and print the age.

# SOLUTION
myVariable = int(input('ENTER YOUR AGE: '))
print('Your age is = ', myVariable)


# *******************************************

print('\n')
print('***************')
print('Program 3')
print('***************'+'\n')

# Q3. Comment the program written in [Q2].

# SOLUTION 
'''
this section of code accepts user input and prints an output 
'''
myVariable = int(input('ENTER YOUR AGE: '))
print('Your age is = ', myVariable)

# *NOTE* -> you can comment tour program using # or ''' '''
#           # -> use this for single line commenting
#           ''' ''' -> use this for multiline commenting


# *******************************************

print('\n')
print('***************')
print('Program 4')
print('***************'+'\n')


# Q4. Write a python program and perform following instructions:
# 	1. Take two user *integer* input.
# 	2. perfrom mathematical operation over it like:
# 		- addition
# 		- subtraction
# 		- multiplication
# 		- division
# 		- find square of both the input individually
# 		- square root of both the input individually
# 	3. Print the output of all the operations. 

# SOLUTIONS:

'''
1. making two int type varaible.
'''
a = 10
b = 22

'''
2. Perform mathematical operation
'''
# addition
sum = a+b


# subtract
sub = a-b


# multiplication
mul = a*b



# division
div = a/b

# square of both the input individually
a_square = a**2
b_square = b**2



# square root of both the input individually 

'''import python inbuilt libarary to perform sqaure root. '''

import math  # library

a_squareRoot = math.sqrt(a)
b_squareRoot = math.sqrt(b)


'''
3. Printing the values
'''

print('a is: ', a)
print('b is: ', b, '\n')

print('sum is: ', sum ,'\n')

print('difference is: ', sub, '\n')

print('Multiplication is: ', mul,'\n')

print('Division is: ', div, '\n')

print('Square of a is: ', a_square, '\n')
print("square of b is: ", b_square, '\n')

print('Square root of a is: ', a_squareRoot, '\n')
print("square root of b is: ", b_squareRoot, '\n')




