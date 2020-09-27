import pandas as pd
import pickle
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

dataset = pd.read_csv('./dataset/weight-height.csv')
X = dataset[['Weight']].values
y = dataset[['Height']].values


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=1/3)
regressor = LinearRegression()
regressor.fit(X_train, y_train)

filename = 'model.pkl'
pickle.dump(regressor, open(filename, 'wb'))
print('Model saved as {}'.format(filename))
