float bx;
float by;
int boxSize = 75;
int score = 0;
boolean overBox = false;
boolean locked = false;
float xOffset = 0.0; 
float yOffset = 0.0; 

void setup() {
  size(640, 360);
  bx = width/2.0;
  by = height/2.0;
  rectMode(RADIUS);  
}

void draw() { 
  if(millis() < 10000){
    background(0);
    text("Score:" + score, 320, 20); 
    text("Time left" + (10-millis()/1000), 500,20);
    // Test if the cursor is over the box 
    if (mouseX > bx-boxSize && mouseX < bx+boxSize && 
        mouseY > by-boxSize && mouseY < by+boxSize) {
      overBox = true;  
      if(!locked) { 
        stroke(255); 
        fill(153);
      } 
    } else {
      stroke(153);
      fill(153);
      overBox = false;
    }
    
    // Draw the box
    rect(bx, by, boxSize, boxSize);
  }
}

void mousePressed() {
  if(overBox) { 
    locked = true; 
    fill(255, 255, 255);
    bx = random(boxSize, 640-boxSize);
    by = random(boxSize, 360-boxSize);
    score = score +1;
    
  } else {
    locked = false;
  }
  xOffset = mouseX-bx; 
  yOffset = mouseY-by; 

}

void mouseDragged() {
  if(locked) {
    bx = mouseX-xOffset; 
    by = mouseY-yOffset; 
  }
}

void mouseReleased() {
  locked = false;
}
