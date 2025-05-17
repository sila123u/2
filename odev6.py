import cv2
import numpy as np

img= cv2.imread("pyy.jpg")
olcek_yuzde = 40
genislik = int(img.shape[1] * olcek_yuzde / 100)
yukseklik = int(img.shape[0] * olcek_yuzde / 100)
boyut = (genislik, yukseklik)
resized = cv2.resize(img, boyut, interpolation=cv2.INTER_AREA)

gri = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
gri = cv2.medianBlur(gri, 5)

circles = cv2.HoughCircles(
    gri,
    cv2.HOUGH_GRADIENT,
    dp=1.2,
    minDist=95,
    param1=100,
    param2=35,
    minRadius=55,
    maxRadius=113
)

sayi = 0
if circles is not None:
    circles = np.uint16(np.around(circles))
    for (x, y, r) in circles[0, :]:
        cv2.circle(resized, (x, y), r, (0, 255, 0), 3)
        sayi += 1

cv2.putText(resized, f"Para Sayisi: {sayi}", (30, 60), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (255, 0, 0), 3)

cv2.imshow("Sonuc", resized)
cv2.waitKey(0)
cv2.destroyAllWindows()

