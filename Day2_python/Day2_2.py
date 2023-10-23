
# 369게임
def ThreeSixNine(Max_value):

    for val in range(1, int(Max_value)+1):
        for val1 in str(val):
            if(val1 == '3' or val == '6' or val == '9'):
                print('x', end="")
            else:
                print(val, end="")

Max_value = input("Max값을 입력하세요: ")

ThreeSixNine(Max_value = Max_value)
