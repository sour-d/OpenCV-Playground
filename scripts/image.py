import cv2 as cv
import sys

img = cv.imread("res/nature.jpeg")

if img is None:
    sys.exit("Could not read the image.")

cv.imshow("Display window", img)
