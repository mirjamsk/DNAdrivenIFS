'''
Created on 31. 3. 2014.

@author: Monsieur
'''
import math

class Fitness():

    #distanceFunc =euclideanDistance
    
    @classmethod
    def setDistanceFunction(cls, fitnessFunc):
        if fitnessFunc == "euclidean":
            cls.distanceFunc = cls.euclideanDistance
        elif fitnessFunc == "manhattan":
            cls.distanceFunc = cls.manhattanDistance
        else :       
            raise "In Fitness.setDistanceFunction:no such function"
        
       
    @classmethod
    def getFitnessValue(cls, p1,p2):
        return cls.distanceFunc(p1,p2)  

    @classmethod
    def euclideanDistance(cls,  point1, point2):
        return math.sqrt( (point1[0]-point2[0])**2 + (point1[1]-point2[1])**2 ) 
    
    @classmethod
    def manhattanDistance(cls,  point1, point2):
        return math.fabs( point1[0]-point2[0]) + math.fabs(point1[1]-point2[1])
           
    distanceFunc = euclideanDistance
    