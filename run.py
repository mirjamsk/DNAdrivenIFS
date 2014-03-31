'''
Created on 18. 3. 2014.

@author: Monsieur
'''
from Population import Population
import random
#import argparse
from Fitness import Fitness
from argsParser import argsParser

#def run(numberOfGenerations, populationSize, crossoverFactor, mutationFactor, input1, input2, outputFile):
def run (args):
    p = Population(args.populationSize, args.input1, args.input2)
    p.evaluateAll()
    for i in range(0, args.numberOfGenerations):

        ##crossover
        for j in range (0, int(args.crossoverFactor*args.populationSize)):                              
            p.crossover(int(random.uniform(0, args.populationSize)), int(random.uniform(0, args.populationSize)))

        ##mutation
        for j in range (0, int(args.mutationFactor*args.populationSize)):    
            p.mutation(int(random.uniform(0, args.populationSize)))

        ##selection
        p.selection()

        ##print best 5
        best= []
        for j in range(len(p.chromosomes)):
            best.append(( p.getChromosome(j).getFitness(), j))
        best.sort(key=lambda x: x[0], reverse= True )
        for j in range(5):
            print j , ". best, fitness: " , best[j][0]
        print"**End od run ", i , "**"


    #write out the best Similitude/Index pair to the output
    f = open(args.outputFile, "w");
    data = ""
    
    for similitude in p.chromosomes[best[0][1]].getAllSimilitudesCopy():
        for s in similitude:
            data += str(s) + " "
        data+="\n"
        
    data +="#\n"
    
    for index in p.chromosomes[best[0][1]].getIndexesCopy():
            data += str(index) + " "
    
    f.write(data);
    f.close();




#===============================================================================
# def main():
#     parser = argparse.ArgumentParser(description='Script for evolving list of similitudes and indexes for DNA driven IFS fractal')
#     parser.add_argument('-i1','--input1',help='Input1 file name', type=str, required=True)
#     parser.add_argument('-i2','--input2',help='input2 file name', type=str,  required=True)
#     parser.add_argument('-o','--output',help='Output file name', type=str, default='outputSimilitudes.txt',  required=False)
#     parser.add_argument('-nGen','--nbGenerations',help='Number Of Generations', type=int, default=10, required=False)
#     parser.add_argument('-nPop','--nbPopulation',help='Number Of chromosomes in the population ', type=int, default=100,  required=False)
#     parser.add_argument('-c','--crossover',help='crossover Factor ', type=float, default=0.2,  required=False)
#     parser.add_argument('-m','--mutation',help='Mutation Factor ', type=float, default=0.2,  required=False)
#     parser.add_argument('-d','--distanceFunction',help='Distance function, either \'manhattan\' or \'euclidian\' ', type=str, default=None,  required=False)
#     
#     args = parser.parse_args()
#     if args.distanceFunction == 'manhattan':
#         Fitness.setDistanceFunction(Fitness.manhattanDistance)
#         
#     run(numberOfGenerations = args.nbGenerations , populationSize = args.nbPopulation,  crossoverFactor = args.crossover, mutationFactor = args.mutation,input1 = args.input1, input2 = args.input2, outputFile = args.output)
#     
#     ## show values ##
#     print ("Output file: %s" % args.output )
#===============================================================================
 
def main():
    args = argsParser()
    args.parse('args.xml')
    Fitness.setDistanceFunction(args.fitnessFunction)
    run (args)
    
if __name__ == '__main__':
    main()
