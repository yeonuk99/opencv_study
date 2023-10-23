# d = {"번호: ":10, "성명: ":"코난", "나이":23, "사는곳":"서울"}
# print(d)

# print(type(d))

# print(d["나이"])
# d["나이"] = 24
# print(d["나이"])

# d["직업"] = "탑정"
# print(d)

# print(d.keys())
# print(d.values())

# print("사는곳" in d)
# del d("사는곳")
# print("사는곳" in d)


my_list = [1,2,3,4,5]
del my_list[0:6:2]
print(my_list)


a = {"A":90, "B":80}

print(a["A"])
print(a["B"])

#print(a["C"]) #key값이 없어서 에러
print(a.get("C"))


