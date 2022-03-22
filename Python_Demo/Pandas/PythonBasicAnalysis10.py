import pandas as pd

df = pd.read_csv("Datasets/Question.csv")
#print(df)

melted_data = pd.melt(df, value_vars=['素食?', '尾牙是否參加?'], 
                      var_name='question', value_name='answer')

print(melted_data.groupby(by=['question', 'answer'])['answer'].count())