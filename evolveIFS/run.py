from Population import Population
import random
from Fitness import Fitness, ManhattanDistFit, EuclideanDistFit, MinkowskiDistFit, MeanFit, LinearInterpolation
from Crossover import Crossover
from Selection import Selection
from Mutation import Mutation
from argsParser import argsParser


def printBest(p):
    p.individuals.sort(key=lambda x: x.getFitness(), reverse= True)
    for j in range(5):
        print j , ". best, fitness: " , p.getIndividual(j).getFitness()
    

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
    
def writeOutBatch(i, p):
    #write out the best Similitude/Index pair to the output
    f = open("output/similitude" + str(i) + ".txt", "w");
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

    logStr = "Batch %3d,\t best fitness: %f \n" %(i, p.getIndividual(0).getFitness())
    if i == 1: logFile = open("output/log.txt", "w");
    else:      logFile = open("output/log.txt", "a+");
    logFile.write(logStr)






def main():
    args = argsParser()
    args.parse('args.xml')
    if   args.fitnessFunction == "euclidean" : fitOp = EuclideanDistFit(args.input1, args.input2)
    elif args.fitnessFunction == "manhattan" : fitOp = ManhattanDistFit(args.input1, args.input2)
    elif args.fitnessFunction == "mean"      : fitOp = MeanFit(args.input1, args.input2)
    elif args.fitnessFunction == "minkowski" : fitOp = MinkowskiDistFit(args.input1, args.input2, args.p)
    elif args.fitnessFunction == "linear"    : fitOp = LinearInterpolation(args.input1, args.input2, args.euclF, args.manhF)
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
    
    if args.batch == 1:
        p = Population(args.populationSize, fitOp, selOp, crossOp, mutationOp)
        p.evaluateAll() 
        run (p, args)
        writeOut(args.outputFile, p)
    else:
        for i in range(0, args.batch):
            print "\nBatch: %d/%d" %(i+1, args.batch)
            p = Population(args.populationSize, fitOp, selOp, crossOp, mutationOp)
            p.evaluateAll() 
            run (p, args)
            writeOutBatch(i+1, p)
    
if __name__ == '__main__':
    main()
