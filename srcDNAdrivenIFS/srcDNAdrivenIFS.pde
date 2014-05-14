

void setup() {
  size(700, 700);
  background(0);
  smooth();
  strokeWeight(2);
//  Parser p = new Parser("outputSimil2.txt"); 
  Parser p = new Parser("similitude23.txt");
  p.parse();
  IFSfractal ifs = new IFSfractal(p.getSimilitudes(), p.getIndexes(), "HIVmarkov.txt", color(0,255,0));
   IFSfractal ifs1 = new IFSfractal(p.getSimilitudes(), p.getIndexes(), "MethanocalMarkov.txt", color(255, 0, 255));

  print(ifs.bounds[0], " ", ifs.bounds[1], "\n" );
   print(ifs1.bounds[0], " ", ifs1.bounds[1], "\n" );
  if (ifs.bounds[0] < ifs1.bounds[0]) ifs1.bounds[0] = ifs.bounds[0];
  else ifs.bounds[0] = ifs1.bounds[0];
  if (ifs.bounds[1] > ifs1.bounds[1]) ifs1.bounds[1] = ifs.bounds[1];
  else ifs.bounds[1] = ifs1.bounds[1];
  
   print(ifs.bounds[0], " ", ifs.bounds[1], "\n" );
   print(ifs1.bounds[0], " ", ifs1.bounds[1], "\n" );
  
  ifs.drawFractal();
  ifs.drawFractal();
  save("pics/simili231single"); 
  ifs1.drawFractal();
  save("pics/simili231both"); 
  
}


// Parser p = new Parser("similitudes.txt");
// Parser p = new Parser("outputSimil.txt");
//  Parser p = new Parser("outputSimil2.txt");




//drawFractal(p.getSimilitudes(), p.getIndexes(),"MethanocalMarkov.txt", color(0,255,0));
//drawFractal(p.getSimilitudes(), p.getIndexes(),"HIVmarkov.txt", color(255,0,255));
//drawFractal(p.getSimilitudes(), p.getIndexes(),"g1564a209markov.txt", color(0,2550,0));
//drawFractal(p.getSimilitudes(), p.getIndexes(),"randomSequence.txt", color(255,0,255));


