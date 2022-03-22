from sklearn.preprocessing import StandardScaler
#from sklearn.preprocessing import scale

from sklearn.preprocessing import MinMaxScaler
#from sklearn.preprocessing import minmax_scale

from sklearn.preprocessing import MaxAbsScaler
#from sklearn.preprocessing import maxabs_scale

from sklearn.preprocessing import RobustScaler
#from sklearn.preprocessing import robust_scale

from sklearn.preprocessing import QuantileTransformer
#from sklearn.preprocessing import quantile_transform

from sklearn.preprocessing import PowerTransformer
#from sklearn.preprocessing import power_transform

from sklearn.preprocessing import Normalizer
#from sklearn.preprocessing import normalize

from sklearn.preprocessing import Binarizer
#from sklearn.preprocessing import binarize

#from sklearn.preprocessing import Imputer       #old
from sklearn.impute import SimpleImputer         #new

from sklearn.preprocessing import KBinsDiscretizer 
from sklearn.preprocessing import PolynomialFeatures
from sklearn.preprocessing import FunctionTransformer

import numpy as np
from matplotlib import pyplot

import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

#StandardScalar : normalize/standardize (mean = 0 and standard deviation = 1) your features/variables/columns of X 
#data = [[0, 0], [1, 0], [0, 1], [1, 1]]
#print(data)

#print("StandardScalar:")
#standardscaler = StandardScaler()
#transform_data = standardscaler.fit_transform(data)         # transform_data = scale(data)
#print(transform_data)

##MinMaxScalar : Transform features by scaling each feature to a given range.
#data = [[-1, 2], [-0.5, 6], [0, 10], [1, 18]]
#print(data)

#print("MinMaxScaler:")
#minmaxscaler = MinMaxScaler()     #預設min:0, max:1
#transform_data=minmaxscaler.fit_transform(data)           #transform_data=minmax_scale(data)
#print(transform_data)

##MaxAbsScalar : Transform features by scaling each feature to -1~1
#data = [[ 1., -1.,  2.], [ 2.,  0.,  0.], [ 0.,  1., -1.]]
#print(data)

#print("MaxAbsScaler:")
#maxabsscaler = MaxAbsScaler()     
#transform_data=maxabsscaler.fit_transform(data)           #transform_data=maxabs_scale(data)
#print(transform_data)

##RobustScaler : Transform Outlier
#data = [[ 1., -2.,  2.], [ -2.,  1.,  3.], [ 4.,  1., -2.]]
#print(data)

#print("RobustScaler:")
#robustscaler = RobustScaler()     
#transform_data=robustscaler.fit_transform(data)           #transform_data=robust_scale(data)
#print(transform_data)

##QuantileTransformer : adjust to normal distribution
#data = np.random.randn(1000)
## add a skew to the data distribution
#data = np.exp(data)
## histogram of the raw data with a skew
#pyplot.hist(data, bins=25)
#pyplot.show()

## reshape data to have rows and columns
#data = data.reshape((len(data),1))

#print("QuantileTransformer:")
#quantiletransformer = QuantileTransformer(output_distribution='normal')     
#transform_data=quantiletransformer.fit_transform(data)           #transform_data=quantile_transform(data, output_distribution='normal')
## histogram of the transformed data
#pyplot.hist(transform_data, bins=25)
#pyplot.show()

##PowerTransformer : Box-Cox Transform
#data = np.random.RandomState(616).lognormal(size=(3, 3))
#print(data)

#print("PowerTransformer:")
#powertransformer = PowerTransformer(method='box-cox', standardize=False)
#transform_data=powertransformer.fit_transform(data)           
##transform_data=power_transform(data)
#print(transform_data)

## Normalize : 
#data = [[ 1., -1.,  2.],[ 2.,  0.,  0.],[ 0.,  1., -1.]]
#print(data)

#print("Normalize:")
#normalizer = Normalizer()
#transform_data=normalizer.fit_transform(data)       # transform_data=normalize(data)
#print(transform_data)

##Binarization : greater than 0=>1, less tban 0=>0
#data = [[ 1., -1.,  2.],[ 2.,  0.,  0.],[ 0.,  1., -1.]]  
#print(data)

#print("Binarizer:")
#binarizer=Binarizer()
#transform_data=binarizer.fit_transform(data)        # transform_data=binarize(data)
#print(transform_data)

## SimpleImputer : fill missing data
data= [[1, 2], [np.nan, 3], [7, 6]]
print(data)

