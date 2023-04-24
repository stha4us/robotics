
#include "TinyGPS++.h"
#include <SFE_BMP180.h>
#include <Wire.h>

#include "SoftwareSerial.h"

#include "DHT.h"

#define DHTPIN 3     

#define DHTTYPE DHT11

DHT dht(DHTPIN, DHTTYPE);


SFE_BMP180 pressure;


SoftwareSerial serial_connection(10, 11);
TinyGPSPlus gps;


#define ALTITUDE 1400.0



char status;
double T,P;
int a;
float b,c,d,e,h;
float t;

int val;

 float diameter = 0.75;
 float mph;
 int half_revolutions = 0;
 int rpm = 0;
 unsigned long lastmillis = 0;
 float abc;
 float vout = 0.0;
float vin = 0.0;
//float R1 = 100000.0; // resistance of R1 (100K) -see text!
//float R2 = 10000.0; // resistance of R2 (10K) - see text!
int value1 = 0;

float vout2 = 0.0;
float vin2 = 0.0;
float R1 = 100000.0; // resistance of R1 (100K) -see text!
float R2 = 10000.0; // resistance of R2 (10K) - see text!
int value2 = 0;
 
void setup() {
   Serial.begin(9600);
   dht.begin();
   pressure.begin();
   serial_connection.begin(9600);
   //attachInterrupt(0, rpm_fan, FALLING);

}

void loop() {
  
   detachInterrupt(0);
   
   
  humiditydata();
 // delay(2000);//humidity sensor dth11
  
  
  
 pressuredata();
 //delay(2000); //pressure sensor
  
  gpsdata();
 // delay(2000);
  //gps
  
  //windspeed();
  //delay(2000);
  
  winddirection();
 // delay(2000);
  battery1();
  
  battery2();
  
  attachInterrupt(0, rpm_fan, FALLING);
  delay(1000);
  rpm = half_revolutions*60 ;
  abc=(0.094*(float)rpm)/60;
  half_revolutions=0;
   detachInterrupt(0);
  if(Serial.available())
  {
    char x=Serial.read();
    
      if(x=='a')
      {
  Serial.print(t);                   //prints temperature
  Serial.print("\t");                
  Serial.print(h);                   //prints humidity
  Serial.print("\t");
  Serial.print(P);                   //prints absolute pressure
  Serial.print("\t");
  Serial.print(b);                   //prints latitude
  Serial.print("\t");
  Serial.print(c);                   //prints longitude
  Serial.print("\t");
  Serial.print(e);                   //prints altitude
  Serial.print("\t");
  Serial.print(val);                 //prints wind direction in degree
  Serial.print("\t");
  Serial.print(abc);                 //prints wind speed
  Serial.print("\t");
  Serial.print(vin);                 //prints battery voltage
  Serial.print("\t");
  Serial.println(vin2);               //measures solar voltage
      }
  x='b';

  }
  

}



void humiditydata()
{
  //delay(2000);
   h = dht.readHumidity();
   t = dht.readTemperature();
  //Serial.print("Humidity: ");
  //Serial.print(h);
  //Serial.println(" %\t");
  
}


void pressuredata()
{
  status = pressure.startTemperature();
  
  if (status != 0)
  {
    delay(status);
    
    status = pressure.getTemperature(T);
    
    if (status != 0)
    {
      //Serial.print("temperature: ");
      //Serial.print(T);
      //Serial.println(" deg C ");
      
      
      status = pressure.startPressure(3);
      if (status != 0)
      {
        delay(status);
        
        status = pressure.getPressure(P,T);
        
        if (status != 0)
        {
          //Serial.print("absolute pressure: ");
          //Serial.print(P);
          //Serial.println(" mb ");
          }
          
        //else Serial.println("error\n ");
      }
      //else Serial.println("error\n");
    }
    //else Serial.println("error\n");
  }
  //else Serial.println("error\n");
  
 // delay(2000);
  
}



void gpsdata()
{
  
  while(serial_connection.available())
  {
    gps.encode(serial_connection.read());
  }
  if(gps.location.isUpdated())
  {
    
    //Serial.println("Satellite Count:");
    //a=gps.satellites.value();
    //Serial.println(a);
    //Serial.println("Latitude:");
    b=gps.location.lat();
    //Serial.println(b);
    //Serial.println("Longitude:");
    c=gps.location.lng();
    //Serial.println(c);
    //Serial.println("Speed MPH:");
    d=gps.speed.mph();
    //Serial.println(d);
    //Serial.println("Altitude Feet:");
    e=gps.altitude.feet();
    ///Serial.println(e);
    //Serial.println("");
   }
}

/*void windspeed()
{
 if (millis() - lastmillis == 1000){ //Update every one second, this will be equal to reading frequency (Hz).
 detachInterrupt(0);//Disable interrupt when calculating
 rpm = half_revolutions*60 ; // Convert frequency to RPM, note: 60 works for one interruption per full rotation. For two interrupts per full rotation use half_revolutions * 30.
 Serial.print("RPM =\t"); //print the word "RPM" and tab.
 Serial.println(rpm); // print the rpm value.
 
 mph=(0.094*(float)rpm)/60;
 Serial.print("KMP = ");
 Serial.println(mph);
 half_revolutions=0;
 lastmillis = millis();
 attachInterrupt(0, rpm_fan, FALLING);
  }
}*/
 
 // this code will be executed every time the interrupt 0 (pin2) gets low.
 void rpm_fan(){
  half_revolutions++;
  //Serial.println(half_revolutions);
 }
 
 void winddirection()
 {
  val=analogRead(A0);
  val=map(val,0,1023,0,359);
  //Serial.println(val);
 // delay(1000);
 }
 void battery1()
 {
  value1 = analogRead(A2);
   vout = (value1 * 5.4) / 1024.0;
   vin = vout / (R2/(R1+R2)); 
 }
  void battery2()
 {
  value2 = analogRead(A3);
   vout2 = (value2 * 5.4) / 1024.0;
   vin2 = vout2 / (R2/(R1+R2)); 
 }

