import numpy as np
import pandas as pd

#The Machine learning alogorithm
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import cross_val_predict
from sklearn import tree
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix

# Test train split
from sklearn.model_selection import train_test_split

## Just to switch off pandas warning
#pd.options.mode.chained_assignment = None

# Used to write our model to a file
import joblib

data = pd.read_csv("Datasets/titanic.csv")
#print(data.Age)

#p=data.dropna(axis=0, how='any', thresh=None, subset=None, inplace=False)
#print(p.Age)

columns = ['Pclass', 'Sex', 'Age']

median_age = data['Age'].mean()
data['Age'].fillna(median_age, inplace = True)
#print(data.Age)

data["Pclass"].replace("3rd", 3, inplace = True)
data["Pclass"].replace("2nd", 2, inplace = True)
data["Pclass"].replace("1st", 1, inplace = True)
#print(data)

data["Sex"] = np.where(data["Sex"] == "female", 0, 1)
#print(data.Sex)

#data.Sex=data.Sex.map({"male":0, "female":1})
#print(data.Sex)

data_inputs = data[columns]
#print(data_inputs)
expected_output = data[["Survived"]]
#print(expected_output)
#print(data.Fare.describe())

inputs_train, inputs_test, expected_output_train, expected_output_test = train_test_split (data_inputs, expected_output, test_size = 0.2, random_state = 19)

classifier = tree.DecisionTreeClassifier(class_weight=None, criterion='gini', max_depth=100,
            max_features=None, max_leaf_nodes=5000,
            min_impurity_decrease=0.0, min_impurity_split=None,
            min_samples_leaf=1, min_samples_split=2,
            min_weight_fraction_leaf=0.0, random_state=19,
            splitter='best')

classifier.fit(inputs_train, expected_output_train)

accuracy = classifier.score(inputs_test, expected_output_test)
print("Accuracy = {}%".format(accuracy * 100))

predictions = classifier.predict(inputs_test)
##accuracy = accuracy_score(expected_output_test, predictions)
##print(accuracy)
print(classification_report(expected_output_test, predictions))

#cross validation
scores = cross_val_score(classifier, data_inputs, expected_output, cv=50)
scores.sort()
accuracy = scores.mean()

print(scores)
print(accuracy)

predictions=cross_val_predict(classifier, data_inputs, expected_output, cv=10)
print(confusion_matrix(expected_output, predictions))

# test with unseen data
test = pd.read_csv("Datasets/titanic_test.csv")

median_age = test['Age'].median()
test['Age'].fillna(median_age, inplace = True)

test["Pclass"].replace("3rd", 3, inplace = True)
test["Pclass"].replace("2nd", 2, inplace = True)
test["Pclass"].replace("1st", 1, inplace = True)
#print(data_inputs)

test["Sex"] = np.where(test["Sex"] == "female", 0, 1)
#print(data_inputs)

test_predictions = classifier.predict(test[columns])
print(test_predictions.sum())
print(test_predictions)

#save model
joblib.dump(classifier, "titanic_decisiontree_model", compress=9)

