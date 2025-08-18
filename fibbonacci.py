# s = abcddwerd

# dct = {}
# for I in s:
#    if I in dct:
#        dct[i] +=1
#    else:
#       dct[i] =1
# print(dct)

# 10k  1 1
# 20k  2 2
# 20k  2 2
# 30k  4 
# 3

# lst = [0,1,1,2,3,5,8]

# a b = 0,1
# for I in range(5)
#    if I in [0,1]
#       result.append(I)
#    else:
#      fib = a+b
#      result.append(fib)
#      a,b = b,fib	
# result = []
# for I in range(len(lst)):
#     result.append(lst[i] + lst[i+1])


# product_id product_name price category
# 203        chair         150  furniture
# 204        desk          300    furniture
# 205        monitor       250    furniture 


# update product set price =  where 

# emp_id, emp_name, salary, dept_id

# select MAX(salary) from employee group by dept_id;

# emp_id, emp_name, salary, manager_id


# select emp_name, salary from employee where salary > (select salary from employee group by manager_id);



# select e.emp_name, e2.salary from employee e join employee e2 ON e.manager_id = e2_manger_id where e.salary > e2.salary;


lst = [1,1,2,2,2,3,4,5]
result = list(set(lst))

result = []

for I in lst:
   if I not in result:
        result.append(I)

















a,b=0,1

for i in range(10):
    if i in [0,1]:
        print(i)
    else:
        fib = a+b
        print(fib)
        a,b =b,fib
