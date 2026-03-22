#include <Servo.h>

Servo Servo1;

int servoPin = 9;
int ledPin = 13;
int analogPin = A0;

void setup()
{
  pinMode(ledPin, OUTPUT);
  Servo1.attach(servoPin);
}

void loop()
{
  int analogreader = analogRead(analogPin);
  int a = map(analogreader, 0, 1023, 0, 180);

  if (a > 68)
  {
    Servo1.write(68);
    digitalWrite(ledPin, HIGH);
  }
  else
  {
    Servo1.write(a);
    digitalWrite(ledPin, LOW);
  }

  delay(100);  
}