def d(n, m):
    return not n%m

def f(x, a):
    return ( d(x, 12) <= (not d(x, 90)) ) or ( (x + 2*a) >= 512 )

for a in range(1, 1000):
    fl = True
    for x in range(1, 1000):
        if not f(x, a):
            fl = False
    if fl:
        print(a)
        break
        
