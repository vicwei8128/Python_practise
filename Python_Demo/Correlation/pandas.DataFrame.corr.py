import pandas as pd
from sklearn.preprocessing import LabelEncoder

passengers = pd.read_csv("Datasets/titanic.csv")

#print(passengers.info())
#print(passengers.head())

labelencoder = LabelEncoder()
passengers.loc[:, "Sex"] = labelencoder.fit_transform(passengers.loc[:, "Sex"])
#print(passengers.Sex)

passengers=passengers.loc[:, ['Survived', 'Sex', 'Pclass', 'Age']]
print(passengers.corr())

transactions = pd.read_excel(r"Datasets\Superstore.xls")

#print(transactions.head())
#print(transactions.info())

transactions=transactions.loc[:, ['Profit', 'Sales', 'Quantity', 'Discount']]
print(transactions.corr())
