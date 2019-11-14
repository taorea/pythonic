# 4567---> 7654
number = eval(input("输入最初的数字:"))
while number  >= 10:
    numberMod = number % 10
    number = number // 10
    print(numberMod)
print(number)