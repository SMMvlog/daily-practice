# # Q:find the second largest number from the list
# num_lst = [3,8,9,10,12,0,5,3,6]

# first_larget_num = num_lst[0]
# second_largest_num = 0

# for i in num_lst:
#     if i >first_larget_num:
#         first_larget_num = i
# for j in num_lst:
#     if j > second_largest_num:
#         if j < first_larget_num:
#             second_largest_num = j
# print("first_larget_num---",first_larget_num)
# print("second_largest_num---",second_largest_num)

# lst = [i for i in range(10)]
# print({"Even":[i for i in lst if i%2==0],"Odd":[i for i in lst if i%2!=0]})

# lst = "MehBoob"
# print({i:lst.lower().count(i) for i in lst.lower()})

import string
print(string.printable)