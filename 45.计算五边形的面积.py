#中心到五个角的距离都是r
import math
r = eval(input("输入半径："))
#计算五边形边长
length = 2 * r * math.sin(math.pi / 5)
#计算面积
area = 5 * length ** 2 / (4 * math.tan(math.pi /5))
print("The area is %.2f" % area)
