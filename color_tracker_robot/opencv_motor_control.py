#!/usr/bin/env python3.4
import cv2
from picamera import PiCamera
from picamera.array import PiRGBArray
import time
import numpy as np
import RPi.GPIO as GPIO
#__________________________________________________________________


GPIO.setmode(GPIO.BOARD)

MOTORL1=11  #Left Motor
MOTORL2=13

MOTORR1=15  #Right Motor
MOTORR2=16



GPIO.setup(MOTORL1, GPIO.OUT)
GPIO.setup(MOTORL2, GPIO.OUT)

GPIO.setup(MOTORR1, GPIO.OUT)
GPIO.setup(MOTORR2, GPIO.OUT)

def forward():
      GPIO.output(MOTORL1, GPIO.HIGH)
      GPIO.output(MOTORL2, GPIO.LOW)
      GPIO.output(MOTORR1, GPIO.HIGH)
      GPIO.output(MOTORR2, GPIO.LOW)
     
def reverse():
      GPIO.output(MOTORL1, GPIO.LOW)
      GPIO.output(MOTORL2, GPIO.HIGH)
      GPIO.output(MOTORR1, GPIO.LOW)
      GPIO.output(MOTORR2, GPIO.HIGH)
     
def leftturn():
      GPIO.output(MOTORL1,GPIO.LOW)
      GPIO.output(MOTORL2,GPIO.HIGH)
      GPIO.output(MOTORR1,GPIO.HIGH)
      GPIO.output(MOTORR2,GPIO.LOW)
     
def rightturn():
      GPIO.output(MOTORL1,GPIO.HIGH)
      GPIO.output(MOTORL2,GPIO.LOW)
      GPIO.output(MOTORR1,GPIO.LOW)
      GPIO.output(MOTORR2,GPIO.HIGH)

def stop():
      GPIO.output(MOTORL1,GPIO.LOW)
      GPIO.output(MOTORL2,GPIO.LOW)
      GPIO.output(MOTORR1,GPIO.LOW)
      GPIO.output(MOTORR2,GPIO.LOW)



def segment_colour(frame):    #returns only the red colors in the frame
    hsv_roi =  cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    mask_1 = cv2.inRange(hsv_roi, np.array([169, 120,100]), np.array([190,255,255]))
    #ycr_roi=cv2.cvtColor(frame,cv2.COLOR_BGR2YCrCb)
    #mask_2=cv2.inRange(ycr_roi, np.array((0.,165.,0.)), np.array((255.,255.,255.)))

    mask = mask_1 #| mask_2
    kern_dilate = np.ones((8,8),np.uint8)
    kern_erode  = np.ones((3,3),np.uint8)
    mask= cv2.erode(mask,kern_erode)      #Eroding
    mask=cv2.dilate(mask,kern_dilate)     #Dilating
    cv2.imshow('mask',mask)
    rawCapture.truncate(0)
    return mask

def find_blob(blob): #returns the red colored circle
    largest_contour=0
    cont_index=0
    contours, hierarchy = cv2.findContours(blob, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)[-2:] 
    for idx, contour in enumerate(contours):
        area=cv2.contourArea(contour)
        if (area >largest_contour) :
            largest_contour=area
           
            cont_index=idx
            #if res>15 and res<18:
            #    cont_index=idx
                              
    r=(0,0,1,1)
    if len(contours) > 0:
        r = cv2.boundingRect(contours[cont_index])
       

    return r,largest_contour

'''
def target_hist(frame):
    hsv_img=cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
   
    hist=cv2.calcHist([hsv_img],[0],None,[50],[0,255])
    return hist
'''

time.sleep(0.5)
camera= PiCamera()
camera.resolution=(640,480)

camera.framerate = 16
#camera.hflip = True

rawCapture = PiRGBArray(camera, size=(640,480))
 
# allow the camera to warmup
time.sleep(0.05)

flag=0
found=1
list1=[x for x in range(240,400)]
list2=[y for y in range(0,240)]
list3=[z for z in range(400,640)]

for image in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
      #grab the raw NumPy array representing the image, then initialize the timestamp and occupied/unoccupied text
    frame = image.array
    #frame=cv2.flip(frame,1)

    global centre_x
    global centre_y
    centre_x=0.
    centre_y=0.
    hsv1 = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask_red=segment_colour(frame)      
    loct,area=find_blob(mask_red)
    x,y,w,h=loct            #returned value coordinates of the largest bounding rectangle for largest blob
             
    if ((w*h) < 50):
        print (w*h)
        found=0
    elif((w*h)>=50):
        print (w*h)
        found=1
        cv2.rectangle(frame, (x,y), (x+w,y+h), 255,2)
        centre_x=x+((w)/2)
        centre_y=y+((h)/2)
        cv2.circle(frame,(int(centre_x),int(centre_y)),3,(0,110,255),-1)
        #print (centre_x,centre_y)

	
    initial=200
    second=30000
    if(found==0):
            #if the color is not found and the last time it sees the color in which direction, it will start to rotate in that direction
        if (flag==0):
            rightturn()
            time.sleep(0.01)
        elif (flag==1):
            leftturn()
            time.sleep(0.01)
        #stop()
        #time.sleep(0.0125)
     
    elif(found==1):
        if(area<initial):
              #object is too far
            forward()
            time.sleep(0.001)
        elif(area>=initial and area<second):
                #it brings coordinates of ball to center of camera's imaginary axis.
            if centre_x in list1:
                forward()
            if centre_x in list2:
                flag=1
                leftturn()
            if centre_x in list3:
                flag=0
                rightturn()
            #forward()
            #time.sleep(0.01)
            #stop()
                
        else:
            forward()

    cv2.imshow("draw",frame)    
    rawCapture.truncate(0)

    if (cv2.waitKey(1) & 0xFF==ord('q')):
        break
    
stop()
camera.release()
cv2.destroyAllWindows()
GPIO.cleanup()    



                        

