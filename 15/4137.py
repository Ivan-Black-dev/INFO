def d(n, m):
    return not n % m

def f(x):
    Q = 29 <= x <= 47
    s = {48, 52, 56}
    return ( (not d(x, 3)) and (x not in s) ) <= ((abs(x - 50) <= 7) <= (Q or ( x & a == 0 )))

for a in range(1, 1000):
    if all( [f(x) for x in range(1, 100)] ):
        print(a)
        break
