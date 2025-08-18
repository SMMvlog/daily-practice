lst = [3,8,10]
lst2 = [1,2,9,11]
result =  lst2+lst
# result.sort()
# print(result[::-1])
import pandas as pd

df = pd.DataFrame({
    'id': range(1, 21),
    'value': [x * 5 for x in range(1, 21)]  # values: 5, 10, 15, ..., 100
})
df["lag_value"] = df["value"] - df["value"].shift(1) 
df["lead_value"] =  df["value"] - df["value"].shift(-1)

df.rename(columns={"value":"Range"},inplace=True)
# df.fillna(0,inplace=True)
df["lead_value"] = df["lead_value"]
df = df[df["Range"]>30]
df.loc[10:15,"Range"] = [10,11,12,13,14,15]
df = df.astype(float)
df.sort_values("Range",ascending = True,inplace=True)
df.reset_index(drop=True,inplace=True)

df.loc[(df["Range"] !=0) & (df["Range"].notna()),"Range"] = df["Range"] * 1.50
# df =df.loc[12:13,"Range"]
# df.iloc[[7,10]]
# df = df[df["Range"].isin([67,60,135])]
# df = df[df["Range"] > 30]
# df = df[(df["Range"] >30) & (df["Range"] <200)]
# df =df.loc[(df["Range"] >30) & (df["Range"] <200)]
df = df.iloc[5:10,"Range"]
print(df)

