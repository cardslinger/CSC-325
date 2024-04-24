import os
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.svm import LinearSVR
from sklearn.metrics import mean_squared_error
import warnings
import time

# Ignore warnings because the warnings thrown in this case are irrelevant and clutter results
warnings.filterwarnings("ignore")

dir = "clean/"
total_mse = 0
total_stocks = 0
noisy_stocks = 0
start_time = time.time()
end_time = 0

for file in os.listdir(dir):
    noise = ""
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
    svm_reg = LinearSVR(epsilon=0, random_state=23, dual=True, max_iter=100000)
    svm_reg.fit(X, y)
    # Get the prediction and calculate the MSE
    y_pred = svm_reg.predict(X)
    mse = mean_squared_error(y, y_pred)
    total_mse += mse
    total_stocks += 1
    # Print the result
    print('----------------------------------------------------------------------------------')
    print('The MSE of the regression task for stock ' + symbol.upper() +  ' is:', mse)

end_time = time.time()

#print the average MSE
average_mse = total_mse / total_stocks
print('----------------------------------------------------------------------------------')
print('Over ' + str(total_stocks) + ' total stocks, the average MSE for this model is:', average_mse)
print('This model took ' + str(end_time - start_time) + ' seconds to complete the projection.')
print('----------------------------------------------------------------------------------')