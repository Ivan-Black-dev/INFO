def f(s, e, w):
    if s == e and len(w) == len(set(w)):
        return 1
    elif s > e or len(w) != len(set(w)) or s < -40 or s > 40:
        return 0
    else:
        w.append(s)
        return f(s+2, e, w) + f(s-3, e, w)

print(f(1, 30, []))
