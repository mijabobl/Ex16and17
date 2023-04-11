class InsufficientFundsException(Exception):
    """Custom exception example inheriting from Exception class"""

    def __init__(self, money):
        self.msg = f"Not enough money to withdraw {money} pounds!"

    def __str__(self):
        return self.msg

class Person:
    """ Simple Person class to demo OO principles and a custom exception"""

    def __init__(self, name, accNo, money):
        self._name = name
        self._accNo = accNo.upper()
        self._money = money

    def __str__(self):
        return f"Name: {self.get_name()} Account number: {self.get_accNo()} has an account balance of: {self.get_money()} pounds."

    def get_name(self):
        return self._name

    def get_accNo(self):
        return self._accNo

    def payin(self, num):
        self._money += num
        return

    def get_money(self):
        return self._money

    def withdraw(self, num):
        if num > self._money:
            raise InsufficientFundsException(num)
        else:
            self._money -= num
            return f"{self.get_name()} now has {self.get_money()} pounds!"
