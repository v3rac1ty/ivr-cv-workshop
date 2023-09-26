import cv2

# load the face classifier
face_classifier = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

# capture video from webcam
video = cv2.VideoCapture(1)

# while loop to iterate over the frames
while True:
    # Capture frame-by-frame
    ret, frame = video.read()
    
    # convert frame to grayscale
    gray_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # detect faces in the image with scale factor 1.1 and minNeighbors 4
    faces = face_classifier.detectMultiScale(gray_img, 1.1, 4)

    # Draw a rectangle around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Display the resulting frame
    cv2.imshow('Video', frame)

    # press q to exit the program
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# release the capture
video.release()
cv2.destroyAllWindows()
