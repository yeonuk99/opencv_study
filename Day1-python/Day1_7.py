aa = [30, 10, 20]
print("현재의 리스트 : ", aa)

aa.append(40)
print("append 후 리스트 : ", aa)

aa.pop()
print("pop 후 리스트 : ", aa)

aa.sort()
print("sort 후 리스트 : ", aa)

aa.reverse()
print("reverse 후 리스트 : ", aa)

aa.insert(2, 222)
print("insert 후 리스트", aa)
print("20값의 위치 : ", aa.index(20))

aa.remove(222)
print("remove(222) 후 리스트 : ", aa)

aa.extend([77,88,77])
print("extend([77,88,77]) 후 리스트 : ", aa)
print("77값의 개수 : ", aa.count(77))

