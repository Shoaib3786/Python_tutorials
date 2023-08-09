
""" SOLUTIONS """
# Q1: Find the factorial of 2, 5, 6, 7 & 8.

fact = 1
num = 5
for i in range(1, num+1):

    fact = fact * i

    print(fact)
print(f'factorial of {num} is: {fact}')
