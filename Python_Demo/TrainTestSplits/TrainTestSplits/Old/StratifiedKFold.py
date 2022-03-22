#Complete guide to Python’s cross-validation with examples(https://towardsdatascience.com/complete-guide-to-pythons-cross-validation-with-examples-a9676b5cac12)
#GitHub:Cross Validation(https://github.com/vaasha/Machine-leaning-in-examples/blob/master/sklearn/cross-validation/Cross%20Validation.ipynb)

# Import scikit-learn libraries
from sklearn.model_selection import KFold, StratifiedKFold, train_test_split, cross_validate, cross_val_score
from sklearn.datasets import load_iris, load_boston
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

# import libraries for charting and manipulations with datasets
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
import random

# create the range 1 to 25
rn = range(1,26)

# to demonstrate how the data are split, we will create 3 and 5 folds. 
# KFold function has to be applied on the data and it returns an location (index) of the train and test samples.
kf5 = KFold(n_splits=5, shuffle=False)
kf3 = KFold(n_splits=3, shuffle=False)

# the Kfold function retunrs the indices of the data. Our range goes from 1-25 so the index is 0-24
for train_index, test_index in kf3.split(rn):
    print(train_index, test_index)

# to get the values from our data, we use np.take() to access a value at particular index
for train_index, test_index in kf3.split(rn):
    print(np.take(rn,train_index), np.take(rn,test_index))

# Let's split our test range into 5 and3  folds and display the splits on the chart.
# In order to clearly show which data belongs to each set, we will shift the values by -.1 and +.1
# the first fold will contain values 0.9 in train and 1.1 in the test set, second 1.9 and 2.1, etc.
# we will also give each sets the different color
# because we will repeat this exercise for the shuffled version, let's create a function 

def kfoldize(kf, rn, shift=.1):
    train = pd.DataFrame()
    test = pd.DataFrame()
    i = 1
    for train_index, test_index in kf.split(rn):
        train_df = pd.DataFrame(np.take(rn, train_index), columns=["x"])
        train_df["val"] = i - shift
        train = train.append(train_df)

        test_df = pd.DataFrame(np.take(rn, test_index), columns=["x"])
        test_df["val"] = i + shift
        test = test.append(test_df)
        i += 1
    return train, test

train5, test5 = kfoldize(kf5,rn)
train3, test3 = kfoldize(kf3,rn)

fig,ax = plt.subplots(1,2, figsize=(15,5))
ax[0].scatter(x="x",y="val",c="b",label="train",s=15,data=train5)
ax[0].scatter(x="x",y="val",c="r",label="test",s=15,data=test5)
ax[1].scatter(x="x",y="val",c="b",label="train",s=15,data=train3)
ax[1].scatter(x="x",y="val",c="r",label="test",s=15,data=test3)
ax[0].set_ylabel("Kfold")
ax[0].set_xlabel("feature")
ax[1].set_xlabel("feature")
ax[0].set_title("5 Folds")
ax[1].set_title("3 Folds")
plt.suptitle("Kfold split between train and test features")
plt.legend(bbox_to_anchor=(1.05, 1))
plt.show()

# let's make sure how the values are distributes between the sets; Also we will create function so that we can repeat
def kfold_stats(df, name):
    s =  pd.Series({"Min value: ": df["x"].min(),
              "Max value: ": df["x"].max(),
              "Min occurance: ": df["x"].value_counts().min(),
              "Max occurance: ": df["x"].value_counts().max(),
               "Min lenght": df.groupby("val").count().min().values[0],
               "Max lenght": df.groupby("val").count().max().values[0]})
    s.name = name
    return s
pd.concat([kfold_stats(train5, "Train5"), kfold_stats(test5,"Test5"),
          kfold_stats(train3, "Train3"), kfold_stats(test3,"Test3")], 
          axis=1)

kf42 = KFold(n_splits=5, shuffle=True, random_state=42)
kf123 = KFold(n_splits=5, shuffle=True, random_state=123)

train42, test42 = kfoldize(kf42,rn)
train123, test123 = kfoldize(kf123,rn)
train123_2, test123_2 = kfoldize(kf123,rn,shift=.25)