print("SimpleImputer:")
imputer = SimpleImputer(missing_values=np.nan, strategy='mean')  
transform_data=imputer.fit_transform(data)   
print(transform_data)

# KBinsDiscretizer : Transform continous data to discrete data
data = [[ -3., 5., 15 ],
        [  0., 6., 14 ],
        [  6., 3., 11 ]]
print(data)

print("KBinsDiscretizer:")
kbinsdiscretizer = KBinsDiscretizer(n_bins=[3, 2, 2], encode='ordinal')
transform_data=kbinsdiscretizer.fit_transform(data)   
print(transform_data)

## PolynomialFeatures  : generate polynomial(non-linear) data
#data = np.arange(6).reshape(3, 2)
#print(data)

#print("PolynomialFeatures:")
#polynomialfeatures = PolynomialFeatures(2)
#transform_data=polynomialfeatures.fit_transform(data)   
#print(transform_data)

##FunctionTransformer
##data = [[0, 1], [2, 3]]
##print(data)

##print("FunctionTransformer:")
##functionaltransformer = FunctionTransformer(np.log1p, validate=True)
##transform_data=functionaltransformer.fit_transform(data)
##print(transform_data)

import pandas as pd
#import joblib
from sklearn.preprocessing import OneHotEncoder, StandardScaler, FunctionTransformer
#from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
#from sklearn.metrics import roc_auc_score, accuracy_score, confusion_matrix

# Creating a function to appropriately engineer the ‘Age’ column
def create_age_bins(col):
    """Engineers age bin variables for pipeline"""
 
    # Defining / instantiating the necessary variables
    age_bins = [-1, 12, 18, 25, 50, 100]
    age_labels = ['child', 'teen', 'young_adult', 'adult', 'elder']
    age_imputer = SimpleImputer(strategy = 'median')
    age_ohe = OneHotEncoder()
 
    # Performing basic imputation for nulls
    imputed = age_imputer.fit_transform(col)
    ages_filled = pd.DataFrame(data = imputed, columns = ['Age'])
 
    # Segregating ages into age bins
    age_cat_cols = pd.cut(ages_filled['Age'], bins = age_bins, labels = age_labels)
    age_cats = pd.DataFrame(data = age_cat_cols, columns = ['Age'])
 
    # One hot encoding new age bins
    ages_encoded = age_ohe.fit_transform(age_cats[['Age']])
    ages_encoded = pd.DataFrame(data = ages_encoded.toarray()) 
    return ages_encoded

# Creating function to appropriately engineer the ‘Embarked’ column
def create_embarked_columns(col):
    """Engineers the embarked variables for pipeline"""
 
    # Instantiating the transformer objects
    embarked_imputer = SimpleImputer(strategy = 'most_frequent')
    embarked_ohe = OneHotEncoder()
 
    # Performing basic imputation for nulls
    imputed = embarked_imputer.fit_transform(col)
    embarked_filled = pd.DataFrame(data = imputed, columns = ['Embarked'])
 
    # Performing OHE on the col data
    embarked_columns = embarked_ohe.fit_transform(embarked_filled[['Embarked']])
    embarked_columns_df = pd.DataFrame(data = embarked_columns.toarray()) 
    return embarked_columns_df

# Importing the training dataset
raw_train = pd.read_csv(r'Datasets\titanic.csv')
raw_train["Sex"] = np.where(raw_train["Sex"] == "female", 0, 1)
print(raw_train.Sex)

# Splitting the training data into appropriate training and validation sets
#X = raw_train.drop(columns = ['Survived'])
X = raw_train[["Sex", "Age", "Embarked"]]
y = raw_train['Survived']
X_train, X_val, y_train, y_val = train_test_split(X, y, random_state = 42)

# Creating a preprocessor to transform the 'Sex', 'Age' and 'Embarked' column
data_preprocessor = ColumnTransformer(transformers = [
    ('sex_transformer', OneHotEncoder(), ['Sex']),
    ('age_transformer', FunctionTransformer(create_age_bins, validate = False), ['Age']),
    ('embarked_transformer', FunctionTransformer(create_embarked_columns, validate = False), ['Embarked'])
])

# Creating our pipeline that first preprocesses the data, then scales the data, then fits the data to a RandomForestClassifier
rfc_pipeline = Pipeline(steps = [
    ('data_preprocessing', data_preprocessor),
    ('data_scaling', StandardScaler()),    
])

## Fitting the training data to our pipeline
transform_data=rfc_pipeline.fit_transform(X_train, y_train)
print(transform_data)