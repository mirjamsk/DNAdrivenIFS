import xml.etree.ElementTree as ET

class argsParser(object):

    def __init__(self):
        self.input1= None
        self.input2 = None
        self.outputFile ='outputSimili.txt'
        self.numberOfGenerations = 10
        self.populationSize = 100
        self.crossoverFactor = 0.2
        self.mutationFactor = 0.2
        self.fitnessFunction = "euclidean"
        self.p = 3
        self.euclF = 0.5
        self.manhF = 0.5
        self.selection = "tournament"
        self.elitism = 0
        self.batch = 1
    
    def parse(self, f):
        try:
            tree = ET.parse(f)
            root = tree.getroot()
            self.input1 = root.find('InputFiles')[0].text.strip()
            self.input2 = root.find('InputFiles')[1].text.strip()
            if root.find('OutputFile') is not None: self.outputFile = root.find('OutputFile').text.strip()
            if root.find('GenerationNumber') is not None: self.assignGenerationInput(root.find('GenerationNumber').text.strip())
            if root.find('PopulationSize') is not None: self.assignPopulationInput(root.find('PopulationSize').text.strip())
            if root.find('CrossoverFactor') is not None: self.assignCrossoverInput(root.find('CrossoverFactor').text.strip())
            if root.find('MutationFactor') is not None: self.assignMutationInput(root.find('MutationFactor').text.strip())
            if root.find('FitnessFunction') is not None: self.assignFitnessFunction(root.find('FitnessFunction').text.strip())
            if root.find('Selection') is not None: self.assignSelectionOperator(root.find('Selection').text.strip())
            if root.find('Elitism') is not None: self.elitism = int(root.find('Elitism').text.strip())
            if root.find('p') is not None: self.p = int(root.find('p').text.strip())
            if root.find('euclFactor') is not None: self.euclF = float(root.find('euclFactor').text.strip())
            if root.find('manhFactor') is not None: self.manhF = float(root.find('manhFactor').text.strip())
            if root.find('Batch') is not None: self.batch = int(root.find('Batch').text.strip())
            
            self.printaj()

        except IOError:
            print "Error in argsParser.parse: File does not appear to exist."
          
    def assignGenerationInput(self, inputStr):
        try: 
            self.numberOfGenerations = int(inputStr)
        except  ValueError:
            self.numberOfGenerations = 10
            print "Exception: number of generations: \'%s\' could not be converted to an in" %inputStr
            print "Using the default value: %d" %self.numberOfGenerations
            
            
    def assignPopulationInput(self, inputStr):
        try: 
            self.populationSize = int(inputStr)
        except  ValueError:
            self.populationSize = 100
            print "Exception: population size: \'%s\' could not be converted to an int" %inputStr
            print "Using the default value: %d" %self.populationSize
    
    
    def assignCrossoverInput(self, inputStr):
        try: 
            self.crossoverFactor = float(inputStr)
        except  ValueError:
            self.crossoverFactor = 0.2
            print "Exception: crossover factor: \'%s\' could not be converted to a float" %inputStr
            print "Using the default value: %f" %self.crossoverFactor
        
        
    def assignMutationInput(self, inputStr):
        try: 
            self.mutationFactor = float(inputStr)
        except  ValueError:
            self.mutationFactor = 0.2
            print "Exception: mutation factor: \'%s\' could not be converted to a float" %inputStr
            print "Using the default value: %f" %self.mutationFactor
    
    
    def assignFitnessFunction(self, inputStr):
        if inputStr == "euclidean" or inputStr == "manhattan" or inputStr == "minkowski" or inputStr == "mean"  or inputStr == "linear":
            self.fitnessFunction = inputStr
        else :
            self.fitnessFunction = "euclidean"
            print "Exception: no such fitness function: \'%s\'" %inputStr
            print "Using the default fitness function: %s" %self.fitnessFunction
            
    
    
    def assignSelectionOperator(self, inputStr):
        if inputStr == "tournament" or inputStr == "elimination" :
            self.selection = inputStr
        else :
            self.selection = "tournament"
            print "Exception: no such selection operator: \'%s\'" %inputStr
            print "Using the default selection operator: %s" %self.selection
            
    def assignElitism(self, inputStr):
        if inputStr == "0" or inputStr == "1" :
            self.elitism = int(inputStr)
        else :
            self.elitism = 0
            print "Exception: elitism: could not parse \'%s\'" %inputStr
            print "Accepted values are either 0 or 1"
            print "Using the  default value for elitism: %d" %self.elitism
            
        
    def printaj(self):
        print "Using: "
        print "Batch: %d"                   %self.batch
        print "Input file1: " +             self.input1 
        print "Input file2: " +             self.input2
        if self.batch == 1:
            print "Output file: " +             self.outputFile 
        else: 
             print "Output file: output/similitude_n.txt" 
             print "Log file: output/log.txt"
        print "Number of Generations: %d "  %self.numberOfGenerations 
        print "Population size: %d "        %self.populationSize
        print "Crossover factor: %.3f "     %self.crossoverFactor 
        print "Mutation factor: %.3f "      %self.mutationFactor
        print "Selection operator: " +      self.selection
        print "Elitism: %d "                %self.elitism
        print "Fitness function: " +        self.fitnessFunction
        if self.fitnessFunction == "linear":
            print "Eucld dist factor: %.3f"   %self.euclF
            print "Manh dist factor: %.3f"    %self.manhF
        elif self.fitnessFunction == "minkowski":
             print "p: %.3f"                  %self.p
       