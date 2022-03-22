from sklearn.model_selection import TimeSeriesSplit
import matplotlib.pyplot as plt 
import pandas as pd

series = pd.read_csv(r'Datasets\sunspots.csv', header=0, index_col=0)
print(series)

X = series.values
splits = TimeSeriesSplit(n_splits=3)
plt.figure(1)

index = 1
for train_index, test_index in splits.split(X):
	train = X[train_index]
	test = X[test_index]
	print('Observations: %d' % (len(train) + len(test)))
	print('Training Observations: %d' % (len(train)))
	print('Testing Observations: %d' % (len(test)))
	plt.subplot(310 + index)
	plt.plot(train)
	plt.plot([None for i in train] + [x for x in test])
	index += 1
plt.show()