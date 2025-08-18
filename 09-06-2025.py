l=[34,21,91,7,56]


largest_num = l[0]
second_largest_num = 0
third_largest_num = 0

# for i in l[1:]:
#     if largest_num < i:
#         third_largest_num = second_largest_num
#         second_largest_num = largest_num
#         largest_num = i
#     elif second_largest_num < i:
#         third_largest_num = second_largest_num
#         second_largest_num = i
#     elif third_largest_num < i:
#         third_largest_num = i
# print(largest_num)
# print(second_largest_num)
# print(third_largest_num)



# s1 = "cde"
# s2 =  "abc"
# print(set(s1).union(set(s2)))



# thisset = {"apple", "banana", "cherry"}

# for x in thisset:
#   print(x)
# thisset = {"apple", "banana", "cherry"}

# print("banana" in thisset)

# thisset = {"apple", "banana", "cherry"}
# tropical = {"pineapple", "mango", "papaya"}

# thisset.update(tropical)

# print(thisset)

# x = {"a", "b", "c"}
# y = [1, 2, 3]

# z = x.union(y)
# print(z)


# set1 = {"apple", True,  "banana", 0, "cherry"}
# set2 = {False, "google", 1, "apple", 2, True}

# set1.intersection_update(set2)

# print(set1)

# set1 = {"apple", "banana", "cherry"}
# set2 = {"google", "microsoft", "apple"}

# set3 = set1.difference(set2)

# print(set3)

set1 = list(set("absdjkvuahdakejfnfauhdsaavasdlkj"))
set2 = list(set("djfladfhiawasdkjvalskufhafablsdkashlahdfa"))
set1.sort()
set2.sort()
# set1.symmetric_difference_update(set2)

print(set1)
print(set2)


# set1 = {"apple", "banana", "cherry"}
# set2 = {"google", "microsoft", "apple"}

# set1.difference_update(set2)

# print(set1)


# def second_largest_num(lst):
#     try:
#         largest_num = 0
#         second_largest_num = 0
#         for i in lst:
#             if largest_num < i:
#                 largest_num = i
#             if largest_num
#     except Exception as ex:
#         return ex


# def get_even_num(n):
#     for i in range(n):
#         if i%2==0:
#             yield i
#  even_num = get_even_num(50)

# from threading import Thread

# def get_num(n):
#     for i in range(n):
#         print(i)

# x1 = Thread(get_num)

# x1.start()

# def dec(func):
#     def wrapper(*args,**kwargs):
#         name = args[0]
#         full_name = f"{name} Shaikh"
#         return func(full_name,*args[1:],**kwargs)
        
#     return wrapper

# @dec
# def get_full_name(name):
#     return name
# print(get_full_name("Mehboob"))





