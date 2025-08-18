# n = 12

# factor_num = []

# for i in range(1,n+1):
#     if n%i == 0:
#         factor_num.append(i)

# print(factor_num)



def factorial(n):
    if n == 0:
        return 1
    else:
        return 1 * 1
#   4 * factorial(4-1=3) 6 = 24
#   3 * factorial(3-1=2) 2 =6 
#   2 * factorial(2-1=1) 1 =2 
#   1 * factorial(1-1=0) =1  
  

# print(factorial(4))


# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return "Hello"

# print(factorial(0))












# def collect_numbers(n, acc=[]):
#     print(f"Calling collect_numbers({n}),id of n:{id(n)}, acc id: {id(acc)}")
    
#     if n == 0:
#         return acc

#     acc.append(n)
#     return collect_numbers(n - 1, acc)

# result = collect_numbers(3,[])
# print("Final result:", result)
# a =[]
# b = []

# print(f"a----{id([])}")
# print(f"b----{id([10])}")

# a = 10
# b = 10
# print("a-------",id(a))
# print("a-------",id(b))

# a = []
# print(id(a))
# print(id([3,4]))

# a = (4,6,7,8)

# print(a)
# print(f"id of a: {id(a)}")
# print(f"id of a[0]: {id(a[0])}")
# print(f"id of a[1]: {id(a[1])}")
# print(f"id of a[2]: {id(a[2])}")
# print(f"id of a[3]: {id(a[3])}")

# a = ()
# b = ()
# print(id([]))
# print(id([]))


# a = 300

# b = 300
# print(id(a))
# print(id(b))



# string = "asddrfggthjnngbsaklmyy"
# largest_substring = ""
# sub_string = ""
# for i in range(len(string)):
#     if string[i:i+1] not in sub_string:
#         sub_string += string[i:i+1]
#     else:
#         if len(largest_substring) < len(sub_string):
#             largest_substring = sub_string
#             sub_string = string[i:i+1]
# else:
#     if len(largest_substring) < len(sub_string):
#             largest_substring = sub_string
# print(largest_substring)


# import uuid
# print(str(uuid.uuid4())[:10])

# import random

# print(random.randint(1000,9999))

import string

print(string.punctuation)

letters = string.ascii_letters          # a-z, A-Z
digits = string.digits                  # 0-9
symbols = string.punctuation
import random

password_chars = [
        
    ]
password_chars.extend(random.sample(letters, k=5))
password_chars.extend(random.sample(digits,k=4))
password_chars.extend(random.sample(symbols,k=1))

random.shuffle(password_chars)
# print(password_chars)

all_chars = letters + digits + symbols
print("1111--",all_chars)
remaining_length = 10 - len(password_chars)
password_chars += random.sample(all_chars, k=remaining_length)
random.shuffle(password_chars)
print(password_chars)
# a = ''.join(password_chars)

# print(a)

# print("".join(password_chars))




# def get_password():

#     letters = string.ascii_letters
#     numbers = string.digits
#     special_keywords = string.punctuation
#     password_chars = []
#     password_chars.append(random.sample(letters,k=4))
#     password_chars.append(random.sample(numbers,k=4))
#     password_chars.append(random.sample(special_keywords,k=2))
#     random.shuffle(password_chars)
#     password = "".join(password_chars)
#     return password

# print(get_password)