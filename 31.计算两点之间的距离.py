#1用户输入两个点的坐标,计算两个点之间的直线距离
#优化，将两个点直线显示在图形化窗口
import turtle
x1,y1 = eval(input("输入两个点的坐标:格式(34,56)"))
x2,y2 = eval(input("输入两个点的坐标:格式(34,56)"))
distance = ((x1 - x2)**2 + (y1 - y2)**2) ** 0.5
turtle.penup()
turtle.color("red")
turtle.goto(x1,y1)
turtle.pendown()
turtle.write(str(x1)+","+str(y1))
turtle.goto(x2,y2)
turtle.write(str(x2)+","+str(y2))
turtle.penup()
turtle.goto((x1 + x2)/2 , (y1 + y2)/2)
turtle.write("distance" + str(int(distance * 1000) / 1000))
print("两个点之间的距离是：",int(distance * 1000) / 1000) #保留三位小数
turtle.done()
