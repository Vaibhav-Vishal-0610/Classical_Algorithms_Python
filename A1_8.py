def gcd(m,n):
    # Assume m>=n
    if m<n:
        (m,n)=(n,m)
    while n!=0:
        (m,n)=(n,m%n)       # If m>=n, GCD(m,n) = GCD(n,m%n)
    return(m)
    # This program also takes care of the GCD in case one of the numbers is zero.