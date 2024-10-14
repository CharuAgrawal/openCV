# Therholding is binarization of an image. 
# We take an image and convert that into a binary image
# Binary image= where pixels are either 0(black) or 255(white).
# Two type: 
## Simple Thresholding
## Adaptive Thresholding
import cv2 as cv

img = cv.imread('Photos/cats.jpg')
cv.imshow('Cats', img)

# convert to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# threshold= therhold limit, in this case the second parameter=150
# thres= is the binary image created after thresholding
# cv.imshow('Simple threshold', thresh)


# inverse thresholding
# threshold, thresh_inv = cv.threshold(gray, 150, 255, cv.THRESH_BINARY_INV)

# Adaptive thresholding
# Letting the computer find the optimal valuie by itself.
# adaptive_threshold = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 3)
# cv.imshow('Adaptive threshold', adaptive_threshold)


adaptive_threshold = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 3)
cv.imshow('Adaptive threshold', adaptive_threshold)


cv.waitKey(0)