

void setup() {
  size(700, 700);
  background(0);
  smooth(8);
  strokeWeight(4);
  for (int i = 1; i <31; i++){
    print(i, "\n" );
    background(0);
    
    Parser p = new Parser("HPV-Helico-euclideanSimili/similitude"+i+".txt");
    p.parse();
    
    IFSfractal ifs = new IFSfractal(p.getSimilitudes(), p.getIndexes(), "HumanPapillomavirusType41-markov.txt",color(10,200,255));
    IFSfractal ifs1 = new IFSfractal(p.getSimilitudes(), p.getIndexes(), "HelicobacterPylori2017-markov.txt", color( 255, 120, 10));
    
    
    //boundscheck
    setBounds(ifs, ifs1);
    
    
    ifs.drawFractal();
   
    save("pics/HPV-Helico-euclidean/similitude"+i+"_1.png"); 
    ifs1.drawFractal();
    
    filter(DILATE);
    filter(BLUR,0.7);
 
//    fill(0, 30);
//    rect(0,0, width, height);
    save("pics/HPV-Helico-euclidean/similitude"+i+"_2.png"); 
  
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
