def f(s, e, w):
    global r
    if s == e:
        r.append(w)
        return 1
    if s > e:
        return 0
    else:
        return f(s+2, e, w+1) + f(s*3, e, w+1) + f(s*4, e, w+1)

r = []
f(2, 400, -2)
c = 0
for i in r:
    if i >= 50:
        c += 1
print(c)
