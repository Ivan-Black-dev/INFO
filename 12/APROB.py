def alg(s):
    while '333333' in s or '777' in s:
        if '33333' in s:
            s = s.replace('33333', '7', 1)
        else:
            s = s.replace('777', '3', 1)
    return s

print(alg('7'*104))
