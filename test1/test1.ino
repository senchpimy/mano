int led=1;
int led2 =2;
int option;
void setup() {
	Serial.begin(9600);
}

void loop() {
if (Serial.avaible()>0){
	option=Serial.read();
	if (option=='a'){
	}
}

}
