# import necessary libraries(opencv, numpy)
import cv2
import numpy as np
# read the color pallete image (assets/colors.jpg)
img = None
# convert image to HSV color space
hsv_img = None

# define the lower and upper bounds of the color we want to detect
lower_range = None
upper_range = None

# create a mask for the color
mask = None
# show mask
cv2.imshow('mask', mask)
cv2.waitKey(0)
cv2.destroyAllWindows()

# apply mask onto original image to only show the desired color
result = None
# show result
cv2.imshow('result', result)
cv2.waitKey(0)
cv2.destroyAllWindows()

# find contours from the mask

# draw rectangles around each contour

# show result
cv2.imshow('contours', img)
cv2.waitKey(0)
cv2.destroyAllWindows()