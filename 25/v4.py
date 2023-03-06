def d(c):
    n = [10, 12, 14, 16, 18, 20]
    return all((not c%i) for i in n)

def m(n):
    m = -1
    for i in range(10, 21):
        m = max(0, n%i)
    return m
    

f = 0
n = 320400
while f != 5:
    if d(n):
        print(n, m(n))
        f += 1
    n += 1
