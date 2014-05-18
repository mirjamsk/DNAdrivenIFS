class IFSfractal {

  ArrayList<Similitude> similitudes;
  HashMap<String, Integer> codonMap;
  int[] indexes;
  float[] xBounds;
  float[] yBounds;
  String sequence;
  color c;


  IFSfractal( ArrayList<Similitude> similitudes, int[] indexes, String sequenceFile) {
    this.indexes = indexes;
    this.similitudes = similitudes;
    this.sequence = loadStrings(sequenceFile)[0];
    this.xBounds = new float[2];
    this.yBounds = new float[2];
    this.codonMap = new HashMap<String, Integer>();
    this.initializeCodonMap();
    this.findBounds();
    this.c = color(0,0,0);
    
  }
  
    IFSfractal( ArrayList<Similitude> similitudes, int[] indexes, String sequenceFile, color c) {
    this.indexes = indexes;
    this.similitudes = similitudes;
    this.sequence = loadStrings(sequenceFile)[0];
    this.xBounds = new float[2];
    this.yBounds = new float[2];
    this.codonMap = new HashMap<String, Integer>();
    this.initializeCodonMap();
    this.findBounds();
    this.c = c;
  }



  void initializeCodonMap() {
    String[] bases = {
      "C", "G", "A", "T"
    };
    int counter = 0;
    for (String k:bases) {
      for (String j:bases) {
        for (String i:bases) {
          codonMap.put(k+j+i, indexes[counter]);
          counter++;
        }
      }
    }
  }

  void findBounds() {
    float[] minBounds = {
      MAX_FLOAT, MAX_FLOAT
    };
    float[] maxBounds = {
      MIN_FLOAT, MIN_FLOAT
    };
    String slidingWindow = "";

    float px = 0;
    float py = 0;  
    float rad = 0;
    float translateX =0;
    float translateY =0;
    float scale =0;
    float x = 0;
    float y= 0;
    int index;


    for (int i = 2; i < sequence.length(); i+=3) {

      slidingWindow = ""+sequence.charAt(i-2)+sequence.charAt(i-1)+sequence.charAt(i);
      index = codonMap.get(slidingWindow);
      rad = similitudes.get(index).rotate; 
      translateX = similitudes.get(index).translateX;
      translateY = similitudes.get(index).translateY;
      scale = similitudes.get(index).scale;
      x = px;
      y = py;

      px = scale *(x*cos(rad)- y*sin(rad) + translateX);  
      py = scale *(x*sin(rad)+ y*cos(rad) + translateY);
      //println(px, " ", py);
      if (px < xBounds[0]) xBounds[0] = px;
      if (px > xBounds[1]) xBounds[1] = px;
      if (py < yBounds[0]) yBounds[0] = py;
      if (py > yBounds[1]) yBounds[1] = py;
    }

//    if (maxBounds[0] - minBounds[0] > maxBounds[1] - minBounds[1]) {
//      this.bounds[0] = minBounds[0];
//      this.bounds[1] = maxBounds[0];
//    } 
//    else {
//      this.bounds[0] = minBounds[1];
//      this.bounds[1] = maxBounds[1];
//    }
    //println( this.bounds[0]);
    //println( this.bounds[1]);
  }

  void drawFractal() {

    String slidingWindow = "";
    float px = 0;
    float py = 0;  
    float rad = 0;
    float translateX =0;
    float translateY =0;
    float scale =0;
    float x = 0;
    float y = 0;
    int mapX;
    int mapY;
    int index;
    float xBoundRatio;
    float yBoundRatio;
    
    if (xBounds[1] - xBounds[0] < yBounds[1] - yBounds[0]) {
      xBoundRatio = (xBounds[1] - xBounds[0])/( yBounds[1] - yBounds[0]);
      yBoundRatio = 1;
    }else {
      xBoundRatio = 1;
      yBoundRatio = ( yBounds[1] - yBounds[0])/(xBounds[1] - xBounds[0]);
  }
    for (int i = 2; i < sequence.length(); i+=3) {

      slidingWindow = ""+sequence.charAt(i-2)+sequence.charAt(i-1)+sequence.charAt(i);
      index = codonMap.get(slidingWindow);
      rad = similitudes.get(index).rotate; 
      translateX = similitudes.get(index).translateX;
      translateY = similitudes.get(index).translateY;
      scale = similitudes.get(index).scale;
      x = px;
      y = py;
      px = scale *(x*cos(rad)- y*sin(rad) + translateX);
      py = scale *(x*sin(rad)+ y*cos(rad) + translateY);

      //    println(px, " ", py);
      mapX = int(map(px, xBounds[0], xBounds[1], 0, xBoundRatio*width ));
      mapY = int(map(py, yBounds[0], yBounds[1], yBoundRatio*height, 0));
      
      if(c == color(0,0,0)){
        //r BLEND, ADD, SUBTRACT, DARKEST, LIGHTEST, DIFFERENCE, EXCLUSION, MULTIPLY, SCREEN, OVERLAY, HARD_LIGHT, SOFT_LIGHT, DODGE, or BURN
         //stroke(blendColor(similitudes.get(index).colour, get(mapX, mapY),BURN), 127);
        stroke(blendColor(similitudes.get(index).colour, get(mapX, mapY), SCREEN), 127);
    }
      else stroke(blendColor(c, get(mapX, mapY), SCREEN), 127);
      point(mapX, mapY);
    }
  }
}

