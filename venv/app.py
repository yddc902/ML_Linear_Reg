import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data  = []
X = [0, 25, 20, 15, 10]  # temp in deg celsius
y = [0, 0, 0, 1, 1] # 0 for no, 1 for yes
data=pd.read_csv('data.csv')
X=data.iloc[:,:-1].values
y=data.iloc[:,1].values

#split dataset in train and testing set
from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=4,random_state=0)

from sklearn.linear_model import LinearRegression
regressor=LinearRegression()
regressor.fit(X_train,y_train)
y_pre=regressor.predict(X_test)



# Visualising the Training set results in a scatter plot
plt.scatter(X_train, y_train, color = 'red')
plt.plot(X_train, regressor.predict(X_train), color = 'blue')
#plt.title('Cricket Chirps vs Temperature (Training set)')
#plt.xlabel('Cricket Chirps (chirps/sec for the striped ground cricket) ')
#plt.ylabel('Temperature (in degrees Fahrenheit)')
plt.show()

# Visualising the test set results in a scatter plot
plt.scatter(X_test, y_test, color = 'red')
plt.plot(X_train, regressor.predict(X_train), color = 'blue')
plt.title('Cricket Chirps vs Temperature (Test set)')
plt.xlabel('Cricket Chirps (chirps/sec for the striped ground cricket) ')
plt.ylabel('Temperature (in degrees Fahrenheit)')
plt.show()