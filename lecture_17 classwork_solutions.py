
"""
Q1. Take 10 users age (age should be between the range of 12 to 40), 
sort the age of the user in a ascending order and then perfrom 
backtracing to finally print the sorted age in descending order.

Note: In this question you are not allowed to use any of the 
backtracing shortcuts (that means cannot use reversed(), a.reverse()
and not even a[::-1]).

Please Design your own backtracing algorithm for this particular 
problem statement.

Hint: Using for loop.
"""

mlist = []
for i in range(5):

    a = int(input('Enter user age: '))
    
    if 12 < a < 40:
        mlist.append(a)

    else:
        print('Try again!! Enter user age between 12 to 40')
        a = int(input('Enter user age: '))
        mlist.append(a)
    

print(f'my unsorted list: {mlist}')

mlist.sort()

newList = []
for j in range(len(mlist)-1, -1, -1):

    newList.append(mlist[j])
    
print(f'my sorted list in descending order: {newList}')

