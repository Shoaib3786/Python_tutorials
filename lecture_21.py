
"""
Q1. Generate numbers and insert those numbers in the list using while loop.

HINT:
    1. It is not always neccessary to use range() function to generate numbers.
You can even use other way out to generate numbers. Use your brains how to generate numbers and insert them into a list and finally print it out.

    2. Solve this question using WHILE LOOP and FOR LOOP.
"""


# mthd-1 Using foor loop
# mlist = []
# for i in range(2, 13, 1):

#     mlist.append(i)

# print(mlist)


# mtd-2 Using While loop

# i = 2

# mlist = []
# while i <= 12:

#     mlist.append(i)
    
#     i += 1

# print(mlist)






"""
Q2. Print the elements in the list using WHILE LOOP.

mlist = [ 12, 23, 24, 25, 26, 27, 28, 29, 30, 31 ]
"""


# mlist = [ 12, 23, 24, 25, 26, 27, 28, 29, 30, 31 ]

# # print(mlist)

# # using FOR LOOP:::::
# for i in mlist:

#     print(i)


# # Using WHILE LOOP::::
# i = 0 

# while i <= (len(mlist)-1):

#     print(mlist[i]) 

#     i += 1




"""
Q3. Find the sum of the number in the list using WHILE LOOP.

mlist = [ 12, 28, 29, 30, 31 ]
"""

# mlist = [ 12, 28, 29, 30, 31 ]

# i = 0
# sum = 0
# while i < len(mlist):
    
#     sum = sum + mlist[i]

#     i += 1

# print(sum)



"""
Q4. Make a python program to take 5 alphabet letters from the user and remove those 
letters from the given string.

myString = " Hello People!! I'm an Artifical Intelligence Designed to detect malware in the 
system. "

SOLVE THIS QUESTION USING WHILE LOOP...
"""



# myString = "Hello People!! I'm an Artifical Intelligence Designed to detect malware in the system. "

# i = 0
# mlist = []
# while i<5: 
#     mstr = input('Enter your alphabet: ')

#     mlist.append(mstr)

#     i += 1

# print(mlist)


# ms = myString
# for i in range(0, len(mlist)):

#     element = mlist[i]

#     ms = ms.replace(element, "")

# print(ms)





# mstr = "Hello world!! this is an exclusive system designed to work over emebedded systems..."

# a = mstr.split("e")
# print(a)

# commit = " "
# print(commit.join(a))
