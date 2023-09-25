"""

ASSIGNMENT:

1. Global Variable and Local variable
2. Functions with arguments
3. Overloading:
    - Function overloading

3. Functions with same name can't be supported by python (No function overloading)

4. Using return in the python functions .

"""




# age = 10  # Global variable   # 20
# b = age
# c = 10

# def myAge():

#     global b, c
    
#     ac = b
#     print(ac)



# myAge()  # calling


# print('outside age is: ', age)



"""
2. Functions with arguments
"""
    
# def func(age):
#     print('MY AGE IS: ', age  )


# def hello():
#     myage = 10
#     func(myage)


# hello()

# mtd-1
# a = input('Enter value: ')
# print(a)


# mtd-2 - functions

# def mPrint():

#     userInput = input('Enter Value: ')
#     print('your value is: ', userInput) 

# mPrint()


# mtd-3 - functions

# def genFun():   # generate number

#     userInput = input('Enter Value: ')
#     print('my  another value is: ',userInput)

#     value = 7
#     printFun(value)


# def printFun(value):   # print value

#     print('value is; ', value)
#     genFun()


# genFun()



"""
Q: Consider the situation where you need to write a program that prints the number from 1 to 10 but not 6.
"""


def printNum():
    for i in range(1, 11):

        if i == 6:
            continue

        print(i)


# printNum()  # calling the function.







"""
Q. Consider a situation where you want to iterate over a string and want to print all the characters until a 
letter 'e' or 's' is encountered.
"""




def my_fun(myValue, myHello):

    
    for i in myValue:
        
        if i =='e' or i =='s':
            continue
        
        print(i)
    
    print(myHello)


# myStr = int(input('Enter the string: '))
# m = 'hello people'
# my_fun(myStr, 'hello people' )




"""
Q. Using return in the python functions .
"""




"""
Q. Write a Python program to print the even numbers from a given list.
Sample List : [1, 2, 3, 4, 5, 6, 7, 8, 9]
"""

# a = 10
# print('value: ', a)

# print(f'value: {a}')





def fun(mlist):
    
    for i in mlist:


        if i % 2==0:

            print(f'{i} is even ')

        # else:
            # print(f'{i} is odd ')

# m = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# fun(m)



"""
Q. Write a Python program to take user age form one function and prints its age from another function.
"""

def askAge():
    age =  int(input('Enter your age: '))
    
    return (age, "Max")


def printAge():
    
    user_age, mstring = (age, "Max")
    
    print("User's age is :", user_age )
    print("User's name is :", mstring )


printAge()