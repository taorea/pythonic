#提示用户输入矩形中心和矩形的长宽
import turtle
centerx,centery = eval(input("输入矩形的中心坐标")) #输入时必须将两个数用逗号隔开，例如 100,200
length,width = eval(input("输入矩形的长度和宽度"))
turtle.penup()
turtle.goto(centerx,centery)
turtle.write("中心点",font=("黑体",40,"normal")) #文字的大小

turtle.begin_fill() #开始填充
turtle.pensize(10) #笔的大小
turtle.penup()
turtle.goto(centerx + width/2,centery+ length/2)
turtle.pendown()
turtle.goto(centerx+width/2,centery-length/2)
turtle.goto(centerx-width/2,centery-length/2)
turtle.goto(centerx-width/2,centery+length/2)
turtle.goto(centerx+width/2,centery+length/2)
turtle.color("yellow") #填充颜色
turtle.end_fill() #结束填充

turtle.done()