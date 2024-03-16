import os
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dir = "clean/"

for file in os.listdir(dir):
    filename = dir + str(file)
    symbol = str(file).removesuffix('.us.txt')
    data = pd.read_csv(filename)
    dataframe = pd.DataFrame(data)
    dataframe.pop('Date')
    dataframe.pop('Volume')
    dataframe.pop('OpenInt')
    print(dataframe.head())
    break
