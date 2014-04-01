import random
import copy
from Chromosome import Chromosome
from Selection import Selection


class Population():
    def __init__(self, populationSize, file1, file2):
        self.codons1 = []
        self.codons2 = []
        self.chromosomes = []
        self.populationSize = populationSize
        
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
        for i in range (0, populationSize):
            self.chromosomes.append(Chromosome())  

    def addChromosome(self, chromosome):
        chromosome.evaluateSelf(self.codons1, self.codons2)
        self.chromosomes.append(chromosome)
        
    def randomizeChromosome(self, index):
        self.chromosomes[index] = Chromosome()
        self.chromosomes[index].evaluateSelf(self.codons1, self.codons2)
    
    def getChromosome(self, index):
        return self.chromosomes[index]
    
    def getChromosomeCopy(self, index):
        return copy.deepcopy(self.chromosomes[index])

    def crossover(self, indexP1, indexP2):
        parent1 = self.getChromosome(indexP1)
        parent2 = self.getChromosome(indexP2)
        child1 = Chromosome()
        child2 = Chromosome()
        crossPoint1 = random.randrange(0,8)

        ##similitudes one-point crossover
        tempList = parent1.getAllSimilitudes()[:crossPoint1]
        tempList.extend( parent2.getAllSimilitudes()[crossPoint1:] )
        child1.setAllSimilitudes(tempList)

        
        tempList = parent2.getAllSimilitudes()[:crossPoint1]
        tempList.extend( parent1.getAllSimilitudesCopy()[crossPoint1:] )
        child2.setAllSimilitudes(tempList)
        
        ##indexList 2 point crossover
        crossPoint1 = random.randrange(0,64)
        crossPoint2 = random.randrange(0,64)
        if crossPoint1 > crossPoint2:
            crossPoint1, crossPoint2 = crossPoint2, crossPoint1

        tempList = parent1.getIndexes()[:crossPoint1]
        tempList.extend( parent2.getIndexes()[crossPoint1:crossPoint2] )
        tempList.extend( parent1.getIndexes()[crossPoint2:] )
        child1.setAllIndexes(tempList)

        tempList = parent2.getIndexes()[:crossPoint1]
        tempList.extend( parent1.getIndexes()[crossPoint1:crossPoint2] )
        tempList.extend( parent2.getIndexes()[crossPoint2:] )
        child2.setAllIndexes(tempList)
        

        self.addChromosome(child1)
        self.addChromosome(child2)
        
        
    def mutation(self, index):    
        chromosome = self.getChromosome(index);
        
        ##similitudes mutation
        simIndex = int(random.uniform(0, 8.0))
        paramIndex = int(random.uniform(0, 4.0))
        similitude = chromosome.getSingleSimilitude(simIndex)
        similitude[paramIndex] += random.uniform(-0.1, 0.1)
        
       
        if paramIndex == 3 and similitude[paramIndex] >1:
            similitude[paramIndex] = 2- similitude[paramIndex]
        elif paramIndex == 3 and similitude[paramIndex] <0:
            similitude[paramIndex] = -similitude[paramIndex]
         
        ##indexes mutation
        indIndex = int(random.uniform(0, 64.0))
        chromosome.setIndexElement(indIndex,int(random.uniform(0, 8)))        
        chromosome.evaluateSelf(self.codons1, self.codons2)

    def evaluateAll(self):
        for chromosome in self.chromosomes:
            chromosome.evaluateSelf(self.codons1 , self.codons2)   

    def selection(self):
        self.chromosomes = Selection.selection(self)
        
                       
                            
        


        



    
   
