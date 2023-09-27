# import necessary libraries(opencv, numpy)
import cv2
import numpy as np

# read the cat image (assets/cat1.jpg)
img = cv2.imread('./assets/cat1.jpg')
# convert the image to grayscale
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# Blur the image for better edge detection with (5,5) kernel
blurred_img = cv2.GaussianBlur(gray_img, (5, 5), 0)

# Apply Canny edge detection with 100, 100 threshold
edges = cv2.Canny(blurred_img, 100, 100)

# display the edges and wait for a keypress
cv2.imshow('Edge detection', edges)
cv2.waitKey(0)
cv2.destroyAllWindows()

# BONUS: Try applying a dilation/erosion to the edges
bonus_img = cv2.dilate(edges, np.ones(10), iterations=4)
# bonus_img = cv2.erode(edges, np.ones(3), iterations=1)
cv2.imshow('Bonus', bonus_img)
cv2.waitKey(0)
cv2.destroyAllWindows()