import math
import copy
import random
import itertools
from Fitness import Fitness

##similitudes = [[1.15931,0.89346,0.802276,0.166377],
##[5.3227,0.491951,0.453776,0.596091],
##[5.73348,0.985895,0.123306,0.33284],
##[1.2409,0.961873,0.63981,0.375387],
##[5.91113,0.41471,0.15982,0.571791],
##[0.538828,0.660229,-0.137627,0.452674],
##[5.87837,0.993039,0.345593,0.330442],
##[5.09863,0.987267,0.338542,0.408452]]
##indexes = [2,7,5,4,7,7,2,4,1,2,5,5,2,1,5,1,2,2,6,4,2,2,1,2,2,1,6,7,2,2,5,4,7,7,5,5,4,7,1,1,1,6,6,1,5,2,6,1,2,7,5,1,7,4,2,6,2,1,5,5,5,6,6,6]


class Individual:
    def __init__(self):
        self.similitudes = []
        self.indexes = []
        self.fitness = 0.0
        
        for i in range(8):
            self.similitudes.append([random.uniform(0,2*math.pi),
                                random.uniform(-1.0, 1.0),
                                random.uniform(-1.0, 1.0),
                                random.random()])
        for i in range(64):
            self.indexes.append(random.randrange(0,8))
        
    
    def setFitness(self, fitness):
        self.fitness = fitness
        
    def getFitness(self):
        return self.fitness
    
    def getSingleSimilitude(self, index):
        return self.similitudes[index]
    
    def getSingleSimilitudeCopy(self, index):
        return copy.deepcopy(self.similitudes[index])
    
    def setSingleSimilitude(self, index, similitude):
        if len(similitude) != 4:
                raise "In Individual.setSingleSimilitude: type or length of input list  is wrong"
        self.similitudes[index] = similitude
            
    def setAllSimilitudes(self, similitudes):
        if len(similitudes) != 8:
            raise "In Individual.setALlSimilitudes:type or length of input list  is wrong"
        for s in similitudes:
            if len(s) != 4:
                raise "In Individual.setAllSimilitudes: type or length of input list  is wrong"
        self.similitudes = similitudes
        
    def getAllSimilitudes(self):
        return self.similitudes
    
    def getAllSimilitudesCopy(self):
        return copy.deepcopy(self.similitudes)
    
    def setAllIndexes(self, indexes):
        if len(indexes) != 64:
            raise "In Individual.setALlIndexes: type or length of input list  is wrong"
        self.indexes = indexes
        
    def setIndexElement(self, i, val):
        if val not in [0,1,2,3,4,5,6,7]:
            raise "In Individual.setIndexElement: type or length of input val is wrong"
        self.indexes[i] = val
    
    def getIndexElement(self, i):
        return self.indexes[i]

    def getIndexesCopy(self):
        return copy.deepcopy(self.indexes)
    
    def getIndexes(self):
        return self.indexes

