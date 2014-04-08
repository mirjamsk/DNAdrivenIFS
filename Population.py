import random
import copy
from Individual import Individual


class Population():
    def __init__(self, populationSize, fitnessOp, selectionOp, crossoverOp, mutationOp, file1, file2):
        self.codons1 = []
        self.codons2 = []
        self.individuals = []
        self.populationSize = populationSize
        self.fitnessOp = fitnessOp
        self.selectionOp = selectionOp
        self.crossoverOp = crossoverOp
        self.mutationOp = mutationOp
        
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
            self.individuals.append(Individual())  

    def addIndividual(self, individual):
        individual.evaluateSelf(self.fitnessOp, self.codons1, self.codons2)
        self.individuals.append(individual)
        
    def randomizeIndividual(self, index):
        self.individuals[index] = Individual()
        self.individuals[index].evaluateSelf(self.fitnessOp, self.codons1, self.codons2)
    
    def getIndividual(self, index):
        return self.individuals[index]
    
    def getIndividualCopy(self, index):
        return copy.deepcopy(self.individuals[index])

    def crossover(self, indexP1, indexP2):
        child1, child2 = self.crossoverOp( self, indexP1, indexP2);
        self.addIndividual(child1)
        self.addIndividual(child2)
        
        
    def mutation(self, index):    
        individual = self.getIndividual(index);
        self.mutationOp(individual)
        individual.evaluateSelf(self.fitnessOp, self.codons1, self.codons2)
        

    def evaluateAll(self):
        for individual in self.individuals:
            individual.evaluateSelf(self.fitnessOp, self.codons1 , self.codons2)   

    def selection(self):
        self.individuals = self.selectionOp(self)
        
                       
                            
        


        



    
   
