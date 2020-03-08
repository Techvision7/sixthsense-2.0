import cv2
import numpy as np
import math
import imutils

def gestures():
    lowerBound=np.array([110,150,0])
    upperBound=np.array([150,225,255])

    cap= cv2.VideoCapture(0)
    fgbg = cv2.createBackgroundSubtractorMOG2()
    
    kernel = np.ones((3,3),np.uint8)
    while True:
        #capturing a real time video
        ret, frame = cap.read()
        frame = cv2.flip(frame, 1)
    
        #convert BGR to HSV
        hsv= cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

        # create the Mask
        mask=cv2.inRange(hsv,lowerBound,upperBound)

        #extrapolate the hand to fill dark spots within
        mask1 = cv2.dilate(mask,kernel,iterations = 2)

        #combining the original bgr frame with masked frame
        #result = cv2.bitwise_and(frame,frame,mask = mask1)
        #cv2.imshow('frame', frame)
        #cv2.imshow('mask', mask)
        #cv2.imshow('result',result)

        #subtracting background from the frames
        #bgsub = fgbg.apply(mask)
        #cv2.imshow('bgsub', bgsub)

        #edge detection
        #edges = cv2.Canny(mask1,100,200)
        #cv2.imshow('Edges',edges)

        #blur the image
        #blur = cv2.GaussianBlur(edges,(5,5),100)
        #cv2.imshow('blur', blur)

        #find contours
        contours = cv2.findContours(mask1, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        contours = imutils.grab_contours(contours)

        max_area = -1
        for i in range(len(contours)):
            cnt=contours[i]
            area = cv2.contourArea(cnt)
            if(area>max_area):
                max_area=area
                ci=i
        cnt=contours[ci]

        cv2.drawContours(frame, [cnt], -1, (0,255,255),2)

        topmost = tuple(cnt[cnt[:, :, 1].argmin()][0])
        bottommost = tuple(cnt[cnt[:, :, 1].argmax()][0])
        leftmost = tuple(cnt[cnt[:, :, 0].argmin()][0])
        rightmost = tuple(cnt[cnt[:, :, 0].argmax()][0])

        cv2.circle(frame, topmost, 8, (0,255,0),-1)
        cv2.circle(frame, bottommost, 8, (0,255,0),-1)
        cv2.circle(frame, leftmost, 8, (0,255,0),-1)
        cv2.circle(frame, rightmost, 8, (0,255,0),-1)

        cv2.line(frame, bottommost, topmost, (0,0,255), 3)
        cv2.line(frame, bottommost, leftmost, (0,0,255), 3)
        cv2.line(frame, bottommost, rightmost, (0,0,255), 3)
        

        x,y,w,h = cv2.boundingRect(cnt)
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),0)
        hull = cv2.convexHull(cnt)
        drawing = np.zeros(frame.shape,np.uint8)
        cv2.drawContours(drawing,[cnt],0,(0,255,0),0)
        cv2.drawContours(drawing,[hull],0,(0,0,255),0)
        hull = cv2.convexHull(cnt,returnPoints = False)
        defects = cv2.convexityDefects(cnt,hull)
        count_defects = 0
        cv2.drawContours(mask1, contours, -1, (0,255,0), 3)
        for i in range(defects.shape[0]):
            s,e,f,d = defects[i,0]
            start = tuple(cnt[s][0])
            end = tuple(cnt[e][0])
            far = tuple(cnt[f][0])
            a = math.sqrt((end[0] - start[0])**2 + (end[1] - start[1])**2)
            b = math.sqrt((far[0] - start[0])**2 + (far[1] - start[1])**2)
            c = math.sqrt((end[0] - far[0])**2 + (end[1] - far[1])**2)
            angle = math.acos((b**2 + c**2 - a**2)/(2*b*c)) * 57
            if angle <= 90:
                count_defects += 1
                cv2.circle(frame,far,1,[0,0,255],-1)
            #dist = cv2.pointPolygonTest(cnt,far,True)
            cv2.line(frame,start,end,[0,255,0],2)
        if count_defects == 1:
            cv2.putText(frame,"one", (50,50), cv2.FONT_HERSHEY_SIMPLEX, 2, 2)
        elif count_defects == 2:
            cv2.putText(frame, "Two", (50,50), cv2.FONT_HERSHEY_SIMPLEX, 2, 2)
        elif count_defects == 3:
            cv2.putText(frame,"Three", (50,50), cv2.FONT_HERSHEY_SIMPLEX, 2, 2)
        elif count_defects == 4:
            cv2.putText(frame,"Four", (50,50), cv2.FONT_HERSHEY_SIMPLEX, 2, 2)
        elif count_defects == 5:
            cv2.putText(frame,"Five", (50,50), cv2.FONT_HERSHEY_SIMPLEX, 2, 2)
        elif count_defects == 0:
            cv2.putText(frame,"Fist", (50,50), cv2.FONT_HERSHEY_SIMPLEX, 2, 2)
        else:
            cv2.putText(frame,"no hand detected", (50,50), cv2.FONT_HERSHEY_SIMPLEX, 2, 2)
    
        cv2.imshow('frame', frame)
        k = cv2.waitKey(5) & 0xFF
        if k == 27:
            break

    #releasing the resource and destroying all windows
    cap.release()
    cv2.destroyAllWindows()


gestures()
