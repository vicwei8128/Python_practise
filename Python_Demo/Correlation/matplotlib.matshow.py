import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame({'a': np.random.randint(0, 50, 1000)})
df['b'] = df['a'] + np.random.normal(0, 10, 1000)               # positively correlated with 'a'
df['c'] = 100 - df['a'] + np.random.normal(0, 5, 1000)          # negatively correlated with 'a'
df['d'] = np.random.randint(0, 50, 1000)                        # not correlated with 'a' : do not change in value

plt.matshow(df.corr())
plt.xticks(range(len(df.columns)), df.columns)
plt.yticks(range(len(df.columns)), df.columns)
plt.colorbar()
plt.show()
