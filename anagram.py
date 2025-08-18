# a = "xbxb"
# print(a[::-1])
# import random

# import string 
# print(random.sample(string.ascii_lowercase,k=5))
# print(string.ascii_lowercase)
# print(string.ascii_uppercase)

def is_anagram(str1, str2):
    # Remove spaces and convert to lowercase for fair comparison
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()

    # Check if sorted characters are the same
    return sorted(str1) == sorted(str2)


# 🔎 Test the function
s1 = "xbxb"
s2 = "bbxx"
# a = "xbxb"
# b ="bbxx"

if is_anagram(s1, s2):
    print(f'"{s1}" and "{s2}" are anagrams.')
else:
    print(f'"{s1}" and "{s2}" are NOT anagrams.')

