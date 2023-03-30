#create Account class
class Account:
    def __init__(self):
        self.balance = 0
        print("Welcome to The Banker")

    def deposit(self):
        amount = float(input("How Much Would you Like to Deposit? : "))
        self.balance += amount
        print("You Have Deposited:", amount)

    def withdraw(self):
        amount = float(input("How Much Would you like to Withdraw? : "))
        if self.balance >= amount:
            self.balance -= amount
            print("You Withdrew:", amount)
        else:
            print("Insufficient balance  ")
    def final(self):
        print("Your Balance Is =", self.balance)





