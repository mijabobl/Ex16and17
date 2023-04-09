from bank import Account

# creating an object of class
term = Account()

# Calling functions with that class object
term.deposit()

#using an exception
try:
    term.withdraw2()
except:
    print("Insufficent Funds ")
finally:
    term.final()