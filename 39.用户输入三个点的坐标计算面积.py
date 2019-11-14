import math
x1,y1,x2,y2,x3,y3 = eval(input("输入三个点坐标，用逗号分隔，例如：34,56---------"))
side1 = math.sqrt(x1**2 + y1**2)
side2 = math.sqrt(x2**2 + y2**2)
side3 = math.sqrt(x3**2 + y3**2)
print(side1,side2,side3)
s = (side1 + side2 + side3) / 2
s = int(s * 1000) / 1000
print(s)
area = math.sqrt(s * (s - side1)*(s - side2)*(s - side3))
print("The area of the triangle is:%.4f"%area)