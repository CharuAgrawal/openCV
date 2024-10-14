# Four basic BITWISE operators:
# AND, OR, NOT and XOR.
# They are used a lot in image processing
# especially when masks.
# Basically binary operations on pixels. 
# Pixels are turned off, it has a value of Zero.
# turned on, if it has value of one.


import cv2 as cv
import numpy as np

blank = np.zeros((400, 400), dtype='uint8')
# A basis to draw a rectangle and a circle

rectangle = cv.rectangle(blank.copy(), (30,30), (370, 370), 255, -1)
circle = cv.circle(blank.copy(), (200,200), 200, 255, -1)

cv.imshow('Rectangle', rectangle)
cv.imshow('Circle', circle)


cv.waitKey(0)