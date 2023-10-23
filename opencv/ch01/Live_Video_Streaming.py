import cv2
from flask import Flask, render_template, Response

app = Flask(__name__)
# 가중치 파일 경로
cascade_filename = "C:\\python\\opencv-4.x\\opencv-4.x\\data\\haarcascades\\haarcascade_frontalface_alt.xml"

#모델 불러오기
cascade = cv2.CascadeClassifier(cascade_filename)

def imgDetector(img, cascade):
    #영상 압축
    img = cv2.resize(img, dsize = None, fx = 1.0, fy = 1.0)

    #그레이 스케일 변환
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    #cascade 얼굴 탐지 알고리즘
    results = cascade.detectMultiScale(
            gray,
            scaleFactor = 1.1,
            minNeighbors = 5,
            minSize = (20, 20),

        )
    for box in results:
        x, y, w, h = box
        cv2.rectangle(img, (x,y), (x+w,y+h), (255, 255, 255), thickness = 2)
    return img

def gen():
    camera = cv2.VideoCapture(cv2.CAP_DSHOW + 0)
    camera.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
    while 1:
        _, frame = camera.read()
        
        retImg = imgDetector(frame, cascade)
        cv2.imwrite("pic.jpg", retImg)
        yield (
            b"--frame\r\n"
            b"Content-Type: image/jpeg\r\n\r\n" + open("pic.jpg", "rb").read() + b"\r\n"
        )
    camera.release()
    cv2.destroyAllWindows()

@app.route("/")
def index():
    """Video streaming ."""
    return render_template("index.html")

@app.route("/video_feed")
def video_feed():
    """Video streaming route. Put this in the src attribute of an img tag."""
    return Response(gen(), mimetype="multipart/x-mixed-replace; boundary=frame")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=9000, debug=True, threaded=True)


  

