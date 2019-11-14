#美元、两角五分、一角、5分、美分
acount = 11.56
cent = round(acount * 100) % 100   #round取整避免出现精度问题
dollar = round(acount * 100) // 100
twenty_five_cent = cent // 25
last_cent = cent % 25
dime = last_cent // 10
last_cent = last_cent % 10
five_cent = last_cent // 5
finally_last_cent = five_cent % 5
print("{0} {1} {2} {3} {4}".format(dollar,twenty_five_cent,dime,five_cent,finally_last_cent))