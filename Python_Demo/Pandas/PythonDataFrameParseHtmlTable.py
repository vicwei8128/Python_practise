import pandas as pd

url = 'http://www.stockq.org/market/asia.php'
df=pd.read_html(url, encoding="utf-8")[4]

print(df)

df.to_csv("StockQ.csv")
