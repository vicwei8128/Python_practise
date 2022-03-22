#Interpret the key results for Correlation
#https://support.minitab.com/en-us/minitab-express/1/help-and-how-to/modeling-statistics/regression/how-to/correlation/
#interpret-the-results/

from scipy.stats import pearsonr

x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

corr, p_value = pearsonr(x, y)

print(corr)             #兩組資料的關聯為1(正相關)
print(p_value)          
print("")

y = [5, 6, 5, 6, 5]
corr, p_value = pearsonr(x, y)

print(corr)             #兩組資料的關聯為0(不相關)
print(p_value)          
print("")

y = [-1, -4, -8, -16, -25]
corr, p_value = pearsonr(x, y)

print(corr)             #兩組資料的關聯為-0.97(負相關)
print(p_value)   

