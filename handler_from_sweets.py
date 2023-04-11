from person import Person, InsufficientFundsException

Erling = Person("Erling:","123456789",0)
Saka = Person("Saka:","987654321",50)
print(Erling)
print("Eerling gets 100 pounds -->")
Erling.payin(100)
print(Erling)
print("Erling withdraws 90 pounds -->")
print(Erling.withdraw(90))
try:
    print(Saka)
    print("Saka withdraws 60 pounds -->")
    print(Saka.withdraw(60))
except InsufficientFundsException as e:
    print(e)
finally:
    print(Saka)

print("End Of Demonstration")