import numpy as np
import pandas as pd

#df=pd.read_csv("Datasets/titanic.csv")
#print(df)

#print(df.describe())
##print(df.describe(include=[np.number])) #對所有的數值欄位執行describe
#print(df.Age.describe())

#print(df.describe(exclude=[np.number]))
#print(df.Sex.describe())

dfdt=pd.read_csv("Datasets/data.csv")

#daterange=pd.date_range(start='1/1/2018', periods=len(dfdt),freq='H')
#dfdt["datetime"]=daterange
##print(dfdt)
#print(dfdt.datetime.describe())

#print(dfdt.describe(include=[np.object]))

print(dfdt.describe(include='all'))
