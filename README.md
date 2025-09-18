# robotics projects
Basic script to get started with robotics, coding, automation and image processing

## Configs and Setups

### First boot setup and LAMP installation
#### >> raspi-config
#### expand root partition
#### set timezone
#### in advanced options: enable ssh server
#### in advanced options: update Raspberry Pi
#### reboot
#### >> sudo apt-get update && sudo apt-get upgrade 
#### Apache: >> sudo apt-get install apache2 php5 libapache2-mod-php5
#### In case of error: >> sudo groupadd www-data && sudo usermod -g www-data "
#### Restart: >> sudo service apache2 restart
#### Access hosted page: >> sudo nano /var/www/html/index.html 

#### MySQL: >> sudo apt-get install mysql-server mysql-client php5-mysql

#### Phpmyadmin: >> sudo nano /etc/apache2/apache2.conf
#### Scroll all the way bottom and add: >> include /etc/phpmyadmin/apache.conf

#### Install FTP


### To check network

#### sudo nano /etc/network/interfaces
#### iface eth0 inet static
#### address 192.100.1.107
#### netmask 255.255.255.0
#### gateway 192.100.1.5
#### Here eth0 would be for Pi

#### Checking my IP address: >> hostname -I
#### Get process number: >> ps aux | grep /home/pi/final.py
#### Kill a process: >> sudo kill <process_number>

#### Check UDB port: >> ls /dev/ttyACM *


### Autorun Using Cronjob:
#### >> sudo crontab -e
#### >> 2
#### >> @ reboot /home/pi/file.py &
#### hit enter and exit

### Autorun Scripts in Linux system: 
#### >> Set boot option to "Desktop/CLI"
#### >> Other config set to "Console Autologin"
#### >> sudo nano /etc/profile
#### >> sudo python /home/file.py

### Autrun 