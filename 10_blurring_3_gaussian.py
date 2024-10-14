# Gaussian Blur
# all pixels are given weights. 
# the pixel intesity if the average of these weights. 
# Gaussian blur is therefore more natural as compared to the average-blur
import cv2 as cv
import numpy as np

img = cv.imread('Photos/park.jpg')
cv.imshow('Park', img)

# Averaging
# First, Define a Kernel window.
# It will compute the avergae instensity of the middle pixel of the true center as the average of the surrounding pixel intensities. 
average = cv.blur(img, (7,7))
cv.imshow('Average Blur', average)

# Gaussian Blur
gauss = cv.GaussianBlur(img, (7,7), 0) #0 is sigma_x or basically the SD in the x direction.
cv.imshow('Gaussian Blur', gauss )
# Result => gaussian blurr is less blur than the average with the sam ekernel size.

cv.waitKey(0)