#splitting and merging color channels 

import cv2 as cv
import numpy as np

img = cv.imread('Photos/park.jpg')
cv.imshow('Park', img)

blank = np.zeros(img.shape[:2], dtype ='uint8')

b, g, r = cv.split(img)

blue = cv.merge([b, blank, blank])
green = cv.merge([blank, g, blank])
red = cv.merge([blank, blank, r])


cv.imshow('Blue', blue)
cv.imshow('Green', green)
cv.imshow('Red', red)
# These are depicted and siplayed as grayscale images
# that show the distribution of pixel intensities.

# in the blue image, the places where there is more white (grayscale), 
# there is more blue color. 


print(img.shape) #(427, 640, 3)
print(b.shape) #(427, 640) because shape of the component is 1. Grayscale images also have a shape of 1. 
print(g.shape) #(427, 640)
print(r.shape) #(427, 640)


cv.waitKey(0)