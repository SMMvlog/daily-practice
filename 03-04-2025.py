# lst = [4,8,9,10,3,12,7]

# # target = 11

# # result_dict = {}

# # def add_target(l):
# #     for index,value in enumerate(lst):
# #         subtrac = target - value
# #         if subtrac in result_dict:
# #             result = {subtrac:result_dict[subtrac],value:index}
# #             return result
# #         result_dict[value] = index
# # print(add_target(lst))

# largset_num = 0
# second_largest_num = 0
# for i in lst:
#     if i > largset_num:
#       largset_num = i
#     if i > second_largest_num and i < largset_num:
#        second_largest_num = i
# print(largset_num)
# print(second_largest_num)
# # print(lst*3)


# l1 = [1,2,3,4,5,6,7,8,9,10]
# # output: [1,9,25,49,81]

# result = [i*i for i in l1 if i%2!=0]

# print(result)


# for i in range(101):
#    if i!=0 and i%i==0 and i%2!=0:
#       print(i)


# str = "abbcccddddeeeee"
# # output: 1a2b3c4d5e


# def count_word(str):
#     count_dct = {}
#     result = ""
#     for i in str:
#        count_dct[i] = count_dct.get(i,0)+1
#     for k,v in count_dct.items():
#         result +=f"{v}{k}"
#     return result

# print(count_word(str))

for i in range(2,101):
    for j in range(2,i):
        if i%j==0:
            break
    else:
        print(f"prime number: {i}")
      



# lst = [4,8,9,10,3,12,7]

# target = 11

result = [0,6]

