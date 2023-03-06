res = set()

def f(s, c):
    global res
    if c == 9:
        if s > 0:
            res.add(s)
        return None
    else:
        f(s-3, c+1)
        f(s * -3, c+1)


f(133, 0)
print(len(res))
        
