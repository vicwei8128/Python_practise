from sklearn.preprocessing import MinMaxScaler
import pandas as pd

df=pd.read_excel(r"Datasets\Excel.xlsx")
print(df)

scalar=MinMaxScaler()

df[["Salary", "Age"]]=scalar.fit_transform(df[["Salary", "Age"]])
print(df)
