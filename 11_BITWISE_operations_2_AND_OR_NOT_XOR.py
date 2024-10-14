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


# bitwise AND ->intersecting regions
bitwise_and = cv.bitwise_and(rectangle, circle)
cv.imshow('BITWISE AND', bitwise_and)


# bitwise OR  -> non-intersecting regions and intersecting regions
# finds common region, superimpose them.
# all the white pixels in both the images are displayed as white
bitwise_or = cv.bitwise_or(rectangle, circle)
cv.imshow('BITWISE OR', bitwise_or)




# bitwise XOR
# Returning non-intersecting regions.
# for me it gives a full blank white image-> i think it is the wrong result. 
# If I do the NOT operation before XOR, then i doesn't give the right result. 
# Once I put XOR operation about NOT, it gave what it was supposed to -> non intersection regions.
# (I wonder why-> the function was run on basic rectange and circle, not as appended functions.)
bitwise_xor = cv.bitwise_xor( circle, rectangle)
cv.imshow('BITWISE XOR', bitwise_xor)

# bitwise NOT
bitwise_not = cv.bitwise_not(rectangle)
cv.imshow('BITWISE NOT', bitwise_not)

cv.waitKey(0)