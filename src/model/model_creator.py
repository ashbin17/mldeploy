#!/usr/bin/env python
"""Linear Regression model"""
# Importing libraries
import pandas as pd
import pickle
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
# Loding the dataset
data = pd.read_csv('./dataset/weight-height.csv')
# Preview of the data
data.head()
# Selecting x's and y's
X = data[['Weight']].values
y = data[['Height']].values
# Splitting the data to test and train
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=1/3)
# Creating a LinearRegression object and fitting the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=1/3)
regressor = LinearRegression()
regressor.fit(X_train, y_train)
# Testing the model
heights = [161,187,195,156]
prediction = [regressor.predict([[height]]) for height in heights]
prediction = [round(float(weight[0][0]),2) for weight in prediction]
print("Predicted weights:",end='')
print(prediction)
# Saving the model to a file
try:
    filename = 'model.pkl'
    pickle.dump(regressor, open(filename, 'wb'))
    print('Model saved as {}'.format(filename))
except Exception as e:
    print("Something went wrong when writing to the file")
    print(e)
