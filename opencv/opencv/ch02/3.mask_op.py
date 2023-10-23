import sys
import cv2
import numpy as np

# 마스크 영상을 이용한 영상 합성
def Plus_image():
    src = cv2.imread('airplane.bmp', cv2.IMREAD_COLOR)
    mask = cv2.imread('mask_plane.bmp', cv2.IMREAD_GRAYSCALE)
    dst = cv2.imread('sky2.jpg', cv2.IMREAD_COLOR)

    if src is None or mask is None or dst is None:
        print('Image laod failed!')
        sys.exit()

    cv2.copyTo(src, mask, dst)
    dst[mask > 0] = src[mask > 0]
    cv2.imshow('src',src)
    cv2.imshow('dst', dst)
    cv2.imshow('mask', mask)
    cv2.waitKey()
    cv2.destroyAllWindows()

# 알파 채널을 마스크 영상으로 이용
def alpha_mask():
    
    src = cv2.imread("cat.bmp", cv2.IMREAD_COLOR)
    logo = cv2.imread("opencv-logo-white.png", cv2.IMREAD_UNCHANGED)

    if src is None or logo is None:
        print("Image load failed!")
        sys.exit()

    mask = logo[:, :, 3]  # mask는 알파 채널로 만든 마스크 영상
    logo = logo[:, :, :-1]  # logo는 b, g, r 3채널로 구성된 컬러 영상
    h, w = mask.shape[:2]
    crop = src[10 : 10 + h, 10 : 10 + w]  # logo, mask와 같은 크기의 부분 영상 추출

    cv2.copyTo(logo, mask, crop)
    # crop[mask > 0] = logo[mask > 0]

    cv2.imshow("src", src)
    cv2.imshow("logo", logo)
    cv2.imshow("mask", mask)
    cv2.waitKey()
    cv2.destroyAllWindows()


def alpha_mask1():
    src = cv2.imread("cat.bmp", cv2.IMREAD_COLOR)
    logo = cv2.imread("opencv-logo-white.png", cv2.IMREAD_UNCHANGED)

    if src is None or logo is None:
        print("Image load failed!")
        sys.exit()
    
    mask = logo[:, :, 3]    #mask는 알파 채널로 만든 마스크 영상
    logo = logo[:, :, :-1]   # logo는 b,g,r 3채널로 만든 마스크 영상
    h, w = mask.shape[:2]
    crop = src[10 : 10 + h, 10 : 10 + w] #logo, mask와 같은 크기의 부분 영상 추출

    cv2.copyTo(logo, mask, crop)
    #crop[mask > 0] = logo[mask > 0]

    cv2.imshow("src", src)
    cv2.imshow("logo", logo)
    cv2.imshow("mask", mask)
    cv2.waitKey()
    cv2.destroyAllWindows()


def Draw_shape():
    img = np.full((400, 400, 3), 255, np.uint8)

    cv2.line(img, (50, 50), (200, 50), (0, 0, 255), 5)
    cv2.line(img, (50, 60), (150, 160), (0, 0, 128))

    cv2.rectangle(img, (50, 200, 150, 100), (0, 255, 255), 2)
    cv2.rectangle(img, (70, 220), (180, 280), (0, 128, 0), -1)

    cv2.circle(img, (300, 100), 30, (255, 255, 0), -1, cv2.LINE_AA)
    cv2.circle(img, (300, 100), 60, (255, 0, 0), 3, cv2.LINE_AA)

    pts = np.array([[250, 200], [300, 200], [350, 300], [250, 300]])
    cv2.polylines(img, [pts], True, (255, 0, 255), 2)

    text = 'Hello? OpenCV' + cv2.__version__
    cv2.putText(img, text, (50, 350), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 1, cv2.LINE_AA)

    cv2.imshow("img", img)
    cv2.waitKey()
    cv2.destroyAllWindows()

Draw_shape()
