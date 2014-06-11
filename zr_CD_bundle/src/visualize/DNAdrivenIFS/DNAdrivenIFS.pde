

void setup() {
  size(700, 700);
  background(0);
  smooth(8);
  strokeWeight(4);
    
  Parser p = new Parser("IFSsimilitude.txt");
  p.parse();
  
  IFSfractal ifs = new IFSfractal(p.getSimilitudes(), p.getIndexes(), "DNAsequence1.txt",color(10,200,255));
  IFSfractal ifs1 = new IFSfractal(p.getSimilitudes(), p.getIndexes(), "DNAsequence2.txt", color( 255, 120, 10));
  
  //boundscheck
  setBounds(ifs, ifs1);
  
  ifs.drawFractal();
 
  save("pics/singleDNA.png"); 
  ifs1.drawFractal();
  
  filter(DILATE);
  filter(BLUR,0.7);
 
  save("pics/bothDNA.png"); 

}

void  setBounds(IFSfractal ifs, IFSfractal ifs1){
  
    if (ifs.xBounds[0]> ifs1.xBounds[0]) ifs.xBounds[0]= ifs1.xBounds[0];
    else  ifs1.xBounds[0]= ifs.xBounds[0];
    if (ifs.xBounds[1]< ifs1.xBounds[1]) ifs.xBounds[1]= ifs1.xBounds[1];
    else  ifs1.xBounds[1]= ifs.xBounds[1];
    
    if (ifs.yBounds[0]> ifs1.yBounds[0]) ifs.yBounds[0]= ifs1.yBounds[0];
    else  ifs1.yBounds[0]= ifs.yBounds[0];
    if (ifs.yBounds[1]< ifs1.yBounds[1]) ifs.yBounds[1]= ifs1.yBounds[1];
    else  ifs1.yBounds[1]= ifs.yBounds[1];


}
