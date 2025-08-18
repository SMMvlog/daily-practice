
# generator example

def abc():
    for i in range(31):
        if i%2==0:
            yield i
result = abc()

print(list(result))

lst = [5,8,3,9,10]
it = iter(lst)
print(next(it))
print(next(it))
print(next(it))



class Employee:
    def __init__(self,emp_id,emp_name,dept_name="IT"):
        self.emp_id = emp_id
        self.emp_name = emp_name
        self.dept_name = dept_name
        
emp1 = Employee("0001","Mehboob")

class Department(Employee):
    def __init__(self,dep_name):
        super().__init__(self,dep_name)
        self.dep_name = dep_name
dep1 = Department("HR")

print(dep1.dep_name)


# for i in range(30):
#     if i%2 == 0:
#         print(next(i))
        