# def isOdd(arg):
#     return arg % 2 == 1


# def func01(x):
#     for i in range(1, x+1):
#         if x % i == 0:
#             return True
#         else:
#             return False




# #dicitonaty
# myDict = { x:x*x for x in range(11) if isOdd(x) }
# f = {x for x in range(100) if func01(x)}

# print(myDict)
# print(f)


def isOdd(arg):
 return arg % 2 == 1 # 홀수일때 true 짝수일때 false
# dictionary
myDict = {x: x * x for x in range(11) if isOdd(x)}
print(myDict)