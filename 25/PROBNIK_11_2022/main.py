from fnmatch import *

def fact(n):
    r = []
    d = 1
    while d*d <= n:
        if n % d == 0:
            r.append(d)
            if n//d != d:
                r.append(n//d)
        d += 1
    return sorted(r)

for x in range(1, int((10**7)**(1/2))+1):
    i = x**2
    if fnmatch(str(i), "3*52?"):
            r = fact(i)
            print(i, r[-2])
