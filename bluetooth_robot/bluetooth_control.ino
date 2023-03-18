int c=0;

void setup() {
 
  pinMode(2,OUTPUT);
  pinMode(3,OUTPUT);
  pinMode(4,OUTPUT);
  pinMode(5,OUTPUT);
  Serial.begin(38400);
  pinMode (10,OUTPUT);
  digitalWrite(10,HIGH);
}
void forward()
{
  digitalWrite(2,HIGH);
  digitalWrite(3,LOW);
  digitalWrite(4,HIGH);
  digitalWrite(5,LOW);
}
void left()
{
  digitalWrite(2,HIGH);
  digitalWrite(3,LOW);
  digitalWrite(4,LOW);
  digitalWrite(5,LOW);
}
void right()
{
  digitalWrite(2,LOW);
  digitalWrite(3,LOW);
  digitalWrite(4,HIGH);
  digitalWrite(5,LOW);
}
void backward()
{
  digitalWrite(2,LOW);
  digitalWrite(3,HIGH);
  digitalWrite(4,LOW);
  digitalWrite(5,HIGH);
}
void pause()
{
  digitalWrite(2,LOW);
  digitalWrite(3,LOW);
  digitalWrite(4,LOW);
  digitalWrite(5,LOW);
}

void loop()
{
  if (Serial.available())
  c=Serial.read();
 if(c==200) forward();
 if(c==201) left();
 if(c==202) right();
 if(c==203) backward();
 if(c==204) pause();
 
}

