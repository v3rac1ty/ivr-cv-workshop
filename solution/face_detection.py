import cv2 as cv

image_path = "../assets/2.jpeg"
# read the image
img = cv.imread(image_path)
# convert the image to grayscale
gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# declare the face detector object
face_classifier = cv.CascadeClassifier(cv.data.haarcascades + "haarcascade_frontalface_default.xml")
# run detection on the image
faces = face_classifier.detectMultiScale(gray_img, 1.1, 4)
# draw the bounding boxes
for (x, y, w, h) in faces:
    cv.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
# display the final image
cv.imshow("Face Detection", img)
cv.waitKey(0)
cv.destroyAllWindows()