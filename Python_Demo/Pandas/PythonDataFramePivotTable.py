from collections import OrderedDict
import pandas as pd
import numpy as np

table = OrderedDict((
    ("Item", ['Item0', 'Item0', 'Item0', 'Item1']),
    ('CType',['Gold', 'Bronze', 'Gold', 'Silver']),
    ('USD',  [1, 2, 3, 4]),
    ('EU',   [1.1, 2.2, 3.3, 4.4])
))

df= pd.DataFrame(table)

print("before Pivot:")
print(df)

df = df.pivot_table(index='Item', columns='CType', values='USD', aggfunc=np.mean)

print("after Pivot:")
print(df)

