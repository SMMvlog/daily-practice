Input = "Hello World Python"

# Output = "Python World Hello"

a = Input.split()
b = a[::-1]
print(" ".join(a[::-1]))
# print(Input[::-1])

# Input= [1, 2, 4, 5, 6]

# Output = []

# a = 0
# for i in Input:
#    a +=1
#    if i!=a:
#       Output.append(a)
#       a+=1

# print(Output)




# Input= [1, 2, 3, 4, 2, 5, 3]
# # Output= [2, 3]

# output = []
# a = []

# for i in Input:
#     if i not in a:
#         a.append(i)
#     else:
#         output.append(i)

# print(output)
# Input= [1, 2, 3, 4, 2, 5, 3]
# # Output= [2, 3]

# output = []
# a = []

# for i in Input:
#     if i not in a:
#         a.append(i)
#     else:
#         output.append(i)

# print(output)



# Input: nums = [2, 7, 11, 15], target = 9
# Output: [0, 1] 


def two_sum(nums, target):
    num_map = {}  # Dictionary to store numbers and their indices
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_map:
            return [num_map[complement], i]  # Return indices of the two numbers
        num_map[num] = i  # Store current number's index
    return []  # Return empty if no pair found

# Example Usage
nums = [15, 7, 11, 2]
target = 9
print(two_sum(nums, target))  # Output: [0, 1]

# a,b=[1, 3, 5], [2, 4, 6]
# c = a+b

a = "werewrdsewrew"
print(sum(1 for i in a if i in "aioue"))

from collections import Counter


result = {}
for i in a:
    if i in result:
        result[i] +=1
    else:
       result[i] =+1

print(result)

# script1.py
# print(__name__)

if __name__ == "__main__":
    nums = [15, 7, 11, 2]
    target = 9
    a = two_sum(nums, target)
    print(a)