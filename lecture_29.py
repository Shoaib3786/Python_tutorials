"""
OBJECT ORIENTED PROGRAMMING:> (OOPs concept)
"""

# Classes and Objects

"""BASIC STRUCTURE:"""


class Person:

    """Objective
    1. User input
    2. Making dictionary
    """
    def Gen_personal_info(self):
        mdict = {}
        # 1.
        name = input('Enter your name: ')
        age = int(float(input("Enter your age: ")))
        dob = input('Enter your DOB: ')
        gender = input('Enter your gender: ')

        # 2.
        mdict = {
            'name': name,
            'age': age,
            'dob':dob,
            'gender':gender
        }

        return mdict



    """Objective:
    1. Ask userinput which user want to fetch
    2. Perfrom dictionary operation for fetching user desired query.
    """
    def User_query(self, mdict):

        print('Pleas enter value from the given list: *[name, age, dob, gender]*')
        dic_value = ['name', 'age', 'dob', 'gender']
        
        query = input("ENTER YOUR QUERY") # HELLO
        
        while True:

            if (query in dic_value): #TRUE

                # to show user desired query

                value = mdict[query]

                print(f'Your desired data: {value}')

                break


            else:
                print('Try again')
                query = input("Enter your query: ")



# person_1 = Person()

# mdict = person_1.Gen_personal_info()

# person_1.User_query(mdict)

# class vehicle:

#     def car_info(lalit, self, car_name):

#         print('colour of the car is: ', self)
#         print('name of the car is: ', car_name)


# obj1 = vehicle()

# obj1.car_info('black', 'Alto')













"""
Write a Python program to replace the last value of tuples in a list.
Sample list: [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
Expected Output: [(10, 20, 100), (40, 50, 100), (70, 80, 100)]

# PERFORM USING CLASSES AND OBJECTS 
"""



# class myClass:

    # def changeNum(self,mlist):

    #     mlst2 = []
    #     for i in mlist:  # (10, 20, 40)

    #         lst = list(i)  # typecasting

    #         lst[-1] = 100

    #         mtup = tuple(lst)  # typecasting

    #         mlst2.append(mtup)
        
    #     return mlst2

    
#     def printList(self, color):
    
#         print(color)

# obj1 = myClass()
# obj2 = myClass()

# obj1.printList('red')

# obj2.printList('pink')
