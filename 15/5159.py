def d(n, m):
    return not n%m

def f(x, a):
    return ( d(x, 6) <= (not d(x, 14)) ) or (( x + a >= 70 ) and d(a, 20))

for a in range(1, 500):
    l = [f(x, a) for x in range(1, 1000)]
    if all(l):
        print(a)
        break
