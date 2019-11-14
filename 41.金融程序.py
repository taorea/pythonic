#读取投资额，年利率，年率，然后显示未来额的程序
#未来投资额 = 投资额 * （1+月投资额）** 月数
investment = eval(input("Enter investment amount:"))
annualRate = eval(input("Enter annual interest rate:"))
monthRate = annualRate / 1200
years= eval(input("Enter numbers of year:"))

fultureAcount = investment * (1 + monthRate) ** (years * 12)
print("value is",fultureAcount)