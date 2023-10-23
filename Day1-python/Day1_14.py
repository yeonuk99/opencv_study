# A = [20, 55, 67, 82, 45, 33, 90, 87, 100, 25]

# sum = 0
# for score in A:
#     if score >= 50:
#         sum += score

# print(sum)
# sum = 0
# for score in A:
#     while(score >= 50):
#         sum += score
#         break

# print(sum)

# sum = 0
# while A:
#     score = A.pop()
#     if score >= 50:
#         sum+=score
# print(sum)

##숫자의 총합구하기(문제)
# user_input = "65,45,2,3,45,8"

# user_output = user_input.split(",")

# sum = 0
# for i in user_output:
#     sum += int(i)

# print(sum)

#구구단(문제)

while(True):
    user_input = input("구구단을 출력할 숫자를 입력하세요(2~9): ")
    
    if(2<=int(user_input)<=9):
        for i in range(1, 10):
            print(int(user_input)*i, end=" ")
            #print(user_input, "*", i, "=", int(user_input) * i)
        print()
    else:
        print("잘못된 입력입니다.")

        