

class Bank:
    def __init__(my,account_no,owner_name,balance):
        my.account_no = account_no
        my._owner_name = owner_name
        my.__balance = balance


    def show_account_no(my):
        return f"account_no is {my.account}"
    def show_owner_name(my):
        return f"owner name is {my._owner_name}"
    def show_balance(my):
        return f"your balance is {my.__balance}"
    
    def withdraw_amount(my,amount):
        my.__balance -=amount
        return f"You have debited amount: {amount} and now remaining balance is {my.__balance}"
    def deposite_amount(my,amount):
        my.__balance +=amount
        return f"You have deposited amount: {amount} and now balance is {my.__balance}"
    
obj = Bank("1100321","Mehboob Shaikh",150000000)

# print(obj.deposite_amount(10000))

class Account(Bank):
    def __init__(self,bank_name,bank_branch,account_no,owner_name,balance):
        self.bank_name = bank_name
        self.bank_name = bank_branch
        super().__init__(account_no,owner_name,balance)


obj1 = Account("ICICI BANK","MALAD","11023234","Mehfooz",3000000)

print(obj1.show_owner_name())


    