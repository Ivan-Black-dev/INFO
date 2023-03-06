def f(n):
    if n <= 3:
        return n
    elif n % 2 == 0:
        return 2*n**2 + f(n-1)
    else:
        return n**3 + n + f(n-1)

for n in range(1, 100):
    if f(n) > 10**7:
        print(n-1)
        break
        
