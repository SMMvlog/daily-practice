# def minimumAbsoluteDifference(arr):
#     arr.sort()
#     s = 0
#     min_abs_lsit = []
#     for i in arr:
#         if i == arr[-1]:
#             return min_abs_lsit
        
#         for j in range(s,len(arr)-1):
#             min_abs_lsit.append(abs(i-arr[j+1]))
#         s +=1


# a = [1,3,4,5,6,7,8,9,10,11,12,13,14,4,1,6]
# for i in a:
#     if postion(i)== a[-1]:
#         break
#     i = i + 1



import copy

# Original list with nested list
original = [{1, 2, 3}, 4, 5]

# Creating a shallow copy
shallow_copy = copy.deepcopy(original)

# Modifying the nested list
shallow_copy[0].update([100])
# shallow_copy[1] = 100

print("Original:", original)       # [[99, 2, 3], 4, 5]
print("Shallow Copy:", shallow_copy) # [[99, 2, 3], 4, 5]
# print("Shallow Copy:", shallow_copy[1])



# import copy

# # Original list with nested list
# original = [[1, 2, 3], 4, 5]

# # Creating a deep copy
# deep_copy = copy.deepcopy(original)

# # Modifying the nested list
# deep_copy[0][0] = 99
# deep_copy[1] = 50

# print("Original:", original)   # [[1, 2, 3], 4, 5]
# print("Deep Copy:", deep_copy) # [[99, 2, 3], 4, 5]

a = {1,3,5,6,{"name":"Mehboob","add":"Mumbra"}}
# a[4][0] = 4
print(a)

