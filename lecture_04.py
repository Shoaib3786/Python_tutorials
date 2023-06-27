
#### CONTINUATION OF IF ELSE CONDITIONS ####


"""Discuss:
1. structure of if else condition is 'if' and ends with 'else' elif always comes in between. 
2. Always take care about intendation.
3. comments can be add using #,""" """". 
4. commented statement isn't executed by the programing language.
5. Corrections in Lecture03_assignment solution.
"""


# ASSIGNMENT DOUBTS

"""
Q2. Write python code If tomorrow it isn't too hot, I'll go to
the sea, but if it is, I'll have a walk in the forest. However, 
if it rains, I'll stay at home.     
"""
# Why introduced and in the if else condition?

# 1. If tomorrow it isn't too hot -> I'll go to the sea
# 2. if too hot -> I'll have a walk in the forest
# 3. if it rains -> I'll stay at home.



# != -> not equal to 


# ['too hot', 'rain', 'not too hot' ] # input


# code 


# 2 == 3 False     --> == equal to operator
# 2 != 3 True      --> != not equal to operator


# [2 - 'too hot', 3 - 'rain']

a = 5

if (a == 2): # False
    print(" I'll have a walk in the forest ")

elif (a != 3):  # True
    print(" I'll go to the sea ")

    
elif (a == 4): # False
    print(" I'll stay at home ")
    
else: 
    print("hello")
    












