#输入第一个点的经纬度
import math
x1,y1 = eval(input("输入第一个点的经纬度，角度表示"))
x1,y1 = math.radians(x1),math.radians(y1)
x2,y2 = eval(input("输入第二个点的经纬度，角度表示"))
x2,y2 = math.radians(x2),math.radians(y2)
#计算距离
radius = 6371.01
d = radius * math.acos(math.sin(x1) * math.sin(x2) + math.cos(x1) * math.cos(x2) * math.cos(y1-y2))
print("距离是",d)
