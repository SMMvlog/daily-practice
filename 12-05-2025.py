lst = [[1,3],[2,6],[8,10],[15,18]]
output = [[1,6],[8,10],[15,18]]

result = []
temp = None

for i in lst:
    if not temp:
        temp = i
    elif i[0] < temp[1]:
        temp[1] = i[1]
    else:
        result.append(temp)
        temp = i
else:
    result.append(temp)
print(result)