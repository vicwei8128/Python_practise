import pandas as pd
import numpy as np
import timeit

passengers = pd.read_csv("Datasets/titanic.csv")

#做法1
def count():
    return passengers[passengers['Survived'] == 1].Sex.count()

#做法2
def sum():
    return  (passengers.Survived==1).sum()

#做法3
def value_counts():
    alive=passengers.Survived.value_counts()    
    return alive[1]

#做法4
def in1d():
    return np.in1d(passengers.Survived, 1).sum()

print(count())
print(sum())
print(value_counts())
print(in1d())

t1=timeit.Timer("count()", 'from __main__ import count')
print("count執行時間:\t\t\t%f" % t1.timeit(1))

t2=timeit.Timer("sum()", 'from __main__ import sum')
print("sum執行時間:\t\t\t%f" % t2.timeit(1))

t3=timeit.Timer("value_counts()", 'from __main__ import value_counts')
print("value_counts執行時間:\t\t%f" % t3.timeit(1))

t4=timeit.Timer("in1d()", 'from __main__ import in1d')
print("in1d執行時間:\t\t\t%f" % t4.timeit(1))

