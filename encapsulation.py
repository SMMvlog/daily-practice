

class Bank:
    def __init__(self,balance,user_name,bank_name):
        self.__balance = balance
        self._user_name = user_name
        self.bank_name = bank_name

    def show_balance(self):
        return self.__balance
    def show_user_name(self):
        return self._user_name
    
    def show_bank_name(self):
        return self.bank_name
    

# obj1 = Bank(5000000,"Mehboob Shaikh","ICICI BANK")
# print(obj1.show_balance())

# class Branch(Bank):
#     def show_balance(self):
#         return self._user_name

# obj2 = Branch(15000000,"Mehboob Shaikh2","ICICI BANK2")

# print(obj2.show_balance())

a = "xaxb"
b ="bbxx"
# print(sorted(a)==sorted(b))
k = set(a).difference(set(b))
if len(k) == len(b):
    for i in b:
        if i not in a or a.count(i)!=b.count(i):
            pass

# print()




# class Parent:
#     def __init__(self):
#         self._protected_var = "I am protected"
#         self.__private_var = "I am private"

# class Child(Parent):
#     def access_variables(self):
#         print("Accessing protected:", self._protected_var)  # ✅ Works
        
#         # ❌ Will raise AttributeError:
#         # print("Accessing private:", self.__private_var)
        
#         # ✅ Indirect way using name mangling:
#         print("Accessing private via mangling:", self._Parent__private_var)

# # Testing
# child = Child()
# child.access_variables()

result = []
a, b = 0,1
for i in range(10):
   if i in [0,1]:
      result.append(i)
   else:
     fib = a+b
     result.append(fib)
     a,b = b,fib
print(result)	