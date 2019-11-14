num = "12.345"
print(float(num))
print(eval(num))
#int类型转换只能用于字符串是整数的情况，浮点数不行
print(int("1234"))
# print(int("124.424"))  # 浮点数进行类型转换是会报错Error
# 但是eval()就没有限制了，内部是整数浮点数类型的字符串都可以转换成整数和浮点数数据类型