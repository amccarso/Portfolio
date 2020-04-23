''' 
Nils Napp
Sliding Probelm for AI-Class
'''

from slideproblem import * 
import time
import heapq
import math
import matplotlib.pyplot as plt
## you likely need to inport some more modules to do the serach


class Searches:
    
    
    def plot (h1, h2):
        plt.plot(h1)
        plt.plot(h2)
        plt.ylabel('performance')
        plt.show()
        
        
        
        
    def tree_bfs(self, problem):
        #reset the node counter for profiling
        Node.nodeCount=0
        n=Node(None,None,0,problem.initialState)
        print(n)
        frontier=[n]
        while len(frontier) > 0:
            n = frontier.pop(0)
            for a in p.applicable(n.state):
                nc=childNode(n,a,p)
                if nc.state == p.goalState:
                    return solution(nc)
                else:
                    frontier.append(nc)
            
            
            
    def graph_bfs(self, problem):
        Node.nodeCount=0
        n=Node(None,None,0,problem.initialState)
        frontier=[n]
    
        explored=set()
        
        while len(frontier) > 0:
            n = frontier.pop(0)
            for a in p.applicable(n.state):
                nc=child_node(n,a,p)
                if nc.state == p.goalState:
                    return solution(nc)
                else:
                    childState=nc.state.toTuple()
                    if not(childState in explored):
                        frontier.append(nc)
                        explored.add(childState)    
        
    
    
    
    def recursiveDL_DFS(self, lim,problem):
        n=Node(None,None,0,problem.initialState)
        return self.depthLimitedDFS(n,lim,problem)
    
    def depthLimitedDFS(self, n, lim, problem):
    
        #reasons to cut off brnaches    
        if n.state == problem.goalState:
            return solution(n)
        elif lim == 0:
            return None
       
        cutoff=False    
        for a in p.applicable(n.state):
            nc=child_node(n,a,problem)
            result = self.depthLimitedDFS(nc,lim-1,problem)
    
            if not result==None:
                return result
    
        return None        
    
    def id_dfs(self,problem):
    
        Node.nodeCount=0
        
        maxLim=32
        for d in range(1,maxLim):
            result = self.recursiveDL_DFS(d,problem)
            if not result == None:
                return result
        print('Hit max limit of ' + str(maxLim))
        return None
        
        
    def h_1(self,s0: State,sf: State ) -> numbers.Real:
        #misplaced heuristic
#        print(s0)
#        print(sf)
        
        misplaced = 0
        
        
        for i in range(0,3):
            for j in range(0,3):
                if not s0.board[i][j] == sf.board[i][j] and not s0.board[i][j] == 0:
                    misplaced += 1
                    
#        print(misplaced)
        return misplaced
       
       
       
    def h_2(self,s0: State,sf: State ) -> numbers.Real:
        #manhattan distance heuristic
        
        manhattan_distance = 0
        out_of_place = []
        
        for i in range(0,3):
            for j in  range(0,3): 
                if not s0.board[i][j] == sf.board[i][j] and not s0.board[i][j] in out_of_place and not s0.board[i][j] == 0:
                    out_of_place.append((s0.board[i][j],i,j))
        
        for x in range(0,3):
            for y in range(0,3):
                i = 0
                while i < len(out_of_place):
                    if sf.board[x][y] == out_of_place[i][0]:
                        manhattan_distance += abs((out_of_place[i][1] - x)) + abs((out_of_place[i][2] - y))
                    i+=1
#        print('manhattan_distance is: ', manhattan_distance)
#        print(sf)
#        print(s0)
        return manhattan_distance
        
    def a_star_tree(self,problem : Problem) -> tuple: 
        
        
        nodeCount = 0
        _node = Node(None, None, 0, problem.initialState)
        frontier = [_node]
        
        heapq.heapify(frontier)
        
        while len(frontier) > 0:
        
            n = heapq.heappop(frontier)
            
            
            if n.state == problem.goalState:
                return solution(n)
            
            for action in problem.applicable(n.state):

                child = child_node(n, action, problem)
                                
                if child not in frontier:
                    child.cost = n.cost + 1
                    child.f = child.cost + self.h_2(child.state, problem.goalState)
                    heapq.heappush(frontier, child)
              
        return "cheers"
    
        
    def a_star_graph(self,problem : Problem) -> tuple:
        
        nodeCount = 0
        _node = Node(None, None, 0, problem.initialState)
        frontier = [_node]
        explored = set()
        heapq.heapify(frontier)

        h2vals = []
        h1vals = []
        while len(frontier)>0 :
            n = heapq.heappop(frontier)
            explored.add(n)
            
            
            if n.state == problem.goalState:
#                h2vals.reverse()
#                h1vals.reverse()
#                plt.plot(h2vals)
#                plt.plot(h1vals)
#                plt.ylabel('efficiency')
#                plt.show()
               
                return solution(n)
            
            for action in problem.applicable(n.state):

                child = child_node(n, action, problem)
                childState = child.state.toTuple()
                
                #tentative_cost = child.cost + 1
                
                if childState not in explored:
                    child.cost = n.cost + 1
                    
                    child.f = child.cost + self.h_2(child.state, problem.goalState)
                    heapq.heappush(frontier, child)
                    explored.add(childState)
                     
            h2 = self.h_2(child.state, problem.goalState)
            h1 = self.h_1(child.state, problem.goalState)
            h2vals.append(h2)
            h1vals.append(h1)
            
        plt.plot([h2vals])
        plt.plot([h1vals])
        plt.ylabel('efficiency')
        plt.show()
#            if childState == problem.goalState:
#                return solution(child)
        #num = self.h_2(problem.initialState, problem.goalState)
        
       # State = problem.initialState
        
        return "dilly dilly"


import time

p=Problem()
s=State()
n=Node(None,None, 0, s)
n2=Node(n,None, 0, s)

searches = Searches()

p.goalState=State(s)

p.apply('R',s)
p.apply('R',s)
p.apply('D',s)
p.apply('D',s)
p.apply('L',s)

p.initialState=State(s)

print(p.initialState)

si=State(s)
# change the number of random moves appropriately
# If you are curious see if you get a solution >30 moves. The 
apply_rnd_moves(15,si,p)
p.initialState=si

startTime=time.clock()


print('=== Bfs*  ===')
startTime=time.clock()
res=searches.graph_bfs(p)
print(res)
print(time.clock()-startTime)
print(Node.nodeCount)

print('=== id DFS*  ===')
startTime=time.clock()
res=searches.id_dfs(p)
print(res)
print(time.clock()-startTime)
print(Node.nodeCount)

print('\n\n=== A*-Tree ===\n')
startTime=time.clock()
res=searches.a_star_tree(p)
print(time.clock()-startTime)
print(Node.nodeCount)
print(res)

print('\n\n=== A*-Graph ===\n')
startTime=time.clock()
res=searches.a_star_graph(p)
print(time.clock()-startTime)
print(Node.nodeCount)
print(res)

H1 = []
H2 = []
opt = []
for i in range(0,50):
    p.goalState = State()
    si=State()
    apply_rnd_moves(50,si,p)
    p.initialState=si
    h2 = Searches.h_2(None, si, p.goalState)
    h1 = Searches.h_1(None, si, p.goalState)
    H2.append(h2)
    H1.append(h1)
    opt.append(Searches.a_star_graph(searches, p)[1])
plt.plot(H1)
plt.plot(H2)
plt.plot(opt)
plt.show()