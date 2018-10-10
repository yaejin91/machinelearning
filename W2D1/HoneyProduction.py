import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression


df = pd.read_csv("https://s3.amazonaws.com/codecademy-content/programs/data-science-path/linear_regression/honeyproduction.csv")

#print(df.head())

#Use the .groupby() method provided by pandas to get the mean of totalprod per year.
prod_per_year = df.groupby("year").totalprod.mean().reset_index()

#Create a variable called X that is the column of years in this prod_per_year DataFrame.
X = df["year"].values.reshape(-1,1)

#Create a variable called y that is the totalprod column in the prod_per_year dataset.
y = df["totalprod"]

#Using plt.scatter(), plot y vs X as a scatterplot.
plt.scatter(X,y,alpha=0.8)

#Create a linear regression model from scikit-learn and call it regr.
regr = LinearRegression()

#Fit the model to the data by using .fit(). You can feed X into your regr model by passing it in as a parameter of .fit().
regr.fit(X,y)

#After you have fit the model, print out the slope of the line and the intercept of the line
#print(regr.coef_)
#print(regr.intercept_)

#Create a list called y_predict that is the predictions your regr model would make on the X data.
y_predict = regr.predict(X)

#Plot y_predict vs X as a line, on top of your scatterplot using plt.plot().
plt.scatter(X,y_predict,alpha=0.2)

#create a NumPy array called X_future that is the range from 2013 to 2050
X_future = np.array(range(2013,2051))
X_future = X_future.reshape(-1,1)

#Create a list called future_predict that is the y-values that your regr model would predict for the values of X_future.
future_predict = regr.predict(X_future)

#Plot future_predict vs X_future on a different plot.
plt.scatter(X_future,future_predict)
plt.show()


