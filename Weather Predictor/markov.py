import numpy as np
import json

'''
If you want to implement additional drawing functions please do not 
submit them. The autograder will get upset if you are tyring to inlclude
matplotlib. 

The grader will replace drawprob funcitons with empty ones for grading
'''

#used to visualize robot and maze probability distributions
from drawprob import pList,pShow,robotShow

#Fake weather sequence to test the weather model
days=['rain', 'rain', 'rain', 'clouds', 'rain', 'sun', 'clouds', 'clouds', 
      'rain', 'sun', 'rain', 'rain', 'clouds', 'clouds', 'sun', 'sun', 
      'clouds', 'clouds', 'rain', 'clouds', 'sun', 'rain', 'rain', 'sun',
      'sun', 'clouds', 'clouds', 'rain', 'rain', 'sun', 'sun', 'rain', 
      'rain', 'sun', 'clouds', 'clouds', 'sun', 'sun', 'clouds', 'rain', 
      'rain', 'rain', 'rain', 'sun', 'sun', 'sun', 'sun', 'clouds', 'sun', 
      'clouds', 'clouds', 'sun', 'clouds', 'rain', 'sun', 'sun', 'sun', 
      'clouds', 'sun', 'rain', 'sun', 'sun', 'sun', 'sun', 'clouds', 
      'rain', 'clouds', 'clouds', 'sun', 'sun', 'sun', 'sun']

class weatherModel:
    
    def __init__(self):
        self.types=('sun','clouds','rain')
        
        self.counts=np.zeros((3,3))
        self.transitionMatrix=[]
        self.type2idx=dict(sun=0,clouds=1,rain=2)
 
        self.prob=np.zeros(3)
        
        #set today to cloudy
        self.prob[self.type2idx['clouds']]=1.0


        '''------- PUT YOUR ANSWERS HERE  ---- '''
        self.pTomorrow = np.array([0.71910112, 0.21910112, 0.06179775])  #Should be np.array([psun,pclouds,prain])
        self.predictionHorizon= 5 #Should be integer
        '''----------------------------------- '''
            
        
    def read_weather_log(self,fname):
        with open(fname,'r') as fh:
            days=[]
            for line in fh:
                d=json.loads(line)
                #print(line)
                #print(str(d['weather'][0]['main']))
                days.append(d['weather'][0]['main'])
        print('Read %d days.'%(len(days),))
        print('Possible States: ' + str(set(days)))
        return days
    
    def convert_raw(self,raw_days):
        '''
        Convert from raw days (which include other descriptors) to sun-rain-coulds sequence
        You can also modify the "read_data" function to do this automatically.
        '''
        new = []
        for data in raw_days : 
            if data == "Clear":
                data = 'sun'
                new.append(data)
            elif data == "Thunderstorm" or data == "Rain"  or data == "Snow" :
                data = 'rain'
                new.append(data)
            else :
                data = 'clouds'
                new.append(data)
        #replace with actual sequence
        return new      
           
    def computeTransitionMatirx(self,data):
        '''put something here to comput self.transitionMatrix'''
        #transition is 3x3 matrix. row corresponds to weather today column indicates the weather the day before
        #take count of each weather. divide by total days, gives probability
        #take day before and current day and track how many times that weather pattern appears.
        
        self.transitionMatrix = np.zeros((3,3))
        counts = np.zeros(3)
        idx = 0
        
        while idx < len(data)-1:
            
            if data[idx] == 'sun' :
                counts[0] += 1
                if data[idx+1] == 'sun' :
                    self.transitionMatrix[0, 0] += 1
                elif data[idx+1] == 'clouds' :
                    self.transitionMatrix[0, 1] += 1
                else :
                    self.transitionMatrix[0, 2] += 1
                    
            elif data[idx] == 'clouds' :
                counts[1] += 1
                if data[idx+1] == 'sun' :
                    self.transitionMatrix[1, 0] += 1
                elif data[idx+1] == 'clouds' :
                     self.transitionMatrix[1, 1] += 1
                else :
                    self.transitionMatrix[1, 2] += 1
                    
            elif data[idx] == 'rain' :
                counts[2] += 1
                if data[idx+1] == 'sun' :
                    self.transitionMatrix[2, 0] += 1
                elif data[idx+1] == 'clouds' :
                    self.transitionMatrix[2, 1] += 1
                else :
                    self.transitionMatrix[2, 2] += 1
            idx += 1
            
        self.transitionMatrix[0,:] = self.transitionMatrix[0,:]/counts[0]
        self.transitionMatrix[1,:] = self.transitionMatrix[1,:]/counts[1]
        self.transitionMatrix[2,:] = self.transitionMatrix[2,:]/counts[2]
        
        self.transitionMatrix = np.transpose(self.transitionMatrix)
        return self.transitionMatrix
            
    def predict(self):
        ''' 
        Use current probability to predict one day ahead
        This matrix multiplication means that the entry
        [row][col] is the transition probability from 
        state col to state row
        
        Note, that you need to use np.dot instead of np.mul 
        in order to get the correct matrix multiplication 
        '''
        pnext=np.dot(self.transitionMatrix,self.prob)
        self.prob=pnext

        
