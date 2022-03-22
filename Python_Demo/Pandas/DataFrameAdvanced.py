import numpy as np
import pandas as pd

df=pd.read_csv("Datasets/data.csv")
print(df)

#====copy或deepcopy====
#df2=df
#df2.age+=1

#print(df)

df2=df.copy()
#df2=df.deepcopy()

df2.age+=1
print(df)
#====取num_pets與num_children兩個欄位較大的值====
#df['maximum'] = df.apply(lambda x: max(x['num_pets'], x['num_children']), axis = 1)
df['maximum'] = df[['num_pets','num_children']].max(axis =1)
print(df)

#====value_counts=====
print(df['state'].value_counts())
print(df['state'].value_counts(normalize = True))

#dfvaluecount=df['state'].value_counts().reset_index()
dfvaluecount=df['state'].value_counts().reset_index().sort_values(by='state', ascending=1)
print(dfvaluecount)

#===count null===
df = pd.DataFrame({ 'id': ['A1','A2','B1'], 'c1':[0,0,np.nan], 'c2': [np.nan,1,1]})
df = df[['id', 'c1', 'c2']]
df['num_nulls'] = df[['c1', 'c2']].isnull().sum(axis=1)
print(df)

#====Filter===
df_filter = df['id'].isin(['A1','A2'])
print(df[df_filter])