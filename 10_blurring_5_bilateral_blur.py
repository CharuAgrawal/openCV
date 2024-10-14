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

# Median
# to remove salt and pepper noise in the image.
# people use this in advanced computer vision projects
# that tend to depend on the reduction of substantial amount of noise.
# instead of avergaes, it takes median.
median = cv.medianBlur(img, 7) # openCV assumes that the kernel size will be 3*3 matrix.
cv.imshow('Median BLur', median)

# Bilateral blurring
# applies blurring but retains the edges.
# 
bilateral= cv.bilateralFilter(img, 5, 15, 15)
bilateral= cv.bilateralFilter(img, 10, 15, 15) #not much changes
bilateral= cv.bilateralFilter(img, 10, 15, 35) #larger values, makes it start looking more towards median blur, like a smudged painting of the original picture.
# so becareful while using higher values(above or in kernel size) to reduce noise. You will end with smudges oil paintings.  
cv.imshow('Bilateral Blur', bilateral)


cv.waitKey(0)