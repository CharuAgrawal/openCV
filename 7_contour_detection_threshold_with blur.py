# contours are not the same as edges = mathematically speaking

import cv2 as cv

img = cv.imread('Photos/cats.jpg')

cv.imshow('Cats', img)


gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# #blurring to reduce contours and making function more efficient. 
# # (5,5), => lot of blur
# #  cv.BORDER_DEFAULT => body
blur = cv.GaussianBlur(gray, (5,5), cv.BORDER_DEFAULT)
# cv.imshow('Blur',blur)


# canny = cv.Canny(blur, 125, 175)
# cv.imshow('Canny Edges', canny)

# canny = structuring element, or edges of the image.
# cv.CHAIN_APPROX_NONE = countour approxiamtion method.
# contours, => is the list of all python of all teh coordinates that the contours that were found in the image. 
#  , hierarchies => is out of the scope of the course. 
# , hierarchies => hierarchial represntation of the countours.
# if you have rectangle and inside the rectange their is a square, and inside that square you have circle. 
# then this heirarchy is represnetation that openCV uses to find these contours. 
#  cv.RETR_LIST, => is a mod in which this findCountours method returns and finds the contours.
#  cv.RETR_LIST, => returns all the contours it finds in the image
#  cv.RETR_EXTERNAL,  => returns only the extrenal contours. All the ones in the outside. 
#  cv.RETR_TREE, => returns all teh heirachial countors. 
# cv.CHAIN_APPROX_NONE) => returns all of the contours. 
# Some people prefer cv.CHAIN_APPROX_SIMPLE) => compresses all the contours that are returned.
# compresses all the contours into its end points only. 
# contours, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
# print(f'{len(contours)} contour(s) found')
# found 2794 contour(s) found

# thershold looks at an image an tries to binaries that image. 
# (gray, 125, 255) => anything below 125 is zero and anything above is 255.
ret, thresh = cv.threshold(blur, 125, 255, cv.THRESH_BINARY)
cv.imshow('threshold', thresh)

contours, hierarchies = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
print(f'{len(contours)} contour(s) found')
# 149 countors found



cv.waitKey(0)