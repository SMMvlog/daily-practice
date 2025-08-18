from itertools import combinations
nums = [1,3,-1,-3,5,3,6,7]
k = 3
result = []

# for i,j,k in combinations(nums,3):
#     print(f"{i}=={j}==={k}")

# print(nums[:k])
# Output: [3,3,5,5,6,7]
# final_el = 0
# l = 0
# for i in range(len(nums)):
#     slice_list = nums[l:k]
#     if len(slice_list) < 3:
#         break
#     for j in slice_list:
#         max_elment = slice_list[0]
#         if max_elment < j and final_el < j:
#             final_el = j
#     if final_el:
#         result.append(final_el)
#     else:
#         result.append(max_elment)
#     l +=1
#     k +=1
# print(result)

# print(int(4.7))

lst = [4,6,8,9,10]
target = 19

count_dct = {}
result = []
for index,value in enumerate(lst):
    sub = target - value
    if sub in count_dct:
        print(count_dct[sub])
        result.append(count_dct[sub])
        result.append(index)
    else:
        count_dct[value] = index
print(result)