

void setup() {
  size(700, 700);
  background(0);
  smooth(8);
  strokeWeight(2);
  for (int i = 1; i <31; i++){
    print(i, "\n" );
    background(0);
    
    Parser p = new Parser("randomSimili/similitude"+i+".txt");
    p.parse();
    
    IFSfractal ifs = new IFSfractal(p.getSimilitudes(), p.getIndexes(), "HIVmarkov.txt");
    ifs.drawFractal();
    
   
    filter(BLUR,0.7);
    
    
    save("pics/RandomSimili/similitude"+i+".png"); 
  
  }
}

