import cv2
import numpy as np
#BGR
#B:255,0,0
#G:0,255,0
#R:0,0,255
Blons = cv2.imread("download-blons.jpeg")

#blons = cv2.ellipse(Blons,(256,256),(100,50),0,0,180,255,-1)
Blon = cv2.rectangle(Blons, (100, 70), (150, 500), (0, 0, 255), -1)
Blon2 = cv2.rectangle(Blons, (125, 50), (130,70), (0, 0, 0), -1)
Blon3 = cv2.ellipse(Blons,(130, 40), (10, 20),0, 0, 360, (5, 155, 255), -1)
cv2.imshow("blonscandle", Blon)
cv2.waitKey(0)
cv2.destroyAllWindows()
