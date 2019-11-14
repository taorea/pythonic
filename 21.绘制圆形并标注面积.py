#在屏幕中心画一个圆，提示用户输入圆心和半径，并标注圆的面积
import turtle
import math
#turtle.showturtle()
centerX,centerY = eval(input("输入圆心的位置"))
radius = eval(input("输入圆的半径："))
area = math.pi * radius**2
turtle.penup()
turtle.goto(centerX,centerY)
turtle.pendown()
turtle.write(str(format(area,"10.2f")) +"m2")
turtle.penup()
turtle.goto(centerX,centerY-radius)
turtle.pendown()
turtle.circle(radius)
turtle.done()