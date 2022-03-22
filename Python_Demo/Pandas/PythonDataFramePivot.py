from collections import OrderedDict
import pandas as pd

table = OrderedDict((
    ("Item", ['Item0', 'Item0', 'Item1', 'Item1']),
    ('CType',['Gold', 'Bronze', 'Gold', 'Silver']),
    ('USD',  ['1$', '2$', '3$', '4$']),
    ('EU',   ['1€', '2€', '3€', '4€'])
))
df= pd.DataFrame(table)

#print("before Pivot:")
#print(df)

#df=df.pivot(index='Item', columns='CType', values='USD')

#print("after Pivot:")
#print(df)

print("before Pivot 2 Columns:")
print(df)

df=df.pivot(index='Item', columns='CType')

print("after Pivot 2 Columns:")
print(df)


