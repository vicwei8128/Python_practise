import pandas as pd

data = {'Country': ['Belgium',  'India',  'Brazil'],
    'Capital': ['Brussels',  'New Delhi',  'Brasilia'],
    'Population': [11190846, 1303171035, 207847528]}

df = pd.DataFrame(data,columns=['Country',  'Capital',  'Population'])
print(df)

print(df.loc[:, "Population"].min())
print(df.loc[:, "Population"].max())
print(df.loc[:, "Population"].sum())
print(df.loc[:, "Population"].mean())
print(df.loc[:, "Population"].median())
print(df.loc[:, "Population"].std())

print(df.describe())