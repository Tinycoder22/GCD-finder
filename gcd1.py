#greatest common divisor 1
#Author: Tinycoder
def gcd(m,n):
    fm = []
    for i in range(1, m+1):
        if m%i==0:
            fm.append(i)
    print(fm)

    fn =[]
    for j in range(1,n+1):
        if n%j==0:
            fn.append(j)
    print(fn)

    cf = []
    for f in fm:
        if f in fn:
            cf.append(f)
    return(cf[-1])
