

# # def factorial(n):
# #     if n == 0:
# #         return 1
# #     else:
# #         return n * factorial(n - 1)
    
# # print(factorial(6))
# # result = 1
# # for i in range(1,6+1):
# #     result *=i

# # print(result) 

# def birthday(s, d, m):
#     # Write your code here
#     count = 0
#     result = []
#     sum_of_list = []
#     for i in s:
#         count +=1
#         if i == d and count==m:
#             result.append(i)
#         elif i!=d and count!=m:
#             sum_of_list.append(i)
#         elif m==count:
#             k = sum(sum_of_list)
#             if k == d:
#                 result.append(k)
#             else:
#                 count = 0
#                 sum_of_list = []
#     return len(result)

# print("birthday-----", birthday([1,2,1,3,2], 3, 2))
      
      
      
      
# def generate_substrings(s):
#     substrings = set()
#     n = len(s)

#     for i in range(n):
#         for j in range(i + 1, n + 1):
#             substrings.add(s[i:j])

#     return sorted(substrings)

# def last_student_id(input_string):
#     substrings = generate_substrings(input_string)
#     return substrings[-1]

# input_string = "abcde"
# output = last_student_id(input_string)
# print(output)

# def last_student_id(input_string):
#     suffixes = [input_string[i:] for i in range(len(input_string))]
#     suffixes.sort()
#     return suffixes[-1]

# # Sample Input
# input_string = "abcde"
# # Output
# output = last_student_id(input_string)
# print(output)




      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      