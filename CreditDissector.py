#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 26 15:52:13 2019

This is a file to read a credit card statement to determine who owes how much money on a shared credit card statement.

@author: austinmccarson
"""

import sys

sys.argv.remove(sys.argv[0])
    
filename = sys.argv[0]
#outfilename = sys.argv[1]

file = open(filename, 'r')
lines = file.readlines()


def isnumber(string):
    try:
        float(string)
    except ValueError:
        return False
    return True


def createListOfPurchases(lines):

    purchases = []
    
    for line in lines:
        purchases.append(line.split(','))
                
    for i in range(len(purchases)):
        purchases[i] = list(filter(None, purchases[i]))
        if len(purchases[i]) >= 5:
            purchases[i][-1] = purchases[i][-1].replace('\n','')
        else:
            purchases[i] = list(filter(lambda x: '\n' not in  x, purchases[i]))
        
            
    for i in range(len(purchases)):
        for j in range(len(purchases[i])):
            try:
                purchases[i][j] = purchases[i][j].replace('"', '') #remove redundant quotes
                purchases[i][j] = purchases[i][j].replace('$', '') #remove dollar symbols
                if isnumber(purchases[i][j]) and isnumber(purchases[i][j-1]):
                    merged = ''.join(purchases[i][j-1:j+1])
                    purchases[i][j-1:j+1] = [merged]
            except IndexError:
                break
           
    purchases = list(filter(lambda x: len(x) > 3, purchases))
    purchases = list(filter(lambda x: len(x) < 7, purchases))
    
    return purchases



purchases = createListOfPurchases(lines)



def categorizePurchasesByLabel(purchases):
    
    labeledPurchases = {}

    for i in range(len(purchases)):
        if len(purchases[i]) == 6:
            categoryOfPurchase = purchases[i][0]
            if categoryOfPurchase in labeledPurchases.keys(): # check if category already entered
                labeledPurchases[categoryOfPurchase].append([purchases[i][1:4]])
            else:
                labeledPurchases[categoryOfPurchase] = [purchases[i][1:4]]
            purchases[i].remove(categoryOfPurchase)
        else:
            labeledPurchases[categoryOfPurchase].append(purchases[i])
            
    return labeledPurchases



def categorizePurchasesByPerson(purchases):
    
    personalBuys = list(filter(lambda x: filter(x[0], x), purchases))
    personalBuys = purchases
    personalPurchases = {}
        
#    for i in range(len(purchases)):
#    print(purchases, '\n')
    for i in range(len(personalBuys)):
        if len(personalBuys[i]) == 5:
            personWhoPurchased = personalBuys[i][-1]
            if personWhoPurchased in personalPurchases.keys():
                personalPurchases[personWhoPurchased].append(personalBuys[i][0:4])
            else:
                personalPurchases[personWhoPurchased] = [personalBuys[i][0:4]]
            purchases[i].remove(personWhoPurchased)
        else:
            personalPurchases[personWhoPurchased].append(personalBuys[i][0:4])
            
    return personalPurchases   



def AmountEachPersonOwes(personalPurchases):
    
    AmountOwed = {}
    
    for key, value in personalPurchases.items():
        amount = 0
        #print('\n', key)
        for val in value:
            #print(val)
            amount += float(val[3])
        AmountOwed[key] = amount
        
    reduceCredit(AmountOwed, [person for person in personalPurchases])
    
    return AmountOwed


def reduceCredit(AmountOwed, persons):
    
    for person in persons:
        if person[0] in AmountOwed:
            AmountOwed -= person[1]
            
    return AmountOwed
    
    

labeledPurchases = categorizePurchasesByLabel(purchases)
personalPurchases = categorizePurchasesByPerson(purchases)
AmountOwed = AmountEachPersonOwes(personalPurchases)

#print(labeledPurchases)
print('\n', 'Amount owed per person: ', AmountOwed)

#print(purchases, '\n')
#print(personalPurchases)
