import numpy as np
import cv2 

cap = cv2.VideoCapture(0)

while(True):
    # Pobranie klatki z kamerki
    ret, frame = cap.read()

    # Wyświetlenie klatki z kamerki
#    cv2.imshow("image", frame)

    # Konwersja przestrzeni barw do skali szarosci oraz zmiana wielkosci obrazu
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (3, 3), 0)
    small = cv2.resize(gray, (0, 0), fx=0.5, fy=0.5)

    # Wyświetlenie przekonwertowanej klatki
    cv2.imshow('frame', gray)

    # Wykrywanie krawedzi (usuniecie szumu-filtr Gausa, wygładzenie, maksimum lokalne)
    edged = cv2.Canny(gray, 10, 250)
#    cv2.imshow("Edged", edged)

    # Zamkniecie luk pomiedzy bialymi pikselami
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (7, 7))
    closed = cv2.morphologyEx(edged, cv2.MORPH_CLOSE, kernel)
#    cv2.imshow("Closed", closed) 

    # Oczkiwanie przez 1 sekunde na nacisniecie przycisku, zakonczenie petli jeseli przyciskiem jest "q"
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Zapisanie finalnej klatki do pliku
cv2.imwrite("test.jpg", closed)
image = cv2.imread("test.jpg")

# Znalezienie konturow i zainicjowanie licznika ksiazek
(d, cnts, _) = cv2.findContours(closed.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
total = 0

# Aproksymacja dla konturów
for c in cnts:
	peri = cv2.arcLength(c, True)
	approx = cv2.approxPolyDP(c, 0.02 * peri, True)

    # Wskazanie ksiazki jak liczba katow jest rowna 4
	if len(approx) == 4:
		cv2.drawContours(image, [approx], -1, (0, 255, 0), 4)
		total += 1

# Wyswietlenie wyniku liczenia
if total == 0:
        print "Nie znaleziono ksiazki"
if total != 0:
        print "Znaleiono ksiazki - {0} ".format(total)

# Wyswietlenie klatki z zaznaczonymi konturami ksiazki
cv2.imshow("Output", image)

# Zwolnienie zasobow kmerki, wylaczenie wszystkich okienek
cv2.waitKey(0)
cap.release()
cv2.destroyAllWindows()