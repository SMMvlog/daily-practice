from sqlalchemy import create_engine
import pandas as pd

DATABASE_URL = "postgresql://postgres:postgres@localhost:5432/mehboob"
engine = create_engine(DATABASE_URL)

query = "select * from employee"

# df = pd.read_sql(query,engine)
# print(df.head())
df = pd.read_sql_table("employee",engine)
df['sal_rank'] = df.groupby("department")["salary"].rank(ascending=False)
print(df)