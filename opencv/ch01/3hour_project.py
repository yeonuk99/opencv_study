import cv2
import time
def main():
    camera = cv2.VideoCapture(cv2.CAP_DSHOW + 0)
    camera.set(3, 640)
    camera.set(4, 480)
    xml = "C:\\python\\opencv-4.x\\opencv-4.x\\data\\haarcascades\\haarcascade_frontalface_default.xml"
    change_imgae = cv2.imread('change_face.jpg', cv2.IMREAD_COLOR)
    
    face_cascade = cv2.CascadeClassifier(xml)
    while camera.isOpened():
        _, image = camera.read()
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.05, 5)
        print(faces)
        if len(faces):
            for x, y, w, h in faces:
                
                face_roi = image[y:y+h, x:x+w]

                change_imgae_resized = cv2.resize(change_imgae, (w, h))

                image[y:y+h, x:x+w] = change_imgae_resized
                
                cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)
        
        cv2.imshow("result", image)
    
        
        if cv2.waitKey(1) == ord("q"):
            break
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()