# https://www.geeksforgeeks.org/python-bilateral-filtering/
import cv2 as cv

# Read the image. 
img = cv.imread('Photos/taj.jpg') 
cv.imshow('Noisy Image', img)
# Apply bilateral filter with d = 15, 
# sigmaColor = sigmaSpace = 75. 
bilateral = cv.bilateralFilter(img, 15, 75, 75) 

# Save the output. 
# cv2.imwrite('taj_bilateral.jpg', bilateral) 
cv.imshow('Bilateral Blur', bilateral)

cv.waitKey(0)