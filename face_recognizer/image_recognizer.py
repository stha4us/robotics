import cv2

recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('trainner/trainner.yml')
cascadePath = "haarcascade_frontalface.xml"
faceCascade = cv2.CascadeClassifier(cascadePath);

cam = cv2.VideoCapture(0)
font = cv2.FONT_HERSHEY_SIMPLEX
while True:
    ret, im =cam.read()
    gray=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
    faces=faceCascade.detectMultiScale(gray, 1.2,5)
    for(x,y,w,h) in faces:
        cv2.rectangle(im,(x,y),(x+w,y+h),(225,0,0),2)
        Id, conf = recognizer.predict(gray[y:y+h,x:x+w])
        if(conf<50):
            if(Id==1):
                Id="User1"
            elif(Id==2):
                Id="User2"
        else:
            Id="Unknown"
        cv2.putText(im,str(Id), (x,y+h),font,1,(0,255,255),2)
    cv2.imshow('im',im) 
    if (cv2.waitKey(1) and 0xFF==ord('q')):
        break
cam.release()
cv2.destroyAllWindows()
