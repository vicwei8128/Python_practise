import numpy as np
import pandas as pd

df = pd.read_csv(r"Datasets\Pokemon.csv")
df.drop(labels="#", axis=1, inplace=True)
df.fillna(value="No Type", axis=1, inplace=True)
df.rename({'Type 1': 'type'}, inplace=True, axis=1)
print(df)

n_types = df['type'].nunique()
print("We have:",n_types, "differents pokemons types")

from sklearn.preprocessing import LabelEncoder, MinMaxScaler

encoder = LabelEncoder()
scaler = MinMaxScaler()

df['encoded_type'] = encoder.fit_transform(df['type'])
df['scaled_total'] = scaler.fit_transform(df[['Total']])

types = df['encoded_type']
total = df['scaled_total']

embedding_size = min(np.ceil((n_types)/2),50)           #Jeremy Howard suggest 

from keras.models import Sequential
from keras.layers import Dense, Embedding, Flatten

model = Sequential()
model.add(Embedding(input_dim=n_types,output_dim=int(embedding_size), input_length=1, name="poke_embedding"))
model.add(Flatten())
model.add(Dense(30, activation="relu"))
model.add(Dense(15, activation="relu"))
model.add(Dense(1, activation="linear"))

model.compile(optimizer="adam", loss="mse")
model.fit(x=types.values, y=total.values, epochs=30)

embedding_layer = model.get_layer(name="poke_embedding")
embedding_layer = pd.DataFrame(embedding_layer.get_weights()[0])
embedding_layer.columns = ['C1','C2','C3','C4','C5','C6','C7','C8','C9']
print(embedding_layer)

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d, Axes3D

types_names = list(encoder.inverse_transform([x for x in range(0,n_types)]))
xs = embedding_layer['C1']
ys = embedding_layer['C2']
zs = embedding_layer['C3']
fig = plt.figure(figsize=(8, 4))
ax = fig.add_subplot(111, projection='3d')
for index, embedding in embedding_layer.iterrows():
    x = embedding['C1']
    y = embedding['C2']
    z = embedding['C3']
    ax.scatter(x, y, z, color='b')
    ax.text(x, y, z, '%s' % (types[index]), size=9, zorder=1, color='k')
#plt.draw()
plt.show()
