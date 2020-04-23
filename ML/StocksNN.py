#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 14 22:05:53 2019

@author: austinmccarson
"""
#import main libraries
import numpy as np
import pandas as pd
import talib

#random used to initialize seed to a fixed number
import random
random.seed(42)

#import the dataset then drop missing values
#only using open, high, low, and close data
dataset = pd.read_csv('RELIANCE.NS.csv')
dataset = dataset.dropna()
dataset = dataset[['Open', 'High', 'Low', 'Close']]

#prepare the dataset
#set up the features that will be used to train the neural network
#high minus low price, open minus close price, 3 day moving average, 10 day moving average,
#30 day moving average, standard deviation, Relative Strength Index, Williams %R
dataset['H-L'] = dataset['High'] - dataset['Low']
dataset['O-C'] = dataset['Open'] - dataset['Close']
dataset['3day MA'] = dataset['Close'].shift(1).rolling(window = 3).mean()
dataset['10day MA'] = dataset['Close'].shift(1).rolling(window = 10).mean()
dataset['30day MA'] = dataset['Close'].shift(1).rolling(window = 30).mean()
dataset['std_dev'] = dataset['Close'].rolling(5).std()
dataset['RSI'] = talib.RSI(dataset['Close'].values, timeperiod = 9)
dataset['Williams %R'] = talib.WILLR(dataset['High'].values, dataset['Low'].values, 
       dataset['Close'].values, 7)

#define output as price rise that is either a 1 or 0 depending on whether tomorrows closing price 
#is greater than todays closing price
dataset['Price Rise'] = np.where(dataset['Close'].shift(-1) > dataset['Close'], 1, 0)

#drop all of the rows containing NaN
dataset = dataset.dropna()

#prepare the input features, X, and the expected output features, Y. 
X = dataset.iloc[:, 4:-1]
Y = dataset.iloc[:, -1]

#split the dataset 80-20, train-test
split = int(len(dataset) * 0.8)
X_train, X_test, Y_train, Y_test = X[:split], X[split:], Y[:split], Y[:split]

#feature scaling
#standardize the dataset
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_fit = sc.transform(X_test)

#used to sequentially build the layers of the NN
from keras.models import Sequential
#build layers of artificial NN
from keras.layers import Dense
from keras.layers import Dropout

#instantiate Sequential into classifier
classifier = Sequential()
#add hidden layers into classifier
classifier.add(Dense(units = 128, kernel_initializer = 'uniform', activation = 'relu', input_dim = X.shape[1]))
#add a second hidden layer
classifier.add(Dense(units = 128, kernel_initializer = 'uniform', activation = 'relu'))
#add the output layer
classifier.add(Dense(units = 1, kernel_initializer = 'uniform', activation = 'sigmoid'))
#compile the classifier
classifier.compile(optimizer = 'adam', loss = 'mean_squared_error', metrics = ['accuracy'])
#fit the neural network to train the datasets
classifier.fit(X_train, Y_train, batch_size = 10, epochs = 100)

#predict and store result in y_pred.
#store 1 if the predicted value was greater than 0.5
y_pred = classifier.predict(X_test)
y_pred = (y_pred > 0.5)

#create new column in the dataset for y_pred
#store updated dataset in new dataset without the NaN values
dataset['y_pred'] = np.NaN
dataset.iloc[(len(dataset) - len(y_pred)):, -1:] = y_pred
trade_dataset = dataset.dropna()

#create new feature in dataset called tomorrow returns
#tomorrow returns is the strategy for taking a long position
#store in it the log returns of today
#then shift up one element so that tomorrows returns are stored against
#the prices of today
trade_dataset['Tomorrow Returns'] = 0
trade_dataset['Tomorrow Returns'] = np.log(trade_dataset['Close']/trade_dataset['Close'].shift(1))
trade_dataset['Tomorrow Returns'] = trade_dataset['Tomorrow Returns'].shift(-1)

#create new feature in dataset for strategy returns
#take a long position when the value of y is true and short when false
#store True for long or store negative of the return for short
trade_dataset['Strategy Returns'] = 0
trade_dataset['Strategy Returns'] = np.where(trade_dataset['y_pred'] == True, trade_dataset['Tomorrow Returns'], -trade_dataset['Tomorrow Returns'])

#compute the cumulative returns
trade_dataset['Cumulative Market Returns'] = np.cumsum(trade_dataset['Tomorrow Returns'])
trade_dataset['Cumulative Strategy Returns'] = np.cumsum(trade_dataset['Strategy Returns'])

#plot the graph
import matplotlib.pyplot as plt
plt.figure(figsize=(10,5))
plt.plot(trade_dataset['Cumulative Market Returns'], color = 'r', label = 'Market Returns')
plt.plot(trade_dataset['Cumulative Strategy Returns'], color = 'g', label = 'Strategy Returns')
plt.legend()
plt.show()
