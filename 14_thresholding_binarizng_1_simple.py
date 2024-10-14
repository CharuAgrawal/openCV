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

# simple thresholding
# threshold= therhold limit, in this case the second parameter=150
# thres= is the binary image created after thresholding
threshold, thresh = cv.threshold(gray, 150, 255, cv.THRESH_BINARY)
cv.imshow('Simple threshold', thresh)


# inverse thresholding
threshold, thresh_inv = cv.threshold(gray, 150, 255, cv.THRESH_BINARY_INV)
cv.imshow('Simple threshold Inverse', thresh_inv)


cv.waitKey(0)


