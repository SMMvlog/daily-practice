string = "asddrfggthjnngbs"
# print(string[10:11])

# def get_longest_sub_string(string):
#     longest_subtring = ""
#     for i in range(len(string)):
#         for j in range(i+1,len(string)):
#             sub_string = string[i:j]
#             if len(sub_string) != len(set(sub_string)):
#                 sub_string = string[i:j-1]
#                 longest_subtring = sub_string
#             if len(longest_subtring) < len (sub_string):
                
#                 sub_string = ""
#     return longest_subtring
# print(get_longest_sub_string(string))

# print(set(""))

# def get_longest_sub_string(string):
#     longest_subtring = ""
#     index = 0
#     k = False
#     for i in range(len(string)):
#         substring = string[index:i+1]
#         if len(substring) != len(set(substring)):
#             substring = string[index:i-1]
#             k = True
#         if len(longest_subtring) < len(substring):
#             longest_subtring = substring
#             k = True
#         if k:
#             index = i
#             substring = string[index:i+1]
#             k = False
#     return longest_subtring
# print(get_longest_sub_string(string))


string = "asddrfggthjnngbsaklmyy"
longest_sub_string = ""
sub_string = ""
for i in string:
    if i not in sub_string:
        sub_string +=i
    elif len(longest_sub_string) < len(sub_string):
        longest_sub_string = sub_string
        sub_string = i
    else:
        sub_string = i
else:
    if len(longest_sub_string) < len(sub_string):
        longest_sub_string = sub_string
print(longest_sub_string)