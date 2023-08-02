#include <Servo.h>
Servo thumb;
Servo index;
Servo middle;
Servo ring;
Servo pinky;


byte test[5];
int c;
int d;
int u;
int result;
void setup() {
	Serial.begin(9600);
  thumb.attach(4);
  index.attach(5);
  middle.attach(6);
  ring.attach(7);
  pinky.attach(8);
}

void loop() {
  if (Serial.available()){
    Serial.readBytes(test,5);
    c = test[1] - 48;
    d = test[2] - 48;
    u = test[3] - 48;
    result = (c*100)+(d*10)+u;
    //Serial.println(result);
    
    char dedo = test[0];
    switch (dedo){
      case 'T': // Thumb
        thumb.write(result);
        break;
      case 'I': // Index
        index.write(result);
        break;
      case 'M': // Middle
        middle.write(result);
        break;
      case 'R': // ring
        ring.write(result);
        break;
      case 'P': // Pinky
        pinky.write(result);
        break;
      default:
        Serial.println("Not found");
        break;
    }
  }

}
