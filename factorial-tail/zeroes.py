from math import log

def zeroes(b, n):
    return min(
        sum(n // p**k for k in range(1, int(log(n, p)) + 1)) // e for p, e in factors(b).items())

def factors(b):
    f, p = {}, 2
    while b > 1:
        if b % p == 0:
            f[p] = f.get(p, 0) + 1
            b //= p
        else:
            p += 1 + (p > 2)
    return f
