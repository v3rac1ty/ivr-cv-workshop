# import necessary libraries(opencv, numpy)
import cv2
import numpy as np

# read the cat image (assets/cat1.jpg)
img = None
# convert the image to grayscale
gray_img = None
# Blur the image for better edge detection with (5,5) kernel
blurred_img = None
# Apply Canny edge detection with 100, 100 threshold
edges = None

# display the edges and wait for a keypress
cv2.imshow('Edge detection', edges)
cv2.waitKey(0)
cv2.destroyAllWindows()

# BONUS: Try applying a dilation/erosion to the edges
bonus_img = None
cv2.imshow('Bonus', bonus_img)
cv2.waitKey(0)
cv2.destroyAllWindows()