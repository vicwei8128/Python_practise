import pandas as pd
import numpy as np

raw_data1 = {
        'subject_id': ['1', '2', '3', '4', '5'],
        'first_name': ['Alex', 'Amy', 'Allen', 'Alice', 'Ayoung'], 
        'last_name': ['Anderson', 'Ackerman', 'Ali', 'Aoni', 'Atiches']}
df1 = pd.DataFrame(raw_data1, columns = ['subject_id', 'first_name', 'last_name'])
print(df1)

raw_data2 = {
        'subject_id': ['4', '5', '6', '7', '8'],
        'first_name': ['Billy', 'Brian', 'Bran', 'Bryce', 'Betty'], 
        'last_name': ['Bonder', 'Black', 'Balwner', 'Brice', 'Btisan']}
df2 = pd.DataFrame(raw_data2, columns = ['subject_id', 'first_name', 'last_name'])
print(df2)

print(pd.merge(df1, df2, on='subject_id'))
