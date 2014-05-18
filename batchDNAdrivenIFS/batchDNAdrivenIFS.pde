

void setup() {
  size(700, 700);
  background(0);
  smooth();
  strokeWeight(2);
  for (int i = 1; i <31; i++){
    background(0);
    Parser p = new Parser("randomSimili/similitude"+i+".txt");
    p.parse();
    IFSfractal ifs = new IFSfractal(p.getSimilitudes(), p.getIndexes(), "HIVmarkov.txt");
    print(i, "\n" );
    ifs.drawFractal();
    save("pics/RandomSimili/similitude"+i+".png"); 
  
  }
}

