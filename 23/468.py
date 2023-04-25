def f(s, e):
    if s == e:
        return 1
    if s > e:
        return 0
    else:
        return f(s+1, e) + f(s*2, e)

#Два варианта, 11 и 21

s = 3
v1 = f(s, 20-1-1) # 11
v2 = f(s, (20/2)-1)
print(v1 + v2)
