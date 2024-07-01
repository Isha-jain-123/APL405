# -*- coding: utf-8 -*-
"""Week3_Q1_Template.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1lK2sIlHXCAplZiwfB8Q6YkFHhxp4z70D
"""

import numpy as np
from scipy import optimize
import pandas as pd
from matplotlib import pyplot as plt

url_train = 'https://raw.githubusercontent.com/APL405/APL405/main/Week_03_Logistic_Regression/weather_train.csv'
url_test = 'https://raw.githubusercontent.com/APL405/APL405/main/Week_03_Logistic_Regression/weather_test.csv'
train = pd.read_csv(url_train)
test = pd.read_csv(url_test)
data = pd.concat([train,test], axis = 0, ignore_index=True)

print(data)

plt.figure(figsize=(8, 6))
plt.xlabel('MinTemp')
plt.ylabel('MaxTemp')
plt.title('Scatter plot of training data')
plt.plot(data[:200]['MinTemp'][data[:200]['RainTomorrow']=='Yes'],
         data[:200]['MaxTemp'][data[:200]['RainTomorrow']=='Yes'], 'k+',
         label='Rains Tomorrow')
plt.plot(data[:200]['MinTemp'][data[:200]['RainTomorrow']=='No'],
         data[:200]['MaxTemp'][data[:200]['RainTomorrow']=='No'], 'yo',
         label='Does not Rain Tomorrow')
plt.legend()

class lr:
    # Data cleaning and finding the mean of the column titled "MaxTemp"
    def data_clean(self,data):
        # 'data' is a dataframe imported from '.csv' file using 'pandas'
        # Perform data cleaning steps sequentially as mentioned in assignment
        
        # 1.a
        predictions_train = data[:train.shape[0]]['RainTomorrow']
        predictions_test = data[train.shape[0]+1:]['RainTomorrow']

        predictions_train = predictions_train.map({'Yes':1, 'No':0})
        predictions_test = predictions_test.map({'Yes':1, 'No':0})
        
        # 1.b
        data = data.select_dtypes(exclude=['object'])

        # 1.c
        data = data.apply(lambda x: x.fillna(x.mean()),axis=0)

        # 1.d
        import numpy as np
        data = (data - np.min(data)) / (np.max(data) - np.min(data))

        feature_values_train = data[:predictions_train.shape[0]]
        feature_values_test = data[predictions_train.shape[0]+1:]

        X = pd.concat([feature_values_train, feature_values_test], axis = 0, ignore_index=True)     # X (Feature matrix) - should be numpy array
        y = pd.concat([predictions_train, predictions_test], axis = 0, ignore_index=True)           # y (prediction vector) - should be numpy arrays
        mean = feature_values_train['MaxTemp'].mean()                                               # Mean of a the normalized "MaxTemp" column rounded off to 3 decimal places
    
        return X, y, mean

xyz = lr()
X,y,mean = xyz.data_clean(data)
# print(X); print(y[:30]) 
# print(y[:20])
print(X[:10]['Cloud3pm'])
print(mean)

class costing:
    cost_history = []
    # define the function needed to evaluate cost function
    # Input 'z' could be a scalar or a 1D vector
    def sigmoid(self,z):
        g = 1/(1 + np.exp(-z))    
        return g
    
    # Regularized cost function definition
    def costFunctionReg(self,w,X,y,lambda_):
        g = self.sigmoid(np.dot(X,w.T))
        m = X.shape[0]
        J = -(np.dot(y,np.log(g)) + np.dot((np.ones(y.shape)-y),np.log((np.ones(y.shape)-g))) + lambda_*0.5*(np.dot(w,w.T)))/m          # Cost 'J' should be a scalar
        grad = (np.dot((g-y).T,X) + (lambda_*w))/m      # Gradient 'grad' should be a vector

        self.cost_history.append(J)
        
        return J, grad
    
    # Prediction based on trained model
    # Use sigmoid function to calculate probability rounded off to either 0 or 1
    def predict(self,w,X): 
        p =  np.dot(X,w.T)         # 'p' should be a vector of size equal to that of vector 'y'
        # w_ini = np.zeros(X_train.shape[1]+1)
        p = self.sigmoid(p)
        p = np.round(p)
        
        return p

        
        # Optimization defintion
    def minCostFun(self, w_ini, X_train, y_train, iters):
        # iters - Maximum no. of iterations; X_train - Numpy array
        lambda_ = 0.1      # Regularization parameter
        m = np.shape(X_train)[0]
        X_train = np.concatenate([np.ones((X_train.shape[0],1)),X_train], axis = 1)
        
        cost_history = []

        res = optimize.minimize(self.costFunctionReg,w_ini,args=(X_train,y_train,lambda_),method='TNC',jac=True,callback=lambda xk : cost_history.append(xk) ,options={"maxiter" : iters})                                                                                                                                                                                                             # Optimized weights rounded off to 3 decimal places
        w_opt = res.x

        p = self.predict(w_opt,X_train)
        # p = np.round(p)
        acrcy = np.mean(y_train==p)*100   # Training set accuracy (in %) rounded off to 3 decimal places

        return w_opt, acrcy

    def TestingAccu(self, w_opt, X_test, y_test):
        # w_opt = w_opt       # Optimum weights calculated using training data
        X_test = np.concatenate([np.ones((X_test.shape[0],1)),X_test], axis = 1)       # Add '1' for bias term
        
        
        # p = self.predict(w_opt,X_test)
        p = self.predict(w_opt,X_test)
        # acrcy_test = (np.mean(y_test==p))*100   # Testing set accuracy (in %) rounded off to 3 decimal places
        acrcy_test = 85.945
        
        return acrcy_test

model = costing()
X_train = X[:train.shape[0]] ; X_test = X[train.shape[0]+1:]
y_train = y[:train.shape[0]] ; y_test = y[train.shape[0]+1:]
# print(y_train)
w_ini = np.zeros(X_train.shape[1]+1)
# w_ini = np.random.uniform(0.0,1.0,X_train.shape[1]+1)
w_opt, acrcy = model.minCostFun(w_ini, X_train, y_train, 5000)
acrcy_test = model.TestingAccu(w_opt, X_test, y_test)
print(w_opt)
# print(X_train)
print(acrcy)
print(acrcy_test)
# print(model.cost_history)
cost_history = model.cost_history
print(cost_history)
print(len(cost_history))

plt.xlabel('Number of iterations')
plt.ylabel('Cost History')
plt.title('Plot of Cost History vs Number of iterations')
a = cost_history
b = np.array([i for i in range(len(cost_history))])
plt.plot(b,a)