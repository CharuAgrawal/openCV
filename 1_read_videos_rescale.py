import cv2 as cv

capture = cv.VideoCapture('Videos/dog.mp4')

# create a function for rescaling frames
def rescaleFrame(frame, scale= 0.25): 
  width = int(frame.shape[1] *scale)
  height = int( frame.shape[0] *scale)
  dimensions =(width, height)

  return cv.resize(frame, dimensions, interpolation= cv.INTER_AREA)


while True:
    isTrue, frame  = capture.read()
    frame_resized = rescaleFrame(frame, scale=0.2)

   
    cv.imshow('Resized Video', frame_resized)
    cv.imshow('Video', frame)

    if cv.waitKey(20) &  0xFF== ord('d'):
        break

capture.release()
cv.destroyAllWindows()

