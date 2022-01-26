import cv2
import face_recognition
import datetime,os

def known_faces():
    return os.listdir('img/')


vid = cv2.VideoCapture(0)

while(True):
    ret, frame = vid.read()
    cv2.imshow('frame',frame)
    unknown_encoding = face_recognition.face_encodings(frame)

    if unknown_encoding:
        unknown_encoding=unknown_encoding[0]
        for known_face in known_faces():
            print(known_face)
            known_image = face_recognition.load_image_file('img/'+known_face)
            known_encoding = face_recognition.face_encodings(known_image)[0]
            results = face_recognition.compare_faces([known_encoding],unknown_encoding)
            print(results)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

vid.release()
cv2.destroyAllWindows()
