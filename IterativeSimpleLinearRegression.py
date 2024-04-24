import os
import numpy as np
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import time

dir = "clean/"
total_train_mse = 0
total_test_mse = 0
total_stocks = 0
average_train_mse = 0
average_test_mse = 0
start_time = time.time()
end_time = 0
total_time = 0

for file in os.listdir(dir):
    train_mse = 0
    test_mse = 0
    noise = ""
    filename = dir + str(file)
    symbol = str(file).removesuffix('.us.csv')
    #Get the data and load it into a dataframe
    data = pd.read_csv(filename)
    dataframe = pd.DataFrame(data)
    # Divide the data into X and y
    X = dataframe[['Open']]
    y = dataframe[['Close']]
    
    # Split the data
    from sklearn.model_selection import train_test_split
    X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.2, random_state=1)
    
    # Train the model
    from sklearn.linear_model import LinearRegression
    lr_stocks = LinearRegression()
    lr_stocks.fit(X_train, y_train)

    print('----------------------------------------------------------------------------------')
    
    from sklearn.metrics import mean_squared_error
    train_mse = mean_squared_error(y_train, lr_stocks.predict(X_train))
    print('The training MSE of the regression task for stock ' + symbol.upper() +  ' is:',train_mse)
    total_train_mse += train_mse

    test_mse = mean_squared_error(y_test, lr_stocks.predict(X_test))
    print('The test MSE of the regression task for stock ' + symbol.upper() +  ' is:', test_mse)
    total_test_mse += test_mse
    
    total_stocks += 1
    
end_time = time.time()

#print the average MSE
average_train_mse = total_train_mse / total_stocks
average_test_mse = total_test_mse / total_stocks

print('----------------------------------------------------------------------------------')
print('Over ' + str(total_stocks) + ' total stocks, the average training MSE for this model is:', average_train_mse)
print('Over ' + str(total_stocks) + ' total stocks, the average test MSE for this model is:', average_test_mse)
print('This model took ' + str(end_time - start_time) + ' seconds to complete the projection.')
print('----------------------------------------------------------------------------------')
