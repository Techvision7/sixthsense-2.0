import cv2
import numpy as np
import pickle


def recognise():
    face_cascade = cv2.CascadeClassifier('files/cascades/haarcascade_frontalface_alt2.xml')
    eye_cascade = cv2.CascadeClassifier('files/cascades/haarcascade_eye.xml')

    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.read("trainer.yml")

    labels = {"person_name":1}

    with open("label.pickle",'rb') as f:
        labels = pickle.load(f)
        labels = {v:k for k,v in labels.items()}

    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=5)
        for (x, y, w, h) in faces:
            print(x, y, w, h)
            roi_gray = gray[y:y+h, x:x+w]#for gray frame
            roi_frame = frame[y:y+h, x:x+w]#for normal frame
            eyes = eye_cascade.detectMultiScale(roi_gray)
            for (ex,ey,ew,eh) in eyes:
                cv2.rectangle(roi_frame,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)

            #recognize
            id_, conf = recognizer.predict(roi_gray)
            if conf>=45 and conf<=85:
                print(id_)
                print(labels[id_])
                font = cv2.FONT_HERSHEY_SIMPLEX
                name = labels[id_]
                color = (0, 0, 255)
                stroke = 2
                cv2.putText(frame, name, (x, y), font, 1, color, stroke, cv2.LINE_AA)

            #img_item = "my-image.png"
            #cv2.imwrite(img_item, roi_gray)
            #for normal frame
            roi_frame = frame[y:y+h, x:x+w]

            color = (0, 255, 0)
            stroke = 2
            end_cord_x = x + w
            end_cord_y = y + h
            cv2.rectangle(frame, (x, y), (end_cord_x, end_cord_y), color, stroke)
        
        cv2.imshow('Destiny', frame)
        #cv2.imshow('gray', gray)
    

        if cv2.waitKey(1) & 0xff == ord('q'):
            break
    cap.release()
cv2.destroyAllWindows()
