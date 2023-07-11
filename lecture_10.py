### Objective ###
"""
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


# declare list:
# mtd-1
# mlist = [12,23, 43, 'a', 'hello']
# print(mlist)

# # [or]

# # mtd-2
# a = list( (12,23, 43, 'a', 'hello') )
# print(a)



######## Opertaions #######

# mlist = [12,23, 43, 'a', 'hello']

# 1. append() - add in end
# a = [20, 22, 34] 
# print(a)

# a.append(12223343233233)
# print(a)


#  2. insert() - specify location
# a = [20, 22, 34] 

# a.insert(1, 123455)

# print(a)


# 3. remove() - specify element name
# a = [20, 'max',  22, 34] 
# print(a)

# a.remove('max')
# print(a)


# 4. pop()    - use index
# a = [20, 'max',  22, 34] 
# a.pop(1)
# print(a)



# 5. slicing [:] - print ample of specified contained at once.


# a = [12,23,4,56,7]

# print( a[0 : 3] )



# 6. len()    - find length of the list
# a = [20, 'max',  22, 34] 


#  7. index()  - to find index of specific element and even specify limit till which u want to find

# a = [20, 'max',  22, 34] 
# print(a.index('max'))






# a = [20, 'max',  22, 34] 

# backtracing:::
# value = a[-4:1]
# print(value)








# list1 = ["a", "b", "c"]
# list2 = [1, 2, 3]

# list3 = list1 + list2
# print(list3)

# list1 = ["a", "b" , "c"]
# list2 = [1, 2, 3]

# for x in list2:
#   list1.append(x)

# print(list1)




# 8. sort()   - sort element in ascending order.

# a = [12, 3, 43, 332324, 4545,5,5,7,8,7665]
# print(a)
# a.sort()

# print(a)





"""
Q.2 Write python program that accepts age of 4 users and find the
youngest user out of it.
"""

# mlist = []

# for _ in range(4):
#     age = int(float(input('Enter age; ')))

#     mlist.append(age)

#     # print(mlist)

# print(mlist)

# # sorting in ascending order 
# mlist.sort()

# print(mlist)


# print(f"youngest person's age is: {mlist[0]}")
    











