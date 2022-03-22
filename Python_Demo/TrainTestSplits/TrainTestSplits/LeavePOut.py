#Complete guide to Python’s cross-validation with examples(https://towardsdatascience.com/complete-guide-to-pythons-cross-validation-with-examples-a9676b5cac12)
#GitHub:Cross Validation(https://github.com/vaasha/Machine-leaning-in-examples/blob/master/sklearn/cross-validation/Cross%20Validation.ipynb)

# Import scikit-learn libraries
from sklearn.model_selection import LeavePOut, StratifiedKFold, train_test_split, cross_validate, cross_val_score
from sklearn.datasets import load_iris, load_boston
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

# import libraries for charting and manipulations with datasets
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
import random

iris = load_iris(return_X_y=False)
iris_df = pd.DataFrame(data=iris.data,columns=iris.feature_names)
print(iris_df)

features = iris['feature_names']
iris_df['target'] = iris.target
print(iris_df)

iris_df["target_name"] = iris_df['target'].map({i:name for i,name in enumerate(iris.target_names)})
print(iris_df.sample(5))

# initialize the model
model = LogisticRegression(solver="liblinear", multi_class="auto")

dfs = []
lpo = LeavePOut(p=2)
i = 1

for train_index, test_index in lpo.split(iris_df):
    X_train = iris_df.iloc[train_index].loc[:, features]
    X_test = iris_df.iloc[test_index].loc[:,features]
    y_train = iris_df.iloc[train_index].loc[:,'target']
    y_test = iris_df.loc[test_index].loc[:,'target']
    
    #Train the model
    model.fit(X_train, y_train) #Training the model
    y_pred = model.predict(X_test)
    print(f"Accuracy for the fold no. {i} on the test set: {accuracy_score(y_test, y_pred)}")
    
    # how many occurances appear in the train set
    s_train = iris_df.iloc[train_index].loc[:,'target_name'].value_counts()
    s_train.name = f"train {i}"
    s_test = iris_df.iloc[test_index].loc[:,'target_name'].value_counts()
    s_test.name = f"test {i}"
    df = pd.concat([s_train, s_test], axis=1, sort=False)
    df["|"] = "|"
    dfs.append(df)
    
    i += 1

print(pd.concat(dfs,axis=1, sort=False))