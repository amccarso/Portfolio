#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 20 10:49:12 2019

@author: austinmccarson
"""
import PageRank as PR

class HW1 :
    
    def out_degree(Network) :
        #One way to initialize empty array to specific size
        out_degree = [0] * len(Network)
        
        for node in range(0, len(Network)) :
            out_degree[node] = len(Network[node])
            
            
        return out_degree
    
    
    def in_degree(Network) :
        #Second way to initialize empty array to specific size
        in_degree = [0 for i in range(0, len(Network))]
        
        for toNode in range(0, len(Network)) :
            
            for fromNode in range(0, len(Network)) :
                for edge in range(0, len(Network[fromNode])) :
                    if Network[fromNode][edge] == toNode+1:
                        in_degree[toNode] += 1 
       
        print(in_degree)
        return in_degree
    
    
    def density(Network) :
        
        numberOfNodes = Network.length
        numberOfEdges = 0
        
        for edges in Network :
            numberOfEdges += len(edges)
            
        meanDegree = (2*numberOfEdges)/numberOfNodes
        return meanDegree/(numberOfNodes-1)
    
    
#deleted 5,6,7,11
#8=5, 9=6, 10=7, 12=8, 13=9, 14=10, 15=11, 16=12, 17=13, 18=14        
Friends = [[2], [1,4,9,11], [4], [2,3], [6], [5], [8], [7,9,10], [2,8,10], [8,9],
				[2,12], [11], [14], [13]]

#deleted 5,6,7,11
# 8=5,9=6,10=7,12=8,13=9,14=10,15=11,16=12,17=13,18=14
FirstNames = [[2,4,8], [1,4,9,11], [4], [1,2,3,13,14], [6], [5], [8,13], [1,7,9,10],
              [2,8,10], [8,9,14], [2,12], [11], [4,7,14], [4,10,13]]
		
#deleted 1,5,8,9,11,15,16
# 2=1, 3=2, 4=3, 6=4, 7=5, 10=6, 12=7, 13=8, 14=9, 17=10, 18=11
HaveClass = [[3,8], [3], [1,2,10,11], [5], [4], [7], [6,8], [1,7,11], [11], [3,11], [3,8,9,10]]
		
#deleted 3,5,6,7,11,14,15,16
# 4=3,8=4,9=5,10=6,12=7,13=8,17=9,18=10 
SocialEvents = [[2], [1], [9], [5], [4], [7,9], [6,8], [7], [3,6,10], [9]]
			
#print(HW1.out_degree(Friends))
#print(HW1.in_degree(Friends))
PR.PageRank(Friends)
PR.PageRank(FirstNames)
PR.PageRank(HaveClass)
PR.PageRank(SocialEvents)