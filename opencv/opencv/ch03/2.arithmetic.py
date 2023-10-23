import sys
import numpy as np
import cv2
from matplotlib import pyplot as plt

# 가중치 합
def Add_Weighted():
    src1 = cv2.imread('cropland.png', cv2.IMREAD_GRAYSCALE)
    src2 = cv2.imread('Hawkes.jpg', cv2.IMREAD_GRAYSCALE)

    if src1 is None or src2 is None:
        print("fail")


    dst = cv2.addWeighted(src1, 0.5, src2, 0.5, 0, dst = None, dtype = None)

    cv2.imshow('dst', dst)
    cv2.waitKey()


# 영상의 산술 연산
def Add_Sub():
    src1 = cv2.imread('lenna256.bmp', cv2.IMREAD_GRAYSCALE)
    src2 = cv2.imread('square.bmp', cv2.IMREAD_GRAYSCALE)

    if src1 is None or src2 is None:
        print('Image load falied!')
        sys.exit()

    dst1 = cv2.add(src1, src2, dtype = cv2.CV_8U)
    dst2 = cv2.addWeighted(src1, 0.5, src2, 0.5, 0.0)
    dst3 = cv2.subtract(src1, src2)
    dst4 = cv2.absdiff(src1, src2)

    plt.subplot(231), plt.axis('off'), plt.imshow(src1, 'gray'), plt.title('src1')
    plt.subplot(232), plt.axis('off'), plt.imshow(src2, 'gray'), plt.title('src2')
    plt.subplot(233), plt.axis('off'), plt.imshow(dst1, 'gray'), plt.title('add')
    plt.subplot(234), plt.axis('off'), plt.imshow(dst2, 'gray'), plt.title('addWeighted')
    plt.subplot(235), plt.axis('off'), plt.imshow(dst3, 'gray'), plt.title('subtract')
    plt.subplot(236), plt.axis('off'), plt.imshow(dst4, 'gray'), plt.title('absdiff')
    plt.show()

Add_Sub()