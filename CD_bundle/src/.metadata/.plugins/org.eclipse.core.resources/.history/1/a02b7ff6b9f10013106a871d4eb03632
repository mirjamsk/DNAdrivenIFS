import math
import sys
import itertools

class Fitness(object):
    def __init__(self, file1, file2):
        self.codons1 = []
        self.codons2 = []
        try:
            f = open(file1, 'r')
            fileData = f.read()
            self.codons1 = [fileData[i:i+3] for i in range(0,len(fileData),3)]
            f.close()
        except IOError:
            print "Error in Population.__init__: File1 does not appear to exist."
          
        try:
            f = open(file2, 'r')
            fileData = f.read()
            self.codons2 = [fileData[i:i+3] for i in range(0,len(fileData),3)]
            f.close()
        except IOError:
            print "Error in Population.__init__: File2 does not appear to exist."
            
             ## dictionary mapping all codons to it's index {"CCC": 0, "CCG": 1, ..., "TTT"= 64}
        codon = list(itertools.product('CGAT', repeat= 3))
        self.codonDict = dict(zip([codon[i][0]+codon[i][1]+codon[i][2] for i in range(0, len(codon))], [i for i in range(0, 64)]))
    

    def evaluate(self, individual):
        individual.setFitness(1)
        
    def calcMedian(self, individual, codons): 
        px = 0
        py = 0
        xMedian = 0.0
        yMedian = 0.0
        for codon in codons:
            if codon not in self.codonDict.keys():
                continue
            similitude = individual.getSingleSimilitude(individual.getIndexElement(self.codonDict[codon]))
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
            #print "px, py: %f, %f" %(px, py)
        xMedian = xMedian /float(len(codons))
        yMedian = yMedian /float(len(codons))
        return xMedian, yMedian
        
  
  
class ManhattanDistFit (Fitness):
    def __init__(self, file1, file2):
          super(ManhattanDistFit, self).__init__( file1, file2)  
          
    def evaluate(self, individual):
        median1 = self.calcMedian( individual, self.codons1 )
        median2 = self.calcMedian ( individual, self.codons2 )
        individual.setFitness(self.manhattanDistance(median1, median2))    
        
    def manhattanDistance( self, point1, point2):
        return abs( point1[0]-point2[0]) + math.fabs(point1[1]-point2[1])    
  
  
  
class EuclideanDistFit (Fitness):
    def __init__(self, file1, file2):
          super(EuclideanDistFit, self).__init__( file1, file2)  
          
    def evaluate(self, individual):
        median1 = self.calcMedian( individual, self.codons1 )
        median2 = self.calcMedian ( individual, self.codons2 )
        individual.setFitness(self.euclideanDistance(median1, median2))         

    def euclideanDistance(self,  point1, point2):
        return  (point1[0]-point2[0])**2 + (point1[1]-point2[1])**2 
    
    
    
class LinearInterpolation (Fitness):
    def __init__(self, file1, file2, euclFact, manhFact):
          super(LinearInterpolation, self).__init__( file1, file2)  
          self.euclFact = euclFact
          self.manhFact = manhFact
          
          
    def evaluate(self, individual):
        median1 = self.calcMedian( individual, self.codons1 )
        median2 = self.calcMedian ( individual, self.codons2 )
        euclDist = self.euclideanDistance(median1, median2)
        manhDist = self.manhattanDistance(median1, median2)
        individual.setFitness(self.euclFact*euclDist + self.manhFact*manhDist) 
        
    def euclideanDistance(self,  point1, point2):
        return  math.sqrt((point1[0]-point2[0])**2 + (point1[1]-point2[1])**2)
    
    def manhattanDistance( self, point1, point2):
        return abs( point1[0]-point2[0]) + math.fabs(point1[1]-point2[1])    
  
        
          
class MinkowskiDistFit(Fitness):
    def __init__(self, file1, file2, p=3):
        super(MinkowskiDistFit, self).__init__( file1, file2)  
        self.p = p;
        
        
    def evaluate(self, individual):
        median1 = self.calcMedian( individual, self.codons1 )
        median2 = self.calcMedian ( individual, self.codons2 )
        individual.setFitness(self.minkowskiDistance(median1, median2))      
    
    
    def minkowskiDistance(self,  point1, point2):
        return  (point1[0]-point2[0])**self.p + (point1[1]-point2[1])**self.p
   
    

    
