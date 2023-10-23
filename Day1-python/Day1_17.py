
fruits =[]

fruits.append("Server")
fruits.append("Client")
fruits.append("Database")
fruits.append("Cloud Computing")
fruits.append("Software")
fruits.append("Hardware")

# f = open("fruit.txt", "w")  # w 쓰기모드
# for fruit in fruits:
#     f.write(fruit)
#     f.write("\n")

# f.close()

# f = open("fruit.txt", "r") # r 읽기모드
# fruits = f.readlines()
# f.close()

# print(fruits)

# # # \n없애기
# # r_fruits = []
# # for f in fruits:
# #     r_fruits.append(f.strip())
# #     #r_fruits.append(f.replace("\n", ""))
# # print(r_fruits)

# #다른방법
# fruits = list(map(lambda s: s.strip(), fruits))
# print(fruits)

#sample.txt 파일을 읽어 총합과 평균을 구한 후 평균값을 result.txt 파일에 저장하는 프로그램을 작성하세요
def TextFile_AVG():
    f = open("sample.txt", "r")
    lines = f.readlines()
    f.close()

    #r_lines = list(map(lambda s: s.strip(), lines))

    sum = 0
    for val in lines:
        sum += int(val)

    average = sum / len(lines)

    f = open("result.txt", "a+")
    f.write(str(average))
    f.write(str("\n"))
    f.close()
    
# 시간 읽어와서 파일명 저장하기
import time
from datetime import datetime
def TimeFile_Save():

    filename = time.strftime("%Y%m%d_%H%M%S")
    print(filename)

    f = open(filename + ".txt", "w")
    for fruit in fruits:
        f.write(fruit)
        f.write("\n")
    f.close()

def PrintTime():
    t = time.strftime("%Y-%m-%d %H: %M: %S")
    t1 = datetime.strptime("2시30분", "%H시%M분 ")

    print(t)
    print(t1)

PrintTime()