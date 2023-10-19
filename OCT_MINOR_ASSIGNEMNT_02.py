"""Assignment on OOPs concept:"""

"""
[Q1]

Build a python program for an ATM machine [Program must be based on OOPs concept]
- In this program user deposit the cash and withdraws the cash and If the withdrawal amount is greater than the balance the error throws that says "Insufficient balance"

1. Make a method named it as deposit() -> That takes user deposit and store it in the balance variable.


2. Make another method named it as withdraw() -> That print and returns the user asked amount, but before returning the amount check if user asked value is less than or equal to the balance.
                                              -> If the balance is less than the user entered value than print('Insufficient balance').
                   
NOTE: - Minor details like making argument and passing the parameters for each methods as well as making the constructor for making varaibles of that class instance....these kind of minor details has not mentioned in the question. You have to take care about these minor details.
"""


class My_atm:

    def __init__(self):
        self.balance = 0

    def deposit(self):
       self.balance = float(input('Enter depositing amount: '))
   
    def withdraw(self):
        
        self.amount = float(input('Enter your withdrawal amount: '))

        
        if (self.amount <= self.balance):

            print("Transaction successful")

        else:
            print('Insuffecient balance!!!')



obj_01 = My_atm()

obj_01.deposit()

obj_01.withdraw()