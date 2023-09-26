import cv2

# load the face classifier
face_classifier = None

# capture video from webcam
video = None

# while loop to iterate over the frames
while True:
    # Capture frame-by-frame using video.read() 
    
    # convert frame to grayscale
    gray_img = None

    # detect faces in the image with scale factor 1.1 and minNeighbors 4
    faces = None

    # Draw a rectangle around the faces
    

    # Display the resulting frame

    # press q to exit the program
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# release the capture
video.release()
cv2.destroyAllWindows()
