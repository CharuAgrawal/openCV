# OpenCV reads color in BGR format.
# Outside OpenCV, we use RGB format. 


# color space are space of colors.
# A systemn of representing an array of pixel color. 
# RGB, grayscale, HSV, lab, etc etc..
import cv2 as cv
import matplotlib.pyplot as plt 
# import matplotlib.pyplot as plt

img = cv.imread('Photos/park.jpg')
cv.imshow('Park', img)
plt.imshow(img)

rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow('RGB', rgb)
plt.imshow(rgb)
plt.show()

cv.waitKey(0)
