from abc import ABC, abstractmethod
class Bank(ABC):
    def __init__(self,bank_name="ICICI BANK"):
        self.bank_name = bank_name

    def show_bank_name(self):
        return self.bank_name
    
    @abstractmethod
    def show_branch_name(self):
        pass

class Account(Bank):
    def __init__(self,owner_name,account_number,account_balance):
        self.owner_name = owner_name
        self._account_number = account_number
        self.__account_balance = account_balance

    def show_branch_name(self):
        return "Mumbai Branch"
    
    def show_account_balance(self):
        return self.__account_balance
    
    def deposite_balance(self,amount):
        if amount > 0:
            self.__account_balance += amount
            return f"{amount} Amount Successfully deposited and total Balance is {self.__account_balance}"
        else:
            return "Invalid Amount"
    
    def withdraw_amount(self,amount):
        if amount < self.__account_balance:
            self.__account_balance -=amount
            return f"{amount} amount Withdraw Successfully"
        else:
            "Insufficient Balance"

account_holder1 = Account("Mehboob","12234545",1000000000)

# print(account_holder1.__account_balance)

# import string
# import random
# print(random.choices(string.punctuation,k=4))


a = [] * []

print(a)