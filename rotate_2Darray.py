lst = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [[7,4,1],[8,5,2],[9,6,3]]

result = []

count = 0
while len(result) < len(lst):
    pre_result = []
    for i in lst:
        pre_result.append(i[count])
    pre_result.sort(reverse = True)
    result.append(pre_result)
    count +=1
print(result)
