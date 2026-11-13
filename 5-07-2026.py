input_data = {"a": 1,"b": {"c": 2,"d": {"e": 3}},"f": {"g": [4, 5, {"h": 6}]},"i": [7, 8]}

# k = {"a": 1, "b.c": 2,"b.d.e": 3, "f.g[0]": 4,"f.g[1]": 5,"f.g[2].h": 6,"i[0]": 7,"i[1]": 8}

# def flat_dict(data,prefix=None):
#     result = {}
#     if isinstance(data,dict):
#         for key,value in data.items():
#             new_key = f"{prefix}.{key}" if prefix else key
#             result.update(flat_dict(value,new_key))
#     elif isinstance(data,list):
#         for index,item in enumerate(data):
#             new_key = f"{prefix}[{index}]"
#             result.update(flat_dict(item,new_key))
#     else:
#         result[prefix] = data 

#     return result

# print(flat_dict(input_data))

# a = {"3":4,"2":2}
# b = {"5":5,"7":7} 
# a.update(b)
# print(a)


class Bank:
    bank_name = "ICICI BANK"
    def __init__(self,branch_name,branch_location,amount,blance,dob):
        self.branch_name = branch_name
        self.branch_location = branch_location
        self.amount = amount
        self.__blance = blance
        self._dob = dob

    def get_blance(self):
        return self.__blance

    def deposite(self,amount):
        self.amount +=amount
        return self.amount
    
cust1 = Bank("Mumbra Kausa", "Thane",1000,120000,"08-03-1993")

print(cust1._dob)