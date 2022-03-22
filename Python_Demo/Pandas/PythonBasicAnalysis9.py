import pandas as pd
import numpy as np

df = pd.DataFrame({'Value':[10,100,40] })
#print (df)

df['Value'] = df['Value'].mask(df['Value'] < 90, np.nan)
print (df)
