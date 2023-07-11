### Objective ###
"""
1. break, pass, continue 
2. Backtracing in list
"""





# a = [12, 23, 34, 18, 54, 66]

# for i in a:

#     print(f'now i is {i}')

#     if i == 18:
    
#         continue

#         print(f' now i is {i}')    
#         print('hello')


# print('addittion is: ', 12+32)
        

""" break, continue, pass """

""" 1. break:
break statement helps to come out of the loop. terminates the loop
""" 

# """Exp"""
# a = [1,23,4,5,52]
# for i in a:

#     if i == 4:
#         print(f'i is {i}, I want to come out of the loop')
#         break
#         print('hello')

#     print(f'i is {i} till now not recieved number 4')


""" 2. pass:
does nothing it just fills up the space in the loop for the 
time being until real condition fills up
"""

# """Exp"""
# a = [1,23,4,5,52]
# for i in a:

#     if i == 4:
#         print('hello1')
#         pass
#         print('hello2')


""" 3. continue:
it moves to the next iteration.
"""

# a = [12, 32, 4, 21, 44, 7]

# for i in a:
    
#     if i == 4:
        
#         continue
        

#     print(f'now i is {i}')






# """ 2. Backtracing """

# a = [1,23,43,54,6]

# print('"""""mtd-0""""')

# # [mtd-0]  [reverse as method, it doesn't return any value, it just update the list]
# print('original', a)
# a.reverse()
# print('reverse',a)




# def myfun(a):
#     print('hello', a)
# myfun(12)
# reversed()



# class myAge:

#     def myfun(a):
#         print('hello', a)

#     def pop()
        
#     def insert()



# myObject = myAge

# myObject.myfun()
# a = [12,3]
# list.reverse()

# # a.reverse()  # method 

# # reversed(a) # function





# print('"""""mtd-1""""')
# [mtd-1] [reversed as function]
# for i in reversed(a):
#     print(i)


# print('"""""mtd-2""""')
# [mtd-2]
# for i in a[::-1]:

#     if i == 23:
#         break
#     print(i)

