# def my_decorator(n):
#     def decor(func):
#         def wrapper(*args,**kwargs):
#             if n not in [4,5]:
#                 return "You don't have permission to access page"
#             res = func()
#             return res
#         return wrapper
#     return decor

# @my_decorator(4)
# def abc():
#     return "call abc function"

# print(abc())


# def decor(param):
#     def my_decorator(func):
#         def wrapper(*args,**kwargs):
#             count = 1
#             while count <=param:
#                 try:
#                     return func(*args,**kwargs)
#                 except Exception as ex:
#                     print("eeeeeeeeeeee")
#                     print(f"try {count}--",ex)
#                     count +=1
#             raise Exception("Maximum retries Exceeded")
        
#         return wrapper
#     return my_decorator

# @decor(3)
# def abc():
#     result = "7"/5
#     return result
# print(abc())








# def decor(retries):
def my_decorator(func):
    retries = 3
    def wrapper(*args, **kwargs):
        nonlocal retries
        count = 0

        while retries:
            try:
                return func(*args, **kwargs)

            except Exception as ex:
                retries -= 1
                print(f"Retry {count}: {ex}")
        else:
            raise Exception("Maximum retries exceeded")

    return wrapper

    # return my_decorator


@my_decorator
def abc():
    return "b" / 5


print(abc())

# def numb(k,n=5):
#     n = k+n
#     return n

# print(numb(2))
# print(numb(4))
# def append_numb(k,v,n={}):
#     n[k]=v
#     return n

# print(append_numb("two",2))
# print(append_numb("four",4))

# from time import time
# def my_decorator(func):
#     def my_wrapper(*args):
#         start = time()
#         b = args[1]
#         if b%2!=0:
#             b=b*b
#         print(b)
#         end = time()
#         print(f"Excetion time {end-start}")
#         return func(args[0],b)
#     return my_wrapper
# @my_decorator
# def abc(a,b):
#     print("abc--",b)
#     return True

# print(abc(2,3))
