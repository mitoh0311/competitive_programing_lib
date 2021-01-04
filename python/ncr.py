MOD = 10 ** 9 + 7
MAX = 200000
fac = [0] * MAX
finv = [0] * MAX
inv = [0] * MAX

def combinit():
    fac[0] = 1
    fac[1] = 1
    finv[0] = 1
    finv[1] = 1
    inv[1] = 1
    for i in range(2, MAX):
        fac[i] = fac[i - 1] * i % MOD
        inv[i] = MOD - inv[MOD % i] * (MOD // i) % MOD
        finv[i] = finv[i - 1] * inv[i] % MOD
    
def comb(n, k):
    if n < k: return 0
    if (n < 0 or k < 0): return 0
    return fac[n] * (finv[k] * finv[n - k] % MOD) % MOD

"""
combinit()
print(comb(5, 2))
print(comb(1000, 500))
"""