fig,ax = plt.subplots(1,2, figsize=(15,5))
ax[0].scatter(x="x",y="val",c="b",label="train",s=15,data=train42) 
ax[0].scatter(x="x",y="val",c="r",label="test",s=15,data=test42)
ax[1].scatter(x="x",y="val",c="b",label="train",s=15,data=train123)
ax[1].scatter(x="x",y="val",c="r",label="test",s=15,data=test123)
ax[1].scatter(x="x",y="val",c="k",label="test second run",s=15,data=test123_2)
ax[0].set_ylabel("Kfold")
ax[0].set_xlabel("feature")
ax[0].set_title("Shuffled KFold with random state 42")
ax[1].set_ylabel("Kfold")
ax[1].set_xlabel("feature")
ax[1].set_title("Shuffled KFold with random state 123")
plt.suptitle("Shuffled KFold")
plt.legend(bbox_to_anchor=(1.05, 1))
plt.show()

iris = load_iris(return_X_y=False)
iris_df = pd.DataFrame(data=iris.data,columns=iris.feature_names)
features = iris['feature_names']
iris_df['target'] = iris.target
iris_df["target_name"] = iris_df['target'].map({i:name for i,name in enumerate(iris.target_names)})
print(iris_df.sample(5))

# Let's see how many samples of each iris type we have in our set
print(pd.DataFrame(iris_df.groupby("target_name").size().reset_index()).rename(columns={0:"samples"}))

# initialize the model
model = LogisticRegression(solver="liblinear", multi_class="auto")

#Logistic regression without Kfold, just split into 80% train and 20% test set
X = iris_df[features]
y = iris_df["target"]
X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.2, random_state=42)

#Train the model
model.fit(X_train, y_train) #Training the model
pd.DataFrame({"Accurancy on Train":[accuracy_score(y_train, model.predict(X_train))],
    "Accurancy on Test":[accuracy_score(y_test, model.predict(X_test))]})

i = 1
for train_index, test_index in kf3.split(iris_df):
    X_train = iris_df.iloc[train_index].loc[:, features]
    X_test = iris_df.iloc[test_index][features]
    y_train = iris_df.iloc[train_index].loc[:,'target']
    y_test = iris_df.loc[test_index]['target']
        
    #Train the model
    model.fit(X_train, y_train) #Training the model
    print(f"Accuracy for the fold no. {i} on the test set: {accuracy_score(y_test, model.predict(X_test))}")
    i += 1

target_name = iris_df["target"]

fig, ax = plt.subplots(1,3, figsize=(13,3), sharey=True)
for i, (train_index, test_index) in enumerate(kf3.split(iris_df)):
    ax[i].scatter(x=train_index,y=target_name.iloc[train_index],label ="train", c='b')
    ax[i].scatter(x=test_index,y=target_name.iloc[test_index], label = "test", c='r')
    ax[i].set_title(f"Fold {i+1}")

ax[0].set_yticks([0,1,2])
ax[0].set_yticklabels(iris["target_names"])
plt.legend(bbox_to_anchor=(1.05, 1))
plt.show()

dfs = []
kf = KFold(n_splits=3, shuffle=True, random_state=123)
i = 1

for train_index, test_index in kf.split(iris_df):
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

plt.scatter(x=y_train.index,y=iris_df.iloc[train_index].loc[:,'target_name'],label ="train")
plt.scatter(x=y_test.index,y=iris_df.iloc[test_index].loc[:,'target_name'], label = "test")
plt.legend()
plt.show()

print(pd.concat(dfs,axis=1, sort=False))

dfs = []
kf = StratifiedKFold(n_splits=3, shuffle=True, random_state=123)
i = 1
for train_index, test_index in kf.split(iris_df, iris_df["target"]):
    X_train = iris_df.iloc[train_index].loc[:, features]
    X_test = iris_df.iloc[test_index].loc[:,features]
    y_train = iris_df.iloc[train_index].loc[:,'target']
    y_test = iris_df.loc[test_index].loc[:,'target']

    #Train the model
    model.fit(X_train, y_train) #Training the model
    print(f"Accuracy for the fold no. {i} on the test set: {accuracy_score(y_test, model.predict(X_test))}, doublecheck: {model.score(X_test,y_test)}")
    
    # how many occurances appear in the train set
    s_train = iris_df.iloc[train_index].loc[:,'target_name'].value_counts()
    s_train.name = f"train {i}"
    s_test = iris_df.iloc[test_index].loc[:,'target_name'].value_counts()
    s_test.name = f"test {i}"
    df = pd.concat([s_train, s_test], axis=1, sort=False)
    df["|"] = "|"
    dfs.append(df)
    
    i += 1

