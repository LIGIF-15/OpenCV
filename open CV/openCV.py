import cv2

img = cv2.imread("download-cubism.jpeg", cv2.IMREAD_COLOR)

cv2.imshow("._.", img)

cv2.waitKey(0)

cv2.destroyAllwindows()
