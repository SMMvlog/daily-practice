lst  = [(1,3),(5,9),(10,11), (13,16), (17,20)]
new_interval = (7,12)

# lst  = [(1,3),(5,12) (13,16), (17,20)]

# result = []

# for interval in lst:
#       if interval[-1]< new_interval[0]:
#         result.append(interval)
#       elif interval[0] > new_interval[1]:
#           result.append(new_interval)
#           new_interval = interval
#       else:
#          new_interval = (min(interval[0],new_interval[0]),max(interval[1],new_interval[1]))
# result.append(new_interval)
# print(result)






# # for i in lst:
# #    if new_interval[0] < i[1] and new_interval[1] > i[0]:
# #       result.append(i)

# # print(result)    





arr1 = [1, 3, 5, 7]
arr2 = [2, 4, 6, 8]

result = []
i = 0
j = 0

while i<len(arr1) and j<len(arr2):
  if arr1[i] < arr2[j]:
    result.append(arr1[i])
    i +=1
  else:
    result.append(arr2[j])
    j +=1
result.extend(arr1[i:])
result.extend(arr2[j:])

print(result)