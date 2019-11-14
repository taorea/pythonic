#常量名用大写
PI = 3.141592653
radius,length = eval(input("Please input the radius and length of the parameter:"))
area = int(PI * radius ** 2 * 10000) / 10000
volume = area * length
print("The area is{} m2\
\nThe volume is {} m3".format(area,volume))
