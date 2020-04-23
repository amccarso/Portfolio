import numpy as np

'''
If you want to implement additional drawing functions please do not 
submit them. The autograder will get upset if you are tyring to inlclude
matplotlib. 

The grader will replace drawprob funcitons with empty ones for grading
'''
#used to visualize robot and maze probability distributions
from drawprob import pShow

'''
These are the possible actions. They all apply all the time
'''

ACTIONS=('N','E','S','W','A')
        
class Ocean:
    def __init__(self,world,reward):
        self.world=world
        self.worldShape=world.shape
        self.stateSize=self.worldShape[0]*self.worldShape[1]

        self.reward=reward

        #These should be the sams size matrix        
        assert self.reward.shape==self.worldShape

    #Functions for going between the two representations 
    def state2coord(self,s):
    	# transfer state to grid world coordinate (x,y)
    	row=int(s/self.worldShape[1])
    	col=np.mod(s,self.worldShape[1])
    	return row,col

    def coord2state(self,c):
    	# transfer grid world coordinate (x,y) to state 
    	return c[0]*self.worldShape[1] + c[1]

    def numNbrs(self,s):
        nbrs=0
        rows,cols=self.worldShape
        r,c=self.state2coord(s)        
        if self.world[(r-1)%rows,c]==0:
            nbrs+=1
        if self.world[(r+1)%rows,c]==0:
            nbrs+=1
        if self.world[r,(c-1)%cols]==0:
            nbrs+=1
        if self.world[r,(c+1)%cols]==0:
            nbrs+=1
        return nbrs

    def nbrList(self,s):
    # returns neighbors index of a given state (0-79)
        nbrs=[]
        rows,cols=self.worldShape
        r,c=self.state2coord(s)
        if self.world[(r-1)%rows,c]==0:
            nbrs.append(self.coord2state((r-1,c)))
        if  self.world[(r+1)%rows,c]==0:
            nbrs.append(self.coord2state((r+1,c)))
        if self.world[r,(c-1)%cols]==0:
            nbrs.append(self.coord2state((r,c-1)))
        if self.world[r,(c+1)%cols]==0:
            nbrs.append(self.coord2state((r,c+1)))
        return nbrs

    def actionList(self,s):
        nbrs=[]
        rows,cols=self.worldShape
        r,c=self.state2coord(s)
        if self.world[(r-1)%rows,c]==0:
            nbrs.append('N')
        if self.world[(r+1)%rows,c]==0:
            nbrs.append('S')
        if self.world[r,(c-1)%cols]==0:
            nbrs.append('W')
        if self.world[r,(c+1)%cols]==0:
            nbrs.append('E')
        
        for a in nbrs:
           assert a in ACTIONS
            
        return nbrs

''' 
Ship class that contains 
 
 * ocean model  
 * action model 
 * probability distribution over where it is
 
 '''    

class Ship:
    def __init__(self,ocean : Ocean):
        self.ocean=ocean

        self.actionList=self._makeActions()           #<--- Transition Matrix


        '''
        Make a nice dictionary so you can get the right transition matrix for
        each action.
        '''
        self.actionDict={}
        for a,A in zip(ACTIONS,self.actionList):
            self.actionDict[a]=A
        
        self.prob=np.zeros(ocean.stateSize)  #<--- estimate of robot position        
        self.prob[0]=1                      #Assume you start out at location 0

        ''''
        PUT YOUR ANSWERS HERE
        '''
        self.daysToSail=0 #<---- Until within 0.00001 total difference 
        self.numberOfIslands=0

            
    #matrix power
    def mpower(self,A,n):
        res=np.identity(A.shape[0])
        for i in range(n):
            res=np.dot(res,A)
        return res
            
        
    def obsLiklihood(self,o):
        likelihood = None #Should be vector of appropriate length
        return likelihood

        
    #Giving you this one for free!
    def Aanchor(self):
        A=np.eye(self.ocean.stateSize) 
        return A
    
    
    '''
    This function should return a List or Tuple of transition matrics,
    one for each action. The list should be in the same order as:
    
    ACTIONS=('N','E','S','W','A')

    '''
    def _makeActions(self):
        '''
        YOU NEED TO CHANGE THIS CODE, the first four elements of the list
        should be the transition matrices for N,E,S, and W. You can leave the 
        fifth (last) entry unchanged.
        '''
        ANorth = np.zeros((self.ocean.stateSize, self.ocean.stateSize))
        ASouth = np.zeros((self.ocean.stateSize, self.ocean.stateSize))
        AWest = np.zeros((self.ocean.stateSize, self.ocean.stateSize))
        AEast = np.zeros((self.ocean.stateSize, self.ocean.stateSize))
        
        for idx in range(0,self.ocean.stateSize):
            for neighbor in self.ocean.nbrList(idx):
                print(neighbor)
        return (ANorth,
                AEast,
                ASouth,
                AWest,
                self.Aanchor())


        
    def sail(self, action):
        
        #once you get the As to work, this will give you 
        #the next probabilty distribution
        pn=np.dot(self.actionDict[action],self.prob)
        
        self.prob=pn        



