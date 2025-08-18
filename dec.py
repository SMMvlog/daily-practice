def my_decorator(n):
    def decor(func):
        def wrapper(*args,**kwargs):
            if n not in [4,5]:
                return "You don't have permission to access page"
            res = func()
            return res
        return wrapper
    return decor

@my_decorator(4)
def abc():
    return "call abc function"

print(abc())