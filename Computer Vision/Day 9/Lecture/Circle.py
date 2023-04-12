import numpy as np
import matplotlib.pyplot as plt
import cv2

# Q2- make trackbar to control line position ,color and thickness in image 500*500 rgb.
img = np.zeros((300,300,3), np.uint8)
cv2.namedWindow('Image')

def Nothing(x):
    pass

cv2.createTrackbar("X", 'Image', 0, img.shape[0]-1, Nothing)
cv2.createTrackbar("y", 'Image', 0, img.shape[1]-1, Nothing)

cv2.createTrackbar("Radius", 'Image', 0, img.shape[0]-1, Nothing)
cv2.createTrackbar("Thickness", 'Image', 0, 20, Nothing)

# cv2.createTrackbar("Angle", 'Image', 1, 10, Nothing)

while True:

    img = np.zeros((300,300,3), np.uint8)

    x = cv2.getTrackbarPos("X", 'Image')
    y = cv2.getTrackbarPos("y", 'Image')
    
    r = cv2.getTrackbarPos("Radius", 'Image')
    t = cv2.getTrackbarPos("Thickness", 'Image')

    # angle = cv2.getTrackbarPos("Angle", 'Image')

    cv2.circle(img, (x,y), r, (0,0,255), t)
    # cv2.line(img, p1, p2, color, thick)

    cv2.imshow('Image', img)
    k = cv2.waitKey(1)
    if k == ord('q'):
        break

print('Destroying....')
cv2.destroyAllWindows()
