import gifAnimation.*;

GifMaker gifExport;
int frames = 0;
int totalFrames = 120;

public void setup() {
  smooth();
  size(400, 400);

  gifExport = new GifMaker(this, "export.gif", 100);
  gifExport.setRepeat(0); // make it an "endless" animation

  noFill();
  stroke(0);
  strokeWeight(20);
}

void draw() {
  background(255);
  rectMode(CENTER);
  float size = 100.0 * sin(TWO_PI * frames / float(totalFrames))+100.0;
  float size2 = 100.0 * cos(TWO_PI * frames / float(totalFrames) + PI/6)+100.0;
  float size3 = 100.0 * sin(TWO_PI * frames / float(totalFrames) + PI/3)+100.0;
  stroke((size/2.0)%255.0);
  ellipse(width/ 2.0, height / 2.0, size, size);
  ellipse(width/ 3.0, height / 3.0, size2, size2);
  ellipse(width/ 2.0, height / 2.0, size3, size3);
  ellipse(width*2.0/ 3.0, height*2.0/ 3.0, size2, size2);
  ellipse(width/ 2.0, height / 2.0, size/.3, size/.3);
  export();
}

void export() {
  if(frames < totalFrames) {
    gifExport.setDelay(20);
    gifExport.addFrame();
    frames++;
  } else {
    gifExport.finish();
    frames++;
    println("gif saved");
    exit();
  }
}
