#1. 리스트를 사용하지 않고 숫자형 변수 4개를 선언하여 출력한 예
a,b,c,d = 0,0,0,0
hap = 0

a = int(input("1번째 숫자: "))
b = int(input("2번째 숫자: "))
c = int(input("3번째 숫자: "))
d = int(input("4번째 숫자: "))
hap = a+b+c+d
print("합계1 => %d" %hap)  #%d는 %뒤에 선언한 hap값이 대입한다.


#2. 리스트 변수를 선언하여 앞 예제를 수정
aa = [0,0,0,0]
hap = 0
aa[0] = int(input("1번째 숫자: "))
aa[1] = int(input("2번째 숫자: "))
aa[2] = int(input("3번째 숫자: "))
aa[3] = int(input("4번째 숫자: "))
#hap = aa[0] + aa[1] + aa[2] + aa[3]

for val in range(len(aa)):
    hap += aa[val]

print("합계2 => %d" %hap)