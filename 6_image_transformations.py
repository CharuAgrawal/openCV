import cv2 as cv
import numpy as np

img = cv.imread('Photos/lady.jpg')

cv.imshow('Lady', img)

# Translation: shifting the image along x and y axis
 # up down, left right, with any combination of the above. 

def translate(img, x, y):
    transMat = np.float32([[1,0,x],[0,1,y]]) 
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMat, dimensions)

# -x --> Left
# -y --> Up
# x --> Right
# y --> Down

translated = translate(img,-40, -100)
cv.imshow('Translated', translated)


def rotate(img, angle, rotPoint= None):
    (height, width ) = img.shape[:2]

    if rotPoint is None:
        rotPoint = (width//2, height//2) #rotate from the centre
    rotMat= cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions= (width, height)

    return cv.warpAffine(img, rotMat, dimensions)


rotated = rotate(img, 45)
# to rotate the image clockwise: -45
cv.imshow('Rotated', rotated)

# one can also rotate a rotated image.
rotated_rotated = rotate(rotated, 45)
# to rotate the image clockwise: -45
cv.imshow('Rotated_rotated', rotated_rotated)




cv.waitKey(0)