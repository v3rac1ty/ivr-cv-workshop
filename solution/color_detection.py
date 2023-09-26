# import libraries
import cv2
import numpy as np

# read the image
img = cv2.imread('../assets/colors.png')
# convert image to HSV color space
hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# define the lower and upper bounds of the color we want to detect
lower_range = np.array([140, 50, 0])
upper_range = np.array([170, 255, 255])

# create a mask for the color
mask = cv2.inRange(hsv_img, lower_range, upper_range)
# show mask
cv2.imshow('mask', mask)
cv2.waitKey(0)
cv2.destroyAllWindows()

# apply mask onto original image to only show the desired color
result = cv2.bitwise_and(img, img, mask=mask)
# show result
cv2.imshow('result', result)
cv2.waitKey(0)
cv2.destroyAllWindows()

# find contours from the mask
contours, hierarchy = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
# draw rectangles around each contour
for cnt in contours:
    rect = cv2.boundingRect(cnt)
    cv2.rectangle(img, rect, (0, 0, 0), 10)
# show result
cv2.imshow('contours', img)
cv2.waitKey(0)
cv2.destroyAllWindows()