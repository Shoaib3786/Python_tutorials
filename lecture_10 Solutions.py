
""" ASSIGNMENT SOLUTIONS """

mlist = [ ]

for i in range(0,4):

     a = int(input('Enter value: '))     

     mlist.append(a)

     # print(mlist)

print('my user entered value list: ',mlist)


# fetching the values from mlist one by one
for elements in mlist:

     print(f'mlist value {i}')

     # finding factorial of mlist items one by one
     factorial = 1
     for i in range(1, elements+1):

          factorial = factorial * i

     print(factorial)