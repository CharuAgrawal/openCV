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



mask= cv.circle(blank, (img.shape[1]//2, img.shape[0]//2), 100, 255, -1)
masked = cv.bitwise_and(img, img, mask=mask)
cv.imshow('Masked Image', masked)

# compute grayscale histogram 
colors =('b', 'g', 'r')
plt.figure()
plt.title('Color Histogram')
plt.xlabel('Bins')
plt.ylabel(' # pixels')
for i, col in enumerate(colors):
    hist = cv.calcHist([img], [i], mask, [256], [0, 256])
    plt.plot(hist, color= col)
    plt.xlim([0, 256])

# rgb_hist = cv.calcHist([img], [0], mask , [256], [0,256])
# plt.plot(rgb_hist)
# plt.xlim([0,256])
plt.show()

cv.waitKey(0)