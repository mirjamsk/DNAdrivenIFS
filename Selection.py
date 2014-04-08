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
    def tournament( cls, population):
        tempIndividuals = []
        for i in range (0, population.populationSize):
            t1 = population.getIndividual(int(random.uniform(0, len(population.individuals))))
            t2 = population.getIndividual(int(random.uniform(0, len(population.individuals))))
            if t1.getFitness() > t2.getFitness():
                tempIndividuals.append(copy.deepcopy(t1))
            else:
                tempIndividuals.append(copy.deepcopy(t2))
        if cls.elitism == True:
            population.individuals.sort(key=lambda x: x.getFitness(), reverse= True)
            tempIndividuals.pop()
            tempIndividuals.append(population.getIndividual(0))
        return tempIndividuals
    
    @staticmethod
    def elimination(population):
        count = int(0.3*population.populationSize)
        
        population.individuals.sort(key=lambda x: x.getFitness(), reverse= True)
        population.individuals = population.individuals[:population.populationSize]
        bestFitness = population.getIndividual(0).getFitness()        
        worstFitness = population.getIndividual(-1).getFitness()
        for i in range (0, count):
            index = int(random.uniform(0, len(population.individuals)))
            individual = population.getIndividual(index)
            probability = (bestFitness - individual.getFitness() ) / (bestFitness- worstFitness)
            if random.uniform(0,1)  < probability:
                population.randomizeIndividual(index)
        
        return population.individuals
    
    selectionOperator = tournament