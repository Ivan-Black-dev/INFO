def d(n, m):
    return not n%m

def f(x, a):
    return ( d(x, 2) <= (not d(x, 3)) ) or ( (x + a) >= 80 )


for a in range(1, 100):
    if all([f(x, a) for x in range(1, 1000)]):
        print(a)
        break
