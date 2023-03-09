#improved gcd as we can use one scan to get common factors directly and what if we use no lists at all
#Author: Tinycoder

def gcd(m,n):
    if m<n:
        (m,n)=(n,m)
    if m%n == 0:
        return(n)
    else:
        return(gcd(n,m%n))
print(gcd(16,24))
