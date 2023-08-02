#include <Servo.h>
Servo myservo;


byte test[4];
int p;
int l;
int j;
int result;
void setup() {
	Serial.begin(9600);
  myservo.attach(9);
}

void loop() {
  if (Serial.available()){
    Serial.readBytes(test,4);
    p = test[1] - 48;
    l = test[2] - 48;
    j = test[3] - 48;
    result = (p*100)+(l*10)+j;
    
    char dedo = test[0];
    switch (dedo){
      case 'P': // Pulgar
        myservo.write(result);
        Serial.println(result);
        break;
      case 'A': // Apuntador
        Serial.println("lalalala");
        break;
      case 'M': // Medio
        Serial.println("lalalala");
        break;
      case 'a': // Anillero
        Serial.println("lalalala");
        break;
      case 'm': // Meñique
        Serial.println("lalalala");
        break;
      default:
        break;
    }
  }

}
