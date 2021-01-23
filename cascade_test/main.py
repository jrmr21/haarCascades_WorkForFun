

path = '/home/jrmr/Bureau/pyMachinLearning/haarCascades_WorkForFun/'


#! python3

import numpy as np  #   librarie for the IHM
import cv2          #   librarie for the camera capture an working
import math         #   librarie for mathematic function ( racine carre et puissance ( ² )

face_cascade = cv2.CascadeClassifier(path+"/cascade_test/penguin_cascade.xml")
#       xml file do decript in capture the face of humans

cap = cv2.VideoCapture(0)   # 0 not 1 because is a bug ( in windows sure )
cap.set(3,640)      #   size capture ( x )
cap.set(4,480)      #                ( y )


while 1:                        #   void loooOOOOOoooop :)
    ret, img = cap.read()                                   #   running camera
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)     #   parameter of contoure of face

    for (x,y,w,h) in faces:                                 #   made a contour cube on face
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,120,255),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]

        cv2.circle(img,(int(x+(w/2)),int(y+(h/2))), 10, (0,0,255), -1)  # display point on center face


        #---------------- PREPARE THE VARIABLE TO DISPLAY THE DISTANCE ---------------------  
        
        #    ______________________________________________________________
        #   /!\     distance d un vecteur = racinne²(xa-xb)²+(yb-ya)²    /!\
        #   ________________________________________________________________
        
        display=math.sqrt(math.pow(int(x+(w/2))-320,2)+ 0 )
                                            #yb-ya = 0  ^   car yb == ya   
        if (int(x+(w/2))<300):
            display=str(display*-1)     # negative value 1/2 part of screen
        else :
            display=str(display)        # positive value 2/2 part of screen
            
        #------------ END PREPARE THE VARIABLE TO DISPLAY THE DISTANCE ---------------------    

        font = cv2.FONT_HERSHEY_SIMPLEX # the font of the text
        
        cv2.putText(img,display,((int(x+(w/2)),int(y+(h/2)))), font, 1,(245,68,235),5,cv2.LINE_AA)
        #           (img,string,(x,y),font,(size of caractere),(color),size of caractere,cv2.LINE_AA) 
        #   display a text with a variable (display) is the distance (px) of your head and the 1/2 screen 
        
        cv2.line(img,((int(x+(w/2)),int(y+(h/2)))),(320,int(y+(h/2))),(1,170,120),5)
        #   line to connecte the face with the 1/2 screen
        
    cv2.line(img,(320,0),(320,600),(1,170,120),5)   #   cut the screen in 2 parts withe a line
        #         (x,y) ,   (x,y)
    
    cv2.imshow('img',img)
    k = cv2.waitKey(1) &    0xff    # exit avec le code touche 'echap'
    if k == 27:
        break

cap.release()               #   end camera
cv2.destroyAllWindows()     #   close all windows