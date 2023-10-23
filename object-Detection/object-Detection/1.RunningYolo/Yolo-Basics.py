from ultralytics import YOLO
import cv2

# 8K라서 resize필요
src = cv2.imread("C:\\python\\object-Detection\\object-Detection\\1.RunningYolo\\Images\\child_man.jpg")
src = cv2.resize(src, (640, 1024), interpolation=cv2.INTER_AREA)

model = YOLO("../Yolo-Weights/yolov8n.pt")
results = model(src, show=True)
cv2.waitKey(0)
