import tkinter as tk
import cv2
import numpy as np
from PIL import Image, ImageTk
from math import sqrt, pow
from tkinter import filedialog, colorchooser, StringVar, ttk
import time

# OpenCV 초기화
cv2.namedWindow("Image Board")

window = tk.Tk()
window.title("Grapic Tablet")
window.geometry("500x600+100+100")
window.resizable(True, True)


global mouse_mode
mouse_mode = 1

global file_path
global click
global list_x
global list_y
global text_value

list_x = []
list_y = []
file_path = None
oldx = oldy = -1
b, g, r = 0, 0, 0
bg_b, bg_g, bg_r = 255, 255, 255
text_value = StringVar()

image = np.full((500, 500, 3), (bg_b, bg_g, bg_r), dtype=np.uint8)






def Click_mouse(event, x, y, flags, param):
    
    global oldx, oldy, mouse_mode
    global b, g, r
    global bg_b, bg_g, bg_r
    global click
    global list_x, list_y
    global file_path, text_value

    spinbox_value = int(spinbox.get())
    font_value = float(spinbox_font.get())

    # 펜 모드
    if mouse_mode == 1:
        if event == cv2.EVENT_LBUTTONDOWN:
            oldx, oldy = x, y
        elif event == cv2.EVENT_MOUSEMOVE:                  
            if flags & cv2.EVENT_FLAG_LBUTTON:
                cv2.line(image, (oldx, oldy), (x, y), (b, g, r), spinbox_value, cv2.LINE_AA)
                oldx, oldy = x, y
    
    # 직선 그리기 모드
    if mouse_mode == 2:
        
        if event == cv2.EVENT_LBUTTONDOWN:
            list_x.append(x)
            list_y.append(y)
        elif event == cv2.EVENT_LBUTTONUP:           
            if len(list_x) == 2 and len(list_y) == 2:
                cv2.line(image, (list_x[0], list_y[0]), (list_x[1], list_y[1]), (b, g, r), spinbox_value, cv2.LINE_AA)
                list_x = []
                list_y = []
    
    
    # 사각형 만들기
    if mouse_mode == 4:
        if event == cv2.EVENT_LBUTTONDOWN:
            
            click = True
            
            oldx, oldy = x, y
        elif event == cv2.EVENT_MOUSEMOVE:         
            if click:
                # 현재 마우스 위치까지 네모 그리기                
                cv2.rectangle(image, (oldx, oldy), (x, y), (b, g, r), -1)
                update_canvas(image)                
        elif event == cv2.EVENT_LBUTTONUP:
            
            click = False
            
            # 드래그 완료된 네모 그리기
            cv2.rectangle(image, (oldx, oldy), (x, y), (b, g, r), -1)
            update_canvas(image)
            
    
    # 원 만들기
    if mouse_mode == 5:
        if event == cv2.EVENT_LBUTTONDOWN:                      # 마우스를 누른 상태
            click = True 
            oldx, oldy = x,y
        elif event == cv2.EVENT_MOUSEMOVE:                      # 마우스 이동
            if click: # 마우스를 누른 상태 일경우                                                  
                radius = int(sqrt(pow(x-oldx,2)+pow(y-oldy,2))/2)
                cx = int(((oldx -x) / 2) + x)   # x좌표의 중앙값
                cy = int(((oldy -y) / 2) + y)   # y좌표의 중앙값         
                cv2.circle(image, (cx, cy), radius, (b, g, r), -1)   
                update_canvas(image)
        elif event == cv2.EVENT_LBUTTONUP:
            click = False 
            
    
    if mouse_mode == 6:   
        if event == cv2.EVENT_LBUTTONDOWN:
            if font_style.get() == "FONT_ITALIC":                
                cv2.putText(image, text = text_value, org = (x, y), fontFace=cv2.FONT_ITALIC,
                            fontScale=font_value,color=(b,g,r), lineType=cv2.LINE_AA, thickness=spinbox_value)
            
            elif font_style.get() == "FONT_HERSHEY_COMPLEX":                
                cv2.putText(image, text = text_value, org = (x, y), fontFace=cv2.FONT_HERSHEY_COMPLEX,
                            fontScale=font_value,color=(b,g,r), lineType=cv2.LINE_AA, thickness=spinbox_value)
            
            elif font_style.get() == "FONT_HERSHEY_SIMPLE":               
                cv2.putText(image, text = text_value, org = (x, y), fontFace=cv2.FONT_HERSHEY_SIMPLE,
                            fontScale=font_value,color=(b,g,r), lineType=cv2.LINE_AA, thickness=spinbox_value)
           
            elif font_style.get() == "FONT_HERSHEY_TRIPLEX":             
                cv2.putText(image, text = text_value, org = (x, y), fontFace=cv2.FONT_HERSHEY_TRIPLEX,
                            fontScale=font_value,color=(b,g,r),lineType=cv2.LINE_AA, thickness=spinbox_value)
            
            elif font_style.get() == "FONT_HERSHEY_SCRIPT_COMPLEX":
                cv2.putText(image, text = text_value, org = (x, y), fontFace=cv2.FONT_HERSHEY_SCRIPT_COMPLEX,
                            fontScale=font_value,color=(b,g,r), lineType=cv2.LINE_AA, thickness=spinbox_value)
                
  
    # 지우개 모드
    if mouse_mode == 0:
        if file_path == None:
            if event == cv2.EVENT_LBUTTONDOWN:
                oldx, oldy = x, y
            elif event == cv2.EVENT_MOUSEMOVE:
                if flags & cv2.EVENT_FLAG_LBUTTON:
                    cv2.circle(image, (x, y), 20, (bg_b, bg_g, bg_r), thickness = -1, lineType = cv2.LINE_AA)
                    oldx, oldy = x, y
        else:
            
            image_ = cv2.imread(file_path.name, cv2.COLOR_BGR2RGB)        
            if event == cv2.EVENT_LBUTTONDOWN:
                oldx, oldy = x, y 
            elif event == cv2.EVENT_MOUSEMOVE:
                #update_canvas(image)
              
                if flags & cv2.EVENT_FLAG_LBUTTON:
                    image[y:y+30,x:x+30] = image_[y:y+30, x:x+30]
    
                

    update_canvas(image)

