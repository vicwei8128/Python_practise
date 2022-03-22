import pandas as pd, pyodbc 

server='.'
database='Northwind'
driver='{SQL Server}'
con_string = f'DRIVER={driver};SERVER={server};DATABASE={database}'
cnxn = pyodbc.connect(con_string)
query = """
  SELECT * FROM Customers
"""
df = pd.read_sql(query, cnxn)
print(df)