# 1. Two Sum
# Difficulty: Easy
# Problem: Return indices of two numbers from the list that add up to a target.

# nums = [2, 10, 11,7 ,15]
# target = 9

# result = []

# result_dict = {}
# second solution
# for i in nums:
#     result_dict[i] = nums.index(i)
#     if target-i in result_dict:
#         result.append(nums.index(target-i))
#         result.append(nums.index(i))
# print(result)


# first solution
# for i in range(len(nums)):
#     for j in range(i+1,len(nums)):
#         if nums[i] + nums[j] == target:
#             result.append(i)
#             result.append(j)
# print(result)


# 2. Anagram Checker
# Difficulty: Easy
# Problem: Check if two strings are anagrams of each other.

# s1 = "listen"
# s2 = "silent"

# if sorted(s1) == sorted(s2):
#     print("It's Anagram")
# else:
#     print("its not Anagram")


# 3. Find the Missing Number
# Difficulty: Easy
# Problem: Find the missing number from a list of n elements from 1 to n+1.

# nums = [1, 2, 4, 5]
# # solution
# for i in range(len(nums)-1):
#     if nums[i+1] - nums[i] >1:
#         print(nums[i]+1) 



# 4. Count Pairs with Given Sum
# Difficulty: Medium
# Problem: Count all pairs in a list that sum up to a target value.

# arr = [1, 5, 7, -1]
# target = 6

# result = []
# # solution
# for i in range(len(arr)):
#     for j in range(i+1,len(arr)):
#         if arr[i] +arr[j] == target:
#             result.append((arr[i],arr[j]))
# print(result)

# 5. Longest Substring Without Repeating Characters
# Difficulty: Medium
# Problem: Find the length of the longest substring without repeating characters.

# s = "abcabcbb"

# substring = ""
# longest_substring = ""
# # solution
# for i in s:
#     if i not in substring:
#         substring +=i
#     else:
#         if len(substring) >= len(longest_substring):
#             longest_substring = substring
#         substring = i
# else:
#     if len(substring) >= len(longest_substring):
#             longest_substring = substring
# print(longest_substring)

# 6. Merge Intervals
# Difficulty: Medium
# Problem: Merge overlapping intervals.

# intervals = [[1,3],[2,6],[8,10],[15,18]]
# result = []
# skip = False
# # solution
# for i in range(len(intervals)):
#     try:
#         if skip:
#             skip = False
#             continue
#         elif intervals[i][1] > intervals[i+1][0]:
#             skip = True
#             result.append((intervals[i][0],intervals[i+1][1]))
#         else:
#             result.append(tuple(intervals[i]))
#     except Exception as ex:
#         result.append(tuple(intervals[i]))
# print(result)



# 7. Group Anagrams
# Difficulty: Medium
# Problem: Group all anagrams from a list of words.

# words = ["eat", "tea", "tan", "ate", "nat", "bat"]

# # solution

# # result_dict = {}
# for i in words:
#     if "".join(sorted(i)) in result_dict:
#         result_dict["".join(sorted(i))].append(i)
#     else:
#         result_dict["".join(sorted(i))] = [i]

# print([values for values in result_dict.values()])




# teams = ["RCB", "CSK", "MI", "PBKS"]

# from itertools import combinations

# for t1,t2 in combinations(teams,2):
#     print(f"{t1} vs {t2}")


# 6. Merge Intervals
# Difficulty: Medium
# Problem: Merge overlapping intervals.

# intervals = [[1,3],[2,6],[8,10],[15,18]]

# result = []

# for i in intervals:
#     if not result or result[-1][1]<i[0]:
#         result.append(i)
#     else:
#         result[-1][1] = i[1]
# print(f"result: {result}")

# print(bool(["a"]))
# print(0.1 + 0.3 == 0.4)

# a = "Erwerew"
# print(a[0].lower()=="e")

# for i in range(17, -1,-2):
#     print(i)


# def pageCount(n, p):
#     # Write your code here
#     page_flip = 0
#     if p == 1 or n==p or n%2 !=0 and n-p == 1:
#         return 0
#     elif  p <= n//2:
#         print(1111)
#         page_flip +=1
#         for i in range(2,n//2,2):
#             if p in [i,i+1]:
#                 break
#             page_flip +=1
#     elif n%2 ==0:
#         print(222222222)
#         page_flip +=1
#         for i in range(n-1,n//2,-2):
#             if p in [i,i-1]:
#                 break
#             page_flip +=1
#     else:
#         print(3333333)
#         for i in range(n,n//2,-2):
#             print("iiiiiii---",i)
#             if p in [i,i-1]:
#                 break
#             page_flip +=1
#     return page_flip

# print(pageCount(37455,29835))

# result should be 3810


# def pageCount(n, p):
#     return min(p // 2, (n // 2) - (p // 2))

# # Example
# print(pageCount(37455, 29835))  # ✅ Output: 3810
# print(max("banana", "apple", "cherry",key=len))


# class A:
#     def __init__(self):
#         # super().__init__()
#         print("class A")
# class B(A):
#     def __init__(self):
#         super().__init__()
#         print("class B")
# class C(B):
#     def __init__(self):
#         super().__init__()
#         print("class C")

# c = C()
# print(c)


# a = ["a","b","c","d"]

# my_iter = iter(a)
# print(next(my_iter))
# print(next(my_iter))


def genrator(n):
    for i in range(n):
        yield i
my_generator = genrator(10)

print(id(next(my_generator)))
print(id(next(my_generator)))
print(id(next(my_generator)))