# 전체 초기화 기능 함수
def clear():
    global image
    global file_path
    if file_path == None:
        image = np.full((500, 500, 3), (bg_b, bg_g, bg_r), dtype=np.uint8)
        update_canvas(image)
    else:
        image = cv2.imread(file_path.name)
        update_canvas(image)

# 그리기 기능
def pen():
    global mouse_mode
    mouse_mode = 1

def line():
    global mouse_mode
    mouse_mode = 2

def rectangle():
    global mouse_mode
    global click
    click = False
    mouse_mode = 4

def circle():
    global mouse_mode
    global click
    click = False
    mouse_mode = 5


# 파일에서 이미지 불러오기 함수
def image_read():
    global image
    global file_path
    file_path = filedialog.askopenfile(initialdir="C:\python\opencv_project", title="Select image")
    print(file_path.name)
    image = cv2.imread(file_path.name)
    update_canvas(image)


def image_write():
    global image

    file_name = time.strftime("%Y%m%d_%H-%M-%S") 
    
    cv2.imwrite(file_name+".jpg", image)

def Text_box():
    global mouse_mode
    global text_value
    mouse_mode = 6
    # text_value = StringVar()
    text_value = text_box.get()
    print(text_value)


# 사용자 지정 색상
def choose_color():
    global b, g, r
    global mouse_mode
    color = colorchooser.askcolor(title="색상 선택") #선택한 생상이 color에 저장
    print(color)
    if color:
        r, g, b = color[0]
        


# 라벨
pen_label = tk.Label(window, text = "펜 색상:", height=0, width = 10)
pen_label.place(x =250, y = 2)

bg_label = tk.Label(window, text = "배경 색상:", height=0, width=10)
bg_label.place(x =282, y = 27)

# 글자 색상 변경 함수
def Change_red():
    global b, g, r
    b, g, r = 0, 0, 255

def Change_blue():
    global b, g, r
    b, g, r = 255, 0, 0

def Change_green():
    global b, g, r
    b, g, r = 0, 255, 0

def Change_white():
    global b, g, r
    b, g, r = 255, 255, 255

def Change_black():
    global b, g, r
    b, g, r = 0, 0, 0

# 배경 색상 변경 함수
def bg_red():
    global bg_b, bg_g, bg_r
    global image
    global file_path
    file_path = None
    bg_b, bg_g, bg_r = 0, 0, 255
    image = np.full((500, 500, 3), (bg_b, bg_g, bg_r), dtype=np.uint8)
    update_canvas(image)


def bg_blue():
    global bg_b, bg_g, bg_r
    global image
    global file_path
    file_path = None
    bg_b, bg_g, bg_r = 255, 0, 0
    image = np.full((500, 500, 3), (bg_b, bg_g, bg_r), dtype=np.uint8)
    update_canvas(image)

def bg_green():
    global bg_b, bg_g, bg_r
    global image
    global file_path
    file_path = None
    bg_b, bg_g, bg_r = 0, 255, 0
    image = np.full((500, 500, 3), (bg_b, bg_g, bg_r), dtype=np.uint8)
    update_canvas(image)

def bg_white():
    global bg_b, bg_g, bg_r
    global image
    global file_path
    file_path = None
    bg_b, bg_g, bg_r = 255, 255, 255
    image = np.full((500, 500, 3), (bg_b, bg_g, bg_r), dtype=np.uint8)
    update_canvas(image)

def bg_black():
    global bg_b, bg_g, bg_r
    global image
    global file_path
    file_path = None
    bg_b, bg_g, bg_r = 0, 0, 0
    image = np.full((500, 500, 3), (bg_b, bg_g, bg_r), dtype=np.uint8)
    update_canvas(image)

