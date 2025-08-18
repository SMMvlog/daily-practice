# Find the count of each fruit below

# lst = ['apple', 'mango', ['apple', 'mango', 'banana', ['orange', 'grapes', ['apple', 'grapes']]]]

# result_dict = {}

# count = 0

# while count < len(lst):
#     if isinstance(lst[count],list):
#         lst.extend(lst[count])
#         lst.pop(count)
#     else:
#         result_dict[lst[count]] = result_dict.get(lst[count],0)+1
#         count +=1
# print(result_dict)

# if isinstance(lst[2],list):
#     print("before--",lst)
#     lst.extend(lst[2])
#     print("after--",lst)
# else:
#     print("else--")

lst = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
# def add_sub_list(lst,i,j):
#     if i>=len(lst):
#         return []
#     return [sum(lst[i:i+j])] + add_sub_list(lst,i+j,j)
# print(add_sub_list(lst,0,3))
result = []
for i in range(0,len(lst),3):
      print(i)
      result.append(sum(lst[i:i+3]))

print(result)



# for i in lst:
#     if isinstance(i,list):
#         lst.extend(i)
#     else:
#         result_dict[i] = result_dict.get(i,0)+1
#         lst.pop(lst.index(i))

# def get_count(lst):
#     for i in lst:
#         if isinstance(i,list):
#             get_count(i)
#         else:
#             result_dict[i] =result_dict.get(i,0)+1
# get_count(lst)
# print(result_dict)


