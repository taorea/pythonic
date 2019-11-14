#用户输入半径，在屏幕正中心画四个圆形
import turtle
r = eval(input("输入半径"))
turtle.penup()
turtle.goto(-r,0)
turtle.pendown()
turtle.begin_fill()
turtle.color('red')
turtle.circle(r)
turtle.end_fill()

turtle.penup()
turtle.goto(r,0)
turtle.pendown()
turtle.begin_fill()
turtle.color('yellow')
turtle.circle(r)
turtle.end_fill()

turtle.penup()
turtle.goto(-r,-r*2)
turtle.pendown()
turtle.begin_fill()
turtle.color('green')
turtle.circle(r)
turtle.end_fill()

turtle.penup()
turtle.goto(r,-2*r)
turtle.pendown()
turtle.begin_fill()
turtle.color('blue')
turtle.circle(r)
turtle.end_fill()

turtle.hideturtle
turtle.done()