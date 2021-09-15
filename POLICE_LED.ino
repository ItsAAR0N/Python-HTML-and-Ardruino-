#include <IRremote.h>
#include <pitches.h>
 
#define first_key  0xFF6897
#define second_key  0xFF30CF 
int receiver_pin = 11;   
int first_led_pin = 13;
int second_led_pin = 12;
int buzzer = 10;
int led[] = {0,0,0,0}; 
int delayPeriod = 50;
IRrecv receiver(receiver_pin); 
decode_results output;

int x = 2;

void setup() 
{
  // put your setup code here, to run once:
Serial.begin(9600);
receiver.enableIRIn();  
pinMode(first_led_pin, OUTPUT);
pinMode(second_led_pin, OUTPUT); 
}

void loop() {
if (receiver.decode(&output)) { //Expecting received decoded from IR
  unsigned int value = output.value;
  switch(value) {
    case first_key: //Expecting decoded 
    if(led[1] == 1) {
      // FIRST PIN
      digitalWrite(first_led_pin, HIGH);
      delay(delayPeriod);
      digitalWrite(first_led_pin, LOW);
      delay(delayPeriod);
      digitalWrite(first_led_pin, HIGH);
      delay(delayPeriod);
      digitalWrite(first_led_pin, LOW);
      delay(delayPeriod);
      // SECOND PIN 
      digitalWrite(second_led_pin, LOW);
      delay(delayPeriod);
      digitalWrite(second_led_pin, HIGH);
      delay(delayPeriod);
      digitalWrite(second_led_pin, LOW);
      delay(delayPeriod);
      digitalWrite(second_led_pin, HIGH);
      delay(delayPeriod);
      led[1] = 0;
      
    } else {
        case second_key:
        if(led[1] == 0) {
          digitalWrite(first_led_pin, LOW);
          digitalWrite(second_led_pin, LOW);
          led[1] = 1;
    }
    break;
    
      
    }
    }
    
 
  }
}

  
