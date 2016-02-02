import cv2 
import numpy as np

cap = cv2.VideoCapture(0)

while(True):
    ret, frame = cap.read()

    cv2.imshow("image", frame)

    gray = cv2.cvtColor(frame, cv2.COLOR_BGRq2GRAY)
#    gray = cv2.GaussianBlur(gray, (3, 3), 0)
    small = cv2.resize(gray, (0, 0), fx=0.5, fy=0.5)

    cv2.imshow('frame', gray)