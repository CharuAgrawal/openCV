import cv2 as cv

# capture = cv.VideoCapture(0) # for camera or webcam connected to your computer # zero for inbuilt camera
# capture = cv.VideoCapture(1) # first camera conected to your computer
# capture = cv.VideoCapture(2) # second camera connected to your computer and so on.. 
capture = cv.VideoCapture('Videos/kitten.mp4')
#capture is instance of VideoCapture class.



while True:
    isTrue, frame  = capture.read()
    cv.imshow('Video', frame)

    if cv.waitKey(20) &  0xFF== ord('d'):
        break

capture.release()
cv.destroyAllWindows()

