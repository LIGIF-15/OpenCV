import cv2
import numpy as np

# ADDIION

image1 = cv2.imread('download-DDT.jpeg')
image2 = cv2.imread('download-DDT.jpeg')

image2 = cv2.flip(image1,1)

weightedSum = cv2.addWeighted(image1, 0.7, image2, 0.3, 0)

cv2.imshow('Weighted Image', weightedSum)

cv2.waitKey(0)
cv2.destroyAllWindows()

# SUBTRACTION

#image1 = cv2.imread('BTD6-3D-DDT.webp')
#image2 = cv2.imread('030-BombShooter.webp')

image1 = cv2.imread('BTD6-3D-DDT.webp')
image2 = cv2.imread('bfb-ctq4oz5iz4nd1.webp')

sub = cv2.subtract(image1, image2)

cv2.imshow('Subtracted Image', sub)

cv2.waitKey(0)
cv2.destroyAllWindows()

# IMAGE RESIZING

img = cv2.imread("030-BombShooter.webp", 1)
cv2.imshow("Original Image", img)

resized = cv2.resize(img, (545, 545))
cv2.imshow("resizedImage", resized)

cv2.waitKey(0)
cv2.destroyAllWindows()

# EROSION

image = cv2.imread("bfb-ctq4oz5iz4nd1.webp", 1)

kernal = np.ones((5, 5), np.uint8)

image = cv2.erode(image, kernal)
cv2.imshow("Eroded Image", image)

cv2.waitKey(0)
cv2.destroyAllWindows()

# ROTATION

img = cv2.imread("download-phayze-elite.jpeg")
(rows, cols) = img.shape[:2]
M = cv2.getRotationMatrix2D((cols / 2, rows/ 2), 135, 1)
res = cv2.warpAffine(img, M, (cols, rows))
# cv2.imwrite('result.jpg, res)
 cv2.imshow('result', res)

cv2.waitKey(0)
cv2.destroyAllWindows()
