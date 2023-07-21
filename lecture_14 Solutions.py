"""
Q1. Accept 10 numbers from the user and dispaly their average.
"""

sum = 0
for _ in range(10):
    num = int(input('enter number: '))

    sum = sum + num

avg = sum / 10

print('average : ', avg)
    


"""
Q2. Write a program that prints sum of all even numbers and 
sum of all odd numbers that lies from (12 to 37) including both.
"""

sumE = 0
sumO = 0

for i in range(12, 38):

    if i % 2 == 0:
        sumE = sumE + i 
        

    elif i % 2 != 0:
        sumO = sumO + i

print(f'sum of all even numbers are: {sumE}')

print(f'sum of all odd numbers are: {sumO}')





"""
Q3. Write a program to print the table of user input number.
Example: user input 6 then print the table of 6 as 6*1 = 6 and 
go on till 6 * 10 = 60.
"""


num = int(float(input('Enter type number: ')))

for i in range(1, 11):
    
    mul = num * i

    print(f'{num} x {i} = {mul}')




"""
Q4. Find the error in the provided code:

a = int("Enter a number)
for i in Range(2,6):
if a = i:
    print("A)

else:
print("B")

"""



# ERROR ARE AS FOLLOWS:

"""
1. input is not written properly.
2. for loop block didn't followed indentation correctly.
3. In the if block print() statement is not writtent correctly.
4. else block didn't followed indentation correctly.
"""
