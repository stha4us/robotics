int x;

void setup()
{  pinMode(9, OUTPUT);     

   pinMode(10, OUTPUT);     
 digitalWrite(9, LOW);
}

void loop()
{
  for(x=0; x<=255; x++)
  {
  analogWrite(10, x);
  delay(50);
  }
for(x=255; x>=0; x--)
  {
  analogWrite(10, x);
  delay(50);
  }
}
