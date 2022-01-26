import face_recognition
import cv2

orginal_image = cv2.imread("img.jpg", cv2.IMREAD_COLOR)
image = face_recognition.load_image_file("img.jpg")
face_locations = face_recognition.face_locations(image)

for face_location in face_locations:
    cv2.rectangle(orginal_image,(face_location[3],face_location[2]),(face_location[1],face_location[0]),(255,0,0),2)

cv2.imshow("Image",orginal_image)
cv2.waitKey(0)
cv2.destroyAllWindows()