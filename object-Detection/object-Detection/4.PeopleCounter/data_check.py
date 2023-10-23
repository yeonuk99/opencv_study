from ultralytics import YOLO
import cv2
import cvzone
import math
import time
import numpy as np
from sort import *

cap = cv2.VideoCapture("C:\\python\\object-Detection\\object-Detection\\Videos\\people.mp4")  # For Video
# cap = cv2.VideoCapture(cv2.CAP_DSHOW + 0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
model = YOLO("../Yolo-Weights/yolov8n.pt")
mask = cv2.imread("C:\\python\\object-Detection\\object-Detection\\4.PeopleCounter\\mask.png")

# Tracking
tracker = Sort(max_age=20, min_hits=3, iou_threshold=0.3)

limits_up = [130, 300, 380, 300]
limits_down = [550, 450, 750, 450]

totalCount_up = []
totalCount_down = []

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

    if not success:
        break

    #results = model(img, stream=True)
    imgRegion = cv2.bitwise_and(img, mask)

    imgGraphics = cv2.imread("C:\\python\\object-Detection\\object-Detection\\4.PeopleCounter\\graphics.png", cv2.IMREAD_UNCHANGED)
    img = cvzone.overlayPNG(img, imgGraphics, (730, 300))
    results = model(imgRegion, stream = True)

    detections = np.empty((0, 5))

    for r in results:
        boxes = r.boxes
        for box in boxes:
        # Bounding Box
            x1, y1, x2, y2 = box.xyxy[0] 
            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
            w, h = x2 - x1, y2 - y1
        
        
            conf = math.ceil((box.conf[0] * 100)) / 100 # Confidence
            cls = int(box.cls[0]) # Class Name

            print("cls: ", cls)

            currentClass = classNames[cls]
            print("cls Name: ", currentClass)
            if(
                currentClass == "person"
                and conf > 0.1
            ):
                # cvzone.putTextRect(
                #     img,
                #     f"{classNames[cls]} {conf}",
                #     (max(0, x1), max(35, y1)),
                #     scale=0.8,
                #     thickness=1,
                #     offset=3,
                # )
                # cvzone.cornerRect(img, (x1, y1, w, h))
                currentArray = np.array([x1, y1, x2, y2, conf])
                detections = np.vstack((detections, currentArray))
        
            resultsTracker = tracker.update(detections)
            

            cv2.line(img, (limits_down[0], limits_down[1]), (limits_down[2], limits_down[3]), (0, 0, 255), 5)
            cv2.line(img, (limits_up[0], limits_up[1]), (limits_up[2], limits_up[3]), (0, 255, 0), 5)

            for result in resultsTracker:
                x1, y1, x2, y2, id = result
                x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
                print(result)
                w, h = x2 - x1, y2 - y1
                cvzone.cornerRect(img, (x1, y1, w, h), l = 9, rt = 2, colorR = (255, 0, 0))
                cvzone.putTextRect(
                    img,
                    f"{int(id)}",
                    (max(0, x1), max(35, y1)),
                    scale = 2,
                    thickness = 3,
                    offset = 10,
                )

                cx, cy = x1 + w // 2, y1 + h // 2
                cv2.circle(img, (cx, cy), 5, (255, 0, 255), cv2.FILLED)

                if limits_down[0] < cx < limits_down[2] and limits_down[1] - 15 < cy < limits_down[1] + 15:
                    if totalCount_down.count(id) == 0:
                        totalCount_down.append(id)
                        cv2.line(img, (limits_down[0], limits_down[1]), (limits_down[2], limits_down[3]), (0, 255, 0), 5)
                
                if limits_up[0] < cx < limits_up[2] and limits_up[1] - 15 < cy < limits_up[1] + 15:
                    if totalCount_up.count(id) == 0:
                        totalCount_up.append(id)
                        cv2.line(img, (limits_up[0], limits_up[1]), (limits_up[2], limits_up[3]), (0, 255, 0), 5)  
            cv2.putText(img,str(len(totalCount_down)),(1180,390),cv2.FONT_HERSHEY_PLAIN,5,(50,50,255),8)
            cv2.putText(img,str(len(totalCount_up)),(960,390),cv2.FONT_HERSHEY_PLAIN,5,(50,255,50),8)
    cv2.imshow("Image", img)
    #cv2.imshow("ImageRegion", imgRegion)
    cv2.waitKey(1)