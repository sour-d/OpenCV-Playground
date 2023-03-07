import cv2 as cv
import sys

isDrawing = False


def CreateDrawingHandler(img):
  def DrawingHandler(event, x, y, flags, param):
    global isDrawing
    print(event, isDrawing)
    if event == cv.EVENT_LBUTTONDOWN:
      isDrawing = True
    if event == cv.EVENT_LBUTTONUP:
      isDrawing = False
      return
    if event == cv.EVENT_MOUSEMOVE and isDrawing:
      cv.circle(img, (x, y), 5, (0, 255, 68), -1)
    cv.imshow("Draw", img)

  return DrawingHandler


def Draw(img):
  cv.namedWindow("Draw", cv.WINDOW_AUTOSIZE)
  cv.imshow("Draw", img)
  cv.setMouseCallback("Draw", CreateDrawingHandler(img))
  while True:
    key = cv.waitKey(1)
    if key == ord('s'):
      cv.imwrite("out/output.png", img)
      break
    if key == ord('q'):
      break


def CaptureImageToDraw():
  key = ""
  cam = cv.VideoCapture(0)
  while True:
    ret, frame = cam.read()
    frame = cv.flip(frame, 1)
    img = frame.copy()

    text = "Press \"D\" to capture and draw"
    font = cv.FONT_HERSHEY_SIMPLEX
    frame = cv.putText(frame, text, (0, 50), font, 1, (0, 255, 0), 2)
    cv.imshow("Capture Image to Draw", frame)

    key = cv.waitKey(1)
    if key != -1:
      cam.release()
      break

  if key == ord('d'):
    Draw(img)


CaptureImageToDraw()
