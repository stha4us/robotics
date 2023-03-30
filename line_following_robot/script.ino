#define lmotorf 4
#define lmotorb 5
#define rmotorf 6
#define rmotorb 7

//HIGH white
//LOW black

void setup() {

pinMode(3,OUTPUT);
pinMode(9,OUTPUT);

pinMode(lmotorf,OUTPUT);
pinMode(rmotorf,OUTPUT);
pinMode(lmotorb,OUTPUT);
pinMode(rmotorb,OUTPUT);
pinMode(11,INPUT);
pinMode(10,INPUT);
digitalWrite(3, 90);
digitalWrite(9, 90)
;

}

void loop() {

// dynamic line follower code
// if the sensor is on white it returns LOW value to the Arduino
// if it is on black it returns a HIGH value to the Arduino
int lsensor=digitalRead(11);
int rsensor=digitalRead(10);
if((lsensor==HIGH)&&(rsensor==HIGH))
{
//both sensors on white
// go forward
digitalWrite(lmotorf,HIGH);
digitalWrite(rmotorf,HIGH);
digitalWrite(lmotorb,LOW);
digitalWrite(rmotorb,LOW);
}
else if((lsensor==HIGH)&& (rsensor==LOW))
{
//right sensor on black line
// turn right
digitalWrite(lmotorf,HIGH);
digitalWrite(rmotorf,LOW);
digitalWrite(lmotorb,LOW);
digitalWrite(rmotorb,HIGH);
}
else if((lsensor==LOW)&&(rsensor==HIGH))
{
//left sensor on black line
// turn left
digitalWrite(lmotorf,LOW);
digitalWrite(rmotorf,HIGH);
digitalWrite(lmotorb,HIGH);
digitalWrite(rmotorb,LOW);
}
else
{
digitalWrite(lmotorf,LOW);
digitalWrite(rmotorf,LOW);
digitalWrite(lmotorb,LOW);
digitalWrite(rmotorb,LOW);
}
}
