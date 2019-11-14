numbers = eval(input("输入一个0到1000之间的数字:"))
s = 0
while numbers != 0:
    NextNumber = numbers // 10
    everyNumber = numbers % 10
    s += everyNumber
    numbers = NextNumber
print("各位数之和是:",s)


