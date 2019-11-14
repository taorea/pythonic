import math
import turtle
x1,y1 = eval(input("输入第一个点"))
x2,y2 = eval(input("输入第二个点"))
x3,y3 = eval(input("输入第三个点"))
l1 = ((x2-x3) ** 2 + (y2-y3) **2) ** 0.5
l2 = ((x1 - x3) ** 2 + (y1 - y3) **2) ** 0.5
l3 = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
p3 = math.acos((l1 ** 2 + l2 **2 - l3 ** 2) / (2 * (l1 * l2)))
P3 = math.degrees(p3)
p1 = math.acos((l2 ** 2 + l3 **2 - l1 ** 2) / (2 * (l2 * l3)))
P1 = math.degrees(p1)
p2 = math.acos((l1 ** 2 + l3 **2 - l2 ** 2) / (2 * (l1 * l3)))
P2 = math.degrees(p2)
turtle.penup()
turtle.goto(x1,y1)
turtle.pendown()
turtle.write(format(P1,".2f"))
turtle.goto(x2,y2)
turtle.write(format(P2,".2f"))
turtle.goto(x3,y3)
turtle.write(format(P3,".2f"))
turtle.goto(x1,y1)
turtle.done()