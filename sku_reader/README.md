# robotics projects
Basic script to get started with raspberry pi to setup SKU unit

This scripts allows a system to read the barcode and check if the iteam are in stock

Steps:
>> setup raspberry pi or any computing device
>> pip install virtualenv
>> virtualenv .venv
>> pip install requirements.txt
>> run the script in raspberry pi
>> comment @stha4us on the repo for any assitance needed for the complete process!

>> copy the python script to location "/home/pi" in the raspberry pi

>> In terminal: type "sudo crontab -e"

>> Scroll all the way down and add the following line:
>> "@reboot python /home/pi/scripts.py &"

>press "Ctrl+X to exit"
>press "y" to save followed by enter twice