plt.scatter(x=y_train.index,y=iris_df.iloc[train_index].loc[:,'target_name'],label ="train")
plt.scatter(x=y_test.index,y=iris_df.iloc[test_index].loc[:,'target_name'], label = "test")
plt.legend()
plt.title("Shuffled stratified StratifiedKFold - 3rd Fold")
plt.show()

print(pd.concat(dfs,axis=1, sort=False))

# cross_validate allow to specify metrics which you want to see
for i, score in enumerate(cross_validate(model, X,y, cv=3)["test_score"]):
    print(f"Accuracy for the fold no. {i} on the test set: {score}")

for i, score in enumerate(cross_val_score(model, X,y, cv=3)):
    print(f"Accuracy for the fold no. {i} on the test set: {score}")

# In order to have see how the KFold distributes the features let's have a look on titanic dataset
# https://www.kaggle.com/c/titanic
titanic = pd.read_csv(r'Datasets\titanic.csv').sort_values(by="Sex").reset_index(drop=True)
dfs = []
dfs_data = []

kf = StratifiedKFold(n_splits=3, shuffle=False, random_state=123)
i = 1
for train_index, test_index in kf.split(titanic, titanic["Survived"]):
    X_train = titanic.iloc[train_index].drop(columns=["Survived"])
    X_test = titanic.iloc[test_index].drop(columns=["Survived"])
    y_train = titanic.iloc[train_index].loc[:,"Survived"]
    y_test = titanic.loc[test_index].loc[:,"Survived"]
    
    dfs_data.append({"train": pd.concat([X_train,y_train], axis=1, sort=False), "test": pd.concat([X_test,y_test], axis=1, sort=False)})
    
    #Train the model
    #model.fit(X_train, y_train) #Training the model
    #print(f"Accuracy for the fold no. {i} on the test set: {accuracy_score(y_test, model.predict(X_test))}, doublecheck: {model.score(X_test,y_test)}")
       
    i += 1

statistics = []
for i, data in enumerate(dfs_data):
    for st in ["train","test"]:
        s = data[st][["Survived"]].groupby(["Survived"]).size()
        s.index = s.index.map({0:"Died",1:"Survived"})
        s.name = f"{st} - {i+1}"
        statistics.append(s)

print(pd.concat(statistics, axis=1).reset_index())

for i, data in enumerate(dfs_data):
    fig, ax = plt.subplots(1,2, figsize=(15,5), sharey=True)
    plot_df = dfs_data[i]["train"][["Survived"]].groupby(["Survived"]).size()
    plot_df.index = plot_df.index.map({0:"Died",1:"Survived"})
    sns.barplot(plot_df.index, plot_df.values,ax=ax[0])
    ax[0].set_title(f"Train set - {i+1} fold")
    ax[0].set_xlabel('')
    plot_df = dfs_data[i]["test"][["Survived"]].groupby(["Survived"]).size()
    plot_df.index = plot_df.index.map({0:"Died",1:"Survived"})
    sns.barplot(plot_df.index, plot_df.values,ax=ax[1])
    ax[1].set_title(f"Test set - {i+1} fold")
    ax[1].set_xlabel('')
    plt.suptitle("Stratification works perfect for the target variable")
    plt.show()

# table showing distribution of the sexes in the StratifiedKFold split
metric_dfs = []
for i, data in enumerate(dfs_data):
    s = dfs_data[i]["train"].groupby("Sex").size()
    s.name = f"Fold {i+1} Train"
    st = dfs_data[i]["test"].groupby("Sex").size()
    st.name = f"Fold {i+1} Test"
    metric_df = pd.concat([s,st],axis=1)
    metric_df["|"] = "|"
    metric_dfs.append(metric_df)
print(pd.concat(metric_dfs,axis=1).reset_index())

for i, data in enumerate(dfs_data):
    fig, ax = plt.subplots(1,2, figsize=(15,5), sharey=True)
    plot_df = dfs_data[i]["train"][["Sex"]].groupby(["Sex"]).size()
    sns.barplot(plot_df.index, plot_df.values,ax=ax[0])
    ax[0].set_title(f"Train set - {i+1} fold")
    plot_df = dfs_data[i]["test"][["Sex"]].groupby(["Sex"]).size()
    sns.barplot(plot_df.index, plot_df.values,ax=ax[1])
    ax[1].set_title(f"Test set - {i+1} fold")
    plt.suptitle("Stratification doesn't consider distribution of the features")
    plt.show()