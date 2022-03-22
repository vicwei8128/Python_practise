import pandas as pd

students = [('Riti', 30, 'Delhi'),
            ('Aadi', 16, 'New York'),
            ('Riti', 30, 'Delhi'),
            ('Riti', 30, 'Delhi'),
            ('Riti', 30, 'Mumbai'),
            ('Aadi', 40, 'London')]
 
df = pd.DataFrame(students, columns=['Name', 'Age', 'City'])
print(df)

#print(df.duplicated())
print(df.duplicated().any())
print(df.duplicated().sum())

print(df.duplicated(subset='City').sum())
print(df.duplicated(subset=['Name','City']).sum())

print(df.duplicated(keep=False).sum())          #不保留重複的資料
#print(df.duplicated(keep='first').sum())       #保留第一筆重複的資料(預設值)
#print(df.duplicated(keep='last').sum())        #保留最末筆重複的資料

print(df.drop_duplicates())
print(df.drop_duplicates(subset=['Age','City']))