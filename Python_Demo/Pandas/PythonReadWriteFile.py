import pandas as pd

dfCSV=pd.read_csv('DataFrame.csv')
print(dfCSV)
dfCSV.to_csv('NewDataFrame.csv')

writer = pd.ExcelWriter('DataFrame.xlsx')
dfCSV.to_excel(writer, sheet_name='MSIT117')
writer.save()

dfExcel = pd.read_excel('DataFrame.xlsx',  sheet_name="MSIT117")
print(dfExcel)
