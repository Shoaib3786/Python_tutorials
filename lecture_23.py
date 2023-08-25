"""
OBJECTIVES:
1. Tuple. -> ()
     * Immutable
     * can contain different dtype items like dic and list.
"""


""" OPERATIONS:

1. Making Tuple
    - Use tuple method
    - Use round brackets ()
 """

# # mtd-1
# tup = (12 , "m", 2, 44)

# print(tup)
# print(type(tup))

# # mtd-2

# tup = tuple( [12 , "m", 2, 44, 'hello', 'world'] )

# print(tup)
# print(type(tup))



# a = 10.5
# print(type(a))
# tup = tuple( [12 , "m", 2, 44, 'hello', 'world'] )
# print(type(tup))

# b = int( 12.5 )
# print(type(b))


"""
2. Accessing Tuple
    - Use slicing
"""

# tup = tuple( [12 , "m", 2, 44, 'hello', 'world'] )
# print(tup)


# # accessinhg the elements
# print( 'output: ',tup[3])




"""
3. Updating and removing (Directly not possible bcz Tuple is immutable)
    - Use list type convertion first, perfrom list operation over it & then finally convert that into tuple.
"""

#
# tup = tuple( [12 , "m", 2, 44, 'hello', 'world'] )
#
# print(tup)
# print(type(tup))
#
#
# # typecasting
# mlist = list( tup)
# print(mlist)
# print(type(mlist))
#
#
# mlist[3] = 3
#
# print(mlist)
#
#
# # converting back tuple
# put_01 = tuple( mlist )
#
# print(put_01)
# print(type(put_01))




"""
4. .count() -> get the count of repetation of items in the tuple.
"""



# tup = tuple( [12 , 12, 23, 12, "m", 2, 44, 'hello', 'world'] )

# print(tup.count(23))




"""
5. .index() -> get the index of the first occurance of an item in the tuple.
"""


# tup = tuple( [12 , 12, 23, 12, "m", 2, 44,12, 'hello', 'world'] )

# print(tup.index(12))



"""

# tup = 4,3,2

# x,y,z = tup

# print(x)
# print(y)
# print(z)

# print(tup)
# print(type(tup))
"""


# a = 12.54,  23.2,  44

# x,y,z = a 


# print(a)

# print(type(x))


# print(y)
# print(z)
# print(type(a))






"""

Write a program to print the tuple of string values into a string of 
sentence.
mtuple = ('e', 'x', 'e', 'r', 'c', 'i', 's', 'e', 's')

"""


# mtuple = ('e', 'x', 'e', 'r', 'c', 'i', 's', 'e', 's')


# mstring = "".join(mtuple)


# print(mstring)
















# mtuple = ('e', 'x', 'e', 'r', 'c', 'i', 's', 'e', 's')
# conn = ''

# mystr = conn.join(mtuple)
# print(mystr)







"""
Write a Python program to replace the last value of tuples in a list.

Sample list: [ (10, 20, 40), (40, 50, 60), (70, 80, 90) ]

Expected Output: [(10, 20, 100), (40, 50, 100), (70, 80, 100)]
"""

# m = [ (10, 20, 40), (40, 50, 60), (70, 80, 90) ]
# print('before updating:   ',m)

# for i in range(0, len(m)):

#     a = m[i]

#     mlist = list(a)  # 1. typecasting tuple to list

#     mlist[-1] = 100

#     tup = tuple(mlist)  #2., final typecasting list to tuple

#     m.pop(i)
#     m.insert(i, mlist)

    
# print('After updating: ',m)














# m = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]

# for i in range(0, len(m)):
   
#     mlist = list(m[i])
#     mlist[-1] = 100

#     tup = tuple(mlist)
#     m.pop(i)
#     m.insert(i, tup)
    
# print(m)










# m = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
# print(m)
# for i in range(0,len(m)):

#     tup = list(m[i])

#     tup[-1] = 100

#     m.pop(i)
#     m.insert(i, tup)

# print('Added element after changes: ',m)
