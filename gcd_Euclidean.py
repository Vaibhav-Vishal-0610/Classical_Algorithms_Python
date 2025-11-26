'''
Euclidean algorithm to compute the GCD of two integers.
'''
def gcd(a: int,b: int) -> int:
    m, n = abs(a), abs(b)        # Handle Negative Numbers
    if m<n:            # Assume m >= n
        (m,n)=(n,m)
    while n!=0:
        (m,n)=(n,m%n)       # If m>=n, GCD(m,n) = GCD(n,m%n)
    return(m)
