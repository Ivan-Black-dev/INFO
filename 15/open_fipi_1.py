def d(n, m):
    return not n%m

def f(x):
    B = 50 <= x <= 70
    return d(x, a) or ( B <= (not d(x, 16)) )


for a in range(1, 1000):
    if all(f(x) for x in range(1, 1000)):
        print(a)
        