class maze:
    def __init__(self,world):
        self.world=world
        self.worldShape=world.shape
        self.stateSize=self.worldShape[0]*self.worldShape[1]

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
        r,c=self.state2coord(s)
        if r>0 and self.world[r-1,c]==0:
            nbrs+=1
        if r< self.worldShape[0]-1 and self.world[r+1,c]==0:
            nbrs+=1
        if c>0 and self.world[r,c-1]==0:
            nbrs+=1
        if c< self.worldShape[1]-1 and self.world[r,c+1]==0:
            nbrs+=1
        return nbrs

    def nbrList(self,s):
    # returns neighbors index of a given state (0-79)
        nbrs=[]
        r,c=self.state2coord(s)
        if r > 0 and self.world[r-1,c]==0:
            nbrs.append(self.coord2state((r-1,c)))
        if r < self.worldShape[0]-1 and self.world[r+1,c]==0:
            nbrs.append(self.coord2state((r+1,c)))
        if c > 0 and self.world[r,c-1]==0:
            nbrs.append(self.coord2state((r,c-1)))
        if c < self.worldShape[1]-1 and self.world[r,c+1]==0:
            nbrs.append(self.coord2state((r,c+1)))
        return nbrs

    def actionList(self,s):
        nbrs=[]
        r,c=self.state2coord(s)
        if r > 0 and self.world[r-1,c]==0:
            nbrs.append('U')
        if r < self.worldShape[0]-1 and self.world[r+1,c]==0:
            nbrs.append('D')
        if c > 0 and self.world[r,c-1]==0:
            nbrs.append('L')
        if c < self.worldShape[1]-1 and self.world[r,c+1]==0:
            nbrs.append('R')
        return nbrs

    def observation(self,s):
        #returns: [up, left, down, right]
        wlist=np.zeros(4)
        r,c=self.state2coord(s)
        #up
        if r==0 or self.world[r-1,c]>0:
            wlist[0]=1
        #down
        if r==(self.worldShape[0]-1) or self.world[r+1,c]>0:
            wlist[2]=1
        #left
        if c==0 or self.world[r,c-1]>0:
            wlist[1]=1
        #right
        if c==(self.worldShape[1]-1) or self.world[r,c+1]>0:
            wlist[3]=1
        return wlist
        
        
''' 
robot class that contains 
 
 * maze model  
 * a random action model 
 * estiamte over the possible robot locatins in the maze

 You will implement Bayes filter for localizaiton in this class
 You can think of it as trying to figure our the robot location from
 a stream of sensor measuremtns of the form [0,1,1,0] where the order is
 [up,left,down,right] and zero indicates free space and 1 indicates 
 a maze edge or a wall
'''    

class robot:
    def __init__(self,maze):
        self.maze=maze

        self.prob = np.zeros(maze.stateSize)  #<--- estimate of robot position        
        self.prob[0]=1                      #Assume you start out at location 0
        
        self.A=self.ARandomWalk()           #<--- Transition Matrix

        self.obsError=0.2
        self.kidnapped = False
        
        '''------- Put your answeres here ---- '''
        self.loc1= 53
        self.loc2 = 53
        self.errors1=None
        self.errors2 = None
        '''----------------------------------- '''
        
    #matrix power
    def mpower(self,A,n):
        res=np.identity(A.shape[0])
        for i in range(n):
            res=np.dot(res,A)
        return res

    def randomize(self):
        #get initial condition after long wandering
        Asteady=self.mpower(self.A,1000)
        psteady=Asteady[:,1]
        self.prob=psteady
            
        
    def obsLiklihood(self,o):
        
        likelihood = np.ones(self.maze.stateSize) #Should be vector of appropriate length
        
        for location in range(0,80) :

            idx = 0
            for observation in self.maze.observation(location) :
                if observation == o[idx] :
                    likelihood[location] = likelihood[location] * 0.8
                else :
                    likelihood[location] = likelihood[location] * 0.2
                idx += 1
        return likelihood

        
    def ARandomWalk(self): 
        A = np.zeros((80,80)) #shold be matrix not zeros!
        for idx in range(0,80):
            for neighbor in self.maze.nbrList(idx) :
                A[neighbor][idx] = 1/(len(self.maze.nbrList(idx))+1)
            A[idx][idx] = 1/(len(self.maze.nbrList(idx))+1)
            idx += 1
        return A
            
    def step(self):
        #this is how A should work
        pn=np.dot(self.A,self.prob)
        self.prob=pn

    def bayesFilter(self,obs):
        #update prob
        #obs is individual observation
        #we run through a list of observations
        prediction = np.dot(self.A, self.prob)
        correction = self.obsLiklihood(obs) * prediction

        alpha = 1/sum(correction)
        correction *= alpha
        
        self.prob = correction
        pass
    

