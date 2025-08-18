lst = [1,2,3,4,5,6,7,8,9,10]

def saperate_list(lst,n):
    if not lst:
        return []
    # else:
    #    return [lst[:n]] + saperate_list(lst[n:],n)  [[10]]
    
# [[1,2,3]] + saperate_list(lst[3:],3)        [4,5,6,7,8,9,10]
# [[4,5,6]] + saperate_list(lst[3:],3)       [7,8,9,10]
# [[7,8,9]] + saperate_list(lst[3:],3)   [10]
# [[10]] + saperate_list(lst[3:],3)       []

# print(saperate_list(lst,3))

# print([[7,8,9]]+[[10]])



def add_num(n):
    if n == 1:
        return 1
    else:
        return n + add_num(n-1)
print(add_num(10))
# 10 + add_num(10-1) = 9 
# 9 + add_num(9-1) =8
# 8 + add_num(8-1) =7
# 7 + add_num(7-1) =6
# 6 + add_num(6-1) =5
# 5 + add_num(5-1) =4
# 4 + add_num(4-1) =3
# 3 + add_num(3-1) =2
# 2 + add_num(2-1) =1
# 1 + add_num(1-1) =0


# print(10+9+8+7+6+5+4+3+2+1)


