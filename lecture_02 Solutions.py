
######################## SOLUTIONS #########################

print('\n')
print('***************')
print('Program 1')
print('***************'+'\n')

"""
Q1. Make a varaible that store (DO HARD CODING)
	- integer value
	- string value
	- float value
"""

# I'll make 3 variables calling it as ( value1 , value2 , value3 ) 

value1 = 10              #hardcoded int value
print("value is: ",value1)

value2 = 45.9            #hardcoded float value
print("value is: ",value2)

value3 = "Hello People"  #hardcoded string value
print("value is: ",value3)


# *************************************************************


print('\n')
print('***************')
print('Program 2')
print('***************'+'\n')

""" 
Q2. Make a variable that ask user to input value.
 	- integer value
 	- string value
 	- float value
""" 	

# I'll make the program dynamic by using *user input*.

# value1 = input('Enter Vlaue: ')   # Give int value
# print("value is: ",value1)

# value2 = input('Enter Vlaue: ')   # Give float value   
# print("value is: ",value2)

# value3 = input('Enter Vlaue: ')   # Give string valuer
# print("value is: ",value3)


# ****************************************************************


print('\n')
print('***************')
print('Program 3')
print('***************'+'\n')

"""
Q3. typecaste hardcoded(Progammer feeded) value into:
	- int
	- float
	- string
	The value is -> 49, 49.67, "Tom Cruise"
	
	do the type convertion for each given values into int, float and string and print the results.
"""
	
a = 49
int_a = int(a)         # typecaste 'a' variable into int type
float_a = float(a)     # typecaste 'a' variable into float type
string_a = str(a)      # typecaste 'a' variable into string type

# printing for verification
print('Variable value:',int_a)
print('variable datatype: ',type(int_a))

print('Variable value:',float_a)
print('variable datatype: ',type(float_a))

print('Variable value:',string_a)
print('variable datatype: ',type(string_a))



b = 49.5
int_b = int(b)         # typecaste 'b' variable into int type
float_b = float(b)     # typecaste 'b' variable into float type
string_b = str(b)      # typecaste 'b' variable into string type

# printing for verification
print('Variable value:',int_b)
print('variable datatype: ',type(int_b))

print('Variable value:',float_b)
print('variable datatype: ',type(float_b))

print('Variable value:',string_b)
print('variable datatype: ',type(string_b))



c = "Tom Cruise"
int_c = int(c)         # typecaste 'c' variable into int type
float_c = float(c)     # typecaste 'c' variable into float type
string_c = str(c)      # typecaste 'c' variable into string type

# printing for verification
print('Variable value:',int_c)
print('variable datatype: ',type(int_c))

print('Variable value:',float_c)
print('variable datatype: ',type(float_c))

print('Variable value:',string_c)
print('variable datatype: ',type(string_c))



# *****************************************************************

print('\n')
print('***************')
print('Program 4')
print('***************'+'\n')

"""
Q4. typecast user input value into:
	- int
	- float
	- string
	You as a user insert these values only -> 49, 49.67, "Tom Cruise"

	do the type convertion for each given values into int, float and string and print the results.
"""	

# I'll make the program dynamic by using user input.


# To only take int value from user, even if user insert float value it should be convert into int 
value1 = int(float(input('Enter Vlaue: ')))   # Take int value
print("value is: ",value1)

# Even if user insert int value, it will be represented as float only because of typecasting (Eg: 12 -> 12.0)
value2 = float(input('Enter Vlaue: '))        
print("value is: ",value2)

# input("...") automatically convert user input value into string only so no need to typecaste it into string but if you want you can do that as well.
value3 = input('Enter Vlaue: ')                #Take string value from user
print("value is: ",value3)


# ****************************************************************

print('\n')
print('***************')
print('Program 5')
print('***************'+'\n')

"""
Q5. Build a program that takes the person's age in an integer format 
and stores it into another varaible in a string format then print it.
"""	

# making variable that takes user input (making it dynamic hence using user input)
age = input('User plz enter your age: ') #take user age and store it into string format automatically
age = float(age)            # convert age into float from string
age = int(age)              # then convert float value into int

# [or]  above code can also be written in one line as:
age = int(float((input(" User plz enter your age: "))))

# now convert the age value from int back to string and store it 
# into another variable. (say my another variable is new_variable)
new_variable = str(age)     # typecasting my age from int to string

# for verification...
print('my age in int format: ', age)
print('type of age variable: ', type(age))

print('my age in string format: ', new_variable)
print('type of new_variable', new_variable)


# ************************************************************


print('\n')
print('***************')
print('Program 6')
print('***************'+'\n')

"""
Q6. Build a program that takes the person's name and prints its name.
"""

# make a variable that takes user name
name = input("Enter your name: ")  # input("") by defaut converts into string value so no need to typecaste it
print('Name is: ', name)



# *************************************************************

print('\n')
print('***************')
print('Program 7')
print('***************'+'\n')

"""
Q7. Build a program that takes the person's salary in float format but print it in integer format
"""	

# lets make a varaible that takes user salary
""" - Salary can be in integer or float so its better to take 
value and convert it into float then into int"""
salary = input("Enter your salary: ")
salary = float(salary)
salary = int(salary)

# [or] Above code can also be written in one line as:
salary  = int(float(input("Enter your salary: ")))
print('my salary in int format: ', salary) 