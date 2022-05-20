import cv2
import mediapipe as mp#21 landmarks for a hand/palm
import time
import thesius_module as the
import math
import numpy as np


cap=cv2.VideoCapture(0)
width= int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height= int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
#writer= cv2.VideoWriter('COUNTER.mp4', cv2.VideoWriter_fourcc(*'DIVX'), 20, (width,height))
detector=the.handDetector() 

pTime=0
cTime=0

while True:
    ok,img=cap.read()
    img=detector.findHands(img)
    lmList=detector.findPosition(img,draw=False)

    if len(lmList)!=0:

        if(lmList[8][2] < lmList[7][2]) and (lmList[12][2] < lmList[11][2])and (lmList[16][2]<lmList[15][2])and(lmList[20][2]<lmList[19][2])and (lmList[4][1]>lmList[3][1]):
            cv2.putText(img,"FIVE",(18,78),cv2.FONT_HERSHEY_PLAIN,3,(0,0,0),3)

        elif(lmList[8][2] < lmList[7][2]) and (lmList[12][2] < lmList[11][2])and (lmList[16][2]<lmList[15][2])and(lmList[20][2]<lmList[19][2]):
            cv2.putText(img,"FOUR",(18,78),cv2.FONT_HERSHEY_PLAIN,3,(0,0,0),3)


        elif(lmList[8][2] <lmList[7][2]) and (lmList[12][2] <lmList[11][2]) and (lmList[16][2]<lmList[15][2]):
            cv2.putText(img,"THREE",(18,78),cv2.FONT_HERSHEY_PLAIN,3,(0,0,0),3)


        elif(lmList[8][2] <lmList[7][2]) and (lmList[20][2] <lmList[19][2]) and (lmList[12][2]<lmList[11][2]):
            cv2.putText(img,"HARDY BOYZ!",(18,78),cv2.FONT_HERSHEY_PLAIN,3,(0,0,0),3)


        elif(lmList[8][2] < lmList[7][2]) and (lmList[12][2] < lmList[11][2]):
            cv2.putText(img,"TWO",(18,78),cv2.FONT_HERSHEY_PLAIN,3,(0,0,0),3)

        
        elif lmList[8][2]< lmList[7][2] and lmList[20][2]<lmList[19][2]:
            cv2.putText(img,"YO",(18,78),cv2.FONT_HERSHEY_PLAIN,3,(0,0,0),3)


        elif lmList[8][2] < lmList[7][2]:
            cv2.putText(img,"ONE",(18,78),cv2.FONT_HERSHEY_PLAIN,3,(0,0,0),3)


        elif lmList[12][2] < lmList[11][2]:
            cv2.putText(img,"FCUK",(18,78),cv2.FONT_HERSHEY_PLAIN,3,(0,0,0),3)


        elif lmList[20][2] < lmList[19][2]:
            cv2.putText(img,"WASHROOM?",(18,78),cv2.FONT_HERSHEY_PLAIN,3,(0,0,0),3)
        
 

    cTime=time.time()
    fps=1/(cTime-pTime)
    pTime=cTime

    #cv2.putText(img,str(int(fps)),(18,78),cv2.FONT_HERSHEY_PLAIN,3,(255,255,0),3)

    #writer.write(img)

    cv2.imshow('COUNTING HAND',img)
    key=cv2.waitKey(1)
    if key==ord('q'):
        break
cv2.destroyAllWindows
cap.release
#writer.release()
    
