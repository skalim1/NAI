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

    edged = cv2.Canny(gray, 10, 250)
    cv2.imshow("Edged", edged)

    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (7, 7))
    closed = cv2.morphologyEx(edged, cv2.MORPH_CLOSE, kernel)
    cv2.imshow("Closed", closed) 

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.imwrite("test.jpg", closed)

for c in cnts:
	peri = cv2.arcLength(c, True)
	approx = cv2.approxPolyDP(c, 0.02 * peri, True)

	if len(approx) == 4:
		cv2.drawContours(image, [approx], -1, (0, 255, 0), 4)
		total += 1

if total == 0:
        print "Nie znaleziono ksiazki"
if total != 0:
        print "Znaleiono ksiazki - {0} ".format(total)

cv2.imshow("Output", image)

cv2.waitKey(0)
cap.release()
cv2.destroyAllWindows()