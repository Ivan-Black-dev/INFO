res = set()
def f(s, c):
    if c == 4:
        res.add(s)
    else:
        f(s+1, c+1)
        f(s+5, c+1)
        f(s*3, c+1)

f(1, 0)
print(len(res))
