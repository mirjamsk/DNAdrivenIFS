

void setup() {
  size(700, 700);
  background(0);
  smooth(8);
  strokeWeight(2);
  for (int i = 1; i <5; i++){
    print(i, "\n" );
    background(0);
    
    Parser p = new Parser("euclideanSimili/similitude"+i+".txt");
    p.parse();
    
    IFSfractal ifs = new IFSfractal(p.getSimilitudes(), p.getIndexes(), "HIVmarkov.txt", color(212,53,105));
    IFSfractal ifs1 = new IFSfractal(p.getSimilitudes(), p.getIndexes(), "MethanocaldococcusJannaschiiMarkov.txt", color(255,86,0));
    
    
    //boundscheck
    setBounds(ifs, ifs1);
    
    
    ifs.drawFractal();
   
    save("pics/euclideanSimili/similitude"+i+"_1.png"); 
    ifs1.drawFractal();
    
    filter(DILATE);
    filter(BLUR,0.7);
 
//    fill(0, 30);
//    rect(0,0, width, height);
    save("pics/euclideanSimili/similitude"+i+"_2.png"); 
  
  }
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
