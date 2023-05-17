#include <SoftwareSerial.h>

SoftwareSerial mySerial(2,3); // RX, TX


int tts=1;

//for GPS

int i=0,j=0,comma_count=0,flag=0,count=0,start=0;

String gps_data="";

int latitude[10],longitude[10];

long final_latitude,final_longitude;


void setup()
  
{
    
mySerial.begin(9600);
    
Serial.begin(9600);
    
delay(2000);
   
 }


void loop()  
{
    char gps_char;
    if(mySerial.available()) {
        gps_char=mySerial.read();
       if(gps_char=='$')
         flag=1;
       if(flag==1)
         {
         gps_data=gps_data+gps_char;
         count++;
         if(count==6)
           {
           flag=0;
           count=0;
           }
     }
     else
     {
       if(gps_data.indexOf("$GPGGA")>-1)
       {
         start=1;
       }
     }
     
     if(start==1)
       {
         if(gps_char==',')
           comma_count++;
         if(comma_count==2)
         {
           latitude[i]=gps_char-48;
            i++;
           
         }
         else if(comma_count==4)
         {
           longitude[j]=gps_char-48;
           j++;
           
         }
         else if(comma_count>5)
           {
             int latdd=latitude[1]*10+latitude[2];
             double latmm=latitude[3]*10+latitude[4]+(latitude[6]*1000+latitude[7]*100+latitude[8]*10+latitude[9])/10000.;
             final_latitude=latdd+latmm/60.;
             
             int longdd=longitude[2]*10+longitude[3];
             double longmm=longitude[4]*10+longitude[5]+(longitude[7]*1000+longitude[8]*100+longitude[9]*10+longitude[10])/10000.;
             final_longitude=longdd+longmm/60.;
             
             start=0;
             i=0;
             j=0;
             comma_count=0;
             gps_data="";
           }
       }
  Serial.print("lat");
  Serial.println(final_latitude);
  Serial.print("long");
    Serial.println(final_longitude);
    Serial.println(final_latitude+final_longitude);
      

  }
  }
