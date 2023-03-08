#improved gcd as we can use one scan to get common factors directly and what if we use no lists at all
#Author: Tinycoder
def gcd(m,n):
    for i in range(1,min(m,n)+1):
        if m%i == 0 and n%i ==0:
            cf= i
    return(cf)
print(gcd(14,63))