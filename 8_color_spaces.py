# OpenCV reads color in BGR format.
# Outside OpenCV, we use RGB format. 


# color space are space of colors.
# A systemn of representing an array of pixel color. 
# RGB, grayscale, HSV, lab, etc etc..
import cv2 as cv
import matplotlib.pyplot as plt 
# import matplotlib.pyplot as plt

img = cv.imread('Photos/park.jpg')
cv.imshow('Park', img)

# BGR to Grayscale 
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)


# HSV: Hue Saturation Value
# based on how humans think and concieve color
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('HSV', hsv)

# L * a * b
# closure to how humans percieve color
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow('LAB', lab)


plt.imshow(img)
plt.show()

cv.waitKey(0)
