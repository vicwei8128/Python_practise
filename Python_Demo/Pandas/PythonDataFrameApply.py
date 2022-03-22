import pandas as pd

data = {'Name': ['John',  'Mary',  'Joe'],
        'Age': [10,  20,  30],}

df = pd.DataFrame(data,columns=['Name',  'Age'])

#print(df)

df['Age'] = df['Age'].apply(lambda age: age + 1)
print(df)
