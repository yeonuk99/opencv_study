import sys
import cv2

def camera_show():
    cap = cv2.VideoCapture(0) # 기본 카메라 장치 열기

    while True:
        ret, frame =cap.read() # 카메라로부터 프레임을 정상적으로 받아오면
                                #ret에는 True, frame에는 해당 프레임이 저장
        
        inversed = ~frame #현재 프레임 반전

        cv2.imshow('frame', frame)
        cv2.imshow('inversed', inversed)

        if cv2.waitKey(10) == 27:
            break
    cap. release()
    cv2.destroyAllWindows

def FPS_camera():
    cap = cv2.VideoCapture('dog.mp4')
    
    fps = round(cap.get(cv2.CAP_PROP_FPS))
    delay = round(1000/fps)

    while True:
        ret, frame = cap.read()
        print("FPS: ", fps)
        inversed = ~frame
        cv2.imshow('frame', frame)
        cv2.imshow('inversed', inversed)

        if cv2.waitKey(delay) == 27:
            break
    cap.release()
    cv2.destroyAllWindows()


#카메라와 동영상 처리하기
def video_camera():
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Camera open failed!")
        sys.exit()
    w = round(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    h = round(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = cap.get(cv2.CAP_PROP_FPS)

    fourcc = cv2.VideoWriter_fourcc(*'DIVX') # *'DIVX' == 'D', 'I', 'V', 'X'
    delay = round(1000 / fps)

    out = cv2.VideoWriter('output.avi', fourcc, fps, (w,h))

    if not out.isOpened():
        print('File open failed!')
        cap.release()
        sys.exit()

    while True:
        ret, frame = cap.read()

        if not ret:
            break
        
        cv2.imshow('frame', frame)
        

        if cv2.waitKey(delay) == 27:
            break

    cap.release()
    out.release()
    cv2.destroyAllWindows()

video_camera()