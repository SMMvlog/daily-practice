import pandas as pd

dct ={
    'Employee': ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve', 'Frank'],
    'Department': ['HR', '', 'Engineering', 'HR', 'Finance', 'Engineering'],
    'Salary': [50000, 80000, 70000, 52000, 75000, 85000]

}

df = pd.DataFrame(dct)
print(df.groupby("Department")["Salary"].mean())


























# df = pd.DataFrame(dct,nan_values="")
# df["updated_salary"] = df["Salary"] * 0.90

# df = df.fillna("Engineering")
# print(df)
# # # df =df.iloc[df[""]
# # ]

# # print(df)
# # df2 = pd.DataFrame({"Salary2":[f]})
# # modify table add column Salary2 value(Salary*1.10);

# # max_sal = df.groupby("Department").max("Salary").reset_index()
# # print(df)

# # max_salaries = df.groupby('Department')["Salary"].transform("min")
# # print(max_salaries)
# # # Filter rows where salary equals max salary per department
# # highest_paid = df[df['Salary'] == max_salaries]

# # print(highest_paid)




# # select department,Max(salary) from table group by department;

