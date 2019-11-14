import turtle
turtle.screensize(1024,768)
turtle.write("hello python",font=("宋体","40","normal"))
turtle.begin_fill() #开始填充
turtle.circle(100,steps=8) #八边形
turtle.color("yellow")
turtle.end_fill() #结束填充
turtle.reset()#重置

turtle.pensize(20)#笔的大小
turtle.begin_fill()
turtle.circle(100,steps = 4)
turtle.color("red")
turtle.end_fill()
turtle.showturtle()
turtle.hideturtle()
turtle.done()

import turtle
turtle.showturtle()

turtle.done()