# 5744
from itertools import product as p

def isPrime(n):
    is_prime = True
    d = 2
    while d < n:
        if n % d == 0:
            is_prime = False
            break
        d += 1
    return is_prime



counter = 0
for n in p('0123456', repeat=5):
    if n[0] != '0':
        
        summ = sum([int(i) for i in n])

        s = ''.join(n)
        cCh = 0
        for i in {'0', '2', '4', '6'}:
            cCh += s.count(i)

        if cCh >= 3 and isPrime(summ):
            counter += 1
print(counter)

