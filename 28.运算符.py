#今天是星期二，100天后是星期几
print("一百天后：",(2 + 100) % 7)

print(25 / 4)
print(int(25 / 4))
print(25 // 4)
print(round(25 / 4))

#根据表达式用python编写
#print(4/(3 * (r + 34)) - 9 * (a + b*c) + (3 + d*(2 + a))/(a + b * d))

m = 10
r = 3
print(m * r ** 2)

i = 3
i += 1
print(i) # 4
i *= 2
print(i) # 8
i **= 2 
print(i) # 64
i //= 11
print(i) # 5
i %= 2
print(i) # 1

print(eval("3 + 4"))
print(int("003")) #字符串0开头，用eval("003")会报错

