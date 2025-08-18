lst  = [(1,3),(5,9),(10,11), (13,16), (17,20)]
new_interval = (7,12)

result = []
for i in lst:
   if new_interval[0] < i[1] and new_interval[1] > i[0]:
      result.append(i)

print(result)    



