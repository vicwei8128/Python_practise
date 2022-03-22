import pandas as pd

sales = [('account', ['Jones LLC', 'Alpha Co', 'Blue Inc', 'Mega Corp']),
         ('Total Sales', [150, 200, 75, 300]),
         ('Country', ['US', 'UK', 'US', 'US'])]
df = pd.DataFrame.from_dict(dict(sales))
print(df)

df=df.rename(columns = {'account':'Agent', 'Total Sales':'Sales Amount'})
print(df)

print(df.Country.unique())

grouped = df.groupby('Country', axis=0)
#print(grouped['Sales Amount'].mean())

for name,group in grouped:
    print(name)
    print(group)
    #print(group['Sales Amount'])