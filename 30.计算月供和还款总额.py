#年利率，贷款数，贷款年限
yearRate = eval(input("输入年利率"))
monthrate = yearRate / 1200
loanMoney = eval(input("输入贷款总额"))
loanyear = eval(input("输入贷款年限"))
monthpayment = loanMoney * monthrate / (1 - 1 / (1 + monthrate) ** (loanyear * 12))
totalpayment = monthpayment * loanyear * 12
print("The monthly payment is:",int(monthpayment * 100) / 100) #保留几位小数，就先乘以几百取int后的值然后除以几百
print("The total payment is :",int(totalpayment * 100) / 100)
