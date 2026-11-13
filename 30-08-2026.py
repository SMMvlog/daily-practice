# import pandas as pd

# df = pd.DataFrame({
#     "user_id": [
#         1, 2, 1, 3, 4, 2, 5, 1, 6, 3,
#         7, 4, 2, 8, 5, 6, 1, 9, 3, 7,
#         10, 4, 8, 2, 5, 9, 6, 10, 7, 3
#     ],

#     "amount": [
#         100, 500, 200, 300, 150, 400, 250, 350, 600, 450,
#         700, 200, 300, 800, 150, 500, 250, 900, 350, 400,
#         1000, 450, 550, 200, 300, 650, 750, 500, 350, 200
#     ],

#     "timestamp": [
#         "2026-08-28", "2026-08-27", "2026-08-20", "2026-08-25",
#         "2026-08-15", "2026-08-10", "2026-08-05", "2026-08-01",
#         "2026-07-30", "2026-07-25", "2026-07-20", "2026-07-15",
#         "2026-07-10", "2026-07-05", "2026-07-01", "2026-06-30",
#         "2026-06-25", "2026-06-20", "2026-06-15", "2026-06-10",
#         "2026-06-05", "2026-08-29", "2026-08-18", "2026-08-12",
#         "2026-08-03", "2026-07-28", "2026-07-18", "2026-07-08",
#         "2026-06-28", "2026-06-15"
#     ]
# })

# # print(df)
# end_date = pd.to_datetime(df["timestamp"]).max()
# start_date = end_date - pd.Timedelta(days=30)

# print(df[pd.to_datetime(df["timestamp"]).between(start_date,end_date)
#          ].groupby("user_id")["amount"].sum().reset_index(name="total_amount")
#       )

import pandas as pd

# users = pd.DataFrame({
#     "user_id": [1, 2, 3, 4, 5, 6, 7, 8],
#     "name": ["A", "B", "C", "D", "E", "F", "G", "H"],
#     "city": ["Mumbai", "Pune", "Delhi", "Mumbai", "Pune", "Delhi", "Mumbai", "Nashik"]
# })

# orders = pd.DataFrame({
#     "order_id": [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
#     "user_id": [1, 2, 1, 3, 5, 9, 4, 2, 10, 6],
#     "amount": [500, 700, 300, 900, 400, 200, 800, 100, 600, 250]
# })


# result = pd.merge(users,orders,on="user_id",how="left")
# total_order = result.groupby("user_id")["amount"].sum().reset_index(name="total_amount")



# df1 = pd.DataFrame({
#     "user_id": [1, 2, 3],
#     "name": ["A", "B", "C"],
#     "amount": [100, 200, 300]
# })

# df2 = pd.DataFrame({
#     "user_id": [4, 5, 6],
#     "name": ["D", "E", "F"],
#     "amount": [400, 500, 600]
# })

# print(pd.concat([df1,df2]))

# df1 = pd.DataFrame({
#     "user_id": [1, 2, 3],
#     "name": ["A", "B", "C"]
# })

# df2 = pd.DataFrame({
#     "user_id": [1, 2, 3],
#     "amount": [100, 200, 300]
# })

# print(pd.merge(df1,df2))

# employees = pd.DataFrame({
#     "emp_id": [1, 2, 3, 4, 5, 6, 7],
#     "name": ["A", "B", "C", "D", "E", "F", "G"],
#     "dept_id": [10, 20, 10, 30, 20, 10, 30],
#     "salary": [50000, 60000, 55000, 70000, 65000, 52000, 75000]
# })

# departments = pd.DataFrame({
#     "dept_id": [10, 20, 30],
#     "dept_name": ["IT", "HR", "Finance"]
# })

# dept_avg = employees.groupby("dept_id")["salary"].mean().reset_index(name="average_salary")
# print(pd.merge(dept_avg,departments,on="dept_id"))
# # print(dept_avg)

customers = pd.DataFrame({
    "customer_id": [1, 2, 3, 4, 5],
    "customer_name": ["A", "B", "C", "D", "E"]
})
orders = pd.DataFrame({
    "order_id": [101, 102, 103, 104, 105, 106],
    "cust_id": [1, 2, 1, 3, 5, 2],
    "amount": [500, 200, 300, 700, 400, 100]
})

total_order=orders.groupby("cust_id")["amount"].sum().reset_index(name="total_amount")
print(pd.merge(customers,total_order,left_on="customer_id",right_on="cust_id",how="left"))