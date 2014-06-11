Implementacija genetskog algoritma za evoluciju IFS fraktala
--

<br>

Implementacija genetskog algoritma za "evoluciju" tablica transformacija IFS fraktala.
**Pokretanje** je jednostavno:



```bash
python run.py
```

##### Konfiguracija:
Za konfiguriranje pokretanja, dovoljno je promijeniti parametre u datoteci ***args.xml***
```xml
<args>
	<InputFiles> 
		<item>input/HIVmarkov.txt</item>
		<item>input/MethanocalMarkov.txt</item>
	</InputFiles>

	<OutputFile>output/similiOtuput.txt </OutputFile>

	<GenerationNumber> 10</GenerationNumber>
	<PopulationSize> 100 </PopulationSize>
	<CrossoverFactor> 0.3 </CrossoverFactor>
	<MutationFactor> 0.5 </MutationFactor>
	<FitnessFunction>  manhattan </FitnessFunction> <!-- possible: manhattan, euclidean, linear -->
	<euclFactor> 0.6 </euclFactor>					<!-- in case linear interpolation chosen -->
    <manhFactor> 0.4 </manhFactor>					<!-- in case linear interpolation chosen -->
	<Selection>  elimination </Selection>           <!-- possible: elimination, tournament -->
	<Elitism> 1 </Elitism>                          <!-- possible: 0,1 -->
	<Batch>30</Batch>								<!-- batch run possibility -->
</args>
```

<br>


##### Imam izlaz, što s njim?
U datoteku definiranu unutar čvora `<OutputFile>` bit će ispisana najbolja jedinka. Taj ***izlaz*** je ujedno i ***ulaz*** u program koji crta fraktale
Više o implemenaciji jedinke u slijedećem paragfau.

<br>

##### Par kratkih informacija:
+ Svaki se lanac DNA sastoji od građevnih jedinica zvanih nukleotidi kojih ima 4 vrste: adenin (A), citozin (C), gvanin (G) i timin (T). Ako lanac podijelimo u trojke (kodone), postoji 4^3=***64 mogućih kodona***. 

+ IFS fraktal nastaje kao rezultat iterativne primjene deﬁniranih ***transformacĳa*** na neku početnu točku

<br>

##### Implementacija jedinke
Jedinka se sastoji od 2 strukture podataka:
+ lista transformacija
+ lista duljine 64 koja preslikava `kodon-> transformacija`.
Odnosno kada alg za crtanje IFS fraktala naiđe na određeni kodon, tada na trenutnu točku primjenjuje transformaciju pod pripadajućim rednim brojem. 

Tablicno predstavljena jedinka:

<sub>Npr. u konkretnom slučaju kodona *'CCG'* primijenit će se 2. transformacija jer je preslikavajuca_lista['CCG']=2</sub>


| rb. | rotacija (rad) | x translatacija |y translatacija | skaliranje |
| --- | -------------- | :-------------: | :------------: | ---------: |
| 0 | 6.0176 | 0.8754 | 0.5239 | 0.9086 | 
| 1 | 1.0304 | 0.2503 | -0.657 | 0.9729 | 
| 2 | 5.9167 | -0.525 | 0.1340 | 0.6029 | 
| 3 | 0.1123 | 0.3145 | 0.5260 | 0.6262 | 
| 4 | 0.3586 | 0.5329 | 0.3257 | 0.5669 | 
| 5 | 5.7666 | 0.4117 | -0.817 | 0.9305 | 
| 6 | 0.4247 | 0.9795 | 0.9789 | 0.9910 | 
| 7 | 3.0488 | -0.055 | -0.881 | 0.9690 | 


|CCC|CCG|CCA|CCT|CGC|CGG|CGA|CGT|CAC|CAG|CAA|CAT|CTC|CTG|CTA|CTT|GCC|GCG|GCA|GCT|GGC|GGG|GGA|GGT|GAC|GAG|GAA|GAT|GTC|GTG|GTA|GTT|ACC|ACG|ACA|ACT|AGC|AGG|AGA|AGT|AAC|AAG|AAA|AAT|ATC|ATG|ATA|ATT|TCC|TCG|TCA|TCT|TGC|TGG|TGA|TGT|TAC|TAG|TAA|TAT|TTC|TTG|TTA|TTT|
|--- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | 
| 0 | 2 | 2 | 7 | 4 | 4 | 1 | 3 | 4 | 5 | 5 | 0 | 7 | 2 | 0 | 7 | 5 | 5 | 7 | 3 | 3 | 7 | 0 | 4 | 1 | 4 | 2 | 6 | 1 | 6 | 2 | 0 | 1 | 1 | 4 | 6 | 2 | 5 | 2 | 2 | 5 | 3 | 6 | 0 | 6 | 3 | 3 | 3 | 7 | 0 | 4 | 0 | 1 | 5 | 2 | 2 | 1 | 5 | 3 | 3 | 7 | 0 | 4 | 5 | 


