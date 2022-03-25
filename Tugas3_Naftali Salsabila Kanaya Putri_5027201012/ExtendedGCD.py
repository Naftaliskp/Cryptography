def gcdExtended(p, q): 
    if p == 0:
        return (q, 0, 1)
    else:
        (gcd, u, v) = gcdExtended(q % p, p)
        return (gcd, v - (q // p) * u, u)

p = 26513
q = 32321

gcd, u, v = gcdExtended(p, q)
print(u,v)