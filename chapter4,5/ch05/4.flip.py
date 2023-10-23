import cv2


img = cv2.imread('cat.bmp', cv2.IMREAD_COLOR)

img_left_right = cv2.flip(img, 1, dst = None)

img_up_down = cv2.flip(img, 0, dst = None)

img_all = cv2.flip(img, -1, dst = None)


cv2.imshow('image', img)
cv2.imshow('left, right', img_left_right)
cv2.imshow('up, down', img_up_down)
cv2.imshow('all', img_all)
cv2.waitKey()
cv2.destroyAllWindows()