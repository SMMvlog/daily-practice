# class A:
#     def show(self):
#         super().__init__()
#         print("A")

# class B(A):
#     def show(self):
#         super().show()
#         print("B")

# class C(A):
#     def show(self):
#         super().show()
#         print("C")

# class D(B, C):
#     def show(self):
#         super().show()
#         print("D")


# d = D()
# d.show()
# print(D.__mro__)  

# print([4,5,{"g":3},(3,"r"),{4,5,}])
# a = {0:5,1:8,"r":10}
# k = hash("r")
# print({5,6,{"a":10}})
# print(type((10)))

s = "abcdefgh"

# result = ""
# # print(s[-len(s)])
# for i in range(-1,-(len(s)+1),-1):
#     print(s[i])

# for i in range(50,-1,-1):
#     print(i)

for i in s[::-2]:
    print(i)