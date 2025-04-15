void setup()
{
  Serial.begin(9600);
  pinMode(12, INPUT);
  pinMode(13, OUTPUT);
  pinMode(9, OUTPUT);
}
 
const int ACTIVE = 1;
const int INACTIVE = 2;
int state = INACTIVE;

int pushhandled = 0;

int potval;
int photoval;
byte brightness = 0;

byte debug = 0;

void loop()
{
  
  int btn = digitalRead(12);
  
  if (btn == LOW)
    pushhandled = 0;
  
  switch (state) {
    
    case INACTIVE:
  
      if ((btn == HIGH) && (!pushhandled)) {
    
        pushhandled = 1;
        state = ACTIVE;
        digitalWrite(13, HIGH);
      }
         
     break;  
   
    case ACTIVE:
    	 
      potval = analogRead(A0);
      photoval = analogRead(A1);

      if (photoval < potval) {

         brightness = min(potval - photoval, 255);
     
      } else {
        
        brightness = 0;
      }

      analogWrite(9, brightness);
    
      if ((btn == HIGH) && (!pushhandled)) {
    
        pushhandled = 1;
        state = INACTIVE;
        digitalWrite(13, LOW);
        analogWrite(9, 0);
      }
    break;
  }
  
  // debugging control via serial
  if (Serial.available() > 0) {

     byte input = Serial.read();
     debug = (input == 49);
     
  }

  // debugging output via serial
  if (debug) {
    Serial.print(photoval);
    Serial.print("<");
    Serial.print(potval);
    Serial.print(":");
    Serial.print(brightness);
    Serial.println();
  }

}
