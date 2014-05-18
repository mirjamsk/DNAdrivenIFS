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

