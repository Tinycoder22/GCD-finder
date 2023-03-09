#improved gcd making use of an algorithm to do the same.
#Author: Tinycoder
def gcd(m,n):
    if m<n:
        (m,n) = (n,m)
    if (m%n)==0:
        return(n)
    else:
        diff = m-n
    return(gcd(n,diff))