class MDPSailing():
    def __init__(self, ship : Ship):
        
        
        self.ship=ship
        
        '''
        Make a convenient reward vector
        '''
        self.reward=np.zeros(self.ship.ocean.stateSize)
        for s in range(self.ship.ocean.stateSize):
            '''
            Go through all the states and get the reward from the Ocean Coordinates
            '''
            r,c=self.ship.ocean.state2coord(s)
            self.reward[s]=self.ship.ocean.reward[r,c]

        
        
        '''
        Intialize the V function 
        '''
        self.V=self.reward.copy()
     
        '''
        Set the gamma value for value iteration
        '''
        self.gamma=0.9
        
        
    '''
    Value iteration:
        
    use \gamma = 0.9
    and a reward(u,x) that depends gives you the state rewared and an
    additional -1 for sailing N,E,S,W. 
    Staying achored with action 'A' is free, i.e. you only get the state reward
    
    This funciton should update the self.V vector by N=steps
    '''
        
    def valIter(self,N=1):

        '''
        YOU NEED TO IMPLEMNET THIS FUNCTION
        
        Remember to add an additional reward of -1 for NESW, but not for A.
        '''
        
        #Place holder functions to store the value before taking the max
        VN=np.zeros(self.ship.ocean.stateSize)
        VE=np.zeros(self.ship.ocean.stateSize)
        VS=np.zeros(self.ship.ocean.stateSize)
        VW=np.zeros(self.ship.ocean.stateSize)
        VA=np.zeros(self.ship.ocean.stateSize)
        
        g=self.gamma
        
        for n in range(N):
            '''
            DO ONE SETP OF VALUE ITERATION
            '''
            pass

    def computePolicy(self):
        '''
        YOU NEED TO IMPLEMET THIS FUNCTION 
        '''
        
        '''
        You can cut-paste parts of the value iteration function here.
        Make sure that you return a policy that is a LIST of lenght
        ocean.stateSize with entries that are either 'N','E','S','W', or 'A'
        '''
        policy=[]
        for s in range(self.ship.ocean.stateSize):
            policy.append('A') # Achor everywhere
        
        return policy
    
    def showPolicy(self):
        '''
        You can use this to visualize the current
        policy returned by computePolicy() ... will show all As before
        you implement these functions.
        '''
        chars=iter(self.computePolicy())
        rows,cols = self.ship.ocean.worldShape
        for r in range(rows):
            for c in range(cols):
                print(next(chars)+' ',end='')
            print('')
                       
    def showValue(self):
        '''
        You can use this to help debug value iteration by displaying the
        current value function.
        '''
        vals=iter(self.V)
        rows,cols = self.ship.ocean.worldShape
        for r in range(rows):
            for c in range(cols):
                print('%7.1f'%next(vals)+' ',end='')
            print('')

'''
Saves the MPD data

1) The horizon stored in 'Ship'. Make sure you edit the code.
2) The number of islands also stored in 'Ship' Make sure you edit the code.
3) The current policy extracted from the value funciton 

'''        

