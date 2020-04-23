# -*- coding: utf-8 -*-
"""

"""
import queue

from SlideProblem import *

class Searches:    
    
    def graphBFS(self,problem):
        #reset the node counter for profiling
        nodeCount = 0
        Node = node(None, None, 0, problem.initialState)
        frontier = [Node];
        explored = set()
        
        while len(frontier) > 0:
            _node_ = frontier.pop(0)
            
            for action in p.applicable(_node_.state) :
                child = childNode(_node_, action, p)
                if child.state == p.goalState :
                    print('bingo')
                    print(child.state)
                    print(p.goalState)
                    return solution(child)
                else :
                    childState = child.state.toTuple()
                    if not (childState in explored) :
                        frontier.append(child)
                        explored.add(childState)
                
               
        #the search should return the result of 'solution(node)'
        print("I am an empty shell of a function.")        


    def recursiveDL_DFS(self, limit, problem):
        _node_ = node(None, None, 0, problem.initialState)
        return self.depthLimitedDFS(_node_, limit, problem)
    
    def depthLimitedDFS(self, _node_, limit, problem):
        
        if _node_.state == problem.goalState:
            print(_node_.state)
            return solution(_node_)
        elif limit == 0:
            return None
        
        cutoff = False
        for action in problem.applicable(_node_.state):
            child = childNode(_node_, action, problem)
            result = self.depthLimitedDFS(child, limit-1, problem)
            
            if not result == None:
                return result
            
        return None
            
        
    def idDFS(self,problem):
        #reset the node counter for profiling
        #the serach should return the result of 'solution(node)'
        
        nodeCount = 0
        
        maxLimit = 32
        for d in range(1,maxLimit):
            result = self.recursiveDL_DFS(maxLimit, problem)
            if not result == None:
                return result
            
        print('Hit max limit of ' + str(maxLimit))
        return None
        
        
if __name__ == '__main__':

    import time

    search=Searches()
    
    ''' Set up the search problem '''
    p=problem()
    s=state()
   
    p.goalState=state(s)
    
    p.apply('R',s)
    p.apply('R',s)
    p.apply('D',s)
    p.apply('D',s)
    p.apply('L',s)
    
    p.initialState=state(s)
    print(p.initialState)
    
    ''' 
    The sultion, should basically be the reverse order
    of backward moves above: RUULL
    '''
    
    print('=== Bfs  ===')
    startTime=time.clock()
    node.nodeCount=0
    
    res=search.graphBFS(p)
    print(res)
    print("Time " + str(time.clock()-startTime))
    print("Explored Nodes: "+ str(node.nodeCount))
 
    print('=== ID-Depth Limited Search ===')
    startTime=time.clock()
    node.nodeCount=0

    res=search.idDFS(p)
    print(res)
    print("Time " + str(time.clock()-startTime))
    print("Explored Nodes: "+ str(node.nodeCount))
 
      