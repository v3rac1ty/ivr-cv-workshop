import cv2 as cv

# speficy the path to the image
image_path = None

# read image 
img = None

# convert image to grayscale
gray_img = None

# load the face classifier
face_classifier = None

# detect faces in the image with scale factor 1.1 and minNeighbors 4
faces = None

# draw a rectangle around the faces, with color green and thickness 2
# faces are stored as (x, y, w, h)


# display the image


cv.waitKey(0)
cv.destroyAllWindows()