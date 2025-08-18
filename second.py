# lst = [1,1,0,-1,-1]
# print(sum(lst)/len(lst))

# for i in range(0,5-1):
#     print("#"*(5-i)+" "*i)

import copy
li1 = [1, 2, [3, 5], 4]
li2 = copy.copy(li1)
print("li1----",id(li1))
print("li2 ID: ", id(li2), "Value: ", li2)
li3 = copy.deepcopy(li1)
print("li3 ID: ", id(li3), "Value: ", li3)
li2.append(7)
print("li2 ID: ", id(li2), "Value: ", li2)
li3.append(10)
print("li3 ID: ", id(li3), "Value: ", li3)
print("li1 ID: ", id(li1), "Value: ", li1)







    