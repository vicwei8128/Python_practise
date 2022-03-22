import pandas as pd

sales = [('account', ['Jones LLC', 'Alpha Co', 'Blue Inc', 'Mega Corp']),
         ('Total Sales', [150, 200, 75, 300]),
         ('Country', ['US', 'UK', 'US', 'US'])]
df = pd.DataFrame.from_dict(dict(sales))
print(df)

df["rate"] = 0.02
#print(df)

df.loc[df["Total Sales"] > 100, ["rate"]] = .05
print(df)

df=df.drop("account", axis=1)
print(df)

#df["commission"] = df["Total Sales"] * df["rate"]
#print(df)
