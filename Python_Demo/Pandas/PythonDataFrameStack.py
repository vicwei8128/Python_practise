import pandas as pd

df= pd.read_csv("Datasets/CashBalance.csv")

print("before stack:")
print(df)

print("after stack:")
df=df.set_index(['date', 'name'])
print(df)

print("after unstack:")
df=df.unstack()
print(df)