# 지우개 함수
def eraser():
    global mouse_mode
    mouse_mode = 0



# 색상 버튼
# 글 색상
Change_Red_button = tk.Button(window, bg ="red", width = 3, command=Change_red)
Change_Red_button.place(x = 470, y = 0)

Change_Blue_button = tk.Button(window, bg ="blue", width = 3, command=Change_blue)
Change_Blue_button.place(x = 440, y = 0)

Change_Green_button = tk.Button(window, bg ="green", width = 3, command=Change_green)
Change_Green_button.place(x = 410, y = 0)

Change_Wihte_button = tk.Button(window, bg ="white", width = 3, command=Change_white)
Change_Wihte_button.place(x = 380, y = 0)

Change_Black_button = tk.Button(window, bg ="black", width = 3, command=Change_black)
Change_Black_button.place(x = 350, y = 0)

photo_rainbow = tk.PhotoImage(file = "rainbow.png")
Choose_color_button = tk.Button(window, text = "ch", height= 20, width = 30, command=choose_color, image = photo_rainbow)
Choose_color_button.place(x = 315, y = 0)

# 배경색상
bg_Red_button = tk.Button(window, bg ="red", width = 3, command=bg_red)
bg_Red_button.place(x = 470, y = 25)

bg_Blue_button = tk.Button(window, bg ="blue", width = 3, command=bg_blue)
bg_Blue_button.place(x = 440, y = 25)

bg_Green_button = tk.Button(window, bg ="green", width = 3, command=bg_green)
bg_Green_button.place(x = 410, y = 25)

bg_Wihte_button = tk.Button(window, bg ="white", width = 3, command=bg_white)
bg_Wihte_button.place(x = 380, y = 25)

bg_Black_button = tk.Button(window, bg ="black", width = 3, command=bg_black)
bg_Black_button.place(x = 350, y = 25)

# 그외 기능

photo_pen = tk.PhotoImage(file = "pen.png")
point_button = tk.Button(window, text="pen", height=20, width=20, command = pen, image = photo_pen)
point_button.place(x=0, y=0)

# 스핀박스 생성
sp = tk.IntVar()
spinbox = tk.Spinbox(window, from_ = 1, to = 20, 
                     increment= 1, textvariable=sp, width=5,)
spinbox.place(x = 30, y = 3)

sp_font = tk.DoubleVar()
spinbox_font = tk.Spinbox(window, from_ = 0.8, to = 10, 
                     increment= 0.1, textvariable=sp_font, width=8)
spinbox_font.place(x = 105, y = 28)

# 콤보 박스 생성
font_name = [
    "FONT_ITALIC", 
    "FONT_HERSHEY_COMPLEX", 
    "FONT_HERSHEY_SIMPLE", 
    "FONT_HERSHEY_TRIPLEX", 
    "FONT_HERSHEY_SCRIPT_COMPLEX",
    ]
font_style = ttk.Combobox(window, height= 5, width= 18, value = font_name, state = "readonly")
font_style.place(x = 105, y = 3)



text_box = tk.Entry(window, width = 10, textvariable=text_value)
text_box.place(x=180, y=28)
text_box_button = tk.Button(window, text="OK", width=3, command = Text_box)
text_box_button.place(x = 255, y = 25)

photo_line = tk.PhotoImage(file = "line.png")
line_button = tk.Button(window, height=20, width=20, command = line, image = photo_line)
line_button.place(x=0, y=25)

photo_rectangle = tk.PhotoImage(file = "rectangle.png")
rectangle_button = tk.Button(window, height=20, width=20, command = rectangle, image = photo_rectangle)
rectangle_button.place(x = 25, y = 25)

photo_circle = tk.PhotoImage(file = "circle.png")
circle_button = tk.Button(window, height=20, width=20, command = circle, image = photo_circle)
circle_button.place(x = 50, y = 25)

photo_eraser = tk.PhotoImage(file = "eraser.png")
Eraser_button = tk.Button(window, height=20, width = 20, command=eraser, image = photo_eraser)
Eraser_button.place(x = 75, y = 25)




image_read_button = tk.Button(window, text="img",height=3, width=10, command = image_read)
image_read_button.place(x = 0, y = 550)

image_write_button = tk.Button(window, text="save", height=3, width=10, command = image_write)
image_write_button.place(x = 80, y = 550)

clear_button = tk.Button(window, text="clear", height=3, width=10, command = clear)
clear_button.place(x=160, y=550)


# 캔버스
canvas = tk.Canvas(window, bg="black", width=500, height=500)
canvas.place(x=0, y=50)

def update_canvas(image):
    img_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    pil_image = Image.fromarray(img_rgb)
    img_tk = ImageTk.PhotoImage(image=pil_image)
    canvas.create_image(0, 0, anchor="nw", image=img_tk)
    canvas.img = img_tk


    cv2.imshow("Image Board", image)

update_canvas(image)
window.after(10, update_canvas, image)
cv2.setMouseCallback("Image Board", Click_mouse)

window.mainloop()





