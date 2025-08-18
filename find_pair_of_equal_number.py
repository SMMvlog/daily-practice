# from collections import Counter
arr = [3,2,1,2,3]
# # print(Counter(lst))
# pair_ele = []
# for i in lst:
#     if i not in pair_ele and lst.count(i) == 2:
#         pair_ele.append(i)
        
# # print(pair_ele)

# print(lst.index(3,0+1))
# print(abs(sum(arr)-max(arr)), abs(sum(arr)-min(arr)))

# s = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJkltadsassd"
# print(s[:-2])
s = "abba"
a = True
t = []
count = 0
while a:
    count += 1
    for i in s:
        if i not in t:
           t.append(i)
    else:
        if count == len(s):
          break  
print(t) 