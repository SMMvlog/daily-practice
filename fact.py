
# def get_factorial(n):
#     if n==1:
#         return 1
#     return n* get_factorial(n-1)

# print(get_factorial(5))

a = "acab"

longest_string = ""
substring = ""

for i in a:
    if i not in substring:
        substring +=i
    else:
        if len(substring) >= len(longest_string):
            longest_string = substring
        substring = i
else:
    if len(substring) >= len(longest_string):
        longest_string = substring
print(longest_string)