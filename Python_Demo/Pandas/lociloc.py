import pandas as pd

df=pd.read_csv("Datasets/data.csv")
print(df)

#-----loc-------
#print(df.loc[:,:])
#print(df.loc[3:,:])
#print(df.loc[2:4,:])
#print(df.loc[:2,:])

#print(df.loc[:,:"age"])
#print(df.loc[:,("age", "num_children")])

#print(df.loc[:,"age":"state"])
#print(df.loc[:,"state":])

#print(df.loc[:,"age":"state"])

#print(df.loc[:,["name","num_children"]])

#-----iloc-------
#print(df.iloc[3:,:])
#print(df.iloc[2:4,:])
#print(df.iloc[2:4,:])
#print(df.iloc[:2,:])
#print(df.iloc[:,3:])
#print(df.iloc[:,2:4])
#print(df.iloc[:,:2])
#print(df.iloc[3:4,2:3])

#print(df.iloc[[3,5],:])