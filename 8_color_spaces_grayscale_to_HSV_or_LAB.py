# convert grayscale to BGR and then to HSV/LAB (durectly is not possible)
# you can not do it like the other color scales
#  I am tired, I am finishing this code, but you will get the gist 
#  by the given lines of code.
import cv2 as cv
import matplotlib.pyplot as plt 

img = cv.imread('Photos/cats.jpg')
cv.imshow('Cats', img)

hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('HSV', hsv)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow('RGB', rgb)

# HSV to BGR
hsv_bgr =cv.cvtColor(hsv, cv.COLOR_HSV2BGR)
cv.imshow('HSV --> BGR', hsv)


cv.waitKey(0)
