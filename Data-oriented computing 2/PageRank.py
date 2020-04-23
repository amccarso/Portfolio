#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 20 10:43:56 2019

@author: austinmccarson
"""
import numpy as np
import HW1 as hw1

def adjacencyMatrix (Network) :
    
    #using [0]*7 leads to each value refering to the same value. changing one changes all
    A = [[0 for i in range(len(Network))] for i in range(len(Network))]

    for node in range(len(Network)):
        for toNode in Network[node]:
            A[node][toNode-1] = 1
    
    return A

def PageRank(Network, alpha = 0.85, max_iters = 100) :
    I = np.matrix(np.identity(len(Network))) #identity matrix
    A = np.matrix(adjacencyMatrix(Network)) #Adjacency Matrix: 1 if connected, 0 if not

    Deg = hw1.HW1.in_degree(Network) #degree vector
    D = [[0 for i in range(len(Network))] for i in range(len(Network))]
    
    for nodeDeg in range(len(Deg)):
        D[nodeDeg][nodeDeg] = Deg[nodeDeg]

    D = np.matrix(D)
    #print(D)
    
    #normalize?
    #Dinv = np.linalg.inv(D)
    #print(Dinv)
    alphaA = np.multiply(alpha, A)
    parens = np.subtract(D, alphaA)
    parensInv = np.linalg.inv(parens)
    G = np.multiply(D, parensInv)
    final = np.multiply(G, np.ones(len(G)))
    print(G)

    #print(alphaA)
    #alphaADinv = np.multiply(alphaA, Dinv)
    #print(alphaADinv)
    #parens = np.linalg.inv(np.subtract(I, alphaADinv))
    #G = np.multiply(parens, np.ones(len(Network)))
    #print(G)
