# lst = [1, [2, [3, 4], 5]]
# # output = [1, 2, 3, 4, 5]

# def flatten(lst):
#     result = []

#     for i in lst:
#         if isinstance(i, list):
#             result.extend(flatten(i))
#         else:
#             result.append(i)

#     return result

# # lst = [1, [2, [3, 4], 5]]
# print(flatten(lst))



def get_factorial(n):
    if n==1:
        return 1
    
    return n*get_factorial(n-1)

print(get_factorial(5))






lst = [1, [2, [3, 4], 5]]

# def flat_lst(lst):
#     try:
#         result = []
#         for i in lst:
#             if isinstance(i,list):
#                 lst.extend(flat_lst(i))
#             else:
#                 result.append(i)
#         return result
#     except Exception as ex:
#         print("ex---",ex)
# print(flat_lst(lst))

def flatten(lst):
    result = []

    for i in lst:
        if isinstance(i, list):
            result.extend(flatten(i))
        else:
            result.append(i)

    return result

# lst = [1, [2, [3, 4], 5]]
print(flatten(lst))


# def decor(param):
#     def my_decorator(func):
#         def wrapper(*args,**kwargs):
#             call_func = func(*args,**kwargs)
#             if call_func.ex and param:
#                 call_func = func()
#                 param -=1
#             return call_func
            
#         return wrapper
        
#     return decor
# @decor(param=2)
# def abc():
#     print("abc")
#     a=b%3
#     return a
    
# print(abc())



# a = [[1,2]]
# b =  [[1,2]]
# print(a == b)
 
# a = [[1]]
# b = a[:]
# a.append(2)
# # print(a)
# print(b)
# a = [[1],2]
# b = [[1]]
 
# a= [[1]]
# b = a[:]
# a[0].append(2)
 
# a = [[1,2]]
# b =  [[1]]
 
 
# def append_to_list(val, my_list=[]):

#     my_list.append(val)

#     return my_list
 
# print(append_to_list(1))

# print(append_to_list(2))
 
# [1]
# [2]
 
# def create_multipliers():

#     return [lambda x: i * x for i in range(5)]
 
# for multiplier in create_multipliers():

#     print(multiplier(2), end=" ")
 
# [0,2,4,6,8]
 
# [1, [2, [3, 4], 5]]
 
# 1, 2, 3, 4, 5
 
# [1, 2, 3, 4, 5]



# def decor(param):
#     def my_decorator(func):
#         def wrapper(*args, **kwargs):
#             # nonlocal param

#             while param > 0:
#                 try:
#                     return func(*args, **kwargs)
#                 except Exception as ex:
#                     print(ex)
#                     param -= 1

#             return None

#         return wrapper

#     return my_decorator


# @decor(param=2)
# def abc():
#     print("abc")
#     a = b % 3
#     return a


# print(abc())
 

                    


