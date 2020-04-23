import numpy as np
from markov import *
from drawprob import pList,pShow,robotShow


class MDPSillyGame:
    def __init__(self):
        self.domsize = 160
        self.reward = self._mkreward()

        self.eps = 0.05 #<--- CHANGE ME

        self.A = self.transitionMatrix(self.eps)
        self.value = self._mkreward()
        
        
        ''' 
        Change this answer 
        You shoul play if you have equal or more than this amount
        '''
        self.cutoff = 81 # <--- your answer here
        
        
    def _mkreward(self):
        reward = np.arange(self.domsize)
        for i in range(100,self.domsize):
            reward[i]=reward[i] + 50
        return reward

    def transitionMatrix(self,eps):
        '''put code here to compute the transition matrix '''
        A = np.zeros([self.domsize,self.domsize])
        #0.5% chance for losing (n-1)
        #0.05% chance for breaking even (n)
        #0.45% chance for winning (n+1)
        #Expected Value - multiply each outcome by probability of that outcome
        #n+1 and n-1 like neighbors in ARandomWalk
        
        #want A[col][col+1], A[col][col], A[col][col-1]
        #if col == 0 :
        #    can't play so we transition to 0
        #    all indices in the column are 0
        
        #column is from, row is to.
        
        for col in range(0,160):
            if col == 0 :
                A[col, col] = 1
            elif col == 159:
                A[col-1, col] = .5
                A[col, col] = .5
            else:
                A[col-1, col] = .5
                A[col, col] = .05
                A[col+1, col] = .45
        return A 

    def valIter(self):
        
        '''
        These are the two options 
        When you stop, you can cash out the reward
        when you plan, the you can win or lose 
        '''
        #converge = cutoff
        vstop = self.reward
        vplay = np.zeros(self.domsize)
       
        
        for i in range(self.domsize):
            vplay[i] = np.dot(self.A[:,i],self.value)  #<--Note how this is computed
            
        self.value=np.amax(np.array([vstop,vplay]),axis=0)
        return vplay,self.value


        
#Actions of Maze problem        
actions=['up','left','down','right','stop']
        
