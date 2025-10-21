import time  #imports a time module
import RPi.GPIO as gpio  #imports a RPi.GPIO module to allow the use of GPIO pin of pi giving it nickname as g
from Adafruit_CharLCD import Adafruit_CharLCD  #import the module to allow the use of Liquid Crystal Display(LCD) pins
import MySQLdb as msql  #importing module to allow access to MySQL database

# Specifying the name of database
db_name = 'local_db'
while (True):   #runs the code till power supplied
	
	#using the Adafruit_CharLCD module we are creating an object for manipulating the LCD specifying the Register Select pin of LCD connected to GPIO pin 4 of pi, enable pin to GPIO pin 17, d4 to pin 5, d5 to 6, d6 to 13, d7 to 19 and mentioning that we are using 16 columns by 2 rows LCD
	lcd= Adafruit_CharLCD (rs=4, en=17, d4=5, d5=6, d6=13, d7=19, cols=16, lines=2)  
	
	#using connect function of MySQLdb module we are creating an object specifying the server ip address, username for access to database, password for access to database and name of the database
	cur= msql.connect('localhost','root','raspberry',db_name)  
	
	#using the object name c we just created we are creating a cursor for writing SQL query
	curs=cur.cursor ()
	
	#using the l object we created for LCD, we are running clear function to clear the LCD screen
	lcd.clear()  

	#using the l object we are running message function to display the text passed to the function to display on the LCD screen
	lcd.message('Please scan Item\n Using barcode')   

	#wait until 1 second passes
	time.sleep(1) 
	
	#read the values coming from the barcode scanner using raw_input function
	sku_id=input('Enter the ID:')   

	#writing an SQL query to select Item columns of table named pradeep only if the corresponding barcode column of the table is equal to value read from barcode scanner
	query="SELECT Item FROM %s WHERE Barcode= %s" %(db_name, sku_id)  
	
	#using the cursor named a we created before, we execute SQL query stored in q variable
	curs.execute(query)  

	#using the cursor we fetch the value that is returned when we execute the above SQL query
	val = curs.fetchone()  

	#clear the LCD screen to display new text
	lcd.clear()   
	
	#if no value is returned when execution of SQL query display 'None is available!'
	if (val=='None'):		
		lcd.message('Item \n is not available!')
		#hold the message displayed on screen for 4 seconds
		time.sleep(4)  
	#if some value is returned when execution of SQL query, display on lcd screen that returned value(which is the item name to barcode value stored in v variable)
	else:							
		lcd.message ('%s \n is available!' %v)

		#hold the message for 4 seconds
		time.sleep(4)   

    #gpio.cleanup()   #using the gpio module clean the GPIO pins values for the next loop