from ultralytics import YOLO
import cv2
import cvzone
import math



cap = cv2.VideoCapture("C:\\python\\object-Detection\\object-Detection\\Videos\\ppe-1.mp4")

model = YOLO("C:\\python\\object-Detection\\object-Detection\\5.PPEDetection\\ppe.pt")

className = [
    "Hardhat",
    "Mask",
    "NO-Hardhat",
    "NO-Mask",
    "NO-Safety Vest",
    "Person",
    "Safety Cone",
    "Safety Vest",
    "machinery",
    "vehicle",
]

myColor = (0, 0, 255)

while True:
    success, img = cap.read()
    results = model(img, stream = True)
    for r in results:
        boxes = r.boxes
        for box in boxes:
            #Bounding Box
            x1, y1, x2, y2 = box.xyxy[0]
            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)

            w, h = x2 - x1, y2 - y1

            #Confidence
            conf = math.ceil((box.conf[0]*100)) / 100

            #Class Name
            cls = int(box.cls[0])
            currentClass = className[cls]
            print(currentClass)

            if conf > 0.5:
                if(
                    currentClass == "No-Hardhat"
                    or currentClass == "No-Safety Vest"
                    or currentClass == "No-Mask"
                ):
                    myColor = (0, 0, 255)
                elif (
                    currentClass == "Hardhat"
                    or currentClass == "Safety Vest"
                    or currentClass == "Mask"
                ):
                    myColor = (0, 255, 0)
                else:
                    myColor = (255, 0, 0)

                cvzone.putTextRect(
                    img,
                    f"{className[cls]} {conf}",
                    (max(0, x1), max(35, y1)),
                    scale=1,
                    thickness=1,
                    colorB=myColor,
                    colorT=(255, 255, 255),
                    colorR=myColor,
                    offset=5,
                )
                cv2.rectangle(img, (x1, y1), (x2, y2), myColor, 3)

    
    cv2.imshow("Image", img)
    cv2.waitKey(1)