# from sqlalchemy import create_engine
# import pandas as pd

# DATABASE_URL = "postgresql://postgres:postgres@localhost:5432/mehboob"

# engine = create_engine(DATABASE_URL,pool_size=10,max_overflow=15)

# df = pd.read_sql("employee",engine)
# # print(df[df["name"].str.contains("ashok",case=False,na=False)])

# # print(df.rename(columns={"name":"Name"}))
# df["count_emp"] = df.groupby("location")["name"].transform("count")
# df["rank_emp"] = df.groupby("department")["salary"].rank(method="first",ascending=False)
# df = df.sort_values(["department","rank_emp"])
# df.loc[df["name"].str.contains("Panday",case=False,na=False),["salary","location"]]=[43000,"Now Yourk"]
# print(df)

# new_data = {
#     "name":"Ashok Panday",
#     "location":"Haryana",
#     "salary":45000,
#     "joining_date":"2018-05-10",
#     "age":30,
#     "department":"Support"
# }
# df1 = pd.DataFrame([new_data])
# df1.to_sql("employee",engine,if_exists="append",index=False)
# print(df1)


lst = [45,62,78,90,65,89,25,97,87,56,25,89,55,73,78,25,54,45,78,55,73,78,25,54,45,78,55,73,78,25,54,45,78]

min_element = min(lst)
# print(lst.index(min_element))
result = [i for i,v in enumerate(lst) if v==min_element]
print(result)