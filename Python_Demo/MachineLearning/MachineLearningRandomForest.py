import numpy as np
import pandas as pd

#The Machine learning alogorithm
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import cross_val_predict
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix

# Test train split
from sklearn.model_selection import train_test_split

## Just to switch off pandas warning
#pd.options.mode.chained_assignment = None

# Used to write our model to a file
import joblib

data = pd.read_csv("Datasets/titanic.csv")
#print(data)

columns = ['Pclass', 'Sex', 'Age']

median_age = data['Age'].median()
data['Age'].fillna(median_age, inplace = True)

data["Pclass"].replace("3rd", 3, inplace = True)
data["Pclass"].replace("2nd", 2, inplace = True)
data["Pclass"].replace("1st", 1, inplace = True)
#print(data)

data["Sex"] = np.where(data["Sex"] == "female", 0, 1)
#print(data)

data_inputs = data[columns]
#print(data_inputs)
expected_output = data[["Survived"]]
#print(expected_output)

inputs_train, inputs_test, expected_output_train, expected_output_test = train_test_split (data_inputs, expected_output, test_size = 0.2, random_state = 13)

rf = RandomForestClassifier (n_estimators=100, max_depth=20, max_leaf_nodes=5000)
rf.fit(inputs_train, expected_output_train)

accuracy = rf.score(inputs_test, expected_output_test)
print("Accuracy = {}%".format(accuracy * 100))

predictions = rf.predict(inputs_test)
##accuracy = accuracy_score(expected_output_test, predictions)
##print(accuracy)
print(classification_report(expected_output_test, predictions))

#cross validation
scores = cross_val_score(rf, data_inputs, expected_output, cv=10)
scores.sort()
accuracy = scores.mean()

print(scores)
print(accuracy)

predictions=cross_val_predict(rf, data_inputs, expected_output, cv=10)
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

test_predictions = rf.predict(test[columns])
print(test_predictions.sum())
print(test_predictions)

joblib.dump(rf, "titanic_randomforest_model", compress=9)

