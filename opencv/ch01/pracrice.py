import cv2
import numpy as np

image = cv2.imread('change_face.jpg', cv2.IMREAD_COLOR)


print(image.dtype)

img = np.zeros((500, 500), dtype=np.uint8)
img[:, 0:400] = 255


cv2.imshow("img1", img)

cv2.waitKey(0)
cv2.destroyAllWindows()

logo = cv2.imread("change_face.jpg", cv2.IMREAD_UNCHANGED) # 알파채널 포함한 png
print("logo shape: ", logo.shape[])