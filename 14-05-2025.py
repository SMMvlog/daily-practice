# 1. Using Lambda Function,  remove elements from a list that is larger than a specific value
# Input:
List_Value = [12, 33, 10, 20, 25]
Given_value = 21
# # Output: [12, 10, 20]

print([x for x in List_Value if x<Given_value])

# print(list(filter(lambda x:x<=Given_value,List_Value)))



# result=list(filter(lambda x:x<=Given_value,List_Value))
# print(result)

# result = lambda lst :[i for i in lst if i < 21]
# print(result(List_Value))


# 2. Using recursive method, Concatenate N consecutive elements in String list.
test_list = ['How', 'to', 'use', 'recursive', 'method', 'in', 'Python']
test_list = ['How', 'to', 'use', 'recursive', 'method', 'in', 'Python']
n=3
# Output: ['How to use", 'recursive method in', 'Python']

def split_list(lst,n):
    if not lst:
        return []
    return [" ".join(lst[:n])] + split_list(lst[n:],n)

# the function split_list will reurn like below
["How to use"] + ['How', 'to', 'use']
["How to use"] + ['recursive', 'method', 'in']
["How to use"] + ['Python']
["How to use"] + []

# s = []
# result = []
# for i in test_list:
#         if len(s) < 3:
#             s.append(i)
#         else:
#             result.append(" ".join(s))
#             s = []
#             s.append(i)
# else:
#     if len(s) >1:
#         result.append(" ".join(s))
#     else:
#         result.append("".join(s))
# print(result)