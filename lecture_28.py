"""
Practice Questions:

Q1. Convert 2 list into a single list. map each index members of both the list together as a tuple value.
    mlist_01 = [12, 43, 78]
    mlist_02 = [200, 400, 850]

    OUTPUT must look like: [(12, 200), (43,400), (78,850)]

    HINT: 
    1. Use Google to search for new python inbuilt function to do so...
    2. Even use Looping method to do so,(If possible in this case)
"""

#mtd-1
# mlist_01 = [12, 43, 78]
# mlist_02 = [200, 400, 850]

# m = list(zip(mlist_01, mlist_02))

# print(m)


# # mtd-2
# list_03 = []


# for i in range(0,3):   #i = 0,1,2

#     m = (mlist_01[i], mlist_02[i])  # (12,200) ,(43, 400), (78,850)

#     list_03.append(m)   # [(12,200) ,(43, 400), (78,850)]


# print(list_03)


"""  
Q2. Convert 2 list (list of keys and lisy of values) into a single dictionary.
    list_01 = [ 'key1', 'key2', 'key3' ]
    list_02 = ['play', 'study', 'football']

    HINT:
    1. This is relatable to the previous question. But need to use dictionary conrtuctor use Google to understand more about it.
"""
    


"""
Q3. For the below given program print the value of the key 'history'. 

    sampleDict = {
        "class": {
            "student": {
                "name": "Mike",
                "marks": {
                    "physics": 70,
                    "history": 80
                }
            }
        }
    }

    HINT:
    1. Use slicing approch to solve this, (you can perfrom multiple slicing in the sliced value until you arrived your (key, value) pair)

    2. Thsi type of the dictionary is called as Nested Dictionary.
"""
    

# sampleDict = {
#     "class": {
#         "student": {
#             "name": "Mike",
#             "marks": {
#                 "physics": 70,
#                 "history": 80
#             }
#         }
#     }
# }

# myHistory = sampleDict['class']['student']['name']
# print(myHistory)



"""
Q4. From the given dictionary, extract all the keys into a list format and loop through each key and get the value associated to each keys.

    sample_dict = {
        "name": "Kelly",
        "age": 25,
        "salary": 8000,
        "city": "New york"}

    Example:
    get all keys like this = ['name', 'age', 'salary', 'city']
    get all value like this = ['kelly', 25, 8000, 'New York'] 
"""

# sample_dict = {
#         "name": "Kelly",
#         "age": 25,
#         "salary": 8000,
#         "city": "New york"}

# mlist = []
# for i in sample_dict.keys():
#     mlist.append(i)

# print(mlist)

# mlist_02 = []
# for j in mlist:  # ['name', 'age', 'salary', 'city']
    
#     value = sample_dict[j]   # j = 'name'
#     mlist_02.append(value)

# print(mlist_02)


"""    
Q5. Arrange the given list in descending order.
    mlist_02 = [20, 400, 70]
"""

# mlist_02 = [20, 400, 70]

# mlist_02.sort()
# print('ascending order: ', mlist_02)


# # mlist_02.reverse()
# # print('descending order: ',mlist_02)


# for i in reversed(mlist_02):
#     print(i)



"""
Q6. From the given tuple print 2nd element of the 1st index list of the tuple

    tuple_1 = ([5, 15, 25], [10, 20, 30], (5, 15, 25))
"""

tuple_1 = ("Orange", [10, 20, 30], (5, 15, 25))

# 1st index => index =1
# 2nd element => index = 1 element of list
tuple_1[1][1]  #20


"""
Q7. Modify/Update the given tuple by replacing 2nd index value with a userdefined list.

    tuple = (12, 'levo', 'play', 34)

    HINT:
    1. Get the 5 user Input value and add that into your list.
    2. replace 2nd index value with the your list.
"""

mtuple = (12, 'levo', 'play', 34)


# Get the 5 user input and append in the mlist.
mlist = []
for i in range(5):
    a = int(input('Enter value: '))
    mlist.append(a)

print(mlist)

# convert tuple to list to perfrom updating operation in the tuple because tuple is immutable.
lst = list(mtuple)

# replace 2nd index value of the tuple
lst[2] = mlist
print(lst)

# now convert tuple back to list.
print(list(lst)) # for the output

