def f(a, b, c, d):
    return ((not a) and (not b)) or (b == c) or d

for a in {0, 1}:
    for b in {0, 1}:
        for c in {0, 1}:
            for d in {0, 1}:
                r = f(a, b, c, d)
                if not r:
                    print(a, b, c, d)
