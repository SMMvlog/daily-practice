from abc import ABC,abstractmethod

class RBI(ABC):

    @abstractmethod
    def create_account(self,name,amount):
        pass

    @abstractmethod
    def deposite_amount(self,amount):
        pass

    @abstractmethod
    def withdraw_amount(self,amount):
        pass

    @abstractmethod
    def check_balance(self):
        pass


class SBI(RBI):

    def __init__(self):
        self.name = ""
        self.balance = 0

    def create_account(self, name, amount):
        self.name = name
        self.balance = amount
        return f"Account created for {name}"
    def deposite_amount(self,amount):
        self.balance +=amount
        return f"the amount {amount} deposited and the blance is {self.balance}"
    def withdraw_amount(self, amount):
        print(self.balance)
        if self.balance>=amount:
            self.balance -=amount
            return f"{amount} Withdraw and the total amount is {self.balance}"
        else:
            return "Insuficient Balance"

    def check_balance(self):
        return f"The Total balance iS {self.balance}"


mehboob = SBI()

# print(mehboob.create_account("Mehboob", 1000))
# print(mehboob.deposite_amount(2000))
# print(mehboob.withdraw_amount(1000))
# print(mehboob.check_balance())

# def abc(n,blance=()):
#     blance[0] =n
#     return blance

# print(abc(20))

print(type({}))