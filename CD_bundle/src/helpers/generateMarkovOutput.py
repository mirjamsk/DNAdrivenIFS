import random
import itertools
import argparse


def generateMarkovSequence (inputFile ='HIVgenome.txt',  windowSize = 2, markovSeqenceLength = 2000, outputFile = 'markovOutput.txt'):
    #read the sequence from a given file and store it as a list
    f = open(inputFile, 'r')
    data = f.read()
    f.close()
    
    #generate all possible combinations of "C G A T" for the given windowSize and store them as a set
    words = set(itertools.product('CGAT', repeat= windowSize))
    
    #===========================================================================
    # generate the probability matrix in form of a dictionary of dictionaries
    # e.g. for windowSize=3
    # probabilityMatrix = {('C','C','G'): {'C': 0.4, 'G':0.1, 'A':0.5, 'T':0, 'totalCount' : 20 },
    #                      ('C','C','A'): {'C': 0.25, 'G':0.2, 'A':0.0, 'T':0.05, 'totalCount' : 11  },
    #                      ....
    #                      }
    #===========================================================================
    
    probabilityMatrix = dict.fromkeys(words)
    for key in probabilityMatrix.keys():
        probabilityMatrix[key] = dict.fromkeys(('C','G','A','T','totalCount'),0)
    
    
    #generate slidingWindow[windowSize]
    slidingWindow = [data[i] for i in range(windowSize)]
    #successor base after the slidingWindow
    succ = data[windowSize]
    

    for i in range(windowSize, len(data)-1):
        slidingWindow.pop(0)
        slidingWindow.append(data[i])
        succ = data[i+1]
        
        temp = probabilityMatrix[tuple(slidingWindow)]
        temp['totalCount'] +=1
        temp[succ] +=1
    
    #divide individual base counts with the total count of the sequence to get the probabilities
    #if any sequence was not found set the probabilities of each base to 0.25    
    for sequence in probabilityMatrix.keys():
        totalCount = float(probabilityMatrix[sequence]['totalCount'])
        for base in probabilityMatrix[sequence].keys():
            if totalCount == 0:
                probabilityMatrix[sequence][base] = 0.25
            else:
                probabilityMatrix[sequence][base] = round(probabilityMatrix[sequence][base]/totalCount, 3)
 
    
    #===========================================================================
    # outputProbabilityMatrix calculated from the probabilityMatrix
    # e.g. for windowSize=3
    # probabilityMatrix = {('C','C','G'): {'C': 0.4, 'G':0.1, 'A':0.5, 'T':0, 'totalCount' : 20 },
    #                      ('C','C','A'): {'C': 0.25, 'G':0.2, 'A':0.0, 'T':0.05, 'totalCount' : 11 },
    #                      ....
    #                      }
    # outputProbaMatrix = {('C','C','G'): {'C': 0.4, 'G':0.4+0.1, 'A':0.4+0.1+0.5 },
    #                      ('C','C','A'): {'C': 0.25, 'G':0.25+0.2, 'A':0.25+0.2+0.0 },
    #                      ....
    #                      }
    #===========================================================================
    
    outputProbM =  dict.fromkeys(words)
    for key in outputProbM.keys():
        outputProbM[key] = dict.fromkeys(('C','G','A'))
    
    for sequence in probabilityMatrix.keys():
        outputProbM[sequence]['C'] = probabilityMatrix[sequence]['C']
        outputProbM[sequence]['G'] = outputProbM[sequence]['C'] + probabilityMatrix[sequence]['G']
        outputProbM[sequence]['A'] = outputProbM[sequence]['G'] + probabilityMatrix[sequence]['A']
   
   
    #generate start slidingWindow from a random existing sequence 
    index = random.randrange(0,len(data)-windowSize)    
    slidingWindow = [data[i] for i in range(index, index+windowSize)]
    output = []
    
    #generate the synthetic data
    for i in range (0, markovSeqenceLength):
        p = random.random()
        currSequence = tuple(slidingWindow)
        if p < outputProbM[currSequence]['C']: succ = 'C'
        elif p < outputProbM[currSequence]['G']: succ = 'G'
        elif p < outputProbM[currSequence]['A']: succ = 'A'
        else: succ = 'T'
        output.append(succ)
        slidingWindow.pop(0)
        slidingWindow.append(succ)
       
    ## write the sequence to the outputFile
    f = open(outputFile,  'w')
    for c in output:
        f.write(c)
    f.close()
    
def main():
    parser = argparse.ArgumentParser(description='Script for generating synthetic data from given DNA sequence using MarkovModel')
    parser.add_argument('-i','--input', help='Input file name',required=True)
    parser.add_argument('-o','--output',help='Output file name', default='output.txt',  required=False)
    parser.add_argument('-w','--windowSize', help='Sliding window size', type=int, required=True)
    parser.add_argument('-l','--length',help='Length of generated sequence data ',type=int,  default=2000, required=False)
    
    args = parser.parse_args()
    generateMarkovSequence(inputFile = args.input, windowSize = args.windowSize, markovSeqenceLength=args.length,  outputFile = args.output)
  
    ## show values ##
    print ("Input file: %s" % args.input )
    print ("Output file: %s" % args.output )
 

    
if __name__ == '__main__':
    main()
    #generateMarkovSequence(inputFile ='orionExampleGenome.txt')
