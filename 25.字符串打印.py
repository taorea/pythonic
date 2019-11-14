#显示welcome to python 5次
print("welcome to python " * 5)

#print fun
fun = """
FFFFFFF    U     U    NN    NN
FF         U     U    NNN   NN
FFFFFFF    U     U    NN N  NN
FF          U   UUU   NN  N NN
FF           UUU      NN   NNN
"""
print(fun)

print(format("a","<10s"),format('a**2',"<10s"),format('a**3',"<10s"))
for a in range(1,5):
    # print("%10d %10d %10d"%(a,a**2,a**3))
    print(format(a,"<10d"),format(a**2,"<10d"),format(a**3,"<10d"))
