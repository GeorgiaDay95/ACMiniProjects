void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(LED_BUILTIN, OUTPUT);

}

void loop() {
  // put your main code here, to run repeatedly:
  if(Serial.available()){
    char x = Serial.read();
    if ( x == '1'){
      digitalWrite(LED_BUILTIN, HIGH);
    }

    if ( x == '0'){
      digitalWrite(LED_BUILTIN, LOW);
      
    }
  }


}
