# # nested_list = [1, [2, [3, 4], 5], 6]
# # flat_list = []
# # stack = [nested_list]  # Initialize stack with the nested list

# # while stack:
# #     current = stack.pop()  # Remove last element from stack
# #     if isinstance(current, list):
# #         stack.extend(reversed(current))  # Add elements back to stack in order
# #     else:
# #         flat_list.append(current)

# # print(flat_list)  # Output: [1, 2, 3, 4, 5, 6]

# # a =  [1,32,3]
# # b = reversed(a)
# # c = []
# # c.extend(b)
# # print(c)

# # l = ('apple', 'mango', ('apple', 'mango', 'banana', ('orange', 'grapes', ('apple', 'grapes'))))

# # result_dict = {}
# # lst = list(l)
# # for i in lst:
# #             if isinstance(i,tuple):
# #                 lst.extend(list(i)) 
# #             else:
# #                 result_dict[i] = result_dict.get(i,0) + 1
# # else:
# #        print(lst)
# # print(result_dict)


# a = {"m":2,"O":1,"k":1,"d":1,"m":2}
# # first_two = dict(list(a.items())[:2])

# # print(sorted(a))
# # print(first_two)


# # print(l.pop())
# # stack = [l]
# # final_list = []
# # while stack:
# #     current = stack.pop()
# #     if isinstance(current,tuple):
# #         stack.extend(list(current))
# #     else:
# #         final_list.append(current)

# # print(final_list)

# # fruit_dict = {}
# # for fruit in final_list:
# #     fruit_dict[fruit] = final_list.count(fruit)

# # print(fruit_dict)


# # sorted_by_key = dict(sorted(a.items()))
# # print(sorted_by_key)


# # a = {"Mehfooz":26,"Margoob":19,"Minhaz":22,"Mehboob":29}


# # lst = ["4","6","8","9","1"]
# lst = "My Name is Mehboob Shaikh"
# a=sorted(lst.lower())
# print(a)


list_1 = [9,'$',4,3,'.',5]
# output= [3,'$',4,5,'.',9]
# list_1.sort(key=lambda x:x if type(x)==int else None)
# print(list_1)

result = sorted([i for i in list_1 if type(i)==int])
for i,v in enumerate(list_1):
    if type(v) !=int:
        result.insert(i,v)
print(result)
# result = []
# while len(result)<len(list_1):
#     min = None
#     for i in list_1:
#         if i in result:
#             continue
#         elif type(i)==int:
#             if min and min<i:
#                 min = i
#             else:
#                 min = i
#     result.append(min)

# print(result)