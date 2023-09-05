""" PERFROM OPTIMIZATION IN PATTERN QUESTION """

# LEARNING from this lecture:
# - Their is no right/wrong solution for any problem. 
# - Our job is to find optimized solution.


"""
Q2. Write a program to print the following star pattern using 
the for loop:

* 
* * 
* * * 
* * * * 
* * * * *
* * * * 
* * * 
* * 
*

"""

#########
# MTD-1 #
#########

# row = 5

# # upper-half
# for i in range(1, row+1):

#     for j in range(1, i+1):

#         print('* ', end=' ')

#     print('\n')


# # lower-half
# for i in range(row-1, 0, -1):

#     for j in range(1, i+1):

#         print('* ',end=' ')

#     print('\n')




# ###########
# # MTD - 2 #
# ###########

# row = 5
# for i in range(0, row+1):

#     print("* " * i)

# for j in range(row-1, 0, -1):

#     print('* ' * j)

