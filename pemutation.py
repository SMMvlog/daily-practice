# from itertools import combinations,permutations
# lst = [1,1,2]
# result = []
# # for i ,j in combinations(lst,2):
# #     result.append((i,j))

# # print(result)
# # pre_result = []
# # for i in range(len(lst)):
# #     for j in range(i+1,len(lst)):
# #         pre_result.append(lst[])

# # print(result)
# # result = [list(p) for p in permutations(lst)]
# for p in permutations(lst):
#     if list(p) not in result:
#       result.append(list(p))

# print(result)



# def my_decorator(func):
#     def wrapper(*args,**kwargs):
#         try:
#             b = args[1]
#             if b <1:
#                 return "The divisional number is less than 1"
#             res = func(*args,**kwargs)
#         except Exception as ex:
#             return ex
#         return res
#     return wrapper
# @my_decorator
# def abc(a,b):
#     return a/b
# print(abc(5,0))


# result = []
# for i in range(2,100):
#     for j in range(2,i):
#         if i%j ==0:
#             break
#     else:
#       result.append(i)
# print(result)

# factorial of 10

# def get_factorial(n):
#     if n==1:
#         return 1
#     return n * get_factorial(n-1)

# print(get_factorial(5))

# print fibonacci from 1 to 10
result = []
# def get_fibonacci(n):
#     a,b = 0,1
#     for i in range(n):
#         if i in [0,1]:
#             result.append(i)
#         else:
#             fib = a+b
#             result.append(fib)
#             a,b = b,fib
#     return result
# def get_fibonacci(n):
#     a,b = 0,1
#     for i in range(n):
#         if i in [0,1]:
#             yield i
#         else:
#             fib = a+b
#             yield fib
#             a,b = b,fib

# fib = get_fibonacci(10)

# print(next(fib))
# print(next(fib))
# print(next(fib))
# print(next(fib))
# print(next(fib))
# print(next(fib))

# lst = ["eat","tea","tan","ate","nat","bat"]

# Output = [["bat"],["nat","tan"],["ate","eat","tea"]]

# result = {}
# for i in lst:
#     key= "".join(sorted(i))
#     if key in result:   
#       result[key].append(i)
#     else:
#        result[key] = [i]
# print(result.keys())


nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

# max_sum = nums[0]

# for current in nums[1:]:
#     curr = max(max_sum,current+max_sum)
#     max_sum = curr

print("python"[::-3])
    
