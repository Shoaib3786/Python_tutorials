
"""
Q2. Write a program to print the following star pattern using 
the for loop



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



"""
* 
* * 
* * * 
* * * * 
* * * * *
"""

# mtd- 2


row = 5

for i in range(1, row+1):

    for j in range( 1, i+1):

        print( '*', end=' ')

    print('\n')


"""
* * * * 
* * * 
* * 
*
"""

for i in range(row-1, 0, -1):

    for j in range(1 , i+1):

        print('*', end = " ")

    print('\n')








# row = 8

# for i in range(1 , row+1):   # i-> row,   i = 1

#     for _ in range( 1, i+1):  # j -> column  j = 1

#         print('*', end = ' ')

#     print('\n')



"""
* * * * 
* * * 
* * 
*

"""

# for i in range( row-1, 0, -1): # (4, 0) # i = 4, 3 ,2, 1

#     for j in range( 1, i+1):   # j (1, 2) - j = 1

#         print('*', end = ' ')

#     print('\n')










"""
Q2. Make a equilateral triangle using (Asterisk sybmol('*'))

      *   
     
     * *   

    * * *   

   * * * *   

  * * * * *   

 * * * * * *   

* * * * * * *
"""






# rows = 5
# for i in range(1, rows+1 ):

#     for j in range(1, i+1):

#         print('*', end=' ')
    
#     print('\n')


# for i in range( rows - 1, 0 ,-1):

#     for j in range( 1, i + 1):

#         print ( '*', end = ' ')

#     print('\n')




















"""
Q2. Write a Python program that removes and prints every 
third number from a list of numbers until the list is empty.
"""

# a = [1,2,3,34,4,5,51,56,6,7,71,72,722,7665,45]

# for i in a:

#     ind = a.index(i)

#     print('current index: ', ind)

#     if (ind) % 3 == 0:

#         print(i)
#         print('index:', ind)
#         print('\n') 

#     continue


# val = []
# for i in a:
#     ind = a.index(i)

#     if (ind) % 3 == 0:
#         val.append(a.pop(ind))
#         print(a)
#     continue

# print(val)