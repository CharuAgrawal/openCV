# Histograms allow you to visualise the distribution of pixel intensities in an image.
# You can have histograms for color images, grayscale images, or whatever. 
# It is graph/plot that will give you a high level intuition of pixel distribution in the image.

# Let's compute histograms for grayscale images and RGB images. 

import cv2 as cv
import matplotlib.pyplot as plt


img = cv.imread('Photos/cats 2.jpg')
cv.imshow('Cats', img)


gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# compute grayscale histogram 
gray_hist = cv.calcHist([gray], [0], None, [256], [0,256])
plt.figure()
plt.title('Grayscale Histogram')
plt.xlabel('Bins')
plt.ylabel(' # pixels')
plt.plot(gray_hist)
plt.xlim([0,256])
plt.show()

cv.waitKey(0)