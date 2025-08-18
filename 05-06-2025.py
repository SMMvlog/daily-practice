s = "dvdf"
# s = "abcabcbb"
# s = "bbbbb"
s = "pwwkew"
output = "d","v","f","dv","df","vdf"

result = []
for i in range(1,len(s)+1):
    if list(set(s[:i])) not in result:
        result.append(list(set(s[:i])))


# print(result)
# print(len(max(result,key=len)))

print(type(len({4,6,8} & {3,12,10})))