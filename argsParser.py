'''
Created on 31. 3. 2014.

@author: Monsieur
'''
import xml.etree.ElementTree as ET

class argsParser(object):
    '''
    classdocs
    '''


    def __init__(self):
        self.input1= None
        self.input2 = None
        self.outputFile ='outputSimili.txt'
        self.numberOfGenerations = 10
        self.populationSize = 100
        self.crossoverFactor = 0.2
        self.mutationFactor = 0.2
        self.fitnessFunction = "euclidean"
        self.selection = "tournament"
        self.elitism = 0
    def parse(self, file):

        try:
            tree = ET.parse(file)
            root = tree.getroot()
            self.input1 = root.find('InputFiles')[0].text.strip()
            self.input2 = root.find('InputFiles')[1].text.strip()
            if root.find('OutputFile') is not None: self.outputFile = root.find('OutputFile').text.strip()
            if root.find('GenerationNumber') is not None: self.numberOfGenerations = int(root.find('GenerationNumber').text.strip())
            if root.find('PopulationSize') is not None: self.populationSize = int(root.find('PopulationSize').text.strip())
            if root.find('CrossoverFactor') is not None: self.crossoverFactor = float(root.find('CrossoverFactor').text.strip())
            if root.find('MutationFactor') is not None: self.mutationFactor = float(root.find('MutationFactor').text.strip())
            if root.find('FitnessFunction') is not None: self.fitnessFunction = root.find('FitnessFunction').text.strip()
            if root.find('Selection') is not None: self.selection = root.find('Selection').text.strip()
            if root.find('Elitism') is not None: self.elitism = int(root.find('Elitism').text.strip())
            self.printaj()

        except IOError:
            print "Error in argsParser.parse: File does not appear to exist."
          
    def printaj(self):
        print "Using: "
        print "Input file1: " + self.input1 
        print "Input file2: " + self.input2
        print "Output file: " +self.outputFile 
        print "Number of Generations: %d " %self.numberOfGenerations 
        print "Population size: %d " %self.populationSize
        print "Crossover factor: %f " %self.crossoverFactor 
        print "Mutation factor: %f " %self.mutationFactor
        print "Fitness function: " + self.fitnessFunction
        print "Selection operator: " + self.selection
        print "Elitism: %d " %self.elitism
