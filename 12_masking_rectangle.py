# using bitwise operations to obtain masking.

import cv2 as cv
import numpy as np

img = cv.imread('Photos/cats 2.jpg')
cv.imshow('Cats', img)

# the size of blank should be the same size as that of the image
# else it won't work. 
blank = np.zeros(img.shape[:2], dtype = 'uint8')
cv.imshow('Blank', blank)


mask = cv.rectangle(blank, (img.shape[1]//2 -50, img.shape[0]//2 -50 ), (img.shape[1]//2 + 90, img.shape[0]//2 + 90), 255, -1)
cv.imshow('Mask', mask)

masked_image = cv.bitwise_and(img, img, mask = mask)
cv.imshow('Masked Image', masked_image)


cv.waitKey(0)