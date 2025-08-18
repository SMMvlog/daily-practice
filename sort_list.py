# lst = [4,6,1,2,9,7]
# result = []
# count = 0
# while lst:
#     if count == (len(lst)-1):
#         count = 0
#     el = lst[count]
#     for j in range(len(lst)):
#         if el > lst[j] and lst[j] not in result:
#             el = lst[j]
#     result.append(el)
#     lst.remove(el)
# print(result)


# lst = [4, 6, 1, 2, 9, 7]
# result = []

# while lst:
#     smallest = lst[0]
#     for el in lst:
#         if el < smallest:
#             smallest = el
#     result.append(smallest)
#     lst.remove(smallest)


# https://leetcode.com/problems/rotate-image/description/


lst = [[1,2,3],[4,5,6],[7,8,9]]
# lst = [[7,4,1],[8,5,2],[9,6,3]]
# print(Output)
lst.reverse()
print(lst)