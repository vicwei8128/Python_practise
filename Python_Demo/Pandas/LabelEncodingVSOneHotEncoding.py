from sklearn.preprocessing import LabelEncoder
import pandas as pd

##Label Encoding
#df=pd.read_csv('Datasets/titanic.csv')
#print(df.Sex)

#labelencoder = LabelEncoder()
#df.loc[:, "Sex"] = labelencoder.fit_transform(df.loc[:, "Sex"])
#print(df.Sex)

#One-Hot Encoding
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder

df=pd.read_csv('Datasets/titanic.csv')
#print(df)

#numeric_features = ['Age', 'Fare']
#numeric_transformer = Pipeline(steps=[
#    ('imputer', SimpleImputer(strategy='median')),
#    ('scaler', StandardScaler())])

#categorical_features = ['Embarked', 'Sex', 'Pclass']
categorical_features = ['Sex']
categorical_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='constant', fill_value='missing')),
    ('onehot', OneHotEncoder(handle_unknown='ignore'))])

preprocessor = ColumnTransformer(
    transformers=[
        #('num', numeric_transformer, numeric_features),
        ('cat', categorical_transformer, categorical_features)])


onehotsex = preprocessor.fit_transform(df)
onehotsex=pd.DataFrame(onehotsex, columns=['Sex_Female','Sex_Male'])   
#print(onehotsex)

df = pd.concat([df, onehotsex], axis=1).drop(['Sex'], axis=1)
print(df)

##One-Hot Encoding using DataFrame get_dummies
#df=pd.read_csv('Datasets/titanic.csv')
#print(df.Sex)

#df=pd.get_dummies(df.Sex)
#print(df)

#df=df.rename(columns = {'female':'Sex_Female', 'male':'Sex_Male'})
#print(df)
