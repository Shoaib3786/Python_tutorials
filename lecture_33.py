"""
1. Perform inheritance based problems
2. Look at importing the modules 
"""

"""
Build a python program for an ATM machine [Program must be based on OOPs concept]
- In this program user deposit the cash and withdraws the cash and If the withdrawal amount is greater than the balance the error throws that says "Insufficient balance"

1. Make a method named it as deposit() -> That takes user deposit and store it in the balance variable.


2. Make another method named it as withdraw() -> That print and returns the user asked amount, but before returning the amount check if user asked value is less than or equal to the balance.
                                              -> If the balance is less than the user entered value than print('Insufficient balance').
                   
NOTE: - Minor details like making argument and passing the parameters for each methods as well as making the constructor for making varaibles of that class instance....these kind of minor details has not mentioned in the question. You have to take care about these minor details.
"""


class AxisBank:   # base class or parent class

    def __init__(self, minBalance):
        self.balance = 0
        self.min_balance = minBalance


    def deposit(self):
        self.balance = float(input("Enter your deposit: "))
        print('Entered deposit is: ', self.balance)


    def withdraw(self):

        amount = float(input("Enter your withdraw"))

        if self.balance > self.min_balance:

            if amount <= self.balance:

                print('Transaction successful')

            else:
                print('Insufficient Balance!!')

        else:

            print(f"Ur balance is {self.balance} can't proceed")


# axisObj = AxisBank(minBalance=500)
# axisObj.deposit()
# axisObj.withdraw()


class iciciBank(AxisBank):

    def __init__(self, minBalance):
        
        self.Min_Balance = minBalance

        super().__init__(self.Min_Balance)  # 300


    def deposit(self):
        return super().deposit()
        

    def withdraw(self):

       return super().withdraw()

# iciciObj = iciciBank(minBalance=300)
# iciciObj.deposit()
# iciciObj.withdraw()







