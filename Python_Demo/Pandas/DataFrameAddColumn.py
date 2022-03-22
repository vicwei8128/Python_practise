import pandas as pd
import numpy

data = {'Country': ['Belgium',  'India',  'Brazil'],
    'Capital': ['Brussels',  'New Delhi',  'Brasilia'],
    'Population': [11190846, 1303171035, 207847528]}

df = pd.DataFrame(data,columns=['Country',  'Capital',  'Population'])

describe=df.describe()
print(type(describe))

#做法1 - 將欄位加入到現有欄位的後面
#describe["id"]=numpy.arange(0, len(describe.index))

#做法2 - 將欄位加入到指定的位置
#describe.insert(0, "id", numpy.arange(0, len(describe.index)))

#做法3 - 建立新的DataFrame並附予欄位名稱
df=pd.DataFrame(describe, columns=["Metric", "Value"])
df["Metric"] =describe.index
df["Value"] = describe.values
print(df)

#做法4 - 存成CSV檔再讀回來最左方會多一個欄位
describe.to_csv("describe.csv")
describe=pd.read_csv("describe.csv")

#指定欄位名稱
describe.columns=["Metric", "Value"]
print(describe)


