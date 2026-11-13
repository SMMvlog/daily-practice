import pandas as pd

employees = pd.DataFrame({
    "emp_id": [101, 102, 103, 104, 105, 106],
    "name": ["John", "Alice", "Bob", "David", "Emma", "Frank"],
    "dept_id": [1, 2, 1, 3, 2, 4],
    "salary": [80000, 95000, 75000, 60000, 85000, 70000]
})

departments = pd.DataFrame({
    "dept_id": [1, 2, 3, 5],
    "department": ["IT", "HR", "Finance", "Marketing"],
    "location": ["Mumbai", "Delhi", "Pune", "Bangalore"]
})

employees_2025 = pd.DataFrame({
    "emp_id": [107, 108, 109],
    "name": ["George", "Harry", "Ivy"],
    "dept_id": [1, 3, 2],
    "salary": [82000, 65000, 90000]
})

# new_df =pd.merge(employees,departments,on="dept_id",how="outer")
# new_df = pd.concat([employees,employees_2025],axis=1)

dept_info = pd.DataFrame({
    "manager": ["Raj", "Priya", "Amit", "Sara"],
    "budget": [500000, 300000, 400000, 600000]
}, index=[1, 2, 3, 4])

# employees.set_index("dept_id",inplace=True)

# new_df = employees.join(dept_info)
new_df = pd.merge(
    employees,
    departments,
    on="dept_id",
    how="left",
    indicator=True
)

print(new_df)