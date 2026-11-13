# # print("hello world")


# def deco(func):
#     def rapper(a):
#         try:
#             if a > 5:
#                 return "hellow this is greater than 5"
#             else:
#                 return a
#         except Exception as ex:
#             pass
#     return rapper

# @deco
# def abc(k):
#     return k

# print(abc(5))


# l =[0,1,5,0,7,6,8,0]
# print([i for i in l if i !=0] + [0]*l.count(0))

# print(l)
# new_list = []

# for i in l:
#     if i!= 0:
#         new_list.append(i)
        
# print(new_list)


# find count of each  fruit
# l = ['apple', 'mango', ['apple', 'mango', 'banana', ['orange', 'grapes', ['apple', 'grapes']]]]

# # serializer and modern serializer

# fruit_dict = {}
# count = 0
# for fruit in l:
#     if type(fruit) != list:    
#         fruit_dict[fruit] = count+1
#     else:
#         for sub_fruit in fruit:
#             if type(sub_fruit)!= list:
#                 fruit_dict[sub_fruit] = count+1
#             else:
#                 for sub_sub_fruit in sub_fruit:
#                     if type(sub_sub_fruit)!= list:
#                        fruit_dict[sub_sub_fruit] = count+1
#                     else:
#                         for sub_sub_sub_fruit in sub_sub_fruit:
#                             fruit_dict[sub_sub_sub_fruit] = count+1
                    
    
    
# print(fruit_dict)

# Input = [[1, 3], [2, 6], [8, 10], [15, 18]]
# # output = [1,6]
# output =[[1, 6], [8, 10], [15, 18]]


# lst1 = []
# lst = []
# for i in Input:
#     if lst1[:1]:
#         if lst1[1] > i[0]:
#             lst1[1]=i[1]
#         else:
#             lst.append(lst1)
#             lst1 = []
#             lst1.append(i[0])
#             lst1.append(i[1])

#     else:
#         lst1.append(i[0])
#         lst1.append(i[1])
# else:
#     lst.append(lst1)
# print(lst)
# l = [2]
# if len(l[:2]) == 2:
#     print("hello")
#     print(l[:2])
# else:
#     print("No")


# find count of each  fruit
l = ['apple', 'mango', ['apple', 'mango', 'banana', ['orange', 'grapes', ['apple', 'grapes']]]]


def flat_list(l):
    result = []
    for i in l:
        if isinstance(i,list):
                result.extend(flat_list(i))

        else:
            result.append(i)
    return result

print(flat_list(l))




# fruit_dict = {}
# for i in l:
#     if isinstance(i,list):
#         l.extend(i)
#     else:
#         if i in fruit_dict:
#            fruit_dict[i]+=1
#         else:
#             fruit_dict[i]=1
# print(fruit_dict)


# # l = ['apple', 'mango','apple']
# # for i in l:
# #     if i in fruit_dict:
# #        fruit_dict[i]+=1
# #     else:
# #         fruit_dict[i]=1
# # print(fruit_dict)

# s = "Mehboob"
# a=s.split("o",s[:-2])
# print(a)