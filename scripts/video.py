import numpy as np
import cv2 as cv
out = cv.VideoWriter('out/output.avi', cv.VideoWriter_fourcc(
    *'XVID'), 60.0, (1080,  720))
cap = cv.VideoCapture(0)
if not cap.isOpened():
    print("Cannot open camera")
    exit()
while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    # if frame is read correctly ret is True
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    # Our operations on the frame come here
    gray = cv.cvtColor(frame, cv.COLOR_RGB2GRAY)
    # Display the resulting frame
    cv.imshow('frame', gray)
    out.write(gray)
    if cv.waitKey(1) == ord('q'):
        break
# When everything done, release the capture
out.release()
cap.release()
cv.destroyAllWindows()
