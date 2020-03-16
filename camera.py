import cv2
import numpy as np

def camera():
    cap = cv2.VideoCapture(0)
    cv2.namedWindow("Destiny")
    while True:
        ret, frame = cap.read()
        cv2.imshow('Destiny', frame)
        if cv2.waitKey(1) & 0xff == ord('q'):
            break

cv2.destroyAllWindows()
