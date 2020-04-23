import sudoku
import time

class Solver:
    
#    def add_arcs_to_queue(self, csp) :
#        arc_queue = []
#        arc_queue.append((node, neighbor) for node in csp.variables for neighbor in csp.neighbors[node])
#        return arc_queue
    
    def AC3(self,csp, queue=None, removals=None):
        '''
        your code here
        '''
        '''Returns true if consistent, false if inconsistent'''
        if queue == None :
            queue = []
            for Xi in csp.variables :
                for Xk in csp.neighbors[Xi] :
                    queue.append((Xi, Xk)) #add all arcs to queue
            
                    
        csp.support_pruning()
        while queue : # go through arcs and remove any inconsistent assignments
            (Xi, Xj) = queue.pop(0) #pop first arc on queue
            if self.revise(csp, Xi, Xj, removals) : #if we remove a possible assignment, execute
                if not csp.curr_domains[Xi] : #if curr_domains is empty
                    return False
                for Xk in csp.neighbors[Xi] : 
                    if Xk != Xj :
                        queue.append((Xk, Xi))     #append arc to queue  
                        
        return True
       

    
    
    def revise(self,csp, Xi, Xj, removals): 
        """Return true if we remove a value."""
        '''
        your code here
        '''
        revised = False
        
        for x in csp.curr_domains[Xi] :
            flag = True
            for y in csp.curr_domains[Xj] :
                if csp.constraints(Xi, x, Xj, y) :
                    flag = False
                    break
            if flag : 
                csp.prune(Xi, x, removals)
                revised = True
        return revised
    
    
    
    def rec_backtracking_search(self, assignment, csp) :
        if len(assignment) == len(csp.variables) : 
            return assignment
            #if goal_test(assignment) : return assignment??
        for val in csp.variables : #need to get unassigned values
            if val not in assignment : #val is a variable... assignment contains pairs
                var = val              #can I check for a single value in assignment
        for value in csp.curr_domains[var] :
            if csp.nconflicts(var, value, assignment) == 0 :
                csp.assign(var, value, assignment)
                removals = csp.suppose(var, value) #initialize removals
                if self.AC3(csp, removals=removals) :
                    csp.infer_assignment()
                    result = self.rec_backtracking_search(assignment, csp)
                    if result != None :
                        return result
                csp.restore(removals)
        csp.unassign(var, assignment)
        #print("\n\n\n\n" + str(assignment))
        return None
        
    def backtracking_search(self,csp) :
        '''
        your code here
        '''
        #print("\n\n\n\n"+str(csp.variables))
        
        
    
        result = self.rec_backtracking_search({}, csp)
        return result
        


        
if __name__ == '__main__':
    
    '''
    Some board test cases, each string is a flat enumeration of all the board positions
    where . indicates an unfilled location
    Impossible: 123456789.........123456789123456789123456789123456789123456789123456789123456789
    Easy ..3.2.6..9..3.5..1..18.64....81.29..7.......8..67.82....26.95..8..2.3..9..5.1.3..
    Easy ...7.46.3..38...51.1.9.327..34...76....6.8....62...98..473.6.1.68...13..3.12.5...
    Difficult ..5...1.3....2.........176.7.49....1...8.4...3....7..8.3.5....2....9....4.6...9..
    '''
    
    board = sudoku.Sudoku('12.456789.........12.45678912.45678912.45678912.45678912.45678912.45678912.456789') 
    #Accessing the board as a csp, i.e. display the variable and domains
    #See the extra document for exapmles of how to use the  CSP class
    

    # Display this nonsensical board
    board.display(board)

    
    #Show the "flat" variables
    print(board.variables)
    
    #show the domeians (curr_domains beocmes populated by infer_assignment())
    print(board.curr_domains)
  
    
    '''You'll need to manipulate the CSP domains and variables, so here are some exampels'''
    
    # this is a list of (variable, domain value) pairs that you can use to keep track
    # # of what has been removed from the current domains
    removals=[]

    # #show domains for variable 3
    print("Domain for 3: " + str(board.curr_domains[3]))    
    # #remove the possible value '8' form domain 3
    # #not the differences int key for the first dictionary and the string keys
   
    
    board.prune(3,'8',removals) # This line may not work if the domain for 3 does not contain "8" 

    print("Domain for 3: " + str(board.curr_domains[3]))    
    print("Removal List: " + str(removals))
    
    #Prune some more
    print("Domain for 23: " + str(board.curr_domains[23]))     
    board.prune(23,'1',removals)
    board.prune(23,'2',removals)
    board.prune(23,'3',removals)
    print("Domain for 23: " + str(board.curr_domains[23]))    
    print("Removal List: " + str(removals))
    
    #ooopes took away too muche! Restore removals
    board.restore(removals)
    print("Domain for 23: " + str(board.curr_domains[23]))    
      
    #For assigning vaeiables use a dictionary like
    assignment={}
    board.assign(23,'8',assignment)
    #ocne all the variables are assigned, you can use goal_thest()
    
    #find the neighbors of a varaible
    print("Neighbors of 0: " + str(board.neighbors[0]))
    
    #check for a constraint, need to plug in a specific var,val, var val combination
    #since 0 and 1 and neighbors, they should be different values
    print(board.constraints(0,'0',1,'0')) #should be false
    print(board.constraints(0,'0',1,'1')) #should be true i.e. not a constraint
    
   
    '''to check your implementatios:''' 
    
    # AC3 should return false for impossible example above
    sol = Solver()
    start=time.clock()
    print(sol.AC3(board))
    print("time: " + str(time.clock() - start))
    board.display(board)

    # backtracking search usage example
    start=time.clock()
    #sol.backtracking_search(board)
    print("time: " + str(time.clock() - start))
    board.display(board)
    
    S = sudoku.Sudoku('..3.2.6..9..3.5..1..18.64....81.29..7.......8..67.82....26.95..8..2.3..9..5.1.3..')
    sol=Solver()
    start=time.clock()
    print(sol.AC3(S))
    print(removals)
    print(assignment)
#    print(sol.backtracking_search(S))
    print("time: " + str(time.clock() - start))
    S.display(S)
    
    S = sudoku.Sudoku('...7.46.3..38...51.1.9.327..34...76....6.8....62...98..473.6.1.68...13..3.12.5...')
    sol = Solver()
    start = time.clock()
    print('\n')
    board.display(S)
    print(sol.AC3(S))
    print(removals)
    print(assignment)
    print("time: " + str(time.clock()-start))
    board.display(S)
    
    S = sudoku.Sudoku('..5...1.3....2.........176.7.49....1...8.4...3....7..8.3.5....2....9....4.6...9..')
    sol = Solver()
    start = time.clock()
    print(sol.backtracking_search(S))
    print("time: " + str(time.clock()-start))
    board.display(S)

    S = sudoku.Sudoku('..5...1.3....2.........176.7.49....1...8.4...3....7..8.3.5....2....9....4.6...9..')
    sol = Solver()
    start = time.clock()
    print(sol.backtracking_search(S))
    print("time: " + str(time.clock()-start))
    board.display(S)
    
    S = sudoku.Sudoku('4173698.5.3..........7......2.....6.....8.4......1.......6.3.7.5..2.....1.4......')
    sol = Solver()
    start = time.clock()
    print(sol.backtracking_search(S))
    print("time: " + str(time.clock()-start))
    board.display(S)
    