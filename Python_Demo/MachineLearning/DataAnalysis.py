import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

passengers = pd.read_csv("Datasets/titanic.csv")
#passengers.info()

#p=passengers.dropna(axis=0, how='any', thresh=None, subset=None, inplace=False)
#print(p.head())

passengers["Age"]=passengers["Age"].fillna(passengers["Age"].median())
print(passengers)

def get_full_city_name(cityCode):
    if (cityCode == "S"):
        return "Southampton"
    elif (cityCode == "C"):
        return "Cherbourg"
    elif (cityCode == "Q"):
        return "Queenstown"

print(passengers["Embarked"].apply(get_full_city_name).head(10))

print(passengers["Fare"].describe())

alive=passengers['Survived'] == 1
print("alive:%d" % alive.sum())

print(passengers['Survived'].value_counts(normalize=True) * 100)

print(passengers[['Survived','Age']])
print(passengers[passengers.Survived == 1].Age.mean())

print(pd.crosstab(passengers.Sex, passengers.Survived))

sex_pivot = passengers.pivot_table(index="Sex",values="Survived")
sex_pivot.plot.bar()
plt.show()

print(pd.crosstab( passengers.Pclass, passengers.Survived ))

class_pivot = passengers.pivot_table(index="Pclass",values="Survived")
class_pivot.plot.bar()
plt.show()

print(passengers[ passengers.Age < 5 ]["Survived"].value_counts())

below5yearsold = passengers[(passengers.Age < 5) & (passengers.Survived ==1)]
print(below5yearsold.Age.count())

print(passengers.Embarked.unique())
port_map = {'S': 'Southampton', 'C': 'Cherbourg','Q':'Queenstown'}
passengers['Embarked'] = passengers['Embarked'].map(port_map)
print(passengers.Embarked.unique())
print(passengers.Embarked.value_counts())

sexMap={"female":0, "male":1}
passengers.Sex=passengers.Sex.map(sexMap)
print(passengers.head(10))

top10 = passengers[0:10]
print(top10)

top103col = passengers.iloc[0:10,0:3]
print(top103col)

last5 = passengers[-5:]
print(last5)

top5selectedcolumn=passengers[ ( passengers.Survived == 1 ) & ( passengers.Age < 5 ) ][['Age', 'Sex', 'Pclass']][0:5]
print(top5selectedcolumn)

plt.hist( passengers.Age )
plt.show()

def process_age(df,cut_points,label_names):
    df["Age"] = df["Age"].fillna(-0.5)
    df["AgeRange"] = pd.cut(df["Age"],cut_points,labels=label_names)
    return df

cut_points = [-1,0,5,12,18,35,60,100]
label_names = ["Missing","Infant","Child","Teenager","Young Adult","Adult","Senior"]

train = process_age(passengers,cut_points,label_names)

train.groupby("AgeRange")["PassengerId"].agg(['count']).plot(kind='bar', figsize=(8, 6))
plt.show()

survived_sex = passengers[passengers['Survived']==1]['Sex'].value_counts()
dead_sex = passengers[passengers['Survived']==0]['Sex'].value_counts()
df = pd.DataFrame([survived_sex,dead_sex])
df.index = ['Survived','Dead']
df.plot(kind='bar',stacked=True, figsize=(8,6))
plt.show()

figure = plt.figure(figsize=(8,6))
plt.hist([passengers[passengers['Survived']==1]['Age'], passengers[passengers['Survived']==0]['Age']], stacked=True, color = ['g','r'],
         bins = 30,label = ['Survived','Dead'])
plt.xlabel('Age')
plt.ylabel('Number of passengers')
plt.legend()
plt.show()

figure = plt.figure(figsize=(8,6))
plt.hist([passengers[passengers['Survived']==1]['Fare'],passengers[passengers['Survived']==0]['Fare']], stacked=True, color = ['g','r'],
         bins = 30,label = ['Survived','Dead'])
plt.xlabel('Fare')
plt.ylabel('Number of passengers')
plt.legend()
plt.show()

figure = plt.figure(figsize=(8,6))
plt.hist([passengers[passengers['Survived']==1]['Pclass'],passengers[passengers['Survived']==0]['Pclass']], stacked=True, color = ['g','r'],
         bins = 30,label = ['Survived','Dead'])
plt.xlabel('Pclass')
plt.ylabel('Number of passengers')
plt.legend()
plt.show()

plt.figure(figsize=(8,6))
ax = plt.subplot()
ax.scatter(passengers[passengers['Survived']==1]['Age'],passengers[passengers['Survived']==1]['Fare'],c='green',s=40)
ax.scatter(passengers[passengers['Survived']==0]['Age'],passengers[passengers['Survived']==0]['Fare'],c='red',s=40)
ax.set_xlabel('Age')
ax.set_ylabel('Fare')
ax.legend(('survived','dead'),scatterpoints=1,loc='upper right',fontsize=15)
plt.show()

plt.figure(figsize=(8,5))
ax = plt.subplot(2,1,1)
ax.scatter(passengers[passengers['Survived']==1]['Age'],passengers[passengers['Survived']==1]['Fare'],c='green',s=40)
ax.set_xlabel('Age')
ax.set_ylabel('Fare')
ax.legend(('survived',''),scatterpoints=1,loc='upper right',fontsize=15)

ax = plt.subplot(2,1,2)
ax.scatter(passengers[passengers['Survived']==0]['Age'],passengers[passengers['Survived']==0]['Fare'],c='red',s=40)
ax.set_xlabel('Age')
ax.set_ylabel('Fare')
ax.legend(('dead',''),scatterpoints=1,loc='upper right',fontsize=15)

plt.show()
