import pandas as pd
import numpy as np

url = 'http://bit.ly/drinksbycountry'
#url = 'Datasets/drinks.csv'

drinks = pd.read_csv(url)
#print(drinks)

#drinks=drinks.sort_values(by="beer_servings")
#print(drinks)
#print(drinks.query("beer_servings > 100"))

#print(drinks[["beer_servings", "spirit_servings", "wine_servings"]].apply(lambda row:np.mean(row)))

#print(drinks.loc[:, 'beer_servings':'wine_servings'].apply(max, axis=0))
#print(drinks.loc[:, 'beer_servings': 'wine_servings'].applymap(float))

sort_beer=drinks.sort_values("beer_servings", ascending=0)
print(sort_beer[["country", "beer_servings"]].iloc[:1,:2])

sort_beer=drinks.sort_values("beer_servings", ascending=1)
print(sort_beer[["country", "beer_servings"]].iloc[:1,:2])

sort_spirit=drinks.sort_values("spirit_servings", ascending=0)
print(sort_spirit[["country", "spirit_servings"]].iloc[:1,:2])

sort_spirit=drinks.sort_values("spirit_servings", ascending=1)
print(sort_spirit[["country", "spirit_servings"]].iloc[:1,:2])

sort_wine=drinks.sort_values("wine_servings", ascending=0)
print(sort_wine[["country", "wine_servings"]].iloc[:1,:2])

sort_wine=drinks.sort_values("wine_servings", ascending=1)
print(sort_wine[["country", "wine_servings"]].iloc[:1,:2])

#url = 'http://bit.ly/kaggletrain'
###url = 'Datasets/titanic.csv'

#train = pd.read_csv(url)

##print(train.Sex)
#train['Sex'] = train['Sex'].map({'female': 1, 'male': 0})
#print(train.Sex)
