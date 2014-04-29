import random
import copy
from Individual import Individual


class Population():
    def __init__(self, populationSize, fitnessOp, selectionOp, crossoverOp, mutationOp):
       
        self.individuals = []
        self.populationSize = populationSize
        self.fitnessOp = fitnessOp
        self.selectionOp = selectionOp
        self.crossoverOp = crossoverOp
        self.mutationOp = mutationOp
        for i in range (0, populationSize):
            self.individuals.append(Individual())  
        


    def addIndividual(self, individual):
        self.fitnessOp.evaluate(individual)
        self.individuals.append(individual)
        
    def randomizeIndividual(self, index):
        self.individuals[index] = Individual()
        self.fitnessOp.evaluate( self.individuals[index]);
    
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
        self.fitnessOp.evaluate(individual);
        

    def evaluateAll(self):
        for individual in self.individuals:
            self.fitnessOp.evaluate(individual);

    def selection(self):
        self.individuals = self.selectionOp(self)
        
                       
                            
        


        



    
   
