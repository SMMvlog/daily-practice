# lst = [10,20,30,40,50]
# target = 50
# lower,higher = 0,len(lst)-1
# mid = lower+higher//2

# while lower <=higher:
#     if lst[mid] == target:
#         print("lst--mid",lst[mid])
#         break
#     elif lst[mid] < target:
#         mid +=1
#     elif lst[mid] > target:
#         mid -=1
# else:
#     print("not found")

# lst = [0,1,5,0,7,6,8,0]

# result = [i for i in lst if i!=0] + [0] * lst.count(0)
# print(result)
# print([1,2,3]*3)

a = [3,5,6,7,7,7,7,9,9,15]
target = 7

start = None
end = None

for i in range(len(a)):
    if a[i] == target:
        if not start:
            start = i
        else:
            end = i
    # print(f"start position: -1 -- end position: -1")
print(f"start position: {start} -- end position: {end}")