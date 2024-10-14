# Histograms allow you to visualise the distribution of pixel intensities in an image.
# You can have histograms for color images, grayscale images, or whatever. 
# It is graph/plot that will give you a high level intuition of pixel distribution in the image.

# Let's compute histograms for grayscale images and RGB images. 

import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

img = cv.imread('Photos/cats.jpg')
cv.imshow('Cats', img)

blank = np.zeros(img.shape[:2], dtype = 'uint8')

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

circle= cv.circle(blank, (img.shape[1]//2, img.shape[0]//2), 100, 255, -1)
mask = cv.bitwise_and(gray, gray, mask=circle)
cv.imshow('Mask', mask)

# compute grayscale histogram 
gray_hist = cv.calcHist([gray], [0], mask , [256], [0,256])
plt.figure()
plt.title('Grayscale Histogram')
plt.xlabel('Bins')
plt.ylabel(' # pixels')
plt.plot(gray_hist)
plt.xlim([0,256])
plt.show()

cv.waitKey(0)