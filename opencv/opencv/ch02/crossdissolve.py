import sys
import numpy as np
import cv2

# 두 개의 동영상을 열어서 cap1, cap2로 지정
cap1 = cv2.VideoCapture("video1.mp4")
cap2 = cv2.VideoCapture("video2.mp4")

if not cap1.isOpened() or not cap2.isOpened():
    print("video open failed!")
    sys.exit()

# 두 동영상의 크기, FPS는 같다고 가정함
frame_cnt1 = round(cap1.get(cv2.CAP_PROP_FRAME_COUNT))
frame_cnt2 = round(cap2.get(cv2.CAP_PROP_FRAME_COUNT))
fps = cap1.get(cv2.CAP_PROP_FPS)
effect_frames = int(fps * 2)

print("frame_cnt1:", frame_cnt1)
print("frame_cnt2:", frame_cnt2)
print("FPS:", fps)

fps2 = cap2.get(cv2.CAP_PROP_FPS)
print("fps2:", fps2)

delay = int(1000 / fps)
print("delay:", delay)

w = round(cap1.get(cv2.CAP_PROP_FRAME_WIDTH))
h = round(cap1.get(cv2.CAP_PROP_FRAME_HEIGHT))
fourcc = cv2.VideoWriter_fourcc(*"DIVX")

# 출력 동영상 객체 생성
out = cv2.VideoWriter("output.avi", fourcc, fps, (w, h))

# 회전 각도 초기화
angle = 0

# 전환 구간에서만 회전 적용
for i in range(frame_cnt1 - effect_frames):
    ret1, frame1 = cap1.read()

    if not ret1:
        print("frame read error!")
        sys.exit()

    out.write(frame1)
    print(".", end="")

    if i >= frame_cnt1 - effect_frames:
        angle += 1  # 회전 각도 증가 (예시로 1도씩 증가)
        if angle > 360:
            angle = 0

        # 회전 변환 행렬 생성
        M = cv2.getRotationMatrix2D((w / 2, h / 2), angle, 1)
        frame1 = cv2.warpAffine(frame1, M, (w, h))

    cv2.imshow("output", frame1)
    cv2.waitKey(delay)

# 1번 동영상 뒷부분과 2번 동영상 앞부분을 회전 전환 합성
for i in range(effect_frames):
    ret1, frame1 = cap1.read()
    ret2, frame2 = cap2.read()

    if not ret1 or not ret2:
        print("frame read error!")
        sys.exit()
    
    while True:
        angle += 1  # 회전 각도 증가 (예시로 1도씩 증가)
        
        # 회전 변환 행렬 생성
        M = cv2.getRotationMatrix2D((w / 2, h / 2), angle, 1)
        frame1 = cv2.warpAffine(frame1, M, (w, h))
        frame2 = cv2.warpAffine(frame2, M, (w, h))

        alpha = i / effect_frames
        frame = cv2.addWeighted(frame1, 1 - alpha, frame2, alpha, 0)

        out.write(frame)
        print(".", end="")

        cv2.imshow("output", frame)
        cv2.waitKey(delay)
        

    

# 2번 동영상을 복사
for i in range(effect_frames, frame_cnt2):
    ret2, frame2 = cap2.read()

    if not ret2:
        print("frame read error!")
        sys.exit()

    

    # 회전 변환 행렬 생성
    M = cv2.getRotationMatrix2D((w / 2, h / 2), angle, 1)
    frame2 = cv2.warpAffine(frame2, M, (w, h))

    out.write(frame2)
    print(".", end="")

    cv2.imshow("output", frame2)
    cv2.waitKey(delay)

print("\noutput.avi file is successfully generated!")

cap1.release()
cap2.release()
out.release()
cv2.destroyAllWindows()