# Gradient and Edge detection in OpenCV.
# Gradient and edges are completely different things from mathematical poitn of view. 
# From programming point of view, you can get away with thinking of them as the same. 
# canny edge detection: previously discussed; multi-step process.
# laplacian 
# Sobel

import cv2 as cv
import numpy as np

img = cv.imread('Photos/park.jpg')
cv.imshow('park', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# Lap
lap =cv.Laplacian(gray, cv.CV_64F)
lap =np.uint8(np.absolute(lap))
cv.imshow('Laplacian', lap)



# Sobel
sobelx= cv.Sobel(gray, cv.CV_64F, 1, 0)
sobely= cv.Sobel(gray, cv.CV_64F, 0, 1)
combined_sobel = cv.bitwise_or(sobelx, sobely)

cv.imshow('Sobel X', sobelx)
cv.imshow('Sobel Y', sobely)
cv.imshow('Combined Sobel', combined_sobel)

canny = cv.Canny(gray, 150, 175)
cv.imshow('Canny', canny)

cv.waitKey(0)