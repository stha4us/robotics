import RPi.GPIO as GPIO
import time
import pygame
 
GPIO.setmode(GPIO.BOARD)
 
TRIG = 11
ECHO = 13

pygame.mixer.init() 
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN) 

#Define path to your intial sound clip to play
sound_clip1_path="path_to_file/sample/Forest.mp3"

#Define path to sound clip to be played when at closer range
sound_clip2_path="path_to_file/sample/voice.mp3"
while True:
        distance=0
        GPIO.output(TRIG,0)
        GPIO.output(TRIG,1)
        time.sleep(0.00001)
        GPIO.output(TRIG,0)
        while GPIO.input(ECHO) == 0:
                pass
        StartTime = time.time()
        while GPIO.input(ECHO) == 1:
                pass
        StopTime = time.time()

        TimeElapsed = StopTime - StartTime
        distance = (TimeElapsed * 34000) / 2
        print("Measured Distance = %.1f cm" % distance)
        if (distance < 120.0 and distance >80.0):
                
                pygame.mixer.music.load(sound_clip1_path)
                pygame.mixer.music.play()
                while (pygame.mixer.music.get_busy()==True and distance<130.0 and distance>80.0):
                        GPIO.output(TRIG,0)
                        GPIO.output(TRIG,1)
                        time.sleep(0.00001)
                        GPIO.output(TRIG,0)
                        while GPIO.input(ECHO)==0:
                                pass
                        StartTime=time.time()
                        while GPIO.input(ECHO)==1:
                                pass
                        StopTime=time.time()
                        TimeElapsed=StopTime - StartTime
                        distance=(TimeElapsed*34000)/2
                        
                        print("Measured Distance = %.1f cm" % distance)
        
                        continue
                pygame.mixer.music.stop()
        if (distance <60.0 and distance >15.0):
                pygame.mixer.music.load(sound_clip2_path)
                pygame.mixer.music.play()
                while (pygame.mixer.music.get_busy()==True):
                        print("Measured Distance = %.1f cm" % distance)
                        continue
        pygame.mixer.music.stop()
        
GPIO.cleanup()