class MDPMaze:
    def __init__(self,maze,stateReward):

        self.maze = maze
        self.stateReward = stateReward
        self.stateSize = maze.stateSize
        self.stateReward.resize(self.stateSize)
               
        self.eps = 0.30
        self.gamma = 0.9
        self.rewardM = np.ones(self.stateSize)*(-1)

        
        #place holders for computing transition matrices
        self.Aup= None
        self.Aleft= None
        self.Adown= None
        self.Aright= None
        self.Astop = None

        # computeTransitionMatrices function should compute self.Aup, self.Aleft, self.Adown, self.Aright and self.Astop
        # update the 5 matrices inside computeTransitionMatrices()
        self.computeTransitionMatrices() 

        
        self.value=np.zeros(self.stateSize)
        self.policy=None 
        
        
    # You can use this to construct the noisy matrices    
    def ARandomWalk(self):
        A=np.zeros((self.stateSize,self.stateSize))
    
        for col in range(self.stateSize):
            nbrs=self.maze.nbrList(col)
            p=1/(len(nbrs)+1)       
            A[col,col]=p
            for r in nbrs:
                A[r,col]=p  
        return A

    def computeTransitionMatrices(self):
        '''put code here to initialize the matrices '''
        self.Aup = np.zeros((self.stateSize, self.stateSize))
        self.Aleft = np.zeros((self.stateSize, self.stateSize))
        self.Adown = np.zeros((self.stateSize, self.stateSize))
        self.Aright = np.zeros((self.stateSize, self.stateSize))
        self.Astop = np.zeros((self.stateSize, self.stateSize))
        # pass
        Arandom = np.zeros((self.stateSize, self.stateSize))
        AupP = np.zeros((self.stateSize, self.stateSize))
        AdownP = np.zeros((self.stateSize, self.stateSize))
        AleftP = np.zeros((self.stateSize, self.stateSize))
        ArightP = np.zeros((self.stateSize, self.stateSize))
        print(self.stateSize)
        
        #creating Arandom
        for col in range(self.stateSize):
            self.Astop[col,col] = 1
            if col+10 >= self.stateSize and col%10 == 9:
                Arandom[col, col-1] = .3333
                Arandom[col, col] = .3333
                Arandom[col, col-10] = .3333
            elif col+10 >= self.stateSize and col%10 == 0:
                Arandom[col, col+1] = .3333
                Arandom[col, col] = .3333
                Arandom[col, col-10] = .3333
            elif col-10 < 0 and col%10 == 9:
                Arandom[col, col-1] = .3333
                Arandom[col, col] = .3333
                Arandom[col, col+10] = .3333
            elif col-10 < 0 and col%10 == 0:
                Arandom[col, col+1] = .3333
                Arandom[col, col] = .3333
                Arandom[col, col+10] = .3333
            elif col+10 >= self.stateSize and not (col%10 == 9 or col%10 == 0):
                Arandom[col, col] = .25
                Arandom[col, col+1] = .25
                Arandom[col, col-1] = .25
                Arandom[col, col-10] = .25
            elif col-10 < 0 and not (col%10 == 9 or col%10 == 0):
                Arandom[col, col] = .25
                Arandom[col, col+1] = .25
                Arandom[col, col-1] = .25
                Arandom[col, col+10] = .25
            elif col%10 == 9 and not (col-10 < 0 or col+10 >= self.stateSize):
                Arandom[col, col] = .25
                Arandom[col, col-1] = .25
                Arandom[col, col+10] = .25
                Arandom[col, col-10] = .25
            elif col%10 == 0 and not (col-10 < 0 or col+10 >= self.stateSize):
                Arandom[col, col] = .25
                Arandom[col, col+1] = .25
                Arandom[col, col+10] = .25
                Arandom[col, col-10] = .25
            else:
                Arandom[col, col] = .2
                Arandom[col, col+1] = .2
                Arandom[col, col-1] = .2
                Arandom[col, col+10] = .2
                Arandom[col, col-10] = .2
                     
            
        for col in range(self.stateSize):
            
            if col+10 >= self.stateSize: #if there is a wall below bot
                AdownP[col, col] = 1
            else: 
                AdownP[col, col+10] = 1
                
            if col-10 < 0: #if there is a wall above bot
                AupP[col, col] = 1
            else:
                AupP[col, col-10] = 1
                
            if col%10 == 9: #if there is a wall right of bot
                ArightP[col, col] = 1
            else:
                ArightP[col, col+1] = 1
                
            if col%10 == 0: #if there is a wall left of bot
                AleftP[col, col] = 1
            else:
                AleftP[col, col-1] = 1
                
        AupP = np.transpose(AupP)
        AleftP = np.transpose(AleftP)
        ArightP = np.transpose(ArightP)
        AdownP = np.transpose(AdownP)
        Arandom = np.transpose(Arandom)
        self.Aup = (1-self.eps)*AupP + self.eps*Arandom
        self.Adown = (1-self.eps)*AdownP + self.eps*Arandom
        self.Aleft = (1-self.eps)*AleftP + self.eps*Arandom
        self.Aright = (1-self.eps)*ArightP + self.eps*Arandom
        print(self.Aleft)
        #make sure to use helper functions
        #what if there is a wall for a neighbor
        #can't move into a wall
    def valIter(self):
        ''' This should update self.value'''
        pass

        
    def computePolity(self):
        '''write some code here'''
        self.policy=None #This shoule be a list so 
                         #that each location corresponds to a state and
                         #holds one of the 5 ossible actions
        
                        
        
if __name__=="__main__":

    
    ''' silly game '''    
    N = 2320 # <-change me to get convergence
    
    gambling = MDPSillyGame()
    print(gambling.transitionMatrix(gambling.eps))
    for i in range(N):
        vplay,vn = gambling.valIter()    
    print('V_stop\tV_play\tmax_u V_n')
    for i in range(60,110):
        print(gambling.reward[i],'\t', vplay[i],'\t', vn[i])

    
    ''' MAZE MDP '''
    
    myMaze=maze(np.array([
                [0,0,0,0,0,0,0,0,0,0],
                [0,1,0,0,0,0,0,0,1,0],
                [0,1,0,1,1,0,1,0,1,0],
                [0,1,0,1,0,0,1,0,1,0],
                [0,1,1,1,0,1,1,0,1,0],
                [0,1,0,0,0,1,0,0,0,0],
                [0,0,0,0,0,1,0,0,1,0],
                [0,0,0,0,0,0,0,0,1,0]]))

    stateReward=np.array([
                [0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,100,0,0,0,0,0],
                [-1000,-1000,-1000,-1000,-1000,-1000,-1000,-1000,-1000,-1000]])

    mdp = MDPMaze(myMaze,stateReward)

    iterCount=100
    printSkip=10

    for i  in range(iterCount):
        mdp.valIter()
        if np.mod(i,printSkip)==0:
            print("Iteration ",i) 
            pShow(mdp.value,myMaze)
    
#   Gamma - The discount factor describes the preference of an agent 
#   for current rewards over future rewards. When γ is close to 0, 
#   rewards in the distant future are viewed as insignificant. 
#   When γ is 1, discounted rewards are exactly equivalent to additive rewards, 
#   so additive rewards are a special case of discounted rewards.