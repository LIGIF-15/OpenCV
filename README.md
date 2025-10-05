import cv2
import numpy as np

#C2 = cv2.imread("download-blons.jpeg")
C2 = np.zeros((300, 400, 3), np.uint8)
point = np. array([[100, 200], [50, 50], [300, 100]])
cv2.fillPoly(C2, pts = [point], color = (0, 255, 0))
points = np. array([[250, 200], [200, 50], [30, 130]])
cv2.fillPoly(C2, pts = [points], color = (0, 255, 0))
#Test =
#S =
#T =
#A =
#R =
#s =
cv2.imshow("challenge2", C2)
cv2.waitKey(0)
cv2.destroyAllWindows()
