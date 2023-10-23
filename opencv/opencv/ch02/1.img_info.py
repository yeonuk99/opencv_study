import sys
import cv2

img1 = cv2.imread('cat.bmp', cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread('cat.bmp', cv2.IMREAD_COLOR)

print('type(img1): ', type(img1))
print('img1.shape: ', img1.shape)
print('img2.shape: ', img2.shape)
print('img2.dtype: ', img2.dtype)

h, w = img2.shape[:2]
print('img2 size: {} x {}'.format(w, h))

if len(img1.shape) == 2:
    print('img1 is a grayscale image')
elif len(img1.shape) == 3:
    print('img1 is a truecolor image')

img1 = cv2.imread('cat.bmp', cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread('cat.bmp', cv2.IMREAD_COLOR)

# for y in range(h):
#     for x in range(w):
#         img1[y,x] = 255
#         img2[y,x] = [0,0,255]

# img1[:,:] = 255
# img2[:,:] = (0,0,255)

img1[100:200, 10:300] = 0
img2[100:200, 100:200] = (0,0,0)



cv2.imshow("img1", img1)
cv2.imshow("img2", img2)
cv2.waitKey()

cv2.destroyAllWindows()