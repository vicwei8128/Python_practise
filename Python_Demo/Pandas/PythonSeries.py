import pandas as pd
import numpy as np

series = pd.Series([20, 21, 12], index=['London', 'New York','Helsinki'])
print(series)

def square(x):
    return x**2
print(series.apply(square))

print(series.apply(lambda x: x*10))

def subtract_custom_value(x, custom_value):
    return x-custom_value

print(series.apply(subtract_custom_value, args=(5,)))

def subtract_custom_values(x, *custom_value):
    return x-sum(custom_value)

print(series.apply(subtract_custom_values, args=(1,2)))


def add_custom_values(x, **kwargs):
    for month in kwargs:
        x+=kwargs[month]
    return x
print(series.apply(add_custom_values, june=30, july=20, august=25))

print(series.apply(np.log))
