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
   
    
class MeanFit(EuclideanDistFit):
    def __init__(self, file1, file2):
        super(MeanFit, self).__init__( file1, file2)  
        
    def evaluate(self, individual):
        
        median1 = self.calcMedian( individual, self.codons1 )
        median2 = self.calcMedian ( individual, self.codons2 )
        print "median1: ", median1, "median2:", median2
        scale = self.checkClustering(individual, median1, median2)
        individual.setFitness(self.euclideanDistance(median1, median2) * scale *0.5)     
    
            
    def checkClustering(self, individual, median1, median2):
       
        scale1 = self.getScale(individual, median1, median2, self.codons1)
        scale2 = self.getScale(individual, median2, median1, self.codons2)
        
        return scale1 if scale1<scale2 else scale2;
        
    def getScale(self, individual, medianSelf, medianOther ,codons):
        px = 0
        py = 0
        diffSelf = 0
        diffOther = 0
        diffCurr = sys.maxint;
        scale = 1;
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
            diffSelf = self.euclideanDistance((px,py),medianSelf)
            diffOther = self.euclideanDistance((px,py),medianOther)
            if ( diffOther <= diffSelf and  diffOther < diffCurr ):
                diffCurr = diffOther;
                scale = diffOther/diffSelf;
                print "diff other: ",  diffOther,  "DiffSelf: ",  diffSelf ,  "scale ", scale;
            
            return scale;
                             
    

# class MinMaxDistFit(Fitness):
#     def __init__(self, file1, file2):
#         super(MinMaxDistFit, self).__init__( file1, file2)  
#     
#         
#     def evaluate(self, individual):
#         median1 = self.calcMedian( individual, self.codons1 )
#         median2 = self.calcMedian ( individual, self.codons2 )
#         individual.setFitness(self.minkowskiDistance(median1, median2))    
#           
#     def minMax(self, m1, m2, fp1, fp2):
#         medianEuclidean = self.euclideanDistance(m1, m2)
#         mFpEucl1 =cls.euclideanDistance(m1, fp1)
#         mFpEucl2 =cls.euclideanDistance(m2, fp2)
#         
#         return abs(medianEuclidean - (mFpEucl1+ mFpEucl2))
#     
# 
#     
#     def calcFarthestDistanceFromMedian(self, individual, median, codons):
#         px = 0
#         py = 0
#         farthestPoint = [median[0], median[1]]
#         
#         for codon in codons:
#             if codon not in self.codonDict.keys():
#                 continue
#             similitude = individual.getSingleSimilitude(individual.getIndexElement(self.codonDict[codon]))
#             rad = similitude[0]
#             translateX = similitude[1]
#             translateY = similitude[2]
#             scale = similitude[3]
#             x = px;
#             y = py;
#             px = scale *(x*math.cos(rad)- y*math.sin(rad) + translateX)
#             py = scale *(x*math.sin(rad)+ y*math.cos(rad) + translateY)
#             
#             if Fitness.euclideanDistance(median, (px,py)) > Fitness.euclideanDistance(median, farthestPoint):
#                 farthestPoint = [px, py]
#         
#         return farthestPoint
           
   #def evaluateSelf(self, fitOp):
       # self.setFitness( fitOp.evaluate(self))
       # print "*fitness: %f" %self.getFitness()
        #---------------------------------- median1 = self.calcMedian( codons1 )
        #---------------------------------- median2 = self.calcMedian( codons2 )
        # farthestPoint1 = self.calcFarthestDistanceFromMedian(codons1, median1)
        # farthestPoint2 = self.calcFarthestDistanceFromMedian(codons2, median2)
        # self.setFitness( Fitness.minMax(m1 = median1, m2 = median2, fp1 = farthestPoint1,  fp2 = farthestPoint2 ))
        ##median1 = self.calcMedian( codons1 )
        ##median2 = self.calcMedian ( codons2 )
        #print "*median1 (%f, %f) " %median1
        #print "*median2  (%f, %f)" %median2
        
        #print "*fitness: %f" %self.getFitness()
      #try minmax

       

    