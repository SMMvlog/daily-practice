# iteraor

# l = [35,67,2,5,9]

# lst = iter(l)

# print(next(lst))
# print(next(lst))
# print(next(lst))
# print(next(lst))
# print(next(lst))


#genrator

# def even_num(n):
#     for i in range(n):
#         if i%2 == 0:
#             yield i

# get_even_num = even_num(50)

# print(next(get_even_num))
# print(next(get_even_num))
# print(next(get_even_num))
# print(next(get_even_num))


# import threading
# def get_even_num(n):
#     print("task-----1")
#     for i in range(n):
#         if i%2==0:
#             print (i)
        
# t1 = threading.Thread(target=get_even_num, args=(10,))
# t1.start()

# def get_odd_num(n):
#     print("task-----2")
#     for i in range(n):
#         if i%2!=0:
#             print (i)
        
# t2 = threading.Thread(target=get_odd_num, args=(10,))
# t2.start()

# a =  7 ^ 6
# carry = 7 & 6
# print(carry << 1)

def add(a, b):
    while b != 0:
        carry = a & b          # carry
        a = a ^ b              # sum without carry
        b = carry << 1         # move carry to the left
    return a

# Example
a = 7
b = 6
total = add(a, b)
print("Sum:", total)  # Output: Sum: 13
