import argparse
import random

def generateRandomSequence(seqenceLength, outputFile):
    output = "";
        
    #generate the synthetic data
    for i in range (0, seqenceLength):
        p = random.random()
        if p < 0.25: output+= 'C'
        elif p < 0.5: output+=  'G'
        elif p < 0.75: output+=  'A'
        else: output+=  'T'
        
       
    ## write the sequence to the outputFile
    f = open(outputFile,  'w')
    for c in output:
        f.write(c)
    f.close()
    
def main():
    parser = argparse.ArgumentParser(description='Script for generating random DNA data')
    parser.add_argument('-o','--output',help='Output file name', default='randomSequence.txt',  required=False)
    parser.add_argument('-l','--length',help='Length of generated sequence data ',type=int,  default=20000, required=False)
    
    args = parser.parse_args()
    generateRandomSequence( seqenceLength=args.length,  outputFile = args.output)
  
    ## show values ##
    print ("Output file: %s" % args.output )
 

    
if __name__ == '__main__':
    main()

