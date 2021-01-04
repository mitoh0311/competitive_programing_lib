from math import factorial

def nCr(n, r, mod):
    a = 1
    for i in range(r):
        a *= (n - i)
        a %= mod
    return (a * pow(factorial(r), mod-2, mod)) % mod

# print(nCr(5, 2, 10 ** 9 + 7))
#
# 10
