def gcd(a, b):
    while b != 0: (a, b) = (b, a % b)
    # GCD(a, b) = GCD(b, a % b)
    # If b == 0 at some stage, then a will be the GCD
    return a