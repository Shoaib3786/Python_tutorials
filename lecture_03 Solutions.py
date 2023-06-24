
######################## SOLUTIONS #########################


print('\n')
print('***************')
print('Program 1')
print('***************')

"""
Q1: Write a python program for assigning grades (A, B, C, D, E, F, G) based on marks obtained by a student.
	- if the percentage is above 95, assign grade A
	- if the percentage is above 70 and below and including 95, assign grade B
	- if the percentage is above 60 and below and including 70, assign grade C	
    - if the percentage is between (50, 60), assign D
    - if the percentage is (40 to 50), assign E
    - if the percentage is 29 and 30 , assign F
    - if the percentage is 10 or 11, assign G 
"""

# make a varaible that takes user percentage, percentage can be in float
percentage = float(input("enter your marks"))

if (percentage > 95):
    print("Grade A")

elif(percentage > 70) and (percentage <= 95):
       print("Grade B")

elif(percentage > 60) and (percentage <= 70):
     print("Grade C") 

elif(percentage > 50) and (percentage < 60):
     print("Grade D")

elif(percentage >= 40) and (percentage <= 50):
    print("Grade E")

elif(percentage == 29) and (percentage == 30):
     print("Grade F")

elif(percentage ==10) or (percentage ==11):
     print("rade G")

# ***************************************************************


print('\n')
print('***************')
print('Program 2')
print('***************')
print('\n')


#Q2 :write python code if tomorrow it isn't too hot,i'll go to sea, but if it is,i'll have a walk in the forest.however,if it rains,i'll stay at home.

a = input("enter weather:")

if (a != "too hot") and (a!= "rain"):
  print("i will go to the sea")

elif (a == "too hot"):
  print("i'll have a walk in the forest")

elif (a == "rain"):
  print("i'll stay at home")


# ***************************************************************


print('\n')
print('***************')
print('Program 3')
print('***************')
print('\n')

# # 3.         
# # Q: accept any city name from the user and display the monuments of the city name:
# #  -if city is Delhi then print monuments of Red Fort
# #  -if city is Agra then print monuments of Taj Mahal
# #  -if city is Jaipur then print monuments of Jal Mahal

a = input("enter city name:")

if a == ("Delhi"):
    print("monuments of Red Fort")

elif a == ("Agra"):
    print("monuments of Taj Mahal")   

elif a == ("Jaipur"):
    print("monuments of Jal Mahal")


# # *******************************************************************




print('\n')
print('***************')
print('Program 2')
print('***************')
print('\n')

# # 4.
# # Q:write python program to check whether a person is senior citizen or not:
# #   -if person's age >60 then he/she is a senior citizen
# #   - else he/she is not
a = int(float(input("enter age of citizen:")))

# [or]
a = input("enter age of citizen:")
a = float(a)
a = int(a)

print(type(a))  # to verify

if (a > 60):
    print("senior citizen")

else:
   print("not senior citizen")