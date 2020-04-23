#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  9 01:04:57 2018

This is software that will classify whether a business is profitable or not. 
It determines whether it will be profitable in the future and 
predicts the performance of how the business will do.
This is based upon past performance and thus, this program is subject to uncertainty.
Measurements for a healthy business were based upon Return on Equity.
Return on Equity is directly influenced by net income, assets, and debt.
ROE = net income/ shareholder equity ( = assets-debt )
Utilizing linear regression and classification, the program turns the interpreted information
   into useful projections of future performance
It is trained on the yearly reports of a company and then tested on more recent reports

Using multivariate linear regression, implemented using gradient descent
(possibly other algorithms), we can predict the future ROE for the company passed in.
Net income is dependent upon total revenue - (expenses + taxes)
Equity is determined by assets - liabilities(debt)
predict total revenue, expenses, taxes, assets, and liabilities then pass them into 
@author: Austin McCarson
"""
import matplotlib.pyplot as plt
import numpy
"""Software"""
class BusinessClassification  :

    
    #Train Machine Learning to identify a profitable business
    #Projected cash flow
    #Projected income, net expenses
    #Use statistics
    #Stock Trading volume
    
    def PruneData (inputFile) :
        # get data from input
        # net income, total expenses, revenue, taxes, different incomes, acquisitions, partners
        # field, 
        # Return on Equity && Return on Assets
        # Use set to store data, fast lookup, hash quarter name
        
        quarters = []
        
        file = open(inputFile, 'r')
        for line in file :
            #split: splits line values into array with indices with values
            #quarters appends the array into an array -> will be map 
            quarters.append(line.split(','))
        
        quarters.reverse()
        i = 0
        for quarter in quarters :        
            quarter[0] = "Q" + str(i)
            quarter[1] = str(quarter[2])
            quarter[1] = quarter[1].replace('%', '')
            del quarter[3], quarter[2]
            i+=1
        print(quarters)
        return quarters
        
        #find rate of change from quarter to quarter
    def quarterRateOfChange (quarters) :
        
        changesInPercent = []
        idx = 0
        
        while not idx+2 > len(quarters) :
            q1 = float(quarters[idx][1])
            q2 = float(quarters[idx+1][1])
            changesInPercent.append(q2/q1*100)
            idx+=1
        print(changesInPercent)
        return changesInPercent
    
    
    #plot figures for tracing 
    def PlottingFigures (quarters) :
        
        xdata = []
        ydata = []
        store = []
        quarterz = quarters
        i = 0
        
        #For plotting purposes: remove Q from each quarter.
        for quarter in quarters :
            store.append(quarter[0])
            quarter[0] = i
            i += 1
        
        #feed data to axes.
        for quarter in quarters : 
            xdata.append(quarter[0])
            ydata.append(quarter[1])
            
        plt.plot(xdata, ydata)
        plt.xlabel("Quarters")
        plt.ylabel("ROE")
        plt.title("Quarterly ROE")
        plt.show()
        
        
        #restore quarters for ease of reading for other classes/users
        for quarter in quarters :
            quarter[0] = "Q" + str(quarter[0])
            
            
        return 0
            
    
        #take Return on Equity and compute the change by percentage between each 
        #quarter
    def ChangeInROE (self, quarters) :
        #Return on Equity is second value in the index.
        #Takes value from the second index and computes the percent difference 
        #between each year.
        #Stores difference in a list
        #Change in Percentage = quarter1/quarter2 * 100
        
        
        
        return 0
    
    def predict_ROE (year, weight, bias) :
        return weight*year+bias
    
    
    
    def cost_function (years, ROE, weight, bias) :
        quarters = len(years)
        total_error = 0.0
        for i in range(quarters) :
            total_error += (years[i] - (ROE[i]*weight + bias))**2
        return total_error/quarters
    


    def update_weights (years, ROE, weight, bias, learning_rate) :
        weight_deriv = 0
        bias_deriv = 0
        quarters = len(years)
        
        for i in range(quarters) :
            weight_deriv += -2*years[i] * (ROE - (weight*years + bias))
            bias_deriv += -2*(ROE - (weight*years + bias))
            
        weight -= (weight_deriv/quarters) * learning_rate
        bias -= (bias_deriv/quarters) * learning_rate
        
        return weight, bias
    
    
    
    def train (self, years, ROE, weight, bias, learning_rate, iters) :
        cost_history = []
        
        for i in range(iters) :
            weight, bias = self.update_weights (years, ROE, weight, bias, learning_rate)
            cost = self.cost_function (years, ROE, weight, bias)
            cost_history.append(cost)
            
            if i%10 == 0 :
                print ("iter: "+str(i) + " cost: "+str(cost))

        return weight, bias, cost_history
    

    def ClassifyProfitability (quarters) :
        
        profitable = []
        nonProfitable = []
         
        for quarter in quarters :
            if float(quarter[1]) > 15.0 :
                profitable.append(quarter)
            else :
                nonProfitable.append(quarter)
        return (profitable, nonProfitable)
        
        
data = BusinessClassification.PruneData("apple.csv")
ROC = BusinessClassification.quarterRateOfChange(data)
BusinessClassification.PlottingFigures(data)
print(BusinessClassification.ClassifyProfitability(data)[0])








