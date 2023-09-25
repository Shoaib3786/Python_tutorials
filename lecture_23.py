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


# mtup = ( 12 , 's', 34, 67 )


# mtup = tuple( ( 12, 34, 56, 'k', 'l' ) )

# print(mtup)


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

# mtup = ( 12, 34, 's', 22222, 100)

# print(mtup[3])





# tup = tuple( [12 , "m", 2, 44, 'hello', 'world'] )
# print(tup)


# # accessinhg the elements
# print( 'output: ',tup[3])




"""
3. Updating and removing (Directly not possible bcz Tuple is immutable)
    - Use list type convertion first, perfrom list operation over it & then finally convert that into tuple.
"""

# a = int(12.5)
# print(a)
# print(type(a))




# mtup = tuple( [ 12, 34, 's', 22, 100 ] )
# print('tuple: ', mtup)
# print(type(mtup))


# mlist = list( mtup)  # typecasting (from TUPLE -> LIST)

# print('List: ',mlist)
# print(type(mlist))

# mlist.remove('s')

# print('New List: ',mlist, '\n')


# mtup = tuple(mlist)
# print('New tuple: ', mtup)
# print(type(mtup))




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

# mlist= [ 12, 34, 's', 22, 100 ]

# print(len(mlist))

# mtup = tuple( [ 12, 34, 's', 22, 100 ] )

# # print(mtup[3])

# for i in range(0, len(mtup)): 
    
#     print(mtup[i])



"""
4. .count() -> get the count of repetation of items in the tuple.
"""



# mtup = tuple( [ 12, 34, 's', 22, 12, 100, 12 ] )

# print(mtup.count('s'))






# tup = tuple( [12 , 12, 23, 12, "m", 2, 44, 'hello', 'world'] )

# print(tup.count(23))




"""
5. .index() -> get the index of the first occurance of an item in the tuple.
"""




# mtup = tuple( [ 12, 34, 's', 22, 12, 100, 12 ] )

# print(mtup.index(12))






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


mlist = [ (10, 20, 40), (40, 50, 60), (70, 80, 90) ]

mlist2 = []

for i in range(0, len(mlist)):  # 0, 1, 2

    a = mlist[i]

    # print('Tuple in iteration: ', a)


    b = list(a)  # typecasting (tuple -> list)
    
    # print('typecasting (tuple -> list): ', b)


    b[-1] = 100

    # print("last element changed: ",b)


    a = tuple(b)  # typecasting (list -> tuple)

    # print('My new tuple after typecasting: ', a)
    
    mlist2.append(a)

    # print('Next: ''\n')


print(mlist2)














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



a=  [1, 2, 3]

# mt1
a.reverse()

# m2
for i in reversed(a):
    print(i)