import cv2 as cv

img = cv.imread('Photos/cat_large.jpg')
# img is a matrix

cv.imshow('Cat', img)

cv.waitKey(0)
# keyboard binding function. It waits for specific delay or time in sec. 
