from math import sqrt, ceil

def prime(N):
    temp = [True]*(N+1)
    temp[0] = temp[1] = False
    for i in range(2, ceil(sqrt(N+1))):
        if temp[i]:
            temp[i+i::i] = [False]*(len(temp[i+i::i]))
    primes = [n for n in range(N+1) if temp[n]]
    return primes