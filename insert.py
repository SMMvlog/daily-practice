# my_list = [2, 3, 4]
# my_list.insert(0, 1)  # Inserts 1 at the beginning
# print(my_list)

# # my_list = [1, 3, 4]
# # my_list.insert(-1, 2)  # Inserts 2 before the last element
# # print(my_list)


# a = [5,6,7,8]
# target = 12
# result = []
# from itertools import combinations

# for i,j in combinations(a,2):
#     if i+j == target:
#         result.append(a.index(i))
#         result.append(a.index(j))
#         break
# print(result)

import string
import random
# print(string.ascii_letters)
# print(string.ascii_lowercase)
# print(string.ascii_uppercase)
# print(string.punctuation)
# print(random.randint(1000,9999))
# special_keyword = ["$","*","&","#","@"]

# print(f"{random.choice(string.ascii_uppercase)}{random.choice(string.ascii_lowercase)}{random.choice(special_keyword)}{"".join(random.choices(string.ascii_letters,k=7))}{random.randint(1000,9999)}"[:10])


lst = [0,1,1,2,3,5,8]
result = []
a, b = 0,1
print(a)
for i in range(5):
   if i in [0,1]:
      result.append(i)
   else:
     fib = a+b
     result.append(fib)
     a,b = b,fib
     print(f"a==={a},b===={b}")	



