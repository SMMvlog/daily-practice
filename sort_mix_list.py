lst = [9,'$',4,3,'.',5]
# output= [3,'$',4,5,'.',9]

for i in range(len(lst)):
    if type(lst[i]) !=int:
        continue
    min_index = i
    for j in range(i+1,len(lst)):
        if type(lst[j]) !=int:
                continue
        if lst[j]<lst[min_index]:
            min_index = j
    lst[i],lst[min_index] = lst[min_index],lst[i]
print(lst)