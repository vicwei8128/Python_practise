#Regularization with Ridge, Lasso, and Elastic Net Regressions(https://towardsdatascience.com/what-is-regularization-and-how-do-i-use-it-f7008b5a68c6)

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error, mean_squared_log_error
from sklearn.linear_model import Lasso
from sklearn.linear_model import Ridge
from sklearn.model_selection import GridSearchCV
from sklearn.datasets import load_boston 

def pretty_print_coefs(coefs, names = None):
    if names == None:
        names = ["X%s" % x for x in range(len(coefs))]
    lst = zip(coefs, names)
    return " + ".join("%s * %s" % (round(coef, 3), name)
                                   for coef, name in lst)

#load in a data set
data = load_boston()

#View description of data
#print(data.DESCR)

# Create Dataframe of data
df = pd.DataFrame(data=data.data,columns=data.feature_names)
df['target'] = data.target

#preview data
print(df.head())

#check to see if there are any null values in data set
print(df.isnull().sum())

#checking data types
print(df.info())

#Split data into target variable (Y) and observable variables (X)
Y = df.target
X = df.drop(columns='target')

#split data into test and train datasets
x_train,x_test,y_train,y_test = train_test_split(X, Y, random_state=10)

# Create Scaler Object
scaled_data = StandardScaler()

# Fit and transform Data to Scaler Object
x_train_scaled = scaled_data.fit_transform(x_train)
x_test_scaled = scaled_data.transform(x_test)

# Print separator dashes and view data
print('-'*100)
print('Transformed Data')
print(pd.DataFrame(x_train_scaled, columns=data.feature_names).head())

# Fit the model
linreg = LinearRegression()
linreg.fit(x_train_scaled, y_train)

# Print R2 and MSE for training and test sets round to the nearest .001
print(f'Linear Regression')
print(f'Training r^2: {linreg.score(x_train_scaled, y_train):.3f}')
print(f'Test r^2: {linreg.score(x_test_scaled, y_test): .3f}')
print(f'Training MSE: {mean_squared_error(y_train, linreg.predict(x_train_scaled)): .3f}')
print(f'Test MSE: {mean_squared_error(y_test, linreg.predict(x_test_scaled)): .3f}')

# Lasso is also known as the L1 norm 
# Default alpha value is 1
lasso = Lasso(alpha=1,random_state=1) 
lasso.fit(x_train_scaled, y_train)

##See how many variables were removed
#print(f'There are {len(lasso.coef_)} total parameters')
#print(f'There have been {sum((abs(lasso.coef_) > 0))} features removed with an alpha value of {lasso.alpha}')
#print(f'There are {100 - sum(abs(lasso.coef_) < 10**(-10))/ len(lasso.coef_)*100:.3}% of the original parameters')
#print('-'*100)

# Print R2 and MSE for training and test sets round to the nearest .001
print("")
print(f'Lasso, alpha=1')
print(f'Training r^2: {lasso.score(x_train_scaled, y_train):.3f}')
print(f'Test r^2: {lasso.score(x_test_scaled, y_test): .3f}')
print(f'Training MSE: {mean_squared_error(y_train, lasso.predict(x_train_scaled)): .3f}')
print(f'Test MSE: {mean_squared_error(y_test, lasso.predict(x_test_scaled)): .3f}')

# Ridge is also known as the L2 norm
# Alpha default is 1.0
ridge = Ridge(alpha= 1,random_state = 1)
ridge.fit(x_train_scaled, y_train)

print("")
print(f'Ridge, alpha=1')
print(f'Training r^2: {ridge.score(x_train_scaled, y_train):.3f}')
print(f'Test r^2: {ridge.score(x_test_scaled, y_test): .3f}')
print(f'Training MSE: {mean_squared_error(y_train, ridge.predict(x_train_scaled)): .3f}')
print(f'Test MSE: {mean_squared_error(y_test, ridge.predict(x_test_scaled)): .3f}')

#Finding Optimized Lasso Alpha Value
# Create an array of alpha values to test
# Start np.linspace value is 10**-10 because a value of 0 throws warnings
alphas = np.logspace(-10, 1, 1000,base=10)

# Create dictionary key,value pair of alpha values
tuned_parameters = [{'alpha': alphas}]

# Specify number of folds for cross_validation
#n_folds = 5

# Create grid search instance using desired variables
clf_lasso = GridSearchCV(lasso, tuned_parameters, cv=5, refit=True)
clf_lasso.fit(x_train_scaled, y_train)
lasso_scores = clf_lasso.cv_results_['mean_test_score']

# Plot the results
plt.figure().set_size_inches(8, 6)
plt.plot(alphas, lasso_scores)
plt.xlabel('Alpha Value')
plt.ylabel('Model CV Score')
plt.title('Lasso Regression Alpha Demonstration')
plt.axvline(clf_lasso.best_params_['alpha'], color='k', linestyle='--')
print("")
print(f'The optimal alpha value is :{clf_lasso.best_params_["alpha"]} - found by GridSearch')
plt.show()

