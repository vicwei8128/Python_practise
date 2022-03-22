import pandas as pd

df=pd.read_csv(r"Datasets\Fillna.csv")
print(df)

newdf=df.fillna(0)
print(newdf)

newdf = df.ffill().bfill()
print(newdf)

#newdf = df.fillna(method='ffill').fillna(method='bfill')
#print(newdf)
