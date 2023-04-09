def d(n, m):
    return not n%m

def sumBoll(s, d):
    return s + d > 0

def f(x):
    return (x + a >= 160) or (d(x, 7) <= (not sumBoll(x, -17)))

for a in range(1, 500):
    if all(f(x) for x in range(1, 500)):
        print(a)
        break
