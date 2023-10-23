import easyocr
import cv2
import matplotlib.pyplot as plt

reader = easyocr.Reader(["ko", "en"])

img_path = "04.png"
img = cv2.imread(img_path)

gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

_, th_img = cv2.threshold(gray_img, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
result = reader.readtext(th_img)
print(result)

THRESHOLD = 0.5

for bbox, text, conf in result:
    if conf > THRESHOLD:
        print(text)
        
        
        cv2.rectangle(th_img, pt1=(int(bbox[0][0]), int(bbox[0][1])), pt2=(int(bbox[2][0]), int(bbox[2][1])), color=(0,0,255), thickness=3)



plt.figure(figsize = (8, 8))
plt.imshow(th_img, cmap='gray')
plt.axis("off")
plt.show()

