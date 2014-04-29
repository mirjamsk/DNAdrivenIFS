from Population import Population
import random
from Fitness import Fitness, ManhattanDistFit, EuclideanDistFit
from Crossover import Crossover
from Selection import Selection
from Mutation import Mutation
from argsParser import argsParser


def printBest(p):
    p.individuals.sort(key=lambda x: x.getFitness(), reverse= True)
    for j in range(5):
        print j , ". best, fitness: " , p.getIndividual(j).getFitness()
    

#def run(numberOfGenerations, populationSize, crossoverFactor, mutationFactor, outputFile):
def run ( p, args):

    for i in range(0, args.numberOfGenerations):

        ##crossover
        for j in range (0, int(args.crossoverFactor*args.populationSize)):   
            p.crossover(int(random.uniform(0, args.populationSize)), int(random.uniform(0, args.populationSize)))
            
        ##mutation
        for j in range (0, int(args.mutationFactor*args.populationSize)):    
            p.mutation(int(random.uniform(0, args.populationSize)))

        ##selection
        p.selection()

        ## sort and print best 5
        printBest(p)
        print"**End of run ", i , "**"                
    return


def writeOut(output, p):
    #write out the best Similitude/Index pair to the output
    f = open(output, "w");
    data = ""
    
    for similitude in p.getIndividual(0).getAllSimilitudesCopy():
        for s in similitude:
            data += str(s) + " "
        data+="\n"
        
    data +="#\n"
    
    for index in p.getIndividual(0).getIndexesCopy():
            data += str(index) + " "
    
    f.write(data);
    f.close();




def main():
    args = argsParser()
    args.parse('args.xml')
    if   args.fitnessFunction == "euclidean" : fitOp = EuclideanDistFit(args.input1, args.input2)
    elif args.fitnessFunction == "manhattan" : fitOp = ManhattanDistFit(args.input1, args.input2)
#     elif args.fitnessFunction == "minkowski" : fitOp = Fitness.minkowskiDistance
    else : raise "Something went wrong while assigning the fitness function"
#     
    if   args.selection       == "tournament" : selOp = Selection.tournament
    elif args.selection       == "elimination": selOp = Selection.elimination
    else : raise "Something went wrong while assigning the selection operator"
   
   
    if   args.elitism == 0: Selection.setElitism(0)
    elif args.elitism == 1: Selection.setElitism(1)
    else : raise "Something went wrong while assigning elitism"
    

    crossOp = Crossover.crossover
    mutationOp = Mutation.mutation
    p = Population(args.populationSize, fitOp, selOp, crossOp, mutationOp)
    # set fitness function
    #Fitness.setDistanceFunction(args.fitnessFunction)
    # set selectionOperator
    #Selection.setSelectionOperator(args.selection)
    # set if elitist
    #Selection.setElitism(args.elitism)
    
    #p = Population(args.populationSize, args.input1, args.input2)
    p.evaluateAll()
    run (p, args)
    writeOut(args.outputFile, p)
    
if __name__ == '__main__':
    main()
