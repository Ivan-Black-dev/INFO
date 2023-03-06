def pr(n): # является ли число простым - эффективный алгоритм
    d=2
    while d*d<=n and n%d!=0:
        d+=1
    return d*d>n

c = 0
for num in range(194441, 196501):
    if pr(num) and str(num)[-2:] == '93':
        c += 1
        print(c, num)
