import argparse
#====================================================#
# script to clean up a DNA sequence text file        #
# i.e. remove all whitespace and unwanted characters #
#====================================================#


parser = argparse.ArgumentParser(description='Script to clean up DNA sequence text file')
parser.add_argument('-i','--input', help='Input file name',required=True)
parser.add_argument('-o','--output',help='Output file name', default = "cleanDNA.txt",  required=False)

args = parser.parse_args()

f = open(args.input, "r")
allowedChars = set(['C', 'G', 'A', 'T'])
data = ""
for c in f.read():
    if c in allowedChars:
        data += c
f.close()

f = open(args.output, "w")
for c in data:
    f.write(c)
f.close()

## show values ##
print ("Input file: %s" % args.input )
print ("Output file: %s" % args.output )
