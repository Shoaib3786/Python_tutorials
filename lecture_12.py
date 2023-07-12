"""
1. Backtracing
2. For loop question
"""



# """ 1. Backtracing """


# print('"""""mtd-0""""')

# [mtd-1]  [reverse() as method, it doesn't return any value, it just update the list]

# print('original; ', a)
# a.reverse()   # reversing
# print('reverse: ',a)



# print('"""""mtd-2""""')
# [mtd-2] [reversed() as function it returns a value]
# a = [1,23,43,54,6]
# for i in reversed(a):
#     print(i)


""" UNDERSTANDING MTD-2 reversed() function"""
# # building new function
# def reversed( mlist):

#     print('mlist original a is: ', mlist)


#     # code......


#     c = [6,54,43,23,1]
#     # print('value is:',c)
    
#     return c

# # calling the function
# a = [1,23,43,54,6]   # parameter

# r = reversed ( a )   # calling

# # printing
# print('reversed list is; ', r)


# # print('printing reversed list using for loop')

# for i in r:
#     print(i)
    






# print('"""""mtd-3""""')
# [mtd-2] [reversing using back slicing]
# a = [12, 23, 45, 66]
# # print(a[::-1])

# for i in a[::-1]:

#     if i == 23:
#         break
#     print(i)























