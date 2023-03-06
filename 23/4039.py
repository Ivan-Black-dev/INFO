res = set()

def f(s, c):
    global res
    if c == 13:
        res.add(s)
    else:
        f(s+3, c+1)
        f((s*2)+1, c+1)

f(2, 0)
print(len(res))
