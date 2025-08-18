nums = [2, 8, 11, 15,7,4]
target = 9


dct = {}
result = []
for i,v in enumerate(nums):
   subtract = target - v
   if subtract in dct:
       result.append(dct[subtract])
       result.append(i)
       break
   else:
       dct[v] = i
   
print(result)


# result = []
# for i in range(len(nums)):
#     for j in range(i+1,len(nums)):
#         if nums[i] + nums[j] == target:
#             result.append(nums.index(nums[i]))
#             result.append(nums.index(nums[j]))
#             break


# print(result)

# if isinstance(nums,tuple):
#     print("Yes")

# else:
#     print("No")