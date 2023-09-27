import cv2 as cv

# speficy the path to the image
image_path = "./assets/1.jpeg"

# read image 
img = cv.imread(image_path)

# convert image to grayscale
gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# load the face classifier
face_classifier = cv.CascadeClassifier(cv.data.haarcascades + "haarcascade_frontalface_default.xml")

# detect faces in the image with scale factor 1.1 and minNeighbors 4
faces = face_classifier.detectMultiScale(gray_img, 1.1, 4)

# draw a rectangle around the faces, with color green and thickness 2
# faces are stored as (x, y, w, h)
for(x, y, w, h) in faces:
    cv.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)

# display the image
cv.imshow("Face Detection", img)

cv.waitKey(0)
cv.destroyAllWindows()