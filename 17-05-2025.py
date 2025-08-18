s = [1, 2, 1, 3, 2]
# d = 4
# m = 2
# def birthday(s, d, m):
#     result = []
#     i = 0
#     # while i<=len(s)-1:
#     for i in s:
#         if sum(s[i:m+i])==d:
#             result.append(s[i:m+i])
#         i +=1
#     return result

# print(birthday(s,d,m))
# s.append(10,19)
# print(10%5)

# ar = [1,2,3,4,5,6]
# n = 6
# k = 5
# def divisibleSumPairs(n, k, ar):
#     # Write your code here
    
#     result = []
#     for i in range(n):
#         for j in range(i+1,n):
#             if ar[i]<ar[j] and (ar[i]+ar[j])%k==0:
#                 result.append([ar[i],ar[j]])
#     return result

# print(divisibleSumPairs(n,k,ar))  

a = [1, 4, 4, 4, 5, 3,1,1,0,0,0,0]
# print(a.count(i for i in a))

from collections import Counter
count_elemnt = Counter(a)


# counts = Counter(a)
# max_freq = max(counts.values())

# most_common_ids = [bird_id for bird_id, freq in counts.items() if freq == max_freq]
# return min(most_common_ids)
# print(max(count_elemnt,key=count_elemnt.get))
# result = count_elemnt.most_common()[0]
# for i in count_elemnt.most_common():
#     if 0 in i and i[1] == count_elemnt.most_common()[0][1]:
#         result = i[0]
#     else:
#         result
# print(result)

# k = "We promptly judged antique ivory buckles for the next prize"

# s2 = set(k.lower())
# s2.discard(" ")
# # s3 = "".join(s2)
# print(sorted(s2))
result_dict = {}
lst = [3,6,8,9,7,20]
target_num = 15
for index,v in enumerate(lst):
        if v not in result_dict:
            result_dict[v]=index
        subtract_num = target_num - v
        print(index)
        print(subtract_num)
        if subtract_num in result_dict:
            print([result_dict[subtract_num],index])



            # print(func('abc')) # ['abc', 'bac',cab']


# def func(s):
#     result = []
#     result.append(s)
#     result.append(s[::-1])
#     if s and len(s) <3:
#         reurn result
#     dct = {}
#     for i in s:
#         if i not in dct:
#             dct[i] = [i]
#         else:
#             dct[i]


# s = "abc"
# result = ["abc","bac","cab","bca"]


# def add_item(item, my_list=[]):
#     my_list.append(item)
#     return my_list
# print(add_item(1))
# print(add_item(2))




# Input: height = [1,8,6,2,5,4,8,3,7]
# Output: 49Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

s = "aa"

def get_max_sub_str(s):
    sub_string = ""
    max_sub_string = ""
    if not s:
        return False
    if len(s) <2:
        return s
    for i in s:
        if i not in sub_string:
            sub_string +=i
        else:
            if len(sub_string) > len(max_sub_string):
                max_sub_string = sub_string
                sub_string = ""
            else:
                sub_string = ""
    else:
        if len(sub_string) > len(max_sub_string):
                max_sub_string = sub_string
    return max_sub_string
    
print(get_max_sub_str(s))
        
            

