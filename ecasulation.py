class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance  # private variable (encapsulated)

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited {amount}")
        else:
            print("Invalid deposit amount")

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew {amount}")
        else:
            print("Insufficient balance")

    def get_balance(self):
        return self.__balance



account = BankAccount("John Doe", 1000)

account.deposit(500)           # ✅ Deposited 500
account.withdraw(300)          # ✅ Withdrew 300
print(account.get_balance())   # ✅ 1200

# ❌ Direct access is not allowed
print(account.__balance)       # ❌ AttributeError
