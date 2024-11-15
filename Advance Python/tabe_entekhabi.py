def fact(n):
    m = 1
    for i in range(1, n+1):
        m *= i
    return m


def comb(n, k):
    return fact(n) // (fact(k) * fact(n-k))
    
