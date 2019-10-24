# import os
# os.system("calc") #启动计算器
# os.system("taskkill /f /im QQ.exe") #关闭QQ进程
# os.system("ipconfig") #查看ip地址


import turtle
# # turtle.showturtle()
# turtle.write("hello python")
# turtle.forward(100) #前进步数

turtle.showturtle()
turtle.penup()
turtle.goto(-10,200)
turtle.pendown()
turtle.write("奥运五环")
turtle.penup()
turtle.goto(-10,190)
turtle.pendown()
turtle.write("张涛")

turtle.penup()
turtle.goto(0,0)
turtle.pendown()
turtle.color("red")
turtle.circle(100)

turtle.penup()
turtle.goto(-200,0)
turtle.pendown()
turtle.color("green")
turtle.circle(100)

turtle.penup()
turtle.goto(200,0)
turtle.pendown()
turtle.color("blue")
turtle.circle(100)

turtle.penup()
turtle.goto(-100,-200)
turtle.pendown()
turtle.color("blue")
turtle.circle(100)

turtle.penup()
turtle.goto(100,-200)
turtle.pendown()
turtle.color("green")
turtle.circle(100)

turtle.clear() #清除屏幕内容
turtle.done() 
