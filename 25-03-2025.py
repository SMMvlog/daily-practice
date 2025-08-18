# def func(x, lst=[]):
#     lst.append(x)
#     return lst

# print(func(1))  
# print(func(2))  
# print(func(3))  

# class A:
#     def __init__(self):
#         self.var = 10

# obj1 = A()
# obj2 = obj1
# obj1.var = 20
# print(obj2.var)


# for i in range(2,10):
#     print(i)


input_list  = [(1,3),(5,9),(10,11), (13,16), (17,20)]
 
new_interval = (7,12)
result = []
for i in input_list:
    if i[0] <= new_interval[1] and i[1] >= new_interval[0]:
        result.append(i)
print(result)

# Input list and new interval
# input_list = [(1, 3), (5, 9), (10, 11), (13, 16), (17, 20)]
# new_interval = (7, 12)

# Overlapping logic
# overlapping = [
#     interval for interval in input_list 
#     if interval[0] <= new_interval[1] and interval[1] >= new_interval[0]
# ]

# print("Overlapping intervals:", overlapping)
