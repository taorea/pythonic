import turtle
x1,y1 = eval(input("请输入第一个点的坐标：")) #12,45用逗号分隔
# print(type(x1)) #int
x2,y2 = eval(input("请输入第二个点的坐标："))
turtle.penup()
turtle.goto(x1,y1)
turtle.pendown()
turtle.write(str(x1)+","+str(y1))
turtle.goto(x2,y2)
turtle.write(str(x2)+","+str(y2))
turtle.done()