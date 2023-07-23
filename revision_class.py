
"""
DISCUSSION:
0. Type casting.
1. Always take care about intendation.
2. comments can be added using #,""" """". 
3. commented statement isn't executed by the programing language.
"""
# print(12)

# print ( ' hey  , / ' 'bye' '   ' )
 





# datatype:
# 1. int -> 1, 23, 44, 100, 199, 9999999999
# 2. float -> 2.3 33.6, 9999.0, 2.0
# 3. str -> "hello" or 'hello    -> "23" / ''\
# 4. boolean -> bool -> True/ False true= 1, false =0


# a = rajat
# print(a)



"""
Q1. typecaste hardcoded(Progammer feeded) value into:
	- int
	- float
	- string
	The value is -> 49, 49.67, "Tom Cruise"
"""

# a = '12'
# print(a)

# fetch_data  =  12.55

# print(type(fetch_data))


# a = '1223'

# print(type(a))

# b = float(a)  
# print(b)

# c = int(b)
# print(c)

# print(type(c))





# typecast float -> float
# print(float(a))

# typcaste float -> int
# print(int(a))

# typecaste int to string
# print(str(a))

# typecaste str to int


###### input statement #####


# enter your age, add 2 years in user's age and print it


# a = int( float(   input(" bhaiya enter your age: ")   ) )
# print('bhaiaya ur age is: ', a)

# sum = a+2*21/2

# print('new age is: ', sum)


# a = 12
# sum = a + 2
# print(sum)





















###############
### IF LOOP ###
###############

"""
DISCUSSIONS:
1. structure of if else condition is 'if' and ends with 'else' 
elif always comes in between. 
"""


# if (condition):
    
# 	print('write asny code')

# elif (condition):

# 	print('write asny code')

# elif (condition):

# 	print('write asny code')
# elif (condition):

# 	print('write asny code')

# else:
# 	print('write asny code')


# MATHEMATICAL OPERTAORS:
# + - / * **

# COMPARISON OPERATORS: 
# > < >= <= ==

# =    OR     ==

# a = 12

# a == 14


"""
Q3. Accept any city name from the user and display the monuments 
of the city name:
 - if city is delhi then print monument red fort
 - if city is Agra then print monument Taj Mahal
 - if city is Jaipur then print monument Jal Mahal
"""

# city = input('Enter city: ')

# if city == 'delhi':
#     print('red fort')
    

# elif (city == 'Agra' ):
# 	print('Taj Mahal')
        

# elif (city == 'Jaipur'):
#       print('Jal Mahal')

# else:
#       print('None')



 
"""
Q4. Write python program to check whether a person is senior citizen 
or not:
	- if person's age > 60 then he/she is a senior citizen
	- else he/she is not.
"""

# age = int(float(input("Enter age: ")))

# if age >= 60:
#     print('Senior citizen')
    
# else:
#     print('none')





"""
Q5. Write a python program for assigning grades 
(A, B, C, D, E, F, G) based on marks obtained by a student.
	- if the percentage is above 95, assign grade A
	- if the percentage is above 70 and below and including 95, assign grade B
	- if the percentage is above 60 and below and including 70, assign grade C	
    - if the percentage is between (50, 60), assign D
    - if the percentage is (40 to 50), assign E
    - if the percentage is 29 and 30 , assign F
    - if the percentage is 10 or 11, assign G 
"""

# marks = int(float(input("Enter marks: ")))
# # marks2 = int(float(input("Enter marks: ")))
# if (marks > 95):
#     print('A')

# elif (  70 < marks <= 95):
#     print('B')

# elif (60 < marks <= 70):
#     print('C')

# elif (50 < marks < 60):
#     print('D')

# elif (40 <= marks <= 50):
#     print('E')

# elif (marks==29 or marks==30):
#     print('F')
    
# elif (marks==10 or marks==11):
#     print('G')










"""
Q6: Write python program that ask two user input and find largest 
number out of that two user input number.
"""

# a = int(float(input("Enter value: ")))

# b = int(float(input("Enter value: ")))

# if a>b:
#     print('a')

# elif b>a:
#     print('b')

# else:
#     print('a = b')


"""
Q7: Write python program that accepts age of 4 users and find the
youngest user out  of it.
"""

# a = int(float(input("Enter value: ")))

# b = int(float(input("Enter value: ")))

# c = int(float(input("Enter value: ")))

# d = int(float(input("Enter value: ")))


# if (a < b and a < c and a < d):
#     print('a is youngest')


# elif (b < a and b < c and b < d):
#     print('b is youngest')


# elif (c < a and c < b and c < d):
#     print('c is youngest')


