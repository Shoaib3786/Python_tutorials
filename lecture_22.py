# """
# OBJECTIVE:

# 1. Monthly Assignment (Marks awarding scheme).
# 2. 

# 3. Datatype:
# 0. List. -> [ ]
# 1. Dictionary. -> { }
# 2. Tuple -> ( )



"""
Dictionary Operations:

1. Building dictionary 
    - build using {key : values}
    - build using constructor dict(key=value, key2=value2,)

2. Accessing items
    - accessing via keys
    - accessing via .get()

    - getting all values of the dictionary (.values())
    - getting all keys of the dictionary (.keys())
  

3. Changing items(or Updating) 
    - Changing the item via key 
    - changing the item via .update( {key : value,} ) 

4. Adding item:
    - Adding the item via new key and assign value to it.
    - Adding the item via .update( {key:value}) it append in the last 


5. Remove item:
    - Removing the item via .pop()
    - Removing the item via .popitem(), removes from last.
    - Remoivng the item via del myDict['key'].  // del can even delete the whole dictionary
    
    - Clearing the completedictionary:
      - del myDict
      - myDict.clear()


6. Loop:
  - loop for all keys in the dictionary. (.keys())
  - loop for all values in the dictionary (.values())
  - loop for (key,value) pairs together (.item())

"""





# """

# # Dictionary -> Key value pairs.  -->. {key, value} 



"""
1. Building dictionary 
    - build using {key : values}
    - build using constructor dict(key=value, key2=value2,)
"""

# mtd-1

# player = {
#     "health": 35, 
#     "skill": 75, 
#     'live':  "dead",
#       1: "ball"
#     }

# # print(player)

# # mtd-2.0

# player = dict( {'health':35, "skill": 21}  )
# print(player)


# # mtd-2.1
# mdict = dict( health = 35, skill = 21, live ='dead' )
# print(mdict)





# # mtd-1
# Cars = {
#   "brand": "Tata",
#   "model": "Safari",
#   "year": 1998,
#   "color": "Gray"
# }


# time = {
#     1: "breakFast",
#     2: "Work",
#     3: "Play",
#     4: ['play', 12, 223, 'Football']
# }

# # mtd-2
# mdict = dict(name= "Max", age = '21', country =' UK')
# print(mdict)








"""
2. Accessing items
    - accessing via keys
    - accessing via .get()

    - getting all values of the dictionary (.values())
    - getting all keys of the dictionary (.keys())
"""


time = {                    # dict
    1: "breakFast",
    2: "Work",
    3: "Play",
    "mlist": ['play', 12, 223, 'Football']
}




# getting complete keys of the dict
# print(time.keys())

# # getting complete values
# print(time.values())

# #mtd-1
# # getting values via key by slicing
# print( time['mlist'] )

# #mtd-2
# # getting values via key but by using (.get()) 
# print( time.get( 3 ))




# printing all keys of the ditionary
# print(time.keys())

# printing all values
# print(time.values()) 

# printing specific value (by accessing it)
# print(time[1])

# printing the specif value using .get()
# print(time.get(2))




"""
3. Changing items(or Updating) 
    - Changing the item via key  
    - changing the item via .update( {key : value,} ) 
"""


# time = {
#     1: "breakFast",
#     2: "Work",
#     3: "Play",
#     "mlist": ['play', 12, 223, 'Football']
# }

# slicing
# time[2] = " Hey Day!! "

# print(time)

# using .update()

# a = time["mlist"]

# a[1] = "Bye!!!"

# print( a )

# time["mlist"] = a

# print(time)


# time.update()

# print(time)


# print(time[3]) 
# print(time.get(3))






# # printing the changed item at key 3
# time[3]='Dinner'
# print(time[3]) 
# print(time.get(3))


# # printing the changed item at key 3 by .update() method
# time.update( { 3 : "Hello world!! " } )
# print(time[3]) 
# print(time.get(3))


"""
5. Remove item:
    - Removing the item via .pop()
    - Removing the item via .popitem(), removes from last.
    - Remoivng the item via del myDict['key'].  // del can even delete the whole dictionary
    
    - Clearing the completedictionary:
      - del myDict
      - myDict.clear()
"""

# HOMEWORK 




"""
6. Loop:
  - loop for all keys in the dictionary. (.keys())
  - loop for all values in the dictionary (.values())
  - loop for (key,value) pairs together (.item())
"""

time = {
    1: "breakFast",
    2: "Work",
    3: "Play",
    "mlist": ['play', 12, 223, 'Football']
}


# # used for printing keys of the dictionary!!!
# print(time.keys())

# for x in time.keys():
#   print(x)


# PRINTING VALUES

# print( time.values())

# mlist = ['breakFast', 'Work', 'Play', ['play', 12, 223, 'Football']]
# for i in mlist:

#     print(i)



# printing all keys from the dictionary without .keys()
# for x in time:
#   print(x)


# for i in time:
#   print(time[i])


# for i,j in range(1,10)


# for a,b in time.items():

#     print( a,b )




# # print all keys of the dictionary using forloop
# for x in time.keys():
#   print(x)

# # printing all values
# for y in time.values():
#   print(y)

# printing all keys from the dictionary without .keys()
# for x in time:
#   print(x)

# # printing all values from the dictionary without .value()
# for y in time:
#   print(time[y])





# # printing all the key,values pairs from the dictionary
# for x,y in time.items():
#     print((x,y))




# myDict = {"name": "John", "country": "Norway"}
# mySeparator = "TEST"

a = "hello people!! I'm an AI system designed to work on Embedded systems"

a.strip("")

print()