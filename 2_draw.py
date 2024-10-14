import cv2 as cv
import numpy  as np

img = cv.imread('Photos/cat.jpg')

#to create a blank image #dtype is datatype of uint8
blank = np.zeros((500,500,3), dtype='uint8')
#500,500,3= height,width, number of color channels

# 1. to paint the image in a color
# blank[: :] = 255,0,0 #BGR
# cv.imshow('Green', blank)

# to paint through a range creating a box
# blank[: :] = 255,255,255 #BGR
# blank[200:300, 300:400] = 0,255,0 #BGR
# cv.imshow('box', blank)

# 2. Draw a rectangle
# cv.rectangle(blank, (0,0), (250,250), (0,255,0), thickness=2)
# cv.imshow('rectangle', blank)

# draw a filled rectangle
blank[: :] = 255,255,255 #BGR
# cv.rectangle(blank, (250,250), (300,300), (0,0,255), thickness=cv.FILLED)
# cv.rectangle(blank, (250,250), (300,300), (0,0,255), thickness=-1)
# cv.rectangle(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2), (0,0,255), thickness=-1)
# cv.imshow('rectangle', blank)

# 3. Draw a circle
# cv.circle(blank, (250,250), 50, (0,255,255), thickness=2)
# cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 50, (0,255,255), thickness=2)
# cv.imshow('Circle', blank)

# 4. Draw a line
# cv.line(blank, (30, 50), (50, 100), (0,255,0), thickness=5)
# cv.imshow('Line', blank)

# 5. Write Text on image
cv.putText(img, 'Hello', (225, 225), cv.FONT_HERSHEY_TRIPLEX , 1.0, (0,255,0), 2)
cv.imshow('Text', img)


cv.waitKey(0)
