def f(s, e, c):
    if s == e and c <= 2:
        return 1
    if s > e:
        return 0
    if s == e and c > 2:
        return 0
    res = f(s+2, e, c)
    if s % 2 != 0:
        return res + f(2*s, e, c)
    if s % 2 == 0:
        return res + f((2*s) + 1, e, c+1)



    
print(f(2, 35, 0))