# elif (d < a and d < b and d < c):
#     print('d is youngest')



"""
Q8: Write a python program to find the area of the:
    - Rectangle
    - Circle
    - Triangle
    - Square
"""

# shape  =input("Shape: ")

# if shape == 'rectangle':
    
#     length = int(float(input("Enter length: ")))
#     breadth = int(float(input("Enter breadth: ")))
#     area = length * breadth
#     print(area)
    



"""
Q9: Write a python program, A shop will give discount of 10% 
    - if the cost of purchased quantity is more than 1000 bucks. 
Also,
- Ask user for quantity [Suppose, one unit will cost 100 bucks].
- Judge and print total cost for user.
"""





# # printing ways:
# # 1.
# a = 10
# b = 20
# print('hello', a)

# # 2.
# print(f'hello {a}')

# # 3.
# print('hello {} {}'.format(b, a))




"""
Q10: Write python program to accept the electric units from user 
and calculate the bill according to the following criteria:

First 100 units is Free

next 200 units is Rs 2 per unit

Above 300 units is Rs 5 per unit

"""


# units = float(input('Enter unit: '))

# amount = 0

# if ( 0 < units  <= 100):

#     print(f'user needs to pay {amount}')


# elif ( 100 < units <= 300 ):
    
#     amount = 2 * (units-100)
#     print(f'user needs to pay {amount}')


# else:

#     amount = (0) + (200*2) + (units-300) * 5

#     print(f'user needs to pay {amount}')




################
### FOR LOOP ###
################


"""
DISCUSSION:
1. For loop
    - Iteration -> no.of times to loop 

3. Minor List concept
    - Index -> Location

2. range() funtion
"""




"""
Q11. Print first 10 natural number.
"""

# for i in range(1, 11):

#     print(i)




"""
Q12. Print numbers from -10 to -1 using for loop.
"""

# for i in range(-10, 0, 2):

#     print(i)


"""
Q13. make variables for start and end points for looping and 
printing the values.
"""


# my_start = int(input('enter value'))
# my_end = int(input('enter value'))
# my_jump = int(input('enter value'))

# for i in range( my_start, my_end, my_jump):

#     print(i)



"""
Q find the sum of first 10 numbers:
"""

# sum = 0

# for i in range(1, 11):

#     sum = sum + i


#     print(sum)




"""
Q14: Find the factorial of 2, 5, 6, 7 & 8.
"""

# 5! = 5 * 4 * 3 * 2 * 1 = 120


# s = 1

# for i in range(1,6):

#     fact = s * i
#     s = fact

# print(fact)



"""
DISCUSSIONS:
1. List 

2. List built-in methods:

    1. append() - add in end
    2. insert() - specify location
    3. remove() - specify element name
    4. pop()    - use index
    5. slicing [:] - print ample of specified contained at once.
    6. len()    - find length of the list
    7. index()  - to find index of specific element and even specify limit till which u want to find
    8. sort()   - sort element in ascending order.

"""

# 1
# a = [[ 1, 2, 'max', 12] ,  [1,2] ]


# 2

# a = list( (1, 234, 4) )
# print(a)

#  LIST OPERATIONS:

# a = [1,23,45, 12, 100 , 22 ,23333]

# for i in reversed(a):
#     print(i)

# a.reverse()

# print(a[::-1])]



# a.append( 1000 )

# a.insert(3, 'hellllllooooo')

# a.remove( 'mas' )
# a.pop(4)

# b = a[ 3 ]


# print( len(a) )

# a.sort()

# print(a)

# print(a[ : : -1])





"""
Q16. Write python program that accepts age of 4 users and find the
youngest user out of it.
"""

# mlist = []

# for i in range(4):
    
#     a = int(input('enter age:' ))
    
#     mlist.append(a)

# print(mlist)

# # sorting the list

# mlist.sort()


# print('sorted list: ',mlist)

# print('youngest person age is: ', mlist[0] )




"""
DISCUSSIONS:
1. break, pass, continue 
2. Backtracing in list
    - reversed()
    - a.reverse()
    - a[: : -1]
"""

"""
BREAK - COMES OUT OF THE LOOP
PASS  - DOES NOTHING
CONTINUE - SKIPS THE ITERATIONS
"""

# a = [12, 10, 23, 34, 55, 12]

# for i in a:

#     if i >= 20:

#         break

#     else:
#         print(i)







"""
Q.1 Consider the situation where you need to write a program that prints the number from 1 to 10 but not 6.
"""


"""
Q1. Write a program to print the cube of all numbers from 1 
to a user input numbers.
"""

