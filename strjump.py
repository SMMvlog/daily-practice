# s = "ABCBDEEEED"
# jump = 0
# skip = ""
# for i in s:
#     if skip:
#         if i == skip:
#             jump +=1
#             skip = ""
#             continue
#         else:
#             continue
#     elif s.count(i) > 1:
#         skip = i
#         jump +=1
#     else:
#         if s.index(i) >= 1:
#             jump +=1
# print(jump)


def greet_decorator(greeting,greeting2):
    def decorator(func):
        def wrapper(name):
            print(f"{greeting}, {greeting2}, {name}!")
            func(name)
        return wrapper
    return decorator

@greet_decorator("Hello","Buy")
def say_name(name):
    print(f"My name is {name}")

say_name("Mehboob")
