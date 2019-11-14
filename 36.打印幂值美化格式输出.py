#a b a**b
#1 2 1**2
print("%5s%5s%10s"%("a","b","a**b"))
a = 1
while a < 6:
    b = a + 1
    print("%5s%5s%10s"%(a,b,a**b))
    a += 1
    