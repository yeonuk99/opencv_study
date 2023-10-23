from ultralytics import YOLO
import cv2
import cvzone
import math
import time


cap = cv2.VideoCapture("../Videos/motorbikes.mp4")  # For Video
# cap = cv2.VideoCapture(cv2.CAP_DSHOW + 0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
model = YOLO("../Yolo-Weights/yolov8n.pt")

# 80개
classNames = [
    "person",
    "bicycle",
    "car",
    "motorbike",
    "aeroplane",
    "bus",
    "train",
    "truck",
    "boat",
    "traffic light",
    "fire hydrant",
    "stop sign",
    "parking meter",
    "bench",
    "bird",
    "cat",
    "dog",
    "horse",
    "sheep",
    "cow",
    "elephant",
    "bear",
    "zebra",
    "giraffe",
    "backpack",
    "umbrella",
    "handbag",
    "tie",
    "suitcase",
    "frisbee",
    "skis",
    "snowboard",
    "sports ball",
    "kite",
    "baseball bat",
    "baseball glove",
    "skateboard",
    "surfboard",
    "tennis racket",
    "bottle",
    "wine glass",
    "cup",
    "fork",
    "knife",
    "spoon",
    "bowl",
    "banana",
    "apple",
    "sandwich",
    "orange",
    "broccoli",
    "carrot",
    "hot dog",
    "pizza",
    "donut",
    "cake",
    "chair",
    "sofa",
    "pottedplant",
    "bed",
    "diningtable",
    "toilet",
    "tvmonitor",
    "laptop",
    "mouse",
    "remote",
    "keyboard",
    "cell phone",
    "microwave",
    "oven",
    "toaster",
    "sink",
    "refrigerator",
    "book",
    "clock",
    "vase",
    "scissors",
    "teddy bear",
    "hair drier",
    "toothbrush",
]

while True:
    success, img = cap.read()
    results = model(img, stream=True)
    for r in results:
        boxes = r.boxes
        for box in boxes:
        # Bounding Box
            x1, y1, x2, y2 = box.xyxy[0] 
            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
            w, h = x2 - x1, y2 - y1
        
        
        conf = math.ceil((box.conf[0] * 100)) / 100 # Confidence
        
        if conf >= 0.5:
            cvzone.cornerRect(img, (x1, y1, w, h))
            cls = int(box.cls[0]) # Class Name
            cvzone.putTextRect(
                img,
                f"{classNames[cls]} {conf}",
                (max(0, x1), max(35, y1)),
                scale=1,
                thickness=1,
            )
    cv2.imshow("Image", img)
    cv2.waitKey(1)