windows app za vizualizaciju DNA podataka
---



##### Što je bitno u repozitoriju?
+ appDNAdrivenIFS.bat
+ Data <sup>*ulaz</sup>
 + DNAsequence1.txt
 + DNAsequence2.txt	
 + IFSsimilitude.txt
+ pics   <sup>*izlaz</sup>
 + singleDNA.tif
 + bothDNA.tif

<br>

##### Čemu i kako?


Duplim klikom na ***appDNAdrivenIFS.bat*** pokrece se program i iscrtava se fraktal. Program čita 3 ulazne datoteke *DNAsequence1.txt*,  *DNAsequence2.txt* te *IFSsimilitude.txt*.

*IFSsimilitude.txt* sadrži tablicu od 8 transformacija IFS fraktala te listu svih mogućih trojki DNA sekvence *(4^3 = 64)* i pripadajućeg rednog broja transformacije.
Program, osim što prikaže fraktal, sprema i 2 slike istog u ***pics*** direktorij. 
+ prva  *singleDNA.tif* sprema sliku fraktala generiranog ulaznom datotekom  *DNAsequence1.txt*
+ druga *bothDNA.tif* sprema sliku oba ulaza


==

implementacija: [srcDNAdrivenIFS](https://github.com/mirjamsk/DNAdrivenIFS/blob/master/srcDNAdrivenIFS)
