

void setup() {
  size(700, 700);
  background(0);
  smooth(8);
  strokeWeight(4);
  for (int i = 1; i <101; i++){
    print(i, "\n" );
    background(0);
    
    Parser p = new Parser("convergence/fit900/similitude"+i+".txt");
    p.parse();
    
    IFSfractal ifs = new IFSfractal(p.getSimilitudes(), p.getIndexes(), "HIVmarkov.txt",color(10,200,255));
    IFSfractal ifs1 = new IFSfractal(p.getSimilitudes(), p.getIndexes(), "MethanocaldococcusJannaschiiMarkov.txt.txt", color( 255, 120, 10));
    
    
    //boundscheck
    setBounds(ifs, ifs1);
    
    
    ifs.drawFractal();
   
    //save("pics/convergence/fit900/similitude"+i+"_1.png"); 
    ifs1.drawFractal();
    
    filter(DILATE);
    filter(BLUR,0.7);
 
//    fill(0, 30);
//    rect(0,0, width, height);
    save("pics/convergence/fit900/similitude"+i+"_2.png"); 
  
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
class IFSfractal {

  ArrayList<Similitude> similitudes;
  HashMap<String, Integer> codonMap;
  int[] indexes;
  float[] xBounds;
  float[] yBounds;
  String sequence;
  color c;
  float xBoundRatio;
  float yBoundRatio;


  IFSfractal( ArrayList<Similitude> similitudes, int[] indexes, String sequenceFile) {
    this.indexes = indexes;
    this.similitudes = similitudes;
    this.sequence = loadStrings(sequenceFile)[0];
    this.xBounds = new float[2];
    this.yBounds = new float[2];
    this.xBoundRatio= 1;
    this.yBoundRatio= 1;

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

    
    
    if (xBounds[1] - xBounds[0] < yBounds[1] - yBounds[0]) {
      xBoundRatio = (xBounds[1] - xBounds[0])/( yBounds[1] - yBounds[0]);
      yBoundRatio = 1;
    }else {
      xBoundRatio = 1;
      yBoundRatio = ( yBounds[1] - yBounds[0])/(xBounds[1] - xBounds[0]);
  }
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
      mapX = int(map(px, xBounds[0], xBounds[1], 5, xBoundRatio*(width-100)-50 ));
      mapY = int(map(py, yBounds[0], yBounds[1], yBoundRatio*(height-100)-50, 50));
      
      if(c == color(0,0,0)){
         //stroke(blendColor(similitudes.get(index).colour, get(mapX, mapY),BURN), 127);
        stroke(blendColor(similitudes.get(index).colour, get(mapX, mapY), SCREEN), 127);
    }
      else stroke(blendColor(c, get(mapX, mapY), SCREEN), 127);
      point(mapX, mapY);
    }
  }
}

class Parser {
  int[] indexes;
  String file;
  ArrayList<Similitude> similitudes;
  color[] colors = {
    color(0, 0, 255), 
    color(0, 255, 0), 
    color(0, 255, 255), 
    color(255, 0, 0), 
    color(255, 0, 255), 
    color(255, 255, 0), 
    color(255, 255, 255), 
    color(127)
  };

  Parser(String file) {
    this.file = file;
    this.similitudes = new ArrayList<Similitude>();
    this.indexes = new int[64];
  }

  void parse() {
    boolean isSimilitude = true;
    String line = "notnull";
    String[] temp = new String[4];
    BufferedReader reader = createReader(file);   

    for (int i = 0; i<10; i++) {
      int counter = 0;
      try {
        line = reader.readLine();
      } 
      catch (IOException e ) {
        e.printStackTrace();
        line = null;
        break;
      }

      if (line != null) {

        if (line.equals("#")) {        
          isSimilitude = false;
          continue;
        } 
        else if (isSimilitude) {
          temp = split(line, " ");
          //println(temp);
          similitudes.add(new Similitude(float(temp[0]), float(temp[1]), float(temp[2]), float(temp[3]), colors[i] ));
        } 
        else {
          for (String s : split(line," ")) {         
            //WATCH OUT! INDEXES CODES FROM ZERO TO 7
            indexes[counter] = int(s);

            counter++;
            if (counter == 64)
              break;
          }
        }
      }
    }
    //print("parsed");
  }

  ArrayList<Similitude> getSimilitudes() {
    return similitudes;
  }

  int[] getIndexes() {
    return indexes;
  }
}

class Similitude {
  float rotate;
  float translateX;
  float translateY;
  float scale;
  color colour;

  Similitude(float rotate, float translateX, float translateY, float scale, color colour) {
    this.rotate = rotate;
    this.translateX = translateX;
    this.translateY = translateY;
    this.scale = scale;
    this.colour = colour;
  }
}


