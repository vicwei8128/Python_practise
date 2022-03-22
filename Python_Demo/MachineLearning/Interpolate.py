import pandas as pd
import numpy as np

salary=pd.Series([35000, np.nan, np.nan, np.nan, 100000])
expected_salary=salary.interpolate()
print(expected_salary)