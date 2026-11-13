# a = "xbxb"
# print(a[::-1])
# import random

# import string 
# print(random.sample(string.ascii_lowercase,k=5))
# print(string.ascii_lowercase)
# print(string.punctuation)
# print(string.ascii_uppercase)

# def is_anagram(str1, str2):
#     # Remove spaces and convert to lowercase for fair comparison
#     str1 = str1.replace(" ", "").lower()
#     str2 = str2.replace(" ", "").lower()

#     # Check if sorted characters are the same
#     return sorted(str1) == sorted(str2)


# 🔎 Test the function
# s1 = "xbxb"
# s2 = "bbxx"
# # a = "xbxb"
# # b ="bbxx"

# if is_anagram(s1, s2):
#     print(f'"{s1}" and "{s2}" are anagrams.')
# else:
#     print(f'"{s1}" and "{s2}" are NOT anagrams.')

raw_json = [ {"id": 1, "name": "Amol@Ugale!!", "city": "Mum#bai$$"}, {"id": 2, "name": "Jo%hn^Doe", "city": "New*York"}, {"id": 3, "name": "An@na 123", "city": "Bang@lore!!!"} ]


# Amol Ugale

# id name city 0 1 AmolUgale Mumbai 1 2 JohnDoe NewYork 2 3 Anna 123 Banglore

# a = "tytry#vfdg$rtrt"
# b =a.split("#",1)
# print(b)
import string
print(string.ascii_letters)

def format_name(data):
    str1 = string.ascii_letters
    for dct in data:
        name = ""
        if dct.get("name"):
            for i in dct.get("name"):
                if i in str1:
                    name +=i
            dct["name"] =name
        city = ""
        if dct.get("city"):
            for i in dct.get("city"):
                if i in str1:
                    city +=i
            dct["city"] =city
    return data

print(format_name(raw_json))
