# aa = [10,20,30,40]
# #aa[-1]은 뒤에서 첫번째 , aa[-2]는 뒤에서 두번째 요소를 의미

# print("aa[-1]은 %d, aa[-2]는 %d" %(aa[-1], aa[-2]))
# print(aa[0:2])  #첫 번째부터 두 번째 요소값을 출력
# print(aa[2:4])  #세 번째부터 네 번째 요소값을 출력
# print(aa[0:])   #첫 번째부터 끝까지 요소값을 출력


# my_list = [0,1,2,3,4,5]
# print(id(my_list))

# my_list[1:3] = ["A", "B", "C"]
# print(id(my_list))

# print(my_list)



my_list = [0,1,2,3,4,5]
print(id(my_list))

my_list[1:5] = ["A", "B"]
print(id(my_list))
print(my_list)