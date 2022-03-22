import pandas as pd

Employees=pd.read_excel("Employees.xlsx")
print(Employees)

Employees.年齡+=1
print(Employees)

Employees.薪水*=1.1
print(Employees)
