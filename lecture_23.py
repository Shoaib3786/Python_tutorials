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

2. Accessing Tuple
    - Use slicing

3. Updating and removing (Directly not possible bcz Tuple is immutable)
    - Use list type convertion first, perfrom list operation over it & then finally convert that into tuple.

4. .count() -> get the count of repetation of items in the tuple.

5. .index() -> get the index of the first occurance of an item in the tuple.


"""

# tup = 4,3,2

# x,y,z = tup

# print(x)
# print(y)
# print(z)

# print(tup)
# print(type(tup))



"""
Write a program to print the tuple of string values into a string of sentence.
mtuple = ('e', 'x', 'e', 'r', 'c', 'i', 's', 'e', 's')
"""


""" 
Write a Python program to replace the last value of tuples in a list.
Sample list: [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
Expected Output: [(10, 20, 100), (40, 50, 100), (70, 80, 100)]
"""


m = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
print(m)
for i in range(0,len(m)):

    tup = list(m[i])

    tup[-1] = 100

    m.pop(i)
    m.insert(i, tup)

print('Added element after changes: ',m)

