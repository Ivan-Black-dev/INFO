def f(s, e):
    if s == e:
        return 1
    elif s > e:
        return 0
    else:
        return f(s+1, e) + f(s+2, e)

# Есть два варианта 22 и 21
s = 3
e = 18
v1 = f(s, e-2-2) # 22
v2 = f(s, e-1-2) # 21
print(v1+v2)