### Creating Optimized Lasso Regression

lasso_optimized_alpha = clf_lasso.best_params_['alpha']

# Default alpha value is 1
lasso = Lasso(alpha=lasso_optimized_alpha,random_state=1) 
lasso.fit(x_train_scaled, y_train)

## See how many variables were removed
print(f'Lasso, alpha={lasso_optimized_alpha}')
#print(f'There are {len(lasso.coef_)} total parameters')
#print(f'There have been {sum((abs(lasso.coef_) > 0))} features removed with an alpha value of {lasso.alpha}')
#print(f'There are {100 - sum(abs(lasso.coef_) < 10**(-10))/ len(lasso.coef_)*100:.4}% of the original parameters')
#print('-'*100)

# Print R2 and MSE for training and test sets round to the nearest .001
print(f'Training r^2: {lasso.score(x_train_scaled, y_train):.3f}')
print(f'Test r^2: {lasso.score(x_test_scaled, y_test): .3f}')
print(f'Training MSE: {mean_squared_error(y_train, lasso.predict(x_train_scaled)): .3f}')
print(f'Test MSE: {mean_squared_error(y_test, lasso.predict(x_test_scaled)): .3f}')
print ("Lasso model:", pretty_print_coefs(lasso.coef_))

# Create an array of alpha values to test
alphas = np.logspace(-1, 1.5, 500,base=10)

# Create a Ridge model instance
ridge = Ridge(random_state=0, max_iter=10000,alpha=alphas)

# Create dictionary key,value pair of alpha values
tuned_parameters = [{'alpha': alphas}]

# Specify number of folds for cross_validation
#n_folds = 5

# Create grid search instance using desired variables
clf_ridge = GridSearchCV(ridge, tuned_parameters, cv=5, refit=False)
clf_ridge.fit(x_train_scaled, y_train)
ridge_scores = clf_ridge.cv_results_['mean_test_score']

# Plot the Figure
plt.figure().set_size_inches(8, 6)
plt.plot(alphas, ridge_scores)
plt.xlabel('Alpha Value')
plt.ylabel('Cross Validation Score')
plt.title('Ridge Regression Alpha Demonstration')
plt.axvline(clf_ridge.best_params_['alpha'], color='black', linestyle='--')
print("")
print(f'The optimal alpha value is: {clf_ridge.best_params_["alpha"]} - found by GridSearch')
plt.show()

# Set alpha = optimized alpha value
ridge_optimized_alpha = clf_ridge.best_params_['alpha']

# Default alpha value is 1
ridge = Ridge(alpha=ridge_optimized_alpha,random_state=1) 
ridge.fit(x_train_scaled, y_train)

## Print R2 and MSE for training and test sets round to the nearest .001
print(f'Ridge, alpha={ridge_optimized_alpha}')
#print(f'There are {len(ridge.coef_)} total parameters')
#print(f'There have been {sum((abs(ridge.coef_) > 0))} features removed with an alpha value of {ridge.alpha}')
#print(f'There are {100 - sum(abs(ridge.coef_) < 10**(-10))/ len(ridge.coef_)*100:.4}% of the original parameters')
#print('-'*100)

print(f'Training r^2: {ridge.score(x_train_scaled, y_train):.3f}')
print(f'Test r^2: {ridge.score(x_test_scaled, y_test): .3f}')
print(f'Training MSE: {mean_squared_error(y_train, ridge.predict(x_train_scaled)): .3f}')
print(f'Test MSE: {mean_squared_error(y_test, ridge.predict(x_test_scaled)): .3f}')
print ("Ridge model:", pretty_print_coefs(ridge.coef_))

# Simple Linear Regression
print("")
print('*'*100)
print('Simple Linear Regression - using test data')
print(f'Test r^2: {linreg.score(x_test_scaled, y_test): .3f}')
print(f'Test MSE: {mean_squared_error(y_test, linreg.predict(x_test_scaled)): .3f}')
print(f'Number of model features: {linreg.n_features_in_}')
print ("Linear Regression model:", pretty_print_coefs(linreg.coef_))
print('*'*100)

# Lasso Regression 
print('Lasso Regression - using test data')
print(f'Test r^2: {lasso.score(x_test_scaled, y_test): .3f}')
print(f'Test MSE: {mean_squared_error(y_test, lasso.predict(x_test_scaled)): .3f}')
print(f'Number of model features: {lasso.n_features_in_}')
print ("Ridge model:", pretty_print_coefs(lasso.coef_))

print('*'*100)

# Ridge Regression
print('Ridge Regression - using test data')
print(f'Test r^2: {ridge.score(x_test_scaled, y_test): .3f}')
print(f'Test MSE: {mean_squared_error(y_test, ridge.predict(x_test_scaled)): .3f}')
print(f'Number of model features: {ridge.n_features_in_}')
print ("Ridge model:", pretty_print_coefs(ridge.coef_))