# =======================================================================================

if __name__=="__main__":
	    
    # ------- Weather ------    
    
    weather=weatherModel()
    
    raw_days=weather.read_weather_log('weather.log')
    dayz = raw_days
    
    '''
    Convert raw sequenc into sequcne of ['sun', 'rain', 'clouds']
    '''
    #Train first on fake data
    raw_days = weather.convert_raw(raw_days)
    weather.computeTransitionMatirx(raw_days) #initializes transition matrix
    weather.prob=np.zeros(3)
    weather.prob[weather.type2idx['sun']]=1
    weather.prob #<--- you should report this value
    print(weather.transitionMatrix)
    #print(weather.prob)
    weather.pTomorrow = np.dot(weather.transitionMatrix, np.transpose(weather.prob))
    #print(weather.pTomorrow)
 
        
    '''loop n times and calculate next probability. If p = p+1 then set the horizon to n.'''
    ''' Store the next p in a variable then compare in the next loop compare it to the next p'''
#    for i in range(0, 20) :
#        print (weather.prob, i)
#        weather.predict()
    
   
    # ------- Robot Maze ------    
    
    myMaze=maze(np.array([
				[0,0,0,0,0,0,0,0,0,0],
				[0,1,0,0,0,0,0,0,1,0],
				[0,1,0,1,1,0,1,0,1,0],
				[0,1,0,1,0,0,1,0,1,0],
				[0,1,1,1,0,1,1,0,1,0],
				[0,0,0,0,0,1,0,0,0,0],
				[0,0,1,0,1,1,0,0,1,0],
				[0,0,0,0,0,0,0,0,1,0]]))
    
    # =============================
    # usage of showState(p):
    
    p=np.zeros(myMaze.stateSize)
    p[0] = 0.2
    p[2] = 0.3
    p[8] = 0.5

    #pShow(p,myMaze) #Note that pShow scales the probability so that the 
                    #Maximum values is 1 this makes it helpful to visuzliaze
                    #probabilities that are thinly spread out
                    
    # =============================
    
    
    rob=robot(myMaze)
    rob.prob=p 
    
    #print(rob.A) #80x80 matrix
    #print(rob.prob) #list of length 80. prob of rob being at location x
    #print(rob.maze.world[0])
    #print(rob.maze.world) #map of the world. locations. 1==wall
    #print(rob.maze.worldShape) #dimensions 8x10. 
    #print(rob.maze.stateSize) #number of locations in world
    #robotShow(rob)
    rob.step()
    rob.step()
    rob.step()
    #robotShow(rob)    
    #print(rob.prob)
    rob.obsLiklihood([0,1,0,0])
    ''' Set rob.prob to the steady state'''     
    rob.randomize()
       
     
    #two input sequences both contain occasional sensor errors
    #in one of them the robot got kidnapped!
    
    #Can you tell by the behavior of bayes filter which sequence of 
    #observations comes from the kindnapped robot?

    
    obsA=[[1,0,0,0],[1,0,0,0],[0,0,0,0],[0,1,0,1],[0,0,1,1],
          [1,1,0,0],[1,1,0,1],[0,0,1,1],[1,0,0,0],[0,0,0,1],
          [1,1,0,1],[0,0,0,0],[0,1,0,1],[0,0,0,1],[0,1,0,1],
          [0,0,0,1],[1,0,0,0]]
 
    
    
    obsB=[[0,0,0,1],[1,0,1,0],[0,0,0,0],[0,1,0,1],[0,1,0,1],
          [0,1,0,1],[0,0,0,1],[1,0,0,0],[1,0,1,0],[1,0,0,0],
          [0,0,0,0],[0,1,0,1],[0,0,1,1],[1,1,0,0],[0,1,0,1],
          [0,0,1,1],[1,0,0,0]]
    '''                   
    try this for both input sequences     
    you can run this to test bayes filter
    NOTE: This will show nothing since the functions are not implemented 
    but once you get the bayes filter running, it will show the probability 
    distribution converging over a few steps
    '''
    for obs in obsA :
        rob.bayesFilter(obs)
        #robotShow(rob)
        
#    for obs in obsB :
#        rob.bayesFilter(obs)
#    
#    
    #This will pop up a lot of figures. 
    #You can close them with close_all()
    
    