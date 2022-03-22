import pandas as pd

s1 = pd.Series(['a', 'b'])
s2 = pd.Series(['c', 'd'])

df=pd.concat([s1, s2])
print(df)
df=pd.concat([s1, s2], ignore_index=True)
print(df)
df=pd.concat([s1, s2], keys=['s1', 's2'])
print(df)
df=pd.concat([s1, s2], keys=['s1', 's2'], names=['Series', 'ID'])
print(df)

#df1 = pd.DataFrame([['a', 1], ['b', 2]], columns=['letter', 'number'])
#df2 = pd.DataFrame([['c', 3], ['d', 4]], columns=['letter', 'number'])
#df=pd.concat([df1, df2], ignore_index=True)
#print(df)

#df3 = pd.DataFrame([['c', 3, 'cat'], ['d', 4, 'dog']], columns=['letter', 'number', 'animal'])
#df=pd.concat([df1, df3], ignore_index=True)
#new_order = [1,2,0]
#df = df[df.columns[new_order]]
#print(df)

#df=pd.concat([df1, df3], join="inner")
#print(df)

#df4 = pd.DataFrame([['bird', 'polly'], ['monkey', 'george']], columns=['animal', 'name'])
#df=pd.concat([df1, df4], axis=1)
#print(df)

#df1 = pd.DataFrame([1], index=['a'])
#df2 = pd.DataFrame([2], index=['a'])
#df=pd.concat([df1, df2])
##df=pd.concat([df1, df2], verify_integrity=True)
#print(df)