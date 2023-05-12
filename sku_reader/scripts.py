import time  #imports a time module
import RPi.GPIO as gpio  #imports a RPi.GPIO module to allow the use of GPIO pin of pi giving it nickname as g
from Adafruit_CharLCD import Adafruit_CharLCD  #import the module to allow the use of Liquid Crystal Display(LCD) pins
import MySQLdb as msql  #importing module to allow access to MySQL database

while (True):   #runs the code till power supplied
	
	lcd= Adafruit_CharLCD (rs=4, en=17, d4=5, d5=6, d6=13, d7=19, cols=16, lines=2)  #using the Adafruit_CharLCD module we are creating an object for manipulating the LCD specifying the Register Select pin of LCD connected to GPIO pin 4 of pi, enable pin to GPIO pin 17, d4 to pin 5, d5 to 6, d6 to 13, d7 to 19 and mentioning that we are using 16 columns by 2 rows LCD
	cur= msql.connect('localhost','root','raspberry','pradeep')  #using connect function of MySQLdb module we are creating an object specifying the server ip address, username for access to database, password for access to database and name of the database
	curs=cur.cursor () #using the object name c we just created we are creating a cursor for writing SQL query
	lcd.clear()  #using the l object we created for LCD, we are running clear function to clear the LCD screen
	lcd.message('Please scan Item\n Using barcode')   #using the l object we are running message function to display the text passed to the function to display on the LCD screen
	time.sleep(1)  #wait until 1 second passes
	
	sku_id=input('Enter the ID:')   #read the values coming from the barcode scanner using raw_input function
	query="SELECT Item FROM pradeep WHERE Barcode= %s" %sku_id  #writing an SQL query to select Item columns of table named pradeep only if the corresponding barcode column of the table is equal to value read from barcode scanner
	
	curs.execute(query)  #using the cursor named a we created before, we execute SQL query stored in q variable

	val = curs.fetchone()  #using the cursor we fetch the value that is returned when we execute the above SQL query
	lcd.clear()   #clear the LCD screen to display new text
	
	if (val=='None'):		#if no value is returned when execution of SQL query display 'None is available!'

		lcd.message('Item \n is not available!')
		time.sleep(4)  #hold the message displayed on screen for 4 seconds
	else:							#if some value is returned when execution of SQL query, display on lcd screen that returned value(which is the item name to barcode value stored in v variable)
		lcd.message ('%s \n is available!' %v)
		time.sleep(4)   #hold the message for 4 seconds

    #gpio.cleanup()   #using the gpio module clean the GPIO pins values for the next loop