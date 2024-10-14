import cv2 as cv

img = cv.imread('Photos/cat_large.jpg')
cv.imshow('Cat', img)

# create a function for rescaling frames
def rescaleFrame(frame, scale= 0.75): 
  width = int(frame.shape[1] *scale)
  height = int( frame.shape[0] *scale)
  dimensions =(width, height)

  return cv.resize(frame, dimensions, interpolation= cv.INTER_AREA)

resized_img = rescaleFrame(img, scale=0.1)
cv.imshow('Resized Cat', resized_img)

cv.waitKey(0)
