lst = [4,5,8,10,2,20,1,30,80,15]
k = 4

def get_third_largest(lst,k):
    count = 0
    result = None
    while count < k:
        pre_sult = 0
        for i in lst:
            if not result and i > pre_sult:
                pre_sult = i
            elif result and i < result and i > pre_sult:
                pre_sult = i
        result = pre_sult
        count +=1
    return result
print(get_third_largest(lst,k))