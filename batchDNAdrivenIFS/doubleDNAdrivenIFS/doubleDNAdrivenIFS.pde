

void setup() {
  size(700, 700);
  background(0);
  smooth(8);
  strokeWeight(2);
  for (int i = 12; i <31; i++){
    print(i, "\n" );
    background(0);
    
    Parser p = new Parser("randomSimili/similitude"+i+".txt");
    p.parse();
    
    IFSfractal ifs = new IFSfractal(p.getSimilitudes(), p.getIndexes(), "HIVmarkov.txt", color(10,200,255));
    IFSfractal ifs1 = new IFSfractal(p.getSimilitudes(), p.getIndexes(), "MethanocaldococcusJannaschiiMarkov.txt", color(255,100,100));
    
    
    //boundscheck
    setBounds(ifs, ifs1);
    
    
    ifs.drawFractal();
   
    save("pics/RandomSimili/similitude"+i+"_1.png"); 
    ifs1.drawFractal();
    
    filter(DILATE);
    filter(BLUR,0.7);
 
//    fill(0, 30);
//    rect(0,0, width, height);
    save("pics/RandomSimili/similitude"+i+"_2.png"); 
  
  }
}

void  setBounds(IFSfractal ifs, IFSfractal ifs1){
    float[] maxBounds= new float[2];
    maxBounds[0]=0;
    maxBounds[1]=0;
    
    
    if (ifs.xBounds[1] - ifs.xBounds[0] > maxBounds[1] - maxBounds[0]) {
      maxBounds[0] = ifs.xBounds[0];
      maxBounds[1] = ifs.xBounds[1];
    }
    if (ifs.yBounds[1] - ifs.yBounds[0] > maxBounds[1] - maxBounds[0]) {
      maxBounds[0] = ifs.yBounds[0];
      maxBounds[1] = ifs.yBounds[1];
    }
    if (ifs1.xBounds[1] - ifs1.xBounds[0] > maxBounds[1] - maxBounds[0]) {
      maxBounds[0] = ifs1.xBounds[0];
      maxBounds[1] = ifs1.xBounds[1];
    }
    if (ifs1.yBounds[1] - ifs1.yBounds[0] > maxBounds[1] - maxBounds[0]) {
      maxBounds[0] = ifs1.yBounds[0];
      maxBounds[1] = ifs1.yBounds[1];
    }
    
    //
    
    if (ifs.xBounds[1] - ifs.xBounds[0] < maxBounds[1] - maxBounds[0]) {
      ifs.xBoundRatio = (ifs.xBounds[1] - ifs.xBounds[0])/( maxBounds[1] - maxBounds[0]);
    }
    if (ifs.yBounds[1] - ifs.yBounds[0] < maxBounds[1] - maxBounds[0]) {
      ifs.yBoundRatio = (ifs.yBounds[1] - ifs.yBounds[0])/( maxBounds[1] - maxBounds[0]);
    }
     if (ifs1.xBounds[1] - ifs1.xBounds[0] < maxBounds[1] - maxBounds[0]) {
      ifs1.xBoundRatio = (ifs1.xBounds[1] - ifs1.xBounds[0])/( maxBounds[1] - maxBounds[0]);
    }
    if (ifs1.yBounds[1] - ifs1.yBounds[0] < maxBounds[1] - maxBounds[0]) {
      ifs1.yBoundRatio = (ifs1.yBounds[1] - ifs1.yBounds[0])/( maxBounds[1] - maxBounds[0]);
    
    }
}