def saveData(mdp : MDPSailing):
    import json 
    
    d={}
    d['horizon']=mdp.ship.daysToSail
    d['islands']=mdp.ship.numberOfIslands
    d['policy']=mdp.computePolicy()
    with open('data.json','w') as fh:
        json.dump(d,fh)
        
        
        
        
    
# =======================================================================================

if __name__=="__main__":


    '''
    What to hand in:
        Two files: markov.py and data.json
        
        1) Code up the function _makeActions() in the ship class
        2)* Fill in the ship.numberOfIslands variable based on the ocean map below
        3)* Fill in the ship.daysToSail variable base on how many days
                you need to sail north (i.e. call ship.sail('N')) before the 
                position probabilty ship.prob converges to with in 0.00001 of 
                its steady-state value.
        4) Code up the valIter() function in the MDPSailing class
        5) Code up the computePolicy() function that copmutes the policy
                for the current V-function
        7) Run valIter until the value function converges
        8) Call 'saveData()' on the mdp class: This will use the current
                value function to and the computePolicy() function you created 
                and save it, and the starred answers 2&3 to a data.json file 
                which you should submit.            
    '''
	    
    
    # ------- Robot Maze ------    
    
    oceanMap=np.array([
				[0,0,0,0,0,0,0,0,0,0],
				[0,0,0,0,0,0,0,0,0,0],
				[0,0,0,0,0,0,0,0,0,0],
				[0,0,0,1,0,0,0,0,0,0],
				[0,0,1,1,0,0,0,0,0,0],
				[0,0,0,0,0,0,0,0,0,0],
				[0,0,0,0,0,0,0,1,0,0],
				[0,0,0,0,0,0,0,0,0,0]])
    
    #Land gives you zero rewrad
    #Kraken territory is gnerally dangerous 
    #There are ship sinking cliffs aroudn the safe harbor
    #Harbor givers you 500 reward               
    #                                        Kraken lives around here        
                                                    #|      
    oceanReward=np.array([                          #V 
        [ 1.2,  9.2,  -9000,  7.3,  1.7,  8.7,  -10,   -50,  -50,  -10],
        [ 2.1,  5.5,  0.4,    7.9,  9. ,  -10,  -50, -100 , -50,  -10],
        [ 4.7,  -9000,  8.2,   0.7,  1.7,  3. ,  -50,  -50,  -50,  -10],
        [ 8.4,  3.3,  100,      0,  3.7,  5.2,  -10,  -50,  -10,  7.7],
        [ 3.5,  4.8,    0,      0,  4.6,  8.2,  7.2,  -10,  1.6,  7.7],
        [ 1.6,  3.9,  2.5,    4.9,  3.9,  6.7,  9.4,  1.0,  7.1,  6.8],
        [ 7.7,  9. ,  9.7,    9.3,  0.4,  6.5,  3.9,    0,  1.7,  2.6],
        [ -9000,  2.1,  8.8,   3.8,  8.4,  8.7,  7.9,  5.8,  9.7,  9.2]])


    
    ocean=Ocean(oceanMap,oceanReward)
    ship=Ship(ocean)

    '''
    Show probability of ship sailing north from harbor once (before/after)
    '''
    
    #Harbor coordinates
    harborState = ocean.coord2state((3,2))
    print("Reward for Harbor: %f"%oceanReward[3,2])
    #set location probability for sihp to harbor state
    ship.prob=np.zeros(ocean.stateSize)
    ship.prob[harborState]=1
    
    pShow(ship.prob,ocean) #probability 1 of begin in harbor
    ship.sail('N')
    pShow(ship.prob,ocean) #probability after sailing north from harbor
    
    


    mdp=MDPSailing(ship)
    
    
    #Run Value iteration i.e. call valIter(N=something) until mdp.V
    #has converged. 
    
    '''
    Uncomment the line below to once you are ready to save your answers and
    want to create the data.json file to upload.
    '''
    #saveData(mdp)