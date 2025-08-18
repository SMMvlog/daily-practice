# l = [3,4,-1,1]
# max_el = max(l)

# for i in range(1,max_el):
#     if i not in l:
#         print(i)
#         break


def abc(*args,**kwargs):
    print([1,2,3,*[4,5,4,6]])
    return True

print(abc(4,5,6,7))
