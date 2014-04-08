

void setup() {
  size(500, 500);
  background(0);
  smooth();
  strokeWeight(2);
//  Parser p = new Parser("outputSimil2.txt"); 
  Parser p = new Parser("IFSsimilitude.txt");
  p.parse();
  IFSfractal ifs = new IFSfractal(p.getSimilitudes(), p.getIndexes(), "DNAsequence1.txt", color(0,255,0));
  ifs.drawFractal();
  save("pics/singleDNA"); 
  
  IFSfractal ifs1 = new IFSfractal(p.getSimilitudes(), p.getIndexes(), "DNAsequence2.txt", color(255, 0, 255));
  ifs1.drawFractal();
  save("pics/bothDNA"); 
  
}


// Parser p = new Parser("similitudes.txt");
// Parser p = new Parser("outputSimil.txt");
//  Parser p = new Parser("outputSimil2.txt");




//drawFractal(p.getSimilitudes(), p.getIndexes(),"MethanocalMarkov.txt", color(0,255,0));
//drawFractal(p.getSimilitudes(), p.getIndexes(),"HIVmarkov.txt", color(255,0,255));
//drawFractal(p.getSimilitudes(), p.getIndexes(),"g1564a209markov.txt", color(0,2550,0));
//drawFractal(p.getSimilitudes(), p.getIndexes(),"randomSequence.txt", color(255,0,255));


