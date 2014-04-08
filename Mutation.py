import random

class Mutation():
  
    @staticmethod
    def mutation(individual):
        ##similitudes mutation
        simIndex = int(random.uniform(0, 8.0))
        paramIndex = int(random.uniform(0, 4.0))
        similitude = individual.getSingleSimilitude(simIndex)
        similitude[paramIndex] += random.uniform(-0.1, 0.1)
        
       
        if paramIndex == 3 and similitude[paramIndex] >1:
            similitude[paramIndex] = 2- similitude[paramIndex]
        elif paramIndex == 3 and similitude[paramIndex] <0:
            similitude[paramIndex] = -similitude[paramIndex]
         
        ##indexes mutation
        indIndex = int(random.uniform(0, 64.0))
        individual.setIndexElement(indIndex,int(random.uniform(0, 8)))        
