input_data = {"a": 1,"b": {"c": 2,"d": {"e": 3}},"f": {"g": [4, 5, {"h": 6}]},"i": [7, 8]}

k = {"a": 1, "b.c": 2,"b.d.e": 3, "f.g[0]": 4,"f.g[1]": 5,"f.g[2].h": 6,"i[0]": 7,"i[1]": 8}







# def abc(data,prefix=None):
#     result = {}
#     if isinstance(data,dict):
#         for key,value in data.items():
#             new_key = f"{prefix}.{key}" if prefix else key
#             result.update(abc(value,new_key))
#     elif isinstance(data,list):
#         for index,item in enumerate(data):
#             new_key = f"{prefix}[{index}]"
#             result.update(abc(item,new_key))
#     else:
#         result[prefix] = data 

#     return result
# # print(abc(input_data))

# def fibonacci(n):
#     if n <= 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fibonacci(n - 1) + fibonacci(n - 2)
# print(fibonacci(6))


# x = (1, 2, 3)  # tuple immutable hai
# print(hash(x))  # hash value milega


# from multiprocessing import Process

# def abc():
#     for i in range(10):
#         print(i)
        
        
# def abc1():
#     for i in range(10,20):
#         print(i)
        
# p1 = Process(target=abc)
# p2 = Process(target=abc1)
        
# if __name__ == "__main__":
#     p1.start()
#     p2.start()
# from threading import Thread

# def abc():
#     for i in range(10):
#         print(i)
        
        
# def abc1():
#     for i in range(10,20):
#         print(i)
        
# p1 = Thread(target=abc)
# p2 = Thread(target=abc1)
        
# if __name__ == "__main__":
#     p1.start()
#     p2.start()


# intervals = [[1,3],[2,6],[8,10],[15,18]]
# result = []
# for i in range(len(intervals)):
#     if not result:
#         result.append(intervals[i])
#         continue
#     # print(result)
#     # print(f"{i}==={i-1}")
#     elif result[-1][1] > intervals[i][0]:
#         result[i-1][1] = intervals[i][1]
#     else:
#         result.append(intervals[i])
        # return result

import requests
import json
res = requests.get(url = "https://leetcode.com/problems/insert-interval/")
print(res.json())
        