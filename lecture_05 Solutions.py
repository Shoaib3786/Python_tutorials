"""
Q1: Write python program that ask two user input and find largest 
number out of that two user input number.
"""

a = input(" Enter Value a: ") 
b = input(" Enter Value b: ") 
if a > b:
    print(f' {a} is largest ')
elif b > a:
    print(f' {b} is largest')
else:
    print(f' {a} is equal to {b} ')


"""
Q2: Write python program that accepts age of 4 users and find the
youngest user out of it.
"""
sam = int(float(input(" Enter Value sam: ")) )
max = int(float(input(" Enter Value b: ")) )
robin = int(float(input(" Enter Value robin: ")) ) 
lilly = int(float(input(" Enter Value lilly: ")) )

# example:
sam = 12
max = 10
robin = 15
lilly = 14

if (sam < max) or (sam < robin) and (sam < lilly) :    # if sam is largest
    print(f' {sam} is youngest ')


elif (max < sam) and (max < robin) and (max < lilly):   # if max is largest
    print(f' {max} is youngest')


elif (robin < sam) and (robin < max) and (robin < lilly):   # if robin is largest
    print(f' {robin} is youngest')


elif (lilly < sam) and (lilly < max) and (lilly < robin):   # if lilly is largest
    print(f' {lilly} is youngest')


elif (sam==max) and (sam == robin) and (sam == robin):  # if sam = max = robin = lilly 
    print('All are of equal age')

"""
like this we have to make many more such elif condition
for conditions like a=b=c<d, a=b=d<c, a=c=d<b, b=a=c<d,.....
"""

### [or] ###

# get values in list and then sorting the values



"""
Q3: Write a python program to find the area of the:
    - Rectangle
    - Circle
    - Triangle
    - Square
"""

import math  # import math library

shape = input("Enter shape")

if (shape == 'Rectangle'):  # Area for rectangle
    a = float(input("Enter lenght: "))
    b = float(input("Enter bredth: "))

    area_rec = a * b

    print("Area of rectngle: ", area_rec)


elif (shape == 'Circle'): # Area for circle
    r = float(input("Enter radius: "))
    pi = 3.14    #[or]  pi = math.pi
    pi = math.pi
    area_cir = pi * r ** 2

    print("Area of rectngle: ", area_cir) 


elif (shape == 'Triangle'): # Area for triangle
    h = float(input("Enter height: "))
    b = float(input("Enter base: "))
    area_triangle = 1/2 * b * h

    print("Area of traingle: ", area_triangle) 


elif (shape == 'square'): # Area for sqaure

    a = float(input("Enter side length: "))
    area_square = a**2

    print("Area of square: ", area_square) 


"""
Q4: Write a python program, A shop will give discount of 10% 
    - if the cost of purchased quantity is more than 1000 bucks. 
Also,
- Ask user for quantity [Suppose, one unit will cost 100 bucks].
- Judge and print total cost for user.
"""

quantity = float(input("Enter quantity of good you purchased: "))

print("Quantity of product u purchased is: ", quantity)

"""
unitry method:
 1 quantity product = 100 bucks
 x quantity product = x * 100 bucks
"""
purchased_cost = quantity * 100  # cost of purchased product
cost_afterDiscount = 0  # discounted 
if purchased_cost > 1000:
    print(f' ur actuall cost is: {purchased_cost} bucks')

    print("Congrats u r eligible ofr '10%' discount!!!")

    cost_afterDiscount = purchased_cost - (purchased_cost * 0.1) 
    print(f" Price u have to pay after '10%' discount is: {cost_afterDiscount} bucks")

else:
    print(f'unfortunately!!! u r not eligible for discount,you need to pay: {cost_afterDiscount} bucks')


#### Catch from Q4 ###
"""
1. varaible in if scope is not available for else, elif scope,
 hence need to either declare varaible outside or declare variable as zero outside.

2. unitry method
3. percentage 
4. using 'f' while printing the statement
"""
