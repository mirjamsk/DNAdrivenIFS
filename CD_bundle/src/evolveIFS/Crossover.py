'''
Created on 8. 4. 2014.

@author: Monsieur
'''
from Individual import Individual 
import random
class Crossover(object):
    '''
    classdocs
    '''

    @staticmethod
    def crossover( p, indexP1, indexP2):
        parent1 = p.getIndividual(indexP1)
        parent2 = p.getIndividual(indexP2)
        child1 = Individual()
        child2 = Individual()
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
        
        
        return (child1, child2)
        