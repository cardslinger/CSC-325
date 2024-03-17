import os
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.svm import LinearSVR
from sklearn.metrics import mean_squared_error
import warnings
warnings.filterwarnings("ignore")

dir = "clean/"

for file in os.listdir(dir):
    filename = dir + str(file)
    symbol = str(file).removesuffix('.us.csv')
    #Get the data and load it into a dataframe
    data = pd.read_csv(filename)
    dataframe = pd.DataFrame(data)
    # Divide the data into X and y
    X = dataframe[['Open','High','Low']]
    y = dataframe[['Close']]
    #Convert y to an array so it will fit the model
    y = y['Close'].to_numpy()
    # Fit the data to the model
    svm_reg = LinearSVR(epsilon=1.5, random_state=23, dual=True, max_iter=100000)
    svm_reg.fit(X, y)
    # Get the prediction and calculate the MSE
    y_pred = svm_reg.predict(X)
    mse = mean_squared_error(y, y_pred)
    # Print the result
    print('The MSE of the regression task for stock ' + symbol +  ' is:', mse)
