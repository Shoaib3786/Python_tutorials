
"""
1. Upload assignments on Github
2. All homework assignments
"""


"""
Q1. Consider the situation where you need to write a program that 
prints the number from 1 to 10 but not 6.
"""

# for i in range(1, 11):

#     if i == 6:
#         pass
        
    
#     print(i)

    # if i != 6:
    #     print(i)








# for i in range(1,11):
    
    #[mtd-1]
    # if i == 6:
    #     continue

    # print('number i: ', i)

    # [mt6d-2]
    # if i != 6:
    #     print('number is', i)



"""
Q2. Consider a situation where you want to iterate over a string 
and want to print all the characters until a letter 
'e' or 's' is encountered.
"""
# string_list = ['h', 'l', 'l', 's', 'o', '\n']

# string = 'hllso'

# for i in string:

#     # if i == 'e' or i == 's':
#     #     break

#     # print('letters are:', i)

#     if i in ('s', 'e'):

#         break

#     print('letters are:', i)










# string_list = ['h', 'e', 'l', 'l', 'o']
# myString = 'hello'

# for i in string_list:
    
#     if i == 'e' or i == 's:
#         break

#     print(i)


# for i in myString:
    
#     if i in ('e', 's'):
#         break

#     print(i)


"""
Q3. Write a program to print the cube of all numbers from 1 to a user input numbers.
"""

# n = int(input('Enter value'))
# cube = 0
# for i in range(1, n+1):

#     cube = i**3

#     print(cube)





"""
Q4. Use a loop to display odds numbers from the 3 given list.
if ERROR OCCURS PLZ SPECIFY THE REASONS FOR IT.

list 1: 
[10, 7, 32, 45, 2, 456, 12, 33, 11, 57, 78, 98, 99, 100, 22, 3, 27, 89, 44, 5, 1, 20, 23, 42, 44, 88, 980, 67, 821]

list 2: 
[456, 22, 33, 11, 57, 66, 78, '98', 99, 100, 22, 3, 27, '89', 44, 5, 1, 20, 213, '42', 44, 88, '980', 67, 66, '77']

list 3: 
[10, 7, 32, 45, 2, 456, 12, 'HI', 11, 57, 78, 98, 99, 'MAX', 22, 3, 27, 89, 44, 5, 1, 20, 23, 42, 44, 88, 'TOM', 67, 821]
"""

# mlist = [456, 22, 33, 11, 57, 66, 78, '98', 99, 100, 22, 3, 27, '89', 44, 5, 1, 20, 213, '42', 44, 88, '980', 67, 66, '77']

# m = []
# for i in mlist:
    
#     if i % 2 != 0:

#         m.append(i)


# print(m)








"""
Q5: Write a program that takes 4 input from the user and 
find the factorial of those 4 user input numbers.

**Make sure you run the program once for all this to happen.

Hint:
1. Use for loop
2. Use list concepts 8
"""


# mlist = []
# for _ in range(4):
#     a = int(input('Enter value: '))

#     mlist.append(a)

# print("list of user's value is:", mlist)

# # mlist = [5,4,3,2,1]




# for element in mlist:

#     fact = 1

#     for i in range(1, element+1):

#         fact = fact * i

#     print(fact)














# mlist = []
# for i in range(0,5):
    
#     a = int(input('Enter value: '))

#     mlist.append(a)

# print(mlist)


# for elements in mlist:
    
#     fact = 1

#     print('element is: ',elements, '\n')

#     for i in range(1, elements+1):
#         fact = fact * i

#     print(fact)


