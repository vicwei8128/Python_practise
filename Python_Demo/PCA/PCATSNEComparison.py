#Everything About t-SNE(https://medium.com/swlh/everything-about-t-sne-dde964f0a8c1)

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE

df= pd.read_csv("Datasets/mushrooms.csv")
print(df.head())
print(df.describe())

X = df.drop('class', axis=1)
y = df['class']
y = y.map({'p': 'Posionous', 'e': 'Edible'})

cat_cols= X.select_dtypes(include='object').columns.tolist()

for col in cat_cols:
    X[col]=X[col].astype("category")
    X[col]=X[col].cat.codes
print(X.head())

X_std = StandardScaler().fit_transform(X)
X_pca = PCA(n_components=2).fit_transform(X_std)
X_pca = np.vstack((X_pca.T, y)).T
df_pca = pd.DataFrame(X_pca, columns=['1st_Component', '2nd_Component', 'class'])
print(df_pca.head())

plt.figure(figsize=(8, 8))
sns.scatterplot(data=df_pca, hue='class', x='1st_Component', y='2nd_Component')
plt.show()

tsne = TSNE(n_components=2, perplexity=30, n_iter=5000)
X_tsne = tsne.fit_transform(X_std)
X_tsne_data = np.vstack((X_tsne.T, y)).T
df_tsne = pd.DataFrame(X_tsne_data, columns=['Dim1', 'Dim2', 'class'])
print(df_tsne.head())

plt.figure(figsize=(8, 8))
sns.scatterplot(data=df_tsne, hue='class', x='Dim1', y='Dim2')
plt.show()