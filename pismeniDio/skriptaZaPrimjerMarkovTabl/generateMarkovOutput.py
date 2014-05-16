# -*- coding: cp1250 -*-
import random
import itertools
import argparse
def format_df(df):
    if isinstance(df, (int, long)):
        return "%d" % df
    elif isinstance(df, float):
        return "%.3f" % df
    else:
        return str(df) # fallback just in case

inputFile ='zr.txt'
windowSize = 2
markovSeqenceLength = 2000
outputFile = 'markovOutput.txt'

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

print "================="
print "markov model k = %d" %windowSize
print "Seq\tNc\tNg\tNa\tnt\t"
my_alphabet ="CGAT"
kljucevi = probabilityMatrix.keys()
kljucevi.sort(key= lambda elem: [my_alphabet.index(elem[0]), my_alphabet.index(elem[1])])
for k in kljucevi:
	print "%c%c\t%d\t%d\t%d\t%d" %(k[0],k[1],probabilityMatrix[k]['C'],
                                               probabilityMatrix[k]['G'],
                                               probabilityMatrix[k]['A'],
                                               probabilityMatrix[k]['T']) 

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
#   output za završni
#==========================================================================

print "================="
print "markov model k = %d" %windowSize
print "Seq\tPc\tPg\tPa\tPt"

my_alphabet ="CGAT"
kljucevi = probabilityMatrix.keys()
kljucevi.sort(key= lambda elem: [my_alphabet.index(elem[0]), my_alphabet.index(elem[1])])
for k in kljucevi:
	print "%c%c\t%s\t%s\t%s\t%s" %(k[0],k[1],probabilityMatrix[k]['C'],
                                               probabilityMatrix[k]['G'],
                                               probabilityMatrix[k]['A'],
                                               probabilityMatrix[k]['T']) 
	 
