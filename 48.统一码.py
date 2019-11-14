#显示希腊字母αβγδεζηθ
print("\u03b1\u03b2\u03b3\u03b4\u03b5\u03b6\u03b7\u03b8")


#统一码
print(chr(1161))



# x="(-b±√(b^2-4ac))/2a"用码
x="(-b±√(b^2-4ac))/2a"
print(ord("√"))
print(chr(8730))

s = []
for i in x:
    if i.isdigit():
        s.append(i)
    else:
        s += [ord(i)]
print(s)

for j in s:
    if isinstance(j,int):
        print(chr(int(j)),end="")
    if isinstance(j,str):
        print(j,end = "")