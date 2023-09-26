import cv2 as cv

image_path = "../images/2.jpeg"

img = cv.imread(image_path)

gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

face_classifier = cv.CascadeClassifier(cv.data.haarcascades + "haarcascade_frontalface_default.xml")

faces = face_classifier.detectMultiScale(gray_img, 1.1, 4)

for (x, y, w, h) in faces:
    cv.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

cv.imshow("Face Detection", img)
cv.waitKey(0)
