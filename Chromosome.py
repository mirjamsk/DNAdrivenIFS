'''
Created on 18. 3. 2014.

@author: Monsieur
'''
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


class Chromosome():
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
        
        
        ## dictionary mapping all codons to it's index {"CCC": 0, "CCG": 1, ..., "TTT"= 64}
        codon = list(itertools.product('CGAT', repeat= 3))
        self.codonDict = dict(zip([codon[i][0]+codon[i][1]+codon[i][2] for i in range(0, len(codon))], [i for i in range(0, 64)]))
    
    def getSingleSimilitude(self, index):
        return self.similitudes[index]
    
    def getSingleSimilitudeCopy(self, index):
        return copy.deepcopy(self.similitudes[index])
    
    def setSingleSimilitude(self, index, similitude):
        if len(similitude) != 4:
                raise "In Chromosome.setSingleSimilitude: type or length of input list  is wrong"
        self.similitudes[index] = similitude
            
    def setAllSimilitudes(self, similitudes):
        if len(similitudes) != 8:
            raise "In Chromosome.setALlSimilitudes:type or length of input list  is wrong"
        for s in similitudes:
            if len(s) != 4:
                raise "In Chromosome.setAllSimilitudes: type or length of input list  is wrong"
        self.similitudes = similitudes
        
    def getAllSimilitudes(self):
        return self.similitudes
    
    def getAllSimilitudesCopy(self):
        return copy.deepcopy(self.similitudes)
    
    def setAllIndexes(self, indexes):
        if len(indexes) != 64:
            raise "In Chromosome.setALlIndexes: type or length of input list  is wrong"
        self.indexes = indexes
        
    def setIndexElement(self, i, val):
        if val not in [0,1,2,3,4,5,6,7]:
            raise "In Chromosome.setIndexElement: type or length of input val is wrong"
        self.indexes[i] = val
    
    def getIndexElement(self, i):
        return self.indexes[i]

    def getIndexesCopy(self):
        return copy.deepcopy(self.indexes)
    
    def getIndexes(self):
        return self.indexes

    def setFitness(self, fitness):
        self.fitness = fitness
        
    def getFitness(self):
        return self.fitness
    
    def evaluateSelf(self, codons1, codons2):
        median1 = self.calcMedian( codons1 )
        median2 = self.calcMedian ( codons2 )
        self.setFitness( Fitness.getFitnessValue(median1, median2) )
       

    def calcMedian(self, codons):
        px = 0
        py = 0
        xMedian = 0.0;
        yMedian = 0.0;
        for codon in codons:
            if codon not in self.codonDict.keys():
                continue
            similitude = self.getSingleSimilitude(self.getIndexElement(self.codonDict[codon]))
            rad = similitude[0]
            translateX = similitude[1]
            translateY = similitude[2]
            scale = similitude[3]
            x = px;
            y = py;
            px = scale *(x*math.cos(rad)- y*math.sin(rad) + translateX)
            py = scale *(x*math.sin(rad)+ y*math.cos(rad) + translateY)
            xMedian += px;
            yMedian += py;

        xMedian = xMedian /float(len(codons))
        yMedian = yMedian /float(len(codons))
        return xMedian, yMedian