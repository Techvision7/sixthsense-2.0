import cv2
import time
import numpy as np
import os


def nothing(x):
    pass


image_x, image_y = 64, 64

def create_folder(folder_name):
    if not os.path.exists('./files/images/' + folder_name):
        os.mkdir('./files/images/' + folder_name)
        

        
def capture_images(name):
    create_folder(str(name))
    face_cascade = cv2.CascadeClassifier('files/cascades/haarcascade_frontalface_alt2.xml')
    eye_cascade = cv2.CascadeClassifier('files/cascades/haarcascade_eye.xml')

    
    cam = cv2.VideoCapture(0)

    cv2.namedWindow("Destiny")

    img_counter = 0
    t_counter = 1
    training_set_image_name = 1
    test_set_image_name = 1
    listImage = [1,2,3,4,5]
    
    for loop in listImage:
        while True:

            ret, frame = cam.read()
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=5)
            for (x, y, w, h) in faces:
                print(x, y, w, h)
                roi_gray = gray[y:y+h, x:x+w]#for gray frame
                roi_frame = frame[y:y+h, x:x+w]#for normal frame
                eyes = eye_cascade.detectMultiScale(roi_gray)
                for (ex,ey,ew,eh) in eyes:
                    cv2.rectangle(roi_frame,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
                

                roi_frame = frame[y:y+h, x:x+w]
                color = (0, 255, 0)
                stroke = 2
                end_cord_x = x + w
                end_cord_y = y + h
                cv2.rectangle(frame, (x, y), (end_cord_x, end_cord_y), color, stroke)  

            cv2.imshow("Destiny", frame)
            if cv2.waitKey(1) == ord('c'):

                if t_counter <= 500:
                    img_name = "./files/images/" + str(name) + "/{}.png".format(training_set_image_name)
                    
                    cv2.imwrite(img_name, frame)
                    print("{} written!".format(img_name))
                    training_set_image_name += 1


                t_counter += 1
                if t_counter == 401:
                    t_counter = 1
                img_counter += 1


            elif cv2.waitKey(1) == 27:
                break

        if test_set_image_name > 250:
            break


    cam.release()
    cv2.destroyAllWindows()
    
name = input("Enter Name:- ")
capture_images(name)
