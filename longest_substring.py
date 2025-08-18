# Input = "sdasddeswdgt"

# substring = ""

# subs_lst = []

# for i in Input:
#     if i not in substring:
#         substring += i
#     else:
#         subs_lst.append(substring)
#         substring = i
# # result = max(subs_lst,key=len)
# # print(f"result--{result}:{len(result)}")
# final_result = ""

# for substring in subs_lst:
#     if len(substring) > len(final_result):
#         final_result = substring

# print(final_result)

# Input = [10,11,12,13,15]
# # Output: 2
# missing_num = None
# print(len(Input))
# for i in range(min(Input),len(Input)+min(Input)):
#     if i not in Input:
#         missing_num = i
# print(missing_num)

# input = [3, 2, 1, 5, 6, 4]
# second_largest = 0
# first_largest = input[0]

# for i in input:
#     if i < first_largest and i > second_largest:
#         second_largest = i
#     elif i > first_largest:
#         first_largest = i
    

# print(second_largest)


# dict1 = {"name":"Mehboob"}
# dict2 = {"surname":"Shaikh"}
# # dict1.update(dict2)

# print({**dict1,**dict2})

# s = "My name is Mehboob Shaikh, I live in Mumbai and I have doen Bsc Computer scince from mumbai University"
# lst = list(set(s.upper()))
# result = {}
# for i in lst:
#     if i and i not in result:
#         result[i] = 1
# print(result)

arr = [1, 2, 3, 4, 5, 4, 3, 2, 1, 3, 4]
print(max(arr))

def migratoryBirds(arr):
    # Write your code here
    
    dict_count = {}
    for i in arr:
        if i not in dict_count:
           dict_count[i]=arr.count(i)
    print(dict_count)
    result = max(dict_count,key=dict_count.get)
    return result
print(migratoryBirds(arr))


# lst = ["Mehboob","Shaikh"]
# print(max(lst,key=len))

# my_dict = {'banana': 5, 'ora': 15, 'pineapple': 15,'apple': 10}
# # print(my_dict.items())

# # sorted_by_keys = dict(sorted(my_dict.items(), key=lambda item: item[1],reverse=True))

# # print(sorted_by_keys)

# lst = ["pineapple","banana","apple","mang"]
# print(sorted(lst))

# print(dict(sorted(my_dict.items(),key= lambda item:item[1])))

a = "babad"

def is_palindrom(s):
    if s and len(s) >1:
        return s==s[::-1]
    return False
max_len = ""
for i in range(len(a)):
    for j in range(i+1,len(a)+1):
        sub = a[i:j]
        if is_palindrom(sub):
            if max_len and len(max_len) <= len(sub):
                max_len = sub
            else:
                max_len = sub

print(max_len)
