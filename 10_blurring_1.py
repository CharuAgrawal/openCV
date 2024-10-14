# Smooth and blurring images using openCV
# We need to smooth the image when the image has a lotof noise
# Usually the noise is due to camera sensors or problems in lighting.
# so, we smooth out the image or reduce some of that noise by applying som eblurring method
# we previously used Gaussian blur method. It is one of the most polular methods in blurring
# but in practise, you will realise that gaussian blurr doesn't suit some of your purposes. 
# Therefore ther are many blurring techniques.
# Those techniques are discussed in this part of the tutorial.

# what is kernel window in images?  
# it is a part of the whole image that is under say 'inspection'.
# Kernel size is the number of rows and number of columns. 


import cv2 as cv
import numpy as np

img = cv.imread('Photos/park.jpg')
cv.imshow('Park', img)

# Averaging
# First, Define a Kernel window.
# It will compute the avergae instensity of the middle pixel of the true center as the average of the surrounding pixel intensities. 
average = cv.blur(img, (3,3))
cv.imshow('Average Blur', average)



cv.waitKey(0)