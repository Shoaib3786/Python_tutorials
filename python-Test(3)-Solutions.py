
"""
Python Test3 Solution

Section-B
"""


"""
Q6. From the Sample dictionary delete the dictionary values of the given list of keys provided in the question below.

sample_dict = {
"name": "Kelly",
"age": 25,
"salary": 8000,
"city": "New york"
}

# Key values  to remove from the dictionary 
keys = ["name", "salary"]

Make the above python program within a function called myFun().
"""

# sample_dict = {
#     # "name": "Kelly",
#     "age": 25,
#     # "salary": 8000,
#     "city": "New york"
# }

# keys = ["name", "salary"]



# def myFun(key, mdict):
    
#     for i in key:  #'name', 'salary'

#         mdict.pop(i)

#     print('New dictionary: ', mdict)

#     return mdict


# meraDict = myFun(mdict=sample_dict, key=keys)

# print('New dictionary: ', meraDict)


"""
Q7. Reverse the given the list:
	mlist = [12, 34, 700, 213, 99, 8, 7]
"""


# mlist = [12, 34, 700, 213, 99, 8, 7]
# # print(mlist[::-1])

# mlist.reverse()
# print(mlist)



"""
Q8. From the given list implement the python program within a function called myFun() to add 7000 after 6000 in the given list.
mlist = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
"""

# def myFun(mylist):

#     mylist[2][2].append(7000)
#     print('New list: ', mylist)



# mlist = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
# myFun(mylist= mlist)



"""
Q9. Modify the tuple replace ‘hello’ with 10000 implement the python code for this problem within a function called myTup():
	tuple_01 = (10, 23, [99, 8, 70], ‘hello’)
"""



# def myTup(mtup):

#     a = list(mtup)  #[10, 23, [99, 8, 70], 'hello']

#     a[-1] = 10000

#     b =tuple(a)

#     return b




# tuple_01 = (10, 23, [99, 8, 70], 'hello')  

# myNewB = myTup(tuple_01)

# print('My new tuple: ', myNewB)




"""
Q10. Make two functions named it as getUser(), printUserInfo().
	
    getUser() -> Takes 5 user input and convert them into a list
    
	printUser() -> use the getUser() created list into printUser() by adding this list into a given tuple provided below at index 3.
		
        mTuple = (12, ‘hello’, [12, 9, 88], (12, 55, 44), ‘kiloByte’, ‘MaxPoll’)

"""

def getUser():
    
	i = 0
	mlist = []
	
	while (i < 5):
		a = input('Enter value: ')
		mlist.append(a)

		i += 1

	return mlist


def printUser(mTup):

	mList = getUser()
    
	a = list(mTuple)  # typecasting into list

	# a.insert(3, mList)
	a[3] = mList

	mTup = tuple(a)  # typecasting into tuple

	return mTup


mTuple = (12, 'hello', [12, 9, 88] ,(12, 55, 44), 'kiloByte', 'MaxPoll' )

value = printUser(mTup= mTuple)


print('Final tuple is: ', value)