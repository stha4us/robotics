# Robotics Projects
A collection of basic scripts to get started with robotics, coding, automation, and image processing. Each folder contains a project with its main script and setup instructions.

---

## Project Index

### Arduino & Electronics
- **[bluetooth_robot](bluetooth_robot/README.md)**  
  *Control a robot via Bluetooth using Arduino.*  
  Main script: [`bluetooth_control.ino`](bluetooth_robot/bluetooth_control.ino)

- **[line_following_robot](line_following_robot/README.md)**  
  *Follow a colored line using digital IR sensors.*  
  Main script: [`script.ino`](line_following_robot/script.ino)

- **[mini_weather_station](mini_weather_station/README.md)**  
  *Measure temperature, windspeed, humidity, and more.*  
  Main script: [`script.ino`](mini_weather_station/script.ino)

- **[height_measurer](height_measurer/README.md)**  
  *Measure height using ultrasonic sensor and display on LCD.*  
  Main script: [`HeightMeasurement.ino`](height_measurer/HeightMeasurement.ino)

- **[homeautomation_system](homeautomation_system/README.md)**  
  *Control devices over Ethernet with Arduino.*  
  Main script: [`scripts.ino`](homeautomation_system/scripts.ino)

- **[GPS tracking system](GPS tracking system/README.md)**  
  *Read GPS data via serial communication.*  
  Main script: [`scripts.ino`](GPS tracking system/scripts.ino)

---

### Python & Raspberry Pi

- **[snake_game](snake_game/README.md)**  
  *Classic Snake game using Pygame.*  
  Main script: [`scripts.py`](snake_game/scripts.py)

- **[calculator](calculator/README.md)**  
  *Simple calculator GUI with Tkinter.*  
  Main script: [`scripts.py`](calculator/scripts.py)

- **[color_tracker_robot](color_tracker_robot/README.md)**  
  *Track and follow colored objects using OpenCV and PiCamera.*  
  Main script: [`opencv_motor_control.py`](color_tracker_robot/opencv_motor_control.py)

- **[face_recognizer](face_recognizer/README.md)**  
  *Face recognition using OpenCV.*  
  Scripts:  
    - [`image_collector.py`](face_recognizer/image_collector.py)  
    - [`image_trainer.py`](face_recognizer/image_trainer.py)  
    - [`image_recognizer.py`](face_recognizer/image_recognizer.py)

- **[talking_tree](talking_tree/README.md)**  
  *React to environment with ultrasonic sensor and play sounds.*  
  Main script: [`script.py`](talking_tree/script.py)

- **[sku_reader](sku_reader/README.md)**  
  *Read barcodes and check stock using Raspberry Pi and MySQL.*  
  Main script: [`scripts.py`](sku_reader/scripts.py)

---

### C/C++ Games

- **[ludo_game](ludo_game/README.md)**  
  *Simple Ludo game using C++ graphics.*  
  Main script: [`graphics_game.CPP`](ludo_game/graphics_game.CPP)

---

## Setup Instructions

Each project folder contains a `README.md` with setup steps.  
Typical workflow for Python projects:

```sh
pip install virtualenv
virtualenv .venv
pip install -r [requirements.txt](http://_vscodecontentref_/0)
python [scripts.py](http://_vscodecontentref_/1)


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

### Autorun 