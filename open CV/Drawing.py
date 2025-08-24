import cv2
import numpy as np

Tinkerton = cv2.imread("download-Tinkerton.jpeg")

#start_point = (0, 0)
#end_point = (250, 250)
#red
#color = (0, 0, 255)
#thickness = 9

#Secret = cv2.line(Tinkerton, start_point, end_point, color, thickness)
#cv2.imshow("secret", Tinkerton)
#cv2.waitKey(0)
#cv2.destroyAllWindows()


# CIRCLE

#Secret = cv2.circle(Tinkerton, center_coordinates, radius, color, thickness)

#cv2.imshow("secret", Tinkerton)
#cv2.waitKey(0)
#cv2.destroyAllWindows()

# TEXT
image = cv2.imread("result.jpg")
font = cv2.FONT_HERSHEY_COMPLEX_SMALL
org = (50, 50)
fontscale = 1
# green
color = (0, 255, 0)
thickness = 2
BTD = cv2.putText(image, 'NAPSFRILLS', org, font, fontscale, color, thickness, cv2.LINE_AA)

cv2.imshow("BTD", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# SMILE CHALLENGE
smilebg = cv2.imread("download-Quad.jpeg")
# eye 1
CC = (70, 50)
rad = 25
colour = (0, 0, 255)
thickness = 2
smile = cv2.circle(smilebg, CC, rad, colour, thickness)
# eye 2
CC2 = (205, 50)
smile = cv2.circle(smilebg, CC2, rad, colour, thickness)
# mouth
CC3 = (140, 100)
start_angle = 0
end_angle = 180
rad2 = (50, 50)
angle = 0
smile = cv2.ellipse(smilebg, CC3, rad2, angle, start_angle, end_angle, colour, thickness)
cv2.imshow("smile", smile)
cv2.waitKey(0)
cv2.destroyAllWindows
