import cv2
import numpy as np


cap = cv2.VideoCapture(0)

def nothing(x):
    pass
# Creating a window for later use
cv2.namedWindow('result')
cv2.resizeWindow('result', 600,600)

# Starting with 100's to prevent error while masking
h,s,v = 0,0,0

# Creating track bar
cv2.createTrackbar('huelow', 'result',0,255,nothing)
cv2.createTrackbar('satlow', 'result',0,255,nothing)
cv2.createTrackbar('vallow', 'result',0,255,nothing)

cv2.createTrackbar('huehi', 'result',0,255,nothing)
cv2.createTrackbar('sathi', 'result',0,255,nothing)
cv2.createTrackbar('valhi', 'result',0,255,nothing)

while(1):

    _, frame = cap.read()
    frame = cv2.flip(frame, 1)

    #converting to HSV
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    # get info from track bar and appy to result
    huelow = cv2.getTrackbarPos('huelow','result')
    satlow = cv2.getTrackbarPos('satlow','result')
    vallow = cv2.getTrackbarPos('vallow','result')

    huehi = cv2.getTrackbarPos('huehi','result')
    sathi = cv2.getTrackbarPos('sathi','result')
    valhi = cv2.getTrackbarPos('valhi','result')


    # Normal masking algorithm
    lower = np.array([huelow,satlow,vallow])
    upper = np.array([huehi,sathi,valhi])

    mask = cv2.inRange(hsv,lower, upper)

    result = cv2.bitwise_and(frame,frame,mask = mask)
    cv2.imshow('frame', frame)
    cv2.imshow('mask', mask)
    #cv2.imshow('result',result)

    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cap.release()

cv2.destroyAllWindows()
