finalAcount = eval(input("输入最终的金额值"))
yearRate = eval(input("输入年利率"))
year = eval(input("输入存款年限"))
monthRate = yearRate / 1200
initialAcount = finalAcount / (1 + monthRate) ** (year * 12)
print("initialAcount is",initialAcount)
