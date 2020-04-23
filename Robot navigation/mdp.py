import numpy as np
from markov import *
from drawprob import pList,pShow,robotShow

        
class MDPmaze:
    def __init__(self,maze,stateReward):

        self.maze = maze
        self.stateReward = stateReward
        self.stateSize = maze.stateSize
        self.stateReward.resize(self.stateSize)
               
        self.eps = 0.01
        self.gamma = 0.9
        self.rewardM = np.ones(self.stateSize)*(-1)

        
        #place holders for computing transition matrices
        #Transition Matrices
        self.actions=['up','left','down','right','stop']
        self.Arandom=self.ARandomWalk()
        try:           
            self.Aup= None
            self.Aleft= None
            self.Adown= None
            self.Aright= None
            self.Astop = None
            self.computeTransitionMatrices()       
            self.transDict={'up':self.Aup , 'left':self.Aleft, 'down':self.Adown, 
                            'right':self.Aright, 'stop':self.Astop}
        except:
            TransitionMatrix = "transitionMatrix.pkl"
            if(os.path.isfile(TransitionMatrix)):
                with open(TransitionMatrix,'rb') as fh:    
                        self.transDict=pickle.load(fh,encoding='bytes')
        
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
        self.Aup= None
        self.Aleft= None
        self.Adown= None
        self.Aright= None
        self.Astop = None
        # pass
                
        
    def valIter(self):
        ''' This should update self.value'''
        pass

        
    def computePolity(self):
        '''write some code here'''
        self.policy=None #This shoule be a list so 
                         #that each location corresponds to a state and
                         #holds one of the 5 ossible actions
    
    def showPolicy(self):
        row,col=self.maze.worldShape
        cellstr='{!s: ^7}'
        
        policylist=self.policy.copy()
        policylist.reverse()

        for i in range(row):
            for j in range(col):
                element=policylist.pop()
                if not self.maze.world[i,j]==0:
                    element='#'
                print(cellstr.format(element),end='')          
            print('')
                        
        
if __name__=="__main__":

    
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

    mdp = MDPmaze(myMaze,stateReward)

    iterCount=100
    printSkip=10

    for i  in range(iterCount):
        mdp.valIter()
        if np.mod(i,printSkip)==0:
            print("Iteration ",i) 
            pShow(mdp.value,myMaze)

    
