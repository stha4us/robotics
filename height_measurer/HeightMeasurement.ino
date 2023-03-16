#include <LiquidCrystal.h>

LiquidCrystal lcd(12, 11, 5, 4, 3, 2);
long duration;
long inches;

void setup() {
  // initialize serial communication:
  Serial.begin(9600);
  lcd.begin(16, 2);
  // Print a message to the LCD.
  pinMode(9, OUTPUT);
  pinMode(10, INPUT);
  pinMode (6,OUTPUT);
  
  pinMode(8,OUTPUT);
  digitalWrite(8,HIGH);
  pinMode(7,OUTPUT);
  digitalWrite(7,LOW);

}

void loop()
{
  // establish variables for duration of the ping,
  // and the distance result in inches and centimeters:
  analogWrite(6,150);
 
  //analogWrite(6,100);
  // The PING))) is triggered by a HIGH pulse of 2 or more microseconds.
  // Give a short LOW pulse beforehand to ensure a clean HIGH pulse:
  digitalWrite(9, LOW);
  delayMicroseconds(2);
  digitalWrite(9, HIGH);
  delayMicroseconds(5);
  digitalWrite(9, LOW);

  // The same pin is used to read the signal from the PING))): a HIGH
  // pulse whose duration is the time (in microseconds) from the sending
  // of the ping to the reception of its echo off of an object.
  duration = pulseIn(10, HIGH);

  // convert the time into a distance
  inches = microsecondsToInches(duration);

  lcd.setCursor(0, 1);
  Serial.print(inches);
  Serial.println();
  Serial.print(" inches");
  lcd.print(inches);
  lcd.setCursor (1,1);
  lcd.print ("inches");
  delay(200);  
}

long microsecondsToInches(long microseconds)
{
  // According to Parallax's datasheet for the PING))), there are
  // 73.746 microseconds per inch (i.e. sound travels at 1130 feet per
  // second).  This gives the distance travelled by the ping, outbound
  // and return, so we divide by 2 to get the distance of the obstacle.
  // See: http://www.parallax.com/dl/docs/prod/acc/28015-PING-v1.3.pdf
  return microseconds / 74 / 2;
}
