Pomocne python skripte
---


#### Što je u repozitoriju?
+ cleanDNAseq.py
+ generateMarkovOutput.py
+ generateRandomDNA.py
+ sampleData
 + HIVgenome.txt
 + MethanocaldococcusJannaschii.txt 

<br>

#### Čemu i kako?


######cleanDNAseq.py

Skinuta/sačuvana datoteka s DNA podacima može sadržavati neželjene znakove ( npr. novi red, bjeline). Kako bi uklonili sve neželjene znakove osim nukleotida [A C G T] koristi se *cleanDNAseq.py* 
primjer korištenja ako želimo počistiti HIVgenome.txt:
```bash
python cleanDNAseq.py -i sampleData/HIVgenome.txt          #assumes default output: ./cleanDNA.txt
python cleanDNAseq.py -i sampleData/HIVgenome.txt -o [file]
```
<br>

######generateMarkovOutput.py

Za generiranje Markovljevog modela DNA niza koristi se  *generateMarkovOutput.py*
primjer korištenja ako želimo generirati Markovljem model HIVgenome.txt:
```bash
python generateMarkovOutput.py -i sampleData/HIVgenome.txt -w 3  
#assumes defaults output: ./output.txt, generated sequence lenght: 2000


python generateMarkovOutput.py --help
usage: generateMarkovOutput.py [-h] -i INPUT [-o OUTPUT] -w WINDOWSIZE  [-l LENGTH]
Script for generating synthetic data from given DNA sequence using MarkovModel

arguments:
  -h, --help            show this help message and exit
  -i INPUT, --input INPUT
                        Input file name
  -o OUTPUT, --output OUTPUT
                        Output file name
  -w WINDOWSIZE, --windowSize WINDOWSIZE
                        Sliding window size
  -l LENGTH, --length LENGTH
                        Length of generated sequence data
```
<br>

######generateRandomDNA.py

Za nasumično generiranu DNA sekvencu koristiti *generateRandomDNA.py*
primjer korištenja:
```bash
python generateRandomDNA.py                  #assumes default output: ./randomSequence.txt, sequence length: 2000
python generateRandomDNA.py  -o [file] -l n  #where n is an int
```

===

##### Neke od baza podataka DNA sekvenci:
+ http://www.ebi.ac.uk/
+ http://www.ncbi.nlm.nih.gov/


[1]:(http://www.ncbi.nlm.nih.gov/nuccore/9629357?report=fasta)
