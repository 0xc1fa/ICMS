import numpy as np
import cv2
import pyttsx3
import pickle
import time

def check_face():
    #load the model
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.read('train.yml')


    engine = pyttsx3.init('dummy')
    rate = engine.getProperty("rate")
    engine.setProperty("rate", 175)
    retturn = []


    face_cascade = cv2.CascadeClassifier('haarcascade/haarcascade_frontalface_default.xml')
    cap = cv2.VideoCapture(0)


    # labels = {"person_name": 3035950000} (student_id)
    with open("labels.pickle", "rb") as f:
        pick = pickle.load(f)
        #name to class label (pick['l'])
        #label to student_id (pick['m'])

        labels = {v: k for k, v in pick['l'].items()} 
        arb_id_to_student_id = {k: v for k, v in pick['m'].items()} 

    
    while True:
        ret, frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=5)

        for (x, y, w, h) in faces:
            print(x, w, y, h)
            roi_gray = gray[y:y + h, x:x + w]
            roi_color = frame[y:y + h, x:x + w]

            # predict the id and confidence for faces
            id_, conf = recognizer.predict(roi_gray)
            #print(id_)

            if conf >= 30:
                font = cv2.QT_FONT_NORMAL

                name = labels[id_]
                
                student_id = arb_id_to_student_id[id_]

                color = (255, 0, 0)
                stroke = 2
                cv2.putText(frame, name, (x, y), font, 1, color, stroke, cv2.LINE_AA)
                cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), (2))

                time.sleep(1)
                retturn.append(student_id)
            
            else:
                color = (255, 0, 0)
                stroke = 2
                font = cv2.QT_FONT_NORMAL
                cv2.putText(frame, "UNKNOWN", (x, y), font, 1, color, stroke, cv2.LINE_AA)
                cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), (2))
                hello = ("Your face is not recognized")
                print(hello)
                engine.say(hello)


        #cv2.imshow('Attendance System', frame)
        k = cv2.waitKey(20) & 0xff
        if k == ord('q'):
            break
        
        if retturn:
            break

    cap.release()
    cv2.destroyAllWindows()
    return retturn[-1] if retturn else None



if __name__ == '__main__':
    l = check_face()
    print(l)