import pandas as pd
import numpy as np

df = pd.read_csv("Datasets/data.csv",sep=',')
#print(df)

#print(df[df["age"] > 30])
print(df.query('age>30'))

print(df[ df["num_pets"] > df[ "num_children"] ])
print(df[ (df["age"] > 40) & (df["num_pets"] > 0) ] )
print(df[["age","num_pets","num_children"]].apply(lambda row: np.mean(row),axis=0))

