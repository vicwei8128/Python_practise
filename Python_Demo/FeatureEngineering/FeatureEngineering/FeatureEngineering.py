# Beginner's Guide to Feature Selection in Python(https://www.datacamp.com/community/tutorials/feature-selection-python)

import pandas as pd
import numpy as np

# load data
data = pd.read_csv(r"Datasets\diabetes.csv")
print(data.head())

array = data.values
X = array[:,0:8]
Y = array[:,8]

# Feature extraction using SelectKBest
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2

test = SelectKBest(score_func=chi2, k=4)
fit = test.fit(X, Y)

# Summarize scores
np.set_printoptions(precision=3)
print(fit.scores_)

features = fit.transform(X)
# Summarize selected features
print(features[0:5,:])

# Feature extraction using RFE
from sklearn.feature_selection import RFE
from sklearn.linear_model import LogisticRegression

model = LogisticRegression()
rfe = RFE(model, 3)
fit = rfe.fit(X, Y)
print("Num Features: %s" % (fit.n_features_))
print("Selected Features: %s" % (fit.support_))
print("Feature Ranking: %s" % (fit.ranking_))

# Feature extraction using Linear Regression
from sklearn.linear_model import LinearRegression

linreg = LinearRegression()
linreg.fit(X,Y)

# A helper method for pretty-printing the coefficients
def pretty_print_coefs(coefs, names = None):
    if names == None:
        names = ["X%s" % x for x in range(len(coefs))]
    lst = zip(coefs, names)
    return " + ".join("%s * %s" % (round(coef, 3), name)
                                   for coef, name in lst)

print ("Linear Regression model:", pretty_print_coefs(linreg.coef_))

# Feature extraction using Ridge
from sklearn.linear_model import Lasso

lasso = Lasso(alpha=0.01)
lasso.fit(X,Y)

# A helper method for pretty-printing the coefficients
def pretty_print_coefs(coefs, names = None):
    if names == None:
        names = ["X%s" % x for x in range(len(coefs))]
    lst = zip(coefs, names)
    return " + ".join("%s * %s" % (round(coef, 3), name)
                                   for coef, name in lst)

print ("LASSO model:", pretty_print_coefs(lasso.coef_))

# Feature extraction using Ridge
from sklearn.linear_model import Ridge

ridge = Ridge(alpha=1.0)
ridge.fit(X,Y)

# A helper method for pretty-printing the coefficients
def pretty_print_coefs(coefs, names = None):
    if names == None:
        names = ["X%s" % x for x in range(len(coefs))]
    lst = zip(coefs, names)
    return " + ".join("%s * %s" % (round(coef, 3), name)
                                   for coef, name in lst)

print ("Ridge model:", pretty_print_coefs(ridge.coef_))