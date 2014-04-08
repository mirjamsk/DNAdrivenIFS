class IFSfractal {

  ArrayList<Similitude> similitudes;
  HashMap<String, Integer> codonMap;
  int[] indexes;
  float[] bounds;
  String sequence;
  color c;


  IFSfractal( ArrayList<Similitude> similitudes, int[] indexes, String sequenceFile) {
    this.indexes = indexes;
    this.similitudes = similitudes;
    this.sequence = loadStrings(sequenceFile)[0];
    this.bounds = new float[2];
    this.codonMap = new HashMap<String, Integer>();
    this.initializeCodonMap();
    this.findBounds();
    this.c = color(0,0,0);
    
  }
  
    IFSfractal( ArrayList<Similitude> similitudes, int[] indexes, String sequenceFile, color c) {
    this.indexes = indexes;
    this.similitudes = similitudes;
    this.sequence = loadStrings(sequenceFile)[0];
    this.bounds = new float[2];
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


    for (int i = 2; i < sequence.length(); i++) {

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
      if (px < minBounds[0]) minBounds[0] = px;
      if (px > maxBounds[0]) maxBounds[0] = px;
      if (py < minBounds[1]) minBounds[1] = py;
      if (py > maxBounds[1]) maxBounds[1] = py;
    }

    if (maxBounds[0] - minBounds[0] > maxBounds[1] - minBounds[1]) {
      this.bounds[0] = minBounds[0];
      this.bounds[1] = maxBounds[0];
    } 
    else {
      this.bounds[0] = minBounds[1];
      this.bounds[1] = maxBounds[1];
    }
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

    for (int i = 2; i < sequence.length(); i++) {

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
      mapX = int(map(px, bounds[0], bounds[1], 10, width-10));
      mapY = int(map(py, bounds[0], bounds[1], height-150, 10));
      
      if(c == color(0,0,0)) stroke(blendColor(similitudes.get(index).colour, get(mapX, mapY), SCREEN), 127);
      else stroke(blendColor(c, get(mapX, mapY), SCREEN), 127);
      point(mapX, mapY);
    }
  }
}

