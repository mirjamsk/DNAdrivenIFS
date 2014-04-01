'''
Created on 31. 3. 2014.

@author: Monsieur
'''
import random
import copy

class Selection():
    elitism = False;
    
    @classmethod
    def setElitism(cls, isElitist):
        if isElitist == 0:      cls.elitism = False
        elif  isElitist == 1:   cls.elitism = True
        else :                  raise "In Selection.setElitism: argument can only be either 0 or 1"
        
    @classmethod
    def setSelectionOperator(cls, selOperator):
        if selOperator == "tournament":
            cls.selectionOperator = cls.tournament
        elif selOperator == "elimination":
            cls.selectionOperator = cls.elimination
        else :       
            raise "In Selection.setSelectionOperator:no such selection operator"
        
    
    @classmethod
    def selection(cls, population):
        return cls.selectionOperator(population)
        
    @classmethod
    def tournament(cls, population):
        tempChromosomes = []
        for i in range (0, population.populationSize):
            t1 = population.getChromosome(int(random.uniform(0, len(population.chromosomes))))
            t2 = population.getChromosome(int(random.uniform(0, len(population.chromosomes))))
            if t1.getFitness() > t2.getFitness():
                tempChromosomes.append(copy.deepcopy(t1))
            else:
                tempChromosomes.append(copy.deepcopy(t2))
        if cls.elitism == True:
            population.chromosomes.sort(key=lambda x: x.getFitness(), reverse= True)
            tempChromosomes.pop()
            tempChromosomes.append(population.getChromosome(0))
        return tempChromosomes
    
    @classmethod
    def elimination(cls, population):
  
        count = int(0.3*population.populationSize)
        
        population.chromosomes.sort(key=lambda x: x.getFitness(), reverse= True)
        population.chromosomes = population.chromosomes[:population.populationSize]
        bestFitness = population.getChromosome(0).getFitness()        
        worstFitness = population.getChromosome(-1).getFitness()
        for i in range (0, count):
            index = int(random.uniform(0, len(population.chromosomes)))
            chromosome = population.getChromosome(index)
            probability = (bestFitness - chromosome.getFitness() ) / (bestFitness- worstFitness)
            if random.uniform(0,1)  < probability:
                population.randomizeChromosome(index)
        
        return population.chromosomes
    
    selectionOperator = tournament