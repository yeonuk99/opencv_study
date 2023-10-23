import numpy as np
import cv2

# #영상의 생성 예제 코드
# img1 = np.empty((480, 640), dtype = np.uint8)
# img2 = np.zeros((480, 640, 3), dtype = np.uint8)
# img3 = np.ones((480, 640), dtype = np.uint8) * 255
# img4 = np.full((480, 640, 3), (0,255,255), dtype = np.uint8)

# cv2.imshow('img1', img1)
# cv2.imshow('img2', img2)
# cv2.imshow('img3', img3)
# cv2.imshow('img4', img4)
# cv2.waitKey()
# cv2.destroyAllWindows()

img1 = cv2.imread('HappyFish.jpg')


img2 = img1[40:120, 30:150]
img3 = img1[40:120, 30:150].copy()

img1.fill(0)
cv2.imshow('img1', img1)
cv2.imshow('img2', img2)
cv2.imshow('img3', img3)
cv2.waitKey()
cv2.destroyAllWindows()