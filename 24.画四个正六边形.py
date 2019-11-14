#在屏幕正中央画四个正六边形
import turtle
turtle.circle(50,steps=6)
turtle.penup()
turtle.goto(25*3**0.5*2,0)
turtle.pendown()
turtle.circle(50,steps=6)

turtle.penup()
turtle.goto(0,-100)
turtle.pendown()
turtle.circle(50,steps=6)

turtle.penup()
turtle.goto(25*3**0.5*2,-100)
turtle.pendown()
turtle.circle(50,steps=6)

turtle.done()