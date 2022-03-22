#Learning embeddings for your machine learning model
#https://medium.com/spikelab/learning-embeddings-for-your-machine-learning-model-a6cb4bc6542e
#Categorical Embedding and Transfer Learning
#https://towardsdatascience.com/categorical-embedding-and-transfer-learning-dd3c4af6345d

import pandas as pd

df=pd.read_excel(r"Datasets\Excel.xlsx")
print(df)

#LabelEncoder
from sklearn.preprocessing import LabelEncoder
from sklearn.compose import ColumnTransformer

#le = LabelEncoder()
#df.Gender=le.fit_transform(df.Gender)
#print(df)
#===============
#from sklearn.preprocessing import OrdinalEncoder

#encoder = ColumnTransformer(
#    transformers=[
#        (
#            'ordinal', OrdinalEncoder(), ['Gender', 'JobTitle'],            
#        )
#    ])

#df1=df.iloc[:, 0:2]

#result=encoder.fit_transform(df)  #內含LabelEncoder的ColumnTransformer無法處理多個欄位
#df2=pd.DataFrame(result, columns=['Gender', 'JobTitle'], dtype=int)
#print(df2)

#df=pd.concat([df1, df2], axis=1)
#print(df)
#=======================
from sklearn.preprocessing import OneHotEncoder

#one-hot encoder
encoder = ColumnTransformer(
    transformers=[
        ('Gender', OneHotEncoder(), ['Gender'])])

onehotgender = encoder.fit_transform(df)
onehotgender=pd.DataFrame(onehotgender, columns=['Gender_Female','Gender_Male'], dtype=int) 

df = pd.concat([df, onehotgender], axis=1).drop(['Gender'], axis=1)
print(df)

##Pandas get_dummies
#df1=df.iloc[:, 0:2]
#print(df1)
#df2=pd.get_dummies(df.Gender)
#print(df2)
#df=pd.concat([df1, df2], axis=1)
#print(df)
#df=df.rename(columns = {'Female':'Gender_Female', 'Male':'Gender_Male'})
#print(df)

###LabelBinarizer
##from sklearn.preprocessing import LabelBinarizer

##encoder = LabelBinarizer()
##print(encoder.fit_transform(df.Gender))
##df.Gender=encoder.fit_transform(df.Gender)
##print(df)

###OrdinalEncoder
##from sklearn.preprocessing import OrdinalEncoder
##encoder = OrdinalEncoder()
##df=encoder.fit_transform(df)
##print(df)