import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.preprocessing import LabelEncoder

passengers = pd.read_csv("Datasets/titanic.csv")

#print(passengers.info())
#print(passengers.head())

labelencoder = LabelEncoder()
passengers.loc[:, "Sex"] = labelencoder.fit_transform(passengers.loc[:, "Sex"])
#print(passengers.Sex)

passengers=passengers.loc[:, ['Survived', 'Sex', 'Pclass', 'Age']]
print(passengers.corr())

f, ax = plt.subplots(figsize=(9, 6))
sns.heatmap(passengers.corr(), annot=True, linewidths=.5, ax=ax ,cmap="bwr")
plt.title("Corr HeatMap")
plt.